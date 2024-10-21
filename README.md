# Django Asset Management System

A Django-based web application that allows companies to manage their assets efficiently. This system offers features like adding, editing, deleting assets, and managing asset lending to employees while enforcing business rules to prevent conflicting borrowing dates.

## Features
- Add, edit, and delete company assets.
- Assign assets to employees and mark them as returned.
- Ensure that assets are not lent out during overlapping timeframes, preventing conflicting dates.

## Screenshots

### Dashboard
![Dashboard Screenshot](screenshots/main.png)

<!-- ### Asset Management
![Asset Management Screenshot](path/to/screenshot2.png) -->

## Prerequisites

Before running this project, make sure you have the following installed:
- Python 3.x
- Django 4.x+
- Virtualenv (optional but recommended)

## Installation and Setup

1. **Clone the repository:**

    ```bash
    git clone git@github.com:mostafanawam/assets_ms.git
    cd assets_ms
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    or 

    ```bash
    make install
    ```
4. **Apply migrations:**

    ```bash
    python manage.py makemigrations && python manage.py migrate
    ```
    or 

    ```bash
    make setup

5. **Create a superuser for the admin panel:**

    ```bash
    python manage.py createsuperuser
    ```


6. **(Optional) load testing fixtures(load assets and employees data):**

    ```bash
    python manage.py loaddata */fixtures/*.test.json
    ```
    or 

    ```bash
    make load-testing
    ```



7. **Run the development server:**

    ```bash
    python manage.py runserver localhost:8050
    ```
    or 

    ```bash
    make backend-server-start
    ```

8. **Access the app in your browser:**

    Open your web browser and go to `http://localhost:8050/`.

## Usage

1. **Login:**
   - Use the credentials you created with the superuser during the setup to log in to the dashboard.
   - Navigate to `http://localhost:8050/` and enter your superuser credentials.

2. **Dashboard:**
   - Once logged in, you will be able to manage company assets and asset lending via the dashboard.

   - **Manage Assets**: 
        - Add, update, or delete company assets.
        - **Note**: You cannot delete an asset if it is currently lent out. The asset must be marked as returned before it can be deleted.
   
   - **Manage Asset Lending**: 
     - Assign assets to employees.
     - Mark assets as returned when they are no longer in use.
     - The system will enforce business rules to prevent overlapping borrowing dates.

3. **Adding Employees**:
   - If you haven't loaded the testing fixtures mentioned earlier, you will need to visit `http://localhost:8050/admin/` to add new employees.
   - After logging in with your superuser credentials, navigate to the Employee section and add new employees as needed.