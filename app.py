from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# ---------------------- DB CONNECTION ----------------------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mumthaj@786",
        database="golden_plate"
    )

# ---------------------- WEB PAGES ----------------------

@app.route("/")
def home(): 
    return render_template("index.html")

@app.route("/menu.html")
def menu():
    return render_template("menu.html")

@app.route("/gallery.html")
def gallery():
    return render_template("gallery.html")

@app.route("/booking.html")
def booking():
    return render_template("booking.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")


# ---------------------- SAVE BOOKING ----------------------
@app.route("/save_booking", methods=["POST"])
def save_booking():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    date = request.form["date"]
    time = request.form["time"]
    guests = request.form["guests"]
    message = request.form["message"]

    conn = get_db_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO reservations (name, email, phone, date, time, guests, message)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (name, email, phone, date, time, guests, message)
    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()

    return render_template("booking.html", success=True)

# ---------------------- RUN APP ----------------------
if __name__ == "__main__":
    app.run(debug=True)
