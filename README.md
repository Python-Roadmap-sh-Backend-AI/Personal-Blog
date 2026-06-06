# Personal Blog Project

A simple personal blog web app built with Flask and Markdown files.

## Overview

This project lets a user create, edit, delete, and view blog articles without using a database. Articles are stored as Markdown files in the `articles/` folder, and Flask renders them into HTML.

## Features

### Public Area

- Home page that lists all published articles
- Individual article page with readable content
- Markdown-to-HTML rendering for posts

### Admin Area

- Login page with simple session-based authentication
- Dashboard for managing articles
- Add new articles
- Edit existing articles
- Delete articles

## How It Works

### Article Storage

Each blog post is saved as a separate `.md` file inside `articles/`.

Example:

```text
articles/python_basics.md
```

Each article file contains:

- Title
- Date of publication
- Markdown content

### Workflow

#### Guest Flow

1. The user visits the home page.
2. Flask reads all `.md` files from `articles/`.
3. Articles are shown as a list.
4. Clicking an article opens the full post.
5. Markdown is converted to HTML before display.

#### Admin Flow

1. Admin visits `/login`.
2. Admin enters username and password.
3. Flask checks the credentials and creates a session.
4. Admin is redirected to `/dashboard`.
5. From the dashboard, the admin can add, edit, or delete articles.

## Authentication

The app uses Flask sessions for login state.

Credentials:

```python
USERNAME = "admin"
PASSWORD = "12345"
```

Logged-in state:

```python
session["admin"] = True
```

Only logged-in users can access admin routes.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Markdown
- File system storage

## Run Locally

### 1. Clone the project

```bash
git clone <your-repo-url>
cd personal-blog
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install flask markdown
```

### 5. Run the app

```bash
python app.py
```

### 6. Open in your browser

```text
http://127.0.0.1:5000
```

## Admin Login

- Username: `admin`
- Password: `12345`

## Project Summary

- File-based blog system with no database
- Markdown support for writing articles
- Session-based admin authentication
- CRUD features for articles
- Separate public and admin views


Thank You!
