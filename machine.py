import psutil
import json
from kafka import KafkaProducer
import tkinter as tk
from tkinter import messagebox, Toplevel, Label
import requests

# Kafka configuration
KAFKA_BROKER_URL = "localhost:9092"
TOPIC_NAME = "resource_usage"
WORKER_API_URL = "http://127.0.0.1:5001"
MACHINE_ID = "Machine_B"

def get_resource_usage():
    # Get CPU and memory usage data
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    return {"machine_id": MACHINE_ID, "cpu_usage": cpu_usage, "memory_usage": memory_usage}

def send_usage_data():
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    usage_data = get_resource_usage()
    try:
        # Send resource usage data to Kafka
        producer.send(TOPIC_NAME, usage_data)
        producer.flush()
        messagebox.showinfo("Success", "Resource usage data sent successfully!")
        
        # Display total cost after sending data
        display_total_cost()
    except Exception as e:
        messagebox.showerror("Error", f"Error sending data: {e}")

def fetch_total_cost():
    try:
        response = requests.get(f"{WORKER_API_URL}/api/cost/{MACHINE_ID}")
        if response.status_code == 200:
            data = response.json()
            return data['total_cost']
        else:
            messagebox.showwarning("Warning", f"Could not fetch cost: {response.json().get('error', 'Unknown error')}")
            return None
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching total cost: {e}")
        return None

def display_total_cost():
    total_cost = fetch_total_cost()
    if total_cost is not None:
        # Create a new pop-up window
        cost_window = Toplevel()
        cost_window.title("Total Cost")
        
        # Display total cost in the new window
        Label(cost_window, text=f"Total Cost for {MACHINE_ID}: ${total_cost:.2f}", font=("Arial", 14)).pack(pady=20, padx=20)
        
        # Close button for the window
        close_button = tk.Button(cost_window, text="Close", command=cost_window.destroy)
        close_button.pack(pady=10)

# Tkinter UI setup
def create_ui():
    root = tk.Tk()
    root.title("Resource Usage Billing")

    frame = tk.Frame(root)
    frame.pack(pady=20, padx=20)

    title_label = tk.Label(frame, text="Resource Usage Billing System", font=("Arial", 16))
    title_label.pack(pady=10)

    send_button = tk.Button(frame, text="Send Usage Data", font=("Arial", 12), command=send_usage_data)
    send_button.pack(pady=20)

    quit_button = tk.Button(frame, text="Quit", font=("Arial", 12), command=root.quit)
    quit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
