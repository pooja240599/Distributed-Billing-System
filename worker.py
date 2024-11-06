import json
import sqlite3
import time
from kafka import KafkaConsumer
from flask import Flask, jsonify, render_template

# Database configuration
DB_NAME = 'billing.db'

# Billing rates per unit of resource usage
CPU_RATE = 0.05  # $0.05 per CPU percentage
MEMORY_RATE = 0.01  # $0.01 per memory percentage

# Flask app setup
app = Flask(__name__)

# Initialize SQLite database to store usage data with total cost
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usage (
                machine_id TEXT,
                timestamp INTEGER,
                cpu_usage REAL,
                memory_usage REAL,
                total_cost REAL
                )''')
    conn.commit()
    conn.close()

# Store resource usage data and calculated cost in the database
def store_usage_data(machine_id, cpu_usage, memory_usage, total_cost):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO usage (machine_id, timestamp, cpu_usage, memory_usage, total_cost) VALUES (?, ?, ?, ?, ?)",
              (machine_id, int(time.time()), cpu_usage, memory_usage, total_cost))
    conn.commit()
    conn.close()

# Calculate total cost for a machine
def calculate_cost(cpu_usage, memory_usage):
    cpu_cost = cpu_usage * CPU_RATE
    memory_cost = memory_usage * MEMORY_RATE
    return cpu_cost + memory_cost

def consume_usage_data():
    consumer = KafkaConsumer('resource_usage',
                             bootstrap_servers='localhost:9092',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    
    for message in consumer:
        usage_data = message.value
        machine_id = usage_data['machine_id']
        cpu_usage = usage_data['cpu_usage']
        memory_usage = usage_data['memory_usage']

        # Calculate and store the total cost
        total_cost = calculate_cost(cpu_usage, memory_usage)
        store_usage_data(machine_id, cpu_usage, memory_usage, total_cost)
        
        print(f"Machine ID: {machine_id}, CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%, Total Cost: ${total_cost:.2f}")

# Endpoint to fetch recent usage and cost data for the dashboard
@app.route('/api/usage')
def get_usage_data():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT machine_id, timestamp, cpu_usage, memory_usage, total_cost FROM usage ORDER BY timestamp DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    usage_data = [{'machine_id': row[0], 'timestamp': row[1], 'cpu_usage': row[2], 'memory_usage': row[3], 'total_cost': row[4]} for row in rows]
    return jsonify(usage_data)

# Endpoint to fetch the latest total cost for a specific machine
@app.route('/api/cost/<machine_id>')
def get_machine_cost(machine_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT total_cost FROM usage WHERE machine_id = ? ORDER BY timestamp DESC LIMIT 1", (machine_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return jsonify({"machine_id": machine_id, "total_cost": row[0]})
    else:
        return jsonify({"error": "No data found for machine_id: " + machine_id}), 404

# Dashboard route
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Run Flask app and Kafka consumer
if __name__ == "__main__":
    init_db()
    from threading import Thread
    # Run Kafka consumer in a separate thread
    consumer_thread = Thread(target=consume_usage_data)
    consumer_thread.start()
    # Run Flask app for dashboard API
    app.run(debug=True, host='0.0.0.0', port=5001)
