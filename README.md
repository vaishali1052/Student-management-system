# Django Student Management System 👨‍🎓

A modern Student Management System built with Django — featuring an interactive dashboard, attendance management, feedback system, result generation, leave management, and more.

---

## Features

### A. Admin / HOD Can:
- View overall summary dashboard with charts (Students, Staff, Courses, Subjects, Attendance, Leaves)
- **Manage Staff** — Add, Update, Delete
- **Manage Students** — Add, Update, Delete
- **Manage Courses** — Add, Update, Delete
- **Manage Subjects** — Add, Update, Delete
- **Manage Session Years** — Add, Update, Delete
- **View Student Attendance** — by Subject and Session Year
- **Review & Reply** to Student Feedback
- **Review & Reply** to Staff Feedback
- **Send Broadcast Message** to All Students or All Staff at once
- **Approve / Reject** Student Leave Requests
- **Approve / Reject** Staff Leave Requests
- View who is currently on leave (Students & Staff)
- **Send Notifications** to individual Students or Staff

---

### B. Staff / Teachers Can:
- View overall summary dashboard (students, subjects, attendance, leave status)
- **Take Attendance** for their subjects
- **Update Attendance** for their subjects
- **Add / Update Student Results**
- **Apply for Leave** (with leave type: Sick, Casual, Medical, Emergency, etc.)
- View leave history and status (Pending / Approved / Rejected)
- **Send Feedback to HOD**
- **View Feedback from Students** sent directly to them
- **Reply to Student Feedback**
- View Notifications from HOD

---

### C. Students Can:
- View overall summary dashboard (attendance, subjects, leave status)
- **View Attendance** by subject and date range
- **View Results / Grade Card**
- **Apply for Leave** (with leave type: Sick, Casual, Medical, Exam, Sports, etc.)
- View leave history and status (Pending / Approved / Rejected)
- **Send Feedback to HOD**
- **Send Feedback to a specific Staff member**
- View replies from HOD and Staff on their feedback
- View Notifications from HOD

---

## Tech Stack
- **Backend:** Python 3.10, Django 4.1
- **Database:** SQLite (default) / PostgreSQL
- **Frontend:** Bootstrap 4, AdminLTE, Chart.js, jQuery

---

## Quick Start

```bash
# Clone the repo
git clone <repo-url>
cd Student_Management_System

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run the server
python manage.py runserver
```

Open `http://127.0.0.1:8000` in your browser.

---

## Default Login Credentials

| Role | Email | Password |
|------|-------|----------|
| Admin / HOD | `admin@gmail.com` | `admin123` |
| Staff | `mitansh@gmail.com` | `admin123` |
| Student | `abhishek@gmail.com` | `admin123` |

---

## License

MIT License — feel free to use and modify.
