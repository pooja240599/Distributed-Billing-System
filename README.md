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

## Conclusion

## References
- [Apache Kafka Documentation](https://kafka.apache.org/documentation)
- [Research Paper](https://ieeexplore.ieee.org/document/9361803/)
  
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

