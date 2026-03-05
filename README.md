# 🌱 Kindergarten Management System

A simple web application built with **Django** for managing basic kindergarten operations. Currently in early development (v0.1).

> 🇺🇿 **Note:** This project is written in the **Uzbek language** by default. All UI text, admin panel labels, form fields, and error messages are in Uzbek. If you want to use this project in another language, you are free to replace the Uzbek text with your own language in the templates and models.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [Project Structure](#project-structure)
- [Localization](#localization)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 About the Project

The **Kindergarten Management System** is a Django-based web app for handling basic kindergarten administration. It features a clean, responsive frontend with smooth single-page scroll navigation on the homepage, and uses Django's built-in admin panel for data management.

> ⚠️ This project is in early development — version **0.1**. Some features are planned but not yet implemented.

---

## ✨ Features (v0.1)

- 🎨 **Responsive Frontend** — Clean, well-designed HTML/CSS interface
- 🧭 **Smart Navbar** — Scrolls to sections on homepage, navigates to pages from elsewhere
- 💬 **Contact Form** — Visitors can send messages directly to staff via email
- 🛠️ **Django Admin Panel** — Standard Django data administration
- 🔐 **User Authentication** — Secure login and registration
- 📰 **News Section** — Display kindergarten news and announcements
- 🖼️ **Gallery** — Photo gallery of the kindergarten
- 👩‍🏫 **Staff Section** — Display staff profiles with social links
- 📍 **Contact Page** — Location, phone, email and contact form

---

## 🛠️ Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | Python 3.12, Django               |
| Frontend   | HTML, CSS, JavaScript, Bootstrap  |
| Database   | SQLite (default)                  |
| Auth       | Django Auth System                |
| Images     | Pillow                            |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Git

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/WeskerPRO/KinderGarten_FirstSite.git
cd KinderGarten_FirstSite
```

2. **Create and activate a virtual environment**

```bash
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply database migrations**

```bash
python manage.py migrate
```

5. **Create a superuser** (for admin access)

```bash
python manage.py createsuperuser
```

### Running the App

```bash
python manage.py runserver
```

Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Admin panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 📁 Project Structure

```
KinderGarten_FirstSite/
│
├── Kinder_garden_first/   # Main Django settings folder
│   ├── settings.py        # Project settings
│   ├── urls.py            # Root URL routing
│   └── wsgi.py
│
├── main/                  # Main app
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── forms.py           # Django forms
│   └── admin.py           # Admin configuration
│
├── templates/             # HTML templates
│   ├── base.html          # Base template (navbar, footer, CSS/JS)
│   ├── index.html         # Homepage
│   ├── index-staff.html   # Staff page
│   ├── index-news.html    # News page
│   ├── index-galary.html  # Gallery page
│   └── index-contact.html # Contact page
│
├── static/                # CSS, JS, images
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🌐 Localization

This project is fully written in **Uzbek** by default. This includes:

- All HTML template text
- Admin panel field names and help texts
- Form labels and error messages
- Model verbose names

**Want to use a different language?** You can easily change it:

- **Templates** — find Uzbek text in `/templates/*.html` and replace with your language
- **Models** — field labels like `'Ismi '` (name) or `'Vazifasi '` (position) are in `main/models.py`
- **Forms** — form labels and error messages are in `main/forms.py`
- **Settings** — to change the default language, update `LANGUAGE_CODE` in `settings.py`:

```python
# settings.py
LANGUAGE_CODE = 'en-us'  # change from 'uz' to your language code
```

No other configuration is required — just replace the text and you're good to go!

---

## 🗺️ Roadmap

This project is actively being developed. Planned features for future versions:

- [ ] 👨‍👩‍👧 Parent portal
- [ ] 📅 Attendance tracking
- [ ] 👶 Child/student profile management
- [ ] 📊 Reporting & statistics
- [ ] 🤖 AI bot for answering parent questions
- [ ] 📱 Flutter mobile app for parents

---

## 🤝 Contributing

1. Fork the project
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> © 2026 Bakhodirov Shakhzod — v0.1
