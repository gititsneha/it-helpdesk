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
```

## 🔐 Security

The project uses AWS Security Groups to control network access.

The application also implements:

- Password hashing
- Session-based authentication
- Role-based authorization
- Parameterized SQL queries
- Environment variables for sensitive configuration
- `.gitignore` to prevent secrets and private keys from being committed

Sensitive files such as `.env`, `.pem` files, and the Python virtual environment are excluded from GitHub.

## 📊 Monitoring

Amazon CloudWatch is used to monitor the EC2 instance.

A CloudWatch alarm was configured to monitor CPU utilization. When CPU usage exceeds the configured threshold, the alarm can trigger an Amazon SNS notification.

This provides basic infrastructure monitoring and alerting for the deployed application.

## 🖥️ Application Flow

```text
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
```

## 📁 Project Structure

```text
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
```

## 📸 Application Preview

### Login Page

<p align="center">
  <img width="800" alt="Login Page" src="https://github.com/user-attachments/assets/fdee7fa3-47a1-4ea6-8719-65dd255d3048">
</p>

### User Dashboard

<p align="center">
  <img width="800" alt="User Dashboard" src="https://github.com/user-attachments/assets/2a19c45a-e61f-4349-a9d1-e9c03645f68c">
</p>

### Admin Dashboard

<p align="center">
  <img width="800" alt="Admin Dashboard" src="https://github.com/user-attachments/assets/3da92dd7-9a7d-4de6-a848-380c50242c95">
</p>

### Ticket Details

<p align="center">
  <img width="900" alt="Ticket Details" src="https://github.com/user-attachments/assets/01b09fb8-cc67-4598-aa27-3341faab34c7">
</p>

## 🗄️ Database

### MySQL Database

<p align="center">
  <img width="900" alt="MySQL Database" src="https://github.com/user-attachments/assets/2a166b98-807e-4687-884c-e7c722948cd0">
</p>

### Database Tables

<p align="center">
  <img width="800" alt="Database Tables" src="https://github.com/user-attachments/assets/d8328dde-0483-4ed5-a671-fb93375c86a0">
</p>

## 🖥️ EC2 Instance

<p align="center">
  <img width="900" alt="Amazon EC2 Instance" src="https://github.com/user-attachments/assets/5fbbc2d3-bc1e-413c-8124-48544a8c63cf">
</p>

## 🔐 Security Group

<p align="center">
  <img width="900" alt="AWS Security Group" src="https://github.com/user-attachments/assets/f93f7e1d-2579-4830-a6d6-0fa53f3aaf91">
</p>

## 📊 CloudWatch Monitoring

<p align="center">
  <img width="900" alt="CloudWatch Monitoring" src="https://github.com/user-attachments/assets/12c3648f-27b4-4c96-a6a2-4d9b260e1865">
</p>

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/it-helpdesk-aws.git
cd it-helpdesk-aws
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file containing your database and Flask configuration.

Example:

```text
FLASK_SECRET_KEY=your-secret-key
DB_HOST=your-database-host
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_NAME=helpdesk
```

Do not commit the `.env` file to GitHub.

### 5. Run the application

```bash
python app.py
```

The application will be available locally at:

```text
http://127.0.0.1:5000
```

## ☁️ AWS Deployment

The application was deployed on an Amazon EC2 instance running Amazon Linux.

Deployment involved:

1. Launching an EC2 instance
2. Configuring SSH access
3. Installing Python and required packages
4. Deploying the Flask application
5. Connecting Flask to Amazon RDS MySQL
6. Configuring Security Groups
7. Installing and configuring Nginx
8. Running Flask through systemd
9. Configuring CloudWatch monitoring
10. Creating a CloudWatch CPU alarm
11. Configuring SNS notifications

## 📚 Key Learning Outcomes

Through this project, I gained practical experience in:

- AWS EC2 deployment
- Amazon RDS database management
- AWS networking and Security Groups
- Linux server administration
- SSH
- Nginx configuration
- systemd service management
- Flask application deployment
- MySQL connectivity
- Authentication and authorization
- CloudWatch monitoring
- SNS notifications
- Troubleshooting production deployment issues
- Git and GitHub

## 🔮 Future Improvements

Possible future improvements include:

- HTTPS using SSL/TLS
- Custom domain name
- HTTPS certificate using AWS Certificate Manager
- Automated deployment using CI/CD
- More detailed CloudWatch monitoring
- Application logging
- Email notifications for ticket updates
- File attachments for support tickets

## 👩‍💻 Author

**Sneha Shinde**

BSc Information Technology
Interested in Cloud Computing, IT Infrastructure, Linux and AWS.
