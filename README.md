# CECS-574 Distributed Billing System Using Apache Kafka

## Team : Tech Titans

## Team Members :
  1. Pooja Devendra Chavan (030896136)
  2. Sonal Bijitkar (032169473)
  3. Mitali Manish Admuthe (032175856)
  4. Joyli Rumao

## Problem Statement :
This project implements a distributed system for monitoring resource usage and calculating billing costs based on CPU and memory usage across multiple machines. It uses Apache Kafka for distributed messaging, enabling producers to send resource usage data to consumers who perform billing calculations. The system demonstrates the scalability and efficiency of Kafka in distributed computing environments.

## Project Structure
##.
├── machine1.py        # API server to receive and handle resource data from workers
├── worker1.py         # Worker script to gather and send CPU and memory data
├── dashboard.html     # Front-end HTML file to visualize resource usage in real-time
└── README.md          # Documentation for the project

##Features
Real-Time Monitoring: Continuously tracks and displays CPU and memory usage for each machine.
Interactive Dashboard: Provides an interactive visualization of CPU and memory usage.
Multi-Machine Support: Handles resource data from multiple machines by running an instance of worker1.py on each machine.
Customizable Fetch Interval: The dashboard fetches data every 5 seconds by default, but this interval can be modified.

##Requirements
Python Dependencies
This project requires Python 3.x and the Flask framework for the API server. Install Flask with:

bash
Copy code
pip install flask

