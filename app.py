from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path="/static", static_folder="static")

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Define the User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Create the SQLite database tables
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # In a production application, you should hash the password before storing it.
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Redirect to the user dashboard upon successful registration
        return redirect(url_for("dashboard"))

    return render_template("signup.html")

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # In a production application, you should hash the password for security.
        user = User.query.filter_by(username=username, password=password).first()

        if user:
            # Redirect to the user dashboard upon successful login
            return redirect(url_for("dashboard"))

    return render_template("signin.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/track-courses", methods=["GET", "POST"])
def track_courses():
    if request.method == "POST":
        course_name = request.form["course_name"]
        platform = request.form["platform"]
        progress = request.form["progress"]

        # Store tracked course data in the database or another suitable storage.
        # For a production application, you should consider using a more structured database model.
        tracked_courses[course_name] = {
            "platform": platform,
            "progress": progress
        }

    return render_template("track_courses.html", tracked_courses=tracked_courses)

@app.route("/set-goals", methods=["GET", "POST"])
def set_goals():
    if request.method == "POST":
        goal_name = request.form["goal_name"]
        target_date = request.form["target_date"]
        resources_needed = request.form["resources_needed"]

        # Store user goal data in the database or another suitable storage.
        # For a production application, you should use a structured model for goals.
        user_goals[goal_name] = {
            "target_date": target_date,
            "resources_needed": resources_needed
        }

    return render_template("set_goals.html", user_goals=user_goals)

@app.route("/generate-roadmap")
def generate_roadmap():
    # Customized roadmap generation logic
    # Implement algorithms or rules to suggest a learning roadmap
    return render_template("generate_roadmap.html", tracked_courses=tracked_courses, user_goals=user_goals)

if __name__ == '__main__':
    app.run(debug=True)
