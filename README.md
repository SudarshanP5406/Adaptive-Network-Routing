\# Adaptive Network Routing and Congestion Management



\## Overview



This project implements an Adaptive Network Routing and Congestion Management system using GNS3, FRRouting (FRR), OSPF and Python.



The system monitors network performance using latency and packet loss measurements. When congestion is detected, Python-based monitoring sends notifications to router controllers, which dynamically modify OSPF interface costs to encourage traffic to use an alternative path.



When network conditions return to normal, the interface costs are restored to their original values.



\## Objectives



\- Monitor network latency and packet loss.

\- Detect congestion using Python.

\- Dynamically modify OSPF interface costs.

\- Switch traffic between primary and alternative paths.

\- Automate routing changes using router controllers.

\- Evaluate network performance using iPerf3.



\## Network Topology



The network consists of five FRRouting routers and two Ubuntu hosts, implemented in GNS3.



\*\*Primary Path:\*\*



Source → R1 → R2 → R3 → Destination



\*\*Alternative Path:\*\*



Source → R1 → R4 → R5 → R3 → Destination



See the `GNS3` folder for the topology.



\## Technologies Used



\- GNS3 – Network simulation

\- FRRouting (FRR) – Router implementation

\- OSPF – Dynamic routing protocol

\- Python – Congestion monitoring

\- Ubuntu Linux – Host and router environments

\- Netcat – Controller communication

\- iPerf3 – Network performance testing



\## System Architecture



1\. The Python monitoring program sends periodic ping requests to the destination.

2\. It measures latency and packet loss.

3\. If the configured threshold is exceeded, it identifies the network state as CONGESTED.

4\. Notifications are sent to the R1 and R2 controllers.

5\. The controllers modify OSPF interface costs.

6\. OSPF recalculates the routes and selects the alternative path.

7\. When conditions return to normal, the costs are restored.



\## OSPF Cost Configuration



| Network State | R1 eth0 Cost | R2 eth0 Cost |

|---|---:|---:|

| Normal | 100 | 100 |

| Congested | 500 | 500 |



\## Repository Structure



\- `GNS3/` – Network topology files and images.

\- `Controllers/` – R1 and R2 controller scripts.

\- `Congestion-Monitor/` – Python monitoring program.

\- `Router-Configurations/` – Router configurations.

\- `Results/` – Routing tables, logs and performance results.

\- `Documentation/` – Project report and troubleshooting notes.



\## Performance Evaluation



The system is evaluated under normal and congested network conditions using:



\- OSPF routing table observations.

\- Interface cost changes.

\- Congestion monitoring logs.

\- Controller execution logs.

\- iPerf3 throughput and packet-loss measurements.



Refer to the `Results` folder for experimental evidence.



\## Challenges and Troubleshooting



During implementation, several configuration and connectivity issues were encountered, including routing asymmetry, controller communication, and network performance problems.



Detailed problems, solutions and troubleshooting observations are documented in:



`Documentation/PROBLEMS\_AND\_SOLUTIONS.txt`



\## Future Improvements



\- Implement more reliable congestion detection.

\- Improve automatic recovery and route restoration.

\- Introduce hysteresis to avoid frequent route switching.

\- Evaluate performance under different traffic loads.

\- Compare adaptive routing against standard OSPF.



\## Author



Developed as an academic networking project.





