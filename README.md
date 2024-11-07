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
2. [Project Structure](#Project_Structure)
3. [Technologies used](#Technologies_used)
4. [Installation](#Installation)
5. [Conclusion](#Conclusion)
6. [References](#References)

## Prerequisites


## Project Structure

<!--
##.
##├── machine1.py        # API server to receive and handle resource data from workers
##├── worker1.py         # Worker script to gather and send CPU and memory data
##├── dashboard.html     # Front-end HTML file to visualize resource usage in real-time
##└── README.md          # Documentation for the project
-->
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
- **Set up Kafka:** Install and configure Apache Kafka. Start the Kafka server.
  ```bash
  java -cp "libs/*;config" kafka.Kafka config\server.properties
- **Start the Zookeeper instance:** Open a terminal and navigate to your Kafka directory. Start Zookeeper (if you haven't started it yet).
  ```bash
  C:\Users\abc\Downloads\kafka_2.13-3.8.0\kafka_2.13-3.8.0 java -cp "libs/*;config"
- **Create a Kafka Topic:** 

## Conclusion

## References
- [Apache Kafka Documentation](https://kafka.apache.org/documentation)
- [Research Paper](https://ieeexplore.ieee.org/document/9361803/)
  
## Real Time Dashboard
![image](https://github.com/user-attachments/assets/31dba240-04b4-4d21-b381-701c02e09390)
![image](https://github.com/user-attachments/assets/3681c15f-ae37-4c2d-8163-cff13a5c0895)


