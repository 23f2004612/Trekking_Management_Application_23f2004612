# Author - Kaushik K.S.

# Trekking Management System

## Overview

The Trekking Management System is a full-stack web application developed to streamline the management of trekking activities for administrators, staff members, and users. The application provides role-based access control, trek management, booking management, reporting, and asynchronous background processing.

The project follows a client-server architecture with a Vue.js frontend and Flask backend connected through REST APIs.

---

## Tech Stack

### Frontend
- Vue 3
- Vue Router
- Pinia
- Bootstrap 5
- Axios

### Backend
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Marshmallow
- Flask-Migrate

### Database
- SQLite

### Background Services
- Celery
- Redis

### Other Libraries
- Marshmallow
- Docker
- Bootstrap Icons

---

# Features

## Authentication

- User Registration
- Login for Admin, Staff and Users
- Role-based Authentication
- Protected Routes
- Session Management
- User Blacklisting Support

---

## Admin Module

### Dashboard

- Dashboard summary
- Total Users
- Total Staff
- Total Treks
- Total Bookings

### Trek Management

- View all treks
- Add new trek
- Edit trek details
- Delete trek
- Assign trek to staff members
- Search treks

### Staff Management

- View all staff
- Add staff
- Edit staff
- Activate / Blacklist staff
- Search staff

### User Management

- View registered users
- Activate / Blacklist users
- Search users

---

## Staff Module

### Dashboard

- View assigned treks
- Trek summary

### Assigned Treks

- Search assigned treks
- View trek information
- Manage trek details
- Update available slots
- Change trek status (Open / Closed)
- Mark trek as Completed

### Participants

- View registered participants for assigned treks
- Search participants

---

## User Module

### Browse Treks

- View all available treks
- Search treks
- Filter treks by
  - Difficulty
  - Location
  - Duration

### Booking

- Book available treks
- Prevent duplicate bookings
- Slot availability validation
- Re-book cancelled treks

### Booking History

- View booking history
- Cancel booked treks
- Export booking history as CSV

### Profile

- View profile
- Update profile information

---

# Backend Features

## REST APIs

Role-based REST APIs implemented for:

- Authentication
- Admin
- Staff
- Users

---

## Database

Models implemented for

- User
- Trek
- Booking

Relationships established using SQLAlchemy ORM.

---

## Validation

Server-side validation includes

- Duplicate booking prevention
- Slot availability checks
- Email uniqueness
- Trek status validation
- Role authorization

---

## Caching

Redis caching implemented for

- Available treks
- Dashboard summaries

Cache invalidation performed whenever relevant data is modified.

---

## Background Tasks

Celery tasks implemented for

- Booking history export
- Daily reminders
- Monthly reports

---

# Frontend Features

- Responsive interface
- Dashboard layouts for Admin, Staff and User
- Sidebar navigation
- Search functionality
- Empty state components
- Loading indicators
- Toast notifications
- Reusable modal components
- Reusable table components

---

# Security

- Role-based route protection
- Backend authorization decorators
- Login required for protected APIs
- Restricted access based on user role

---

# Project Structure

```
Frontend
│
├── components
├── services
├── store
├── views
└── router

Backend
│
├── controllers
├── models
├── routes
├── schemas
├── tasks
├── decorators
├── utils
└── extensions
```

---

# API Highlights

### Admin

- Dashboard
- Trek CRUD
- Staff Management
- User Management

### Staff

- Dashboard
- Assigned Treks
- Trek Management
- Participant List
- Trek Completion

### User

- Browse Treks
- Search Treks
- Book Trek
- Booking History
- Cancel Booking
- Export History
- Profile Management

---

# Key Functionalities Implemented

- Role-based Authentication
- Trek Management
- Staff Assignment
- Trek Booking
- Booking History
- Booking Cancellation
- CSV Export
- Search and Filtering
- Dashboard Analytics
- Profile Management
- Cache Management
- Background Task Processing

---

# Future Enhancements

- Trek image uploads
- Email notifications
- Online payment integration
- Trek reviews and ratings
- Admin analytics dashboard
- Real-time booking updates

---

# Running the Project

## Backend

```bash
pip install -r requirements.txt

flask db upgrade

python app.py
```

## Redis

```bash
docker start redis
```

## Celery Worker

```bash
celery -A tasks.celery_app worker --loglevel=info
```

## Frontend

```bash
npm install

npm run dev
```
---