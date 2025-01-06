from flask import Flask, request, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define routes for the homepage
@app.route("/")
def index():
    """
    Render the homepage with the registration form.
    """
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def greet():
    """
    Handle form submission for registration.
    Validate the name and selected sport.
    """
    # Validate submission
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name or sport not in ["Basketball", "Monopoly", "Chess", "Hockey"]:
        return render_template("failure.html")

    # Confirm registration
    return render_template("success.html", name=name, sport=sport)

# Run the application in debug mode
if __name__ == "__main__":
    app.run(debug=True)
