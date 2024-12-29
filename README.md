# RentManagementSystem

## Project Overview
RentManagementSystem is a Django-based web application designed to help property owners and managers efficiently track rental properties and their payments. It provides a user-friendly interface to manage tenants, record rental payments, and oversee property maintenance.

## Features
- **Tenant Management**: Easily add, update, and delete tenant information.
- **Payment Tracking**: Record and monitor rental payments with ease.
- **Property Maintenance**: Schedule and manage maintenance tasks for properties.
- **Reporting**: Generate detailed reports on rental income and expenses to gain insights into property performance.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript (with Django templates)
- **Backend**: Django
- **Database**: SQLite (default), support for other databases like PostgreSQL, MySQL

## Installation
To install and set up the RentManagementSystem locally, follow these steps:

1. Clone the repository:
  ```sh
  git clone https://github.com/aashishChakradhar/RentManagementSystem.git
  ```
2. Navigate to the project directory:
  ```sh
  cd RentManagementSystem
  ```
3. Create a virtual environment:
  ```sh
  python -m venv env
  ```
4. Activate the virtual environment:
   
- On windows:
  ```sh
  .\env\Scripts\activate
  ```
- On mac and linux:
  ```sh
    source env/bin/activate 
  ```
5. Install the required dependencies:
  ```sh
    pip install -r requirements.txt
  ```
6. Apply the database migrations:
  ```sh
    python manage.py migrate
  ```
8. Create a superuser to access the admin panel:
  ```sh
    python manage.py createsuperuser
  ```
10. Start the development server:
  ```sh
    python manage.py runserver
  ```
