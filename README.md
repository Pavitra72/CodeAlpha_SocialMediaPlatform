# Social Media Platform

A mini social media web application built using Django, Python, HTML, CSS, and SQLite.

This project was developed as part of the CodeAlpha Full Stack Development Internship.

## 🚀 Features

- User registration and login
- User profiles
- Create posts
- Comments
- Like and unlike posts
- Follow and unfollow users
- Followers and following counts

## 🛠️ Technologies Used

- Python
- Django
- HTML5
- CSS3
- SQLite
- Git & GitHub
- Visual Studio Code

## 📂 Project Structure

```text
CodeAlpha_SocialMediaPlatform/
│
├── social/
│   ├── migrations/
│   ├── static/
│   │   └── social/
│   │       └── style.css
│   │
│   ├── templates/
│   │   └── social/
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       └── profile.html
│   │
│   ├── admin.py
│   ├── models.py
│   └── views.py
│
├── socialmedia/
│   ├── settings.py
│   └── urls.py
│
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt

## 🗄️ Database Models

The application uses the following models:

- User
- Profile
- Post
- Comment
- Like
- Follow

SQLite is used as the database during development.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL

### STEP 85 — Add the installation section

At the **bottom** of `README.md`, add:

````markdown
## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
````

### 2. Open the project folder

```bash
cd CodeAlpha_SocialMediaPlatform
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Start the server

```bash
python manage.py runserver
```

### 8. Open the application

```text
http://127.0.0.1:8000/
```


## 👩‍💻 Developer

**Pavitra Goud**

B.Tech Final Year Student

## 🏆 Internship Project

Developed as part of the **CodeAlpha Full Stack Development Internship**.

### Task 2: Social Media Platform

**Technologies:** Python | Django | HTML | CSS | SQLite