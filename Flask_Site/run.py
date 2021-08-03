from flaskwebsite import app, db

#only true if we run this script directly
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
