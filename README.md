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

