
## Overview

The roadmaping web app is designed to help users track their courses and set goals for their learning. Users can sign up for an account, log in, and add courses to their dashboard. They can also set goals for each course and track their progress over time. The app provides a visual roadmap for each course, showing the user what they need to learn and when they need to learn it.

## Features

- User authentication (sign up, log in, log out)
- Dashboard for tracking courses
- Course details page with progress tracking and goal setting
- Visual roadmap for each course
- Admin panel for managing users and courses

## Technologies

- Python
- Flask
- SQLAlchemy
- Jinja2
- HTML/CSS/JavaScript
- Materialize CSS

## How to Run

Here are the basic commands to set up and run the app:

1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (on Windows, use `venv\Scripts\activate`)
4. Install the required packages: `pip install -r requirements.txt`
5. Set up the database: `flask db upgrade`
6. Launch the app: `flask run`

Note: You may need to set the `FLASK_APP` environment variable to the name of your Flask app (e.g. `export FLASK_APP=app.py` on Linux/Mac or `set FLASK_APP=app.py` on Windows) before running the `flask` commands.