from app import app
import populate_database

if __name__ == "__main__":
    app.secret_key = "super_secret_key"
    app.run(host="localhost", port=5000, debug=True)
