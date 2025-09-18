📝 Flask To-Do App with GUI & Docker

A simple Flask web application with a PostgreSQL database, fully dockerized.
You can add, complete, and delete tasks from a browser GUI.
Perfect for learning Flask, PostgreSQL, and Docker together.

---

🚀 Features
- ✅ Browser-based GUI for managing tasks
- 🐘 PostgreSQL database container
- 🔄 CRUD operations: Create, Read, Update, Delete tasks
- 🐳 Fully Dockerized with Docker Compose

---

🗂️ Project Structure

flask-todo-gui/
│── app/
│   ├── app.py
│   ├── models.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── templates/
│       ├── index.html
│       └── layout.html
└── docker-compose.yml

---

⚙️ Setup & Run

1️⃣ Clone the repository
git clone https://github.com/nitinthomas20/Flask_Docker_App.git
cd flask-todo-gui

2️⃣ Build and start containers
docker compose up --build

3️⃣ Open the app in your browser:
http://localhost:5000

---

🖥️ Usage

- Add a task: Enter a task in the input box and click "Add"
- Complete/uncomplete a task: Click the ✔ button next to the task
- Delete a task: Click the 🗑 button next to the task

Optional: API Endpoints (for testing)
Method | URL | Description
-------|-----|------------
GET    | /tasks | List all tasks
POST   | /tasks | Add a new task (JSON: {"title":"Task Name"})
PUT    | /tasks/<id> | Update task completion (JSON: {"completed": true})
DELETE | /tasks/<id> | Delete a task

---

🛠️ Tech Stack
- 🐍 Python 3.11
- 🔹 Flask
- 🐘 PostgreSQL 15
- 🐳 Docker & Docker Compose
- 📄 Jinja2 Templates for GUI

---

🔧 Docker Notes
- Web container: Flask app on port 5000
- DB container: PostgreSQL on port 5432
- Flask connects to Postgres using service name 'db'
- Stop containers: docker compose down
- Rebuild containers: docker compose up --build

---

✨ Optional Enhancements
- 💾 Add Docker volumes to persist PostgreSQL data
- 🎨 Improve UI styling with CSS
- 🔐 Add authentication for multiple users
- 📝 Use Flask-WTF for form validation

---

📜 License
This project is for learning purposes. Feel free to use, modify, and experiment.

---

Made with ❤️ using Flask, PostgreSQL, and Docker
