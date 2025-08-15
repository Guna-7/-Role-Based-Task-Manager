# 📋 Django Role-Based Task Manager

A **role-based task management system** built with **Django** and **Django REST Framework (DRF)**, featuring **JWT-secured APIs**.  
The application enforces strict **role-based access control**, where **Managers** can create, assign, and track tasks, while **Employees** can only view and update tasks assigned to them.

---

## 🚀 Features

- **Role-Based Access Control (RBAC)**  
  - **Manager**: Create, assign, update, and monitor tasks for any employee.  
  - **Employee**: View and update only their assigned tasks.

- **JWT Authentication**  
  - Secure API endpoints with JSON Web Tokens.  
  - Login and refresh token functionality for persistent sessions.

- **Task Management**  
  - Create, update, and track progress of tasks.  
  - Status updates and completion tracking.

- **API-Driven Workflow**  
  - Frontend and backend communicate entirely via REST APIs.  
  - Decoupled architecture for easy integration with any frontend.

---

## 🛠 Tech Stack

- **Backend**: Django, Django REST Framework  
- **Authentication**: JWT (JSON Web Tokens)  
- **Language**: Python  
- **Database**: SQLite (can be swapped with PostgreSQL/MySQL)  

---

## 📂 Project Structure
```plaintext

django-role-based-task-manager/
├── tasks/              # App for task management
├── users/              # App for user roles and authentication
├── project_name/       # Project configuration
├── requirements.txt    # Python dependencies
└── manage.py

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/your-username/django-role-based-task-manager.git
cd django-role-based-task-manager


Create and activate virtual environment

python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py migrate


Create superuser (for admin access)

python manage.py createsuperuser


Run server

python manage.py runserver

🔑 API Authentication Flow

Login to receive JWT Access & Refresh tokens.

Access Token is used for API calls.

Refresh Token is used to obtain a new Access Token when it expires.

Example Login:

POST /api/token/
{
    "username": "manager1",
    "password": "securepassword"
}

📌 API Endpoints
Method	Endpoint	Role Access	Description
POST	/api/token/	All	Obtain JWT access/refresh tokens
POST	/api/token/refresh/	All	Refresh JWT token
GET	/api/tasks/	Manager	List all tasks
POST	/api/tasks/	Manager	Create a new task
GET	/api/tasks/my-tasks/	Employee	List own tasks
PATCH	/api/tasks/{id}/	Assigned	Update own task status
