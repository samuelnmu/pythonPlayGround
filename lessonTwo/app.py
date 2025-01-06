from flask import Flask, render_template, request  # Import necessary Flask modules

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route("/")
def index():
    """
    Renders the index.html page where the user can input their name.
    """
    return render_template("index.html")  # Render the index.html template

# Define the route for the greeting page
@app.route("/greet", methods=["POST"])
def greet():
    """
    Retrieves the user's name from the form and renders the greet.html page.
    If no name is provided, a default name ('Guest') is used.
    """
    # Get the value of the 'Name' parameter from the form submission (POST method)
    name = request.form.get("Name", "Guest")
    # Render the greet.html template, passing the name to it
    return render_template("greet.html", name=name)

# Run the application in debug mode when executed directly
if __name__ == "__main__":
    # Starts the Flask development server with debugging enabled
    app.run(debug=True)
