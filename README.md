# CECS-574 Distributed Billing System Using Apache Kafka

## Team : Tech-Titans

## Team Members :

  1. [Mitali Manish Admuthe (032175856)](https://github.com/Mma5901)
  2. [Joyli Marshal Rumao (032176935)](https://github.com/joyli-25)
  3. [Pooja Devendra Chavan (030896136)](https://github.com/pooja240599)
  4. [Sonal Bijitkar (032169473)](https://github.com/so-bit)

## Introduction:
This project implements a distributed system for monitoring resource usage and calculating billing costs based on CPU and memory usage across multiple machines. It uses Apache Kafka for distributed messaging, enabling producers to send resource usage data to consumers who perform billing calculations. The system demonstrates the scalability and efficiency of Kafka in distributed computing environments.

## Table of Contents
1. [Prerequisites](#Prerequisites)
2. [Project Structure](#Project-Structure)
3. [Technologies used](#Technologies-used)
4. [Installation](#Installation)
5. [Conclusion](#Conclusion)
6. [References](#References)
7. [Real Time Dashboard](#Real-Time-Dashboard)

## Prerequisites

Ensure the following software and libraries are installed before setting up the project:

1. **Python 3.7+**: Required to run the scripts.
   - [Python Installation Guide](https://www.python.org/downloads/)

2. **Apache Kafka and Zookeeper**: Install and configure for data streaming and message handling.
   - [Kafka Download and Setup](https://kafka.apache.org/downloads)

3. **Kafka-Python Library**: Connects Python scripts with Kafka.
   ```bash
   pip install kafka-python

4. **Flask**: Used to create the REST API for fetching usage and billing data.
   ```bash
   pip install flask

5. **psutil Library**: For monitoring CPU and memory usage on machine clients.
   ```bash
   pip install psutil

## Project Structure

```plaintext

├── worker.py              # Main worker script for data processing and billing calculations
├── machine.py             # Client machine script for sending resource usage data
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── templates/
│   └── dashboard.html     # Front-end HTML file to visualize resource usage in real-time
└── database/
    └── billing.db         # SQLite database storing resource usage and billing data
```

## Technologies used

- **Apache Kafka:** Distributed data streaming platform for task distribution and fault tolerance
- **SQLite:** Lightweight database for storing usage data and calculated costs
- **psutil:** Python library for gathering system resource usage data
- **Tkinter:** Python library for the client machine’s user interface

## Installation


- **Clone the Repository:** Clone the project repository to your local machine and navigate into the directory
  ```bash
  git clone https://github.com/pooja240599/Distributed-Billing-System.git
  cd Distributed-Billing-System
- **Set up Kafka:** Install and configure Apache Kafka. Start the Kafka server.
  ```bash
  java -cp "libs/*;config" kafka.Kafka config\server.properties
- **Start the Zookeeper instance:** Open a terminal and navigate to your Kafka directory. Start Zookeeper (if you haven't started it yet).
  ```bash
  C:\Users\abc\Downloads\kafka_2.13-3.8.0\kafka_2.13-3.8.0 java -cp "libs/*;config"
- **Create a Kafka Topic:**
  ```bash
  bin/kafka-topics.sh --create --topic resource_usage --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

- **Run Producer and Consumer code**
  ```bash
  python worker.py
  python machine.py


## Conclusion
This project illustrates Apache Kafka's potential for real-time distributed monitoring and billing. 
By separating data production from billing calculations, Kafka enables high-throughput 
processing, fault tolerance, and scalability, meeting the requirements of complex, distributed 
systems.

## References
- [Apache Kafka Documentation](https://kafka.apache.org/documentation)
- [Research Paper](https://ieeexplore.ieee.org/document/9361803/)
  
## Real Time Dashboard
![image](https://github.com/user-attachments/assets/31dba240-04b4-4d21-b381-701c02e09390)
![image](https://github.com/user-attachments/assets/3681c15f-ae37-4c2d-8163-cff13a5c0895)


