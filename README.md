# IT Help Desk Application

A web-based IT Help Desk application built with Flask and MySQL, deployed on AWS. The application allows users to submit and manage IT support tickets, while administrators can monitor tickets, update their status, and manage the help desk.

## 🚀 Project Overview

This project was built to gain practical experience with application development, Linux administration, AWS infrastructure, database connectivity, deployment, and monitoring.

The application is hosted on an Amazon EC2 instance and uses Amazon RDS for the MySQL database.

## ✨ Features

- User login and authentication
- Password hashing
- Role-based access for users and administrators
- Create IT support tickets
- Search and filter tickets
- Filter by category, priority, and status
- Admin dashboard with ticket statistics
- Update ticket status
- Delete tickets
- Individual ticket details
- CloudWatch monitoring and alarms
- Nginx reverse proxy
- systemd service for application management

## 🛠️ Technologies Used

### Application

- Python
- Flask
- HTML
- CSS
- JavaScript
- MySQL

### AWS

- Amazon EC2
- Amazon RDS for MySQL
- Amazon CloudWatch
- Amazon SNS
- AWS Security Groups

### Linux / Deployment

- Amazon Linux
- Nginx
- systemd
- SSH

### Development Tools

- Git
- GitHub
- MySQL
- VS Code

## ☁️ AWS Architecture

```text
                         Internet
                            │
                            ▼
                    ┌───────────────┐
                    │   Amazon EC2  │
                    │               │
                    │    Nginx      │
                    │       │       │
                    │       ▼       │
                    │ Flask App     │
                    │   (Python)    │
                    └───────┬───────┘
                            │
                            │ MySQL
                            ▼
                    ┌───────────────┐
                    │  Amazon RDS   │
                    │    MySQL      │
                    └───────────────┘

              EC2 ──────────────► CloudWatch
                                     │
                                     ▼
                                  Alarm
                                     │
                                     ▼
                                    SNS
                                     │
                                     ▼
                                  Email

              Security Groups control
              network access between
              the application and database.


🔐 Security

The project uses AWS Security Groups to control network access.

The application also implements:

Password hashing
Session-based authentication
Role-based authorization
Parameterized SQL queries
Environment variables for sensitive configuration
.gitignore to prevent secrets and private keys from being committed

Sensitive files such as .env, .pem files, and the Python virtual environment are excluded from GitHub.

📊 Monitoring

Amazon CloudWatch is used to monitor the EC2 instance.

A CloudWatch alarm was configured to monitor CPU utilization. When CPU usage exceeds the configured threshold, the alarm can trigger an Amazon SNS notification.

This provides basic infrastructure monitoring and alerting for the deployed application.

🖥️ Application Flow

User
 │
 ▼
Login
 │
 ▼
Flask Application
 │
 ├── Create Ticket
 │
 ├── Search / Filter Tickets
 │
 └── View Tickets
        │
        ▼
    Amazon RDS
        │
        ▼
     MySQL Database


Administrator
 │
 ▼
Admin Dashboard
 │
 ├── View Ticket Statistics
 ├── Update Ticket Status
 └── Delete Tickets

📁 Project Structure

it-helpdesk-aws/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    ├── login.html
    ├── index.html
    ├── admin.html
    └── ticket_details.html

APPLICATION PREVIEW :

<img width="781" height="647" alt="Screenshot 2026-09-06 030232" src="https://github.com/user-attachments/assets/fdee7fa3-47a1-4ea6-8719-65dd255d3048" />

<img width="628" height="505" alt="Screenshot 2026-09-06 020634" src="https://github.com/user-attachments/assets/2a19c45a-e61f-4349-a9d1-e9c03645f68c" />

<img width="577" height="450" alt="Screenshot 2026-09-06 020649" src="https://github.com/user-attachments/assets/3da92dd7-9a7d-4de6-a848-380c50242c95" />

<img width="1080" height="486" alt="Screenshot 2026-09-06 030320" src="https://github.com/user-attachments/assets/01b09fb8-cc67-4598-aa27-3341faab34c7" />

DATABASE :

<img width="1505" height="266" alt="Screenshot 2026-09-06 031940" src="https://github.com/user-attachments/assets/2a166b98-807e-4687-884c-e7c722948cd0" />

<img width="893" height="691" alt="Screenshot 2026-09-06 033853" src="https://github.com/user-attachments/assets/d8328dde-0483-4ed5-a671-fb93375c86a0" />

EC2-INSTANCE :

<img width="1581" height="737" alt="edited" src="https://github.com/user-attachments/assets/5fbbc2d3-bc1e-413c-8124-48544a8c63cf" />

SECURITY GROUP :

<img width="1611" height="751" alt="Screenshot 2026-09-06 031909" src="https://github.com/user-attachments/assets/f93f7e1d-2579-4830-a6d6-0fa53f3aaf91" />

CLOUDWATCH MONITORING :

<img width="1131" height="595" alt="Screenshot 2026-09-06 033433" src="https://github.com/user-attachments/assets/12c3648f-27b4-4c96-a6a2-4d9b260e1865" />









