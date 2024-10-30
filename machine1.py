# machine.py (Kafka Producer on each machine)

import psutil
import json
from kafka import KafkaProducer
import tkinter as tk
from tkinter import messagebox

# Kafka configuration
KAFKA_BROKER_URL = "localhost:9092"  # Change if needed
TOPIC_NAME = "resource_usage"

machine_id = "Machine_B"

def get_resource_usage():
    # Get CPU and memory usage data
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    return {"machine_id": machine_id, "cpu_usage": cpu_usage, "memory_usage": memory_usage}

def send_usage_data():
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    usage_data = get_resource_usage()
    try:
        # Send resource usage data to the Kafka topic
        producer.send(TOPIC_NAME, usage_data)
        producer.flush()  # Ensure all messages are sent
        messagebox.showinfo("Success", "Resource usage data sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error sending data: {e}")

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
