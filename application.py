from flask import Flask
import routes

# Initialize the application
app = Flask(__name__, template_folder="templates")

# Initialize blueprint
app.register_blueprint(routes.app)

# Run the application
if __name__ == "__main__":
    app.run(debug=True)