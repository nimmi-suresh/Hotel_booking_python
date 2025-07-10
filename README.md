# Hotel Room Booking Web Application

A simple Hotel Room Booking web application built using **Django**. The system allows users to search for rooms, check pricing, register and book rooms, and view their booking history. Admins can register hotels and manage room details. The application uses **SQLite3** as its database and has a minimal frontend built with basic HTML and CSS.

---

## Features

* Hotel and Room Registration (Admin)
* Room Availability Search (No login required)
* Room Booking (Login required)
* Pricing Check (No login required)
* User Booking History (Previous & Upcoming)

---

## Technologies Used

* **Backend:** Python, Django
* **Frontend:** HTML, CSS (basic)
* **Database:** SQLite3

---

## Project Structure

```
hotel_booking/
├── booking/               # Django app for booking features
│   ├── migrations/
│   ├── templates/
│   │   └── booking/
│   │       └── home.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── hotel_booking/         # Project settings and URLs
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3             # SQLite database
├── manage.py              # Django command-line utility
└── venv/                  # Virtual environment (not pushed to GitHub)
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/nimmi-suresh/hotel_booking.git
cd hotel_booking
```

### 2. Create a virtual environment and activate it

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Django

```bash
pip install django
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000`

---

## License

This project is for educational purposes. Feel free to modify and use it as needed.
