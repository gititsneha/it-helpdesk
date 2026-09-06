from flask import Flask, render_template, request, session, redirect
from werkzeug.security import check_password_hash
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return connection


def get_tickets(search="", category="", priority="", status=""):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM tickets WHERE 1=1"
    values = []

    if search:
        query += " AND (name LIKE %s OR title LIKE %s OR description LIKE %s)"
        search_value = "%" + search + "%"
        values.extend([search_value, search_value, search_value])

    if category:
        query += " AND category = %s"
        values.append(category)

    if priority:
        query += " AND priority = %s"
        values.append(priority)

    if status:
        query += " AND status = %s"
        values.append(status)

    query += " ORDER BY id DESC"

    cursor.execute(query, values)

    tickets = cursor.fetchall()

    cursor.close()
    connection.close()

    return tickets


# =========================
# HOME / TICKETS
# =========================

@app.route("/")
def home():

    if "username" not in session:
        return redirect("/login")

    search = request.args.get("search", "")
    category = request.args.get("category", "")
    priority = request.args.get("priority", "")
    status = request.args.get("status", "")

    tickets = get_tickets(
        search,
        category,
        priority,
        status
    )

    return render_template(
        "index.html",
        tickets=tickets,
        search=search,
        username=session["username"],
        role=session["role"]
    )


# =========================
# SUBMIT TICKET
# =========================

@app.route("/submit-ticket", methods=["POST"])
def submit_ticket():

    if "username" not in session:
        return redirect("/login")

    name = request.form["name"]
    title = request.form["title"]
    category = request.form["category"]
    priority = request.form["priority"]
    description = request.form["description"]

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO tickets
        (name, title, category, priority, description)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        name,
        title,
        category,
        priority,
        description
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/")


# =========================
# UPDATE STATUS - ADMIN
# =========================

@app.route("/update-status/<int:ticket_id>", methods=["POST"])
def update_status(ticket_id):

    if "username" not in session:
        return redirect("/login")

    if session["role"] != "admin":
        return "Access denied. Admins only.", 403

    status = request.form["status"]

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        UPDATE tickets
        SET status = %s
        WHERE id = %s
    """

    cursor.execute(
        query,
        (status, ticket_id)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/")


# =========================
# DELETE TICKET - ADMIN
# =========================

@app.route("/delete-ticket/<int:ticket_id>", methods=["POST"])
def delete_ticket(ticket_id):

    if "username" not in session:
        return redirect("/login")

    if session["role"] != "admin":
        return "Access denied. Admins only.", 403

    connection = get_db_connection()
    cursor = connection.cursor()

    query = "DELETE FROM tickets WHERE id = %s"

    cursor.execute(
        query,
        (ticket_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/")


# =========================
# LOGIN
# =========================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT *
            FROM users
            WHERE username = %s
        """

        cursor.execute(
            query,
            (username,)
        )

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user and check_password_hash(
            user["password"],
            password
        ):

            session["username"] = user["username"]
            session["role"] = user["role"]

            return redirect("/")

        return "Invalid username or password"

    return render_template("login.html")


# =========================
# ADMIN DASHBOARD
# =========================

@app.route("/admin")
def admin_dashboard():

    if "username" not in session:
        return redirect("/login")

    if session["role"] != "admin":
        return "Access denied. Admins only.", 403

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT COUNT(*) AS total FROM tickets"
    )
    total = cursor.fetchone()["total"]

    cursor.execute(
        "SELECT COUNT(*) AS open "
        "FROM tickets WHERE status = 'Open'"
    )
    open_tickets = cursor.fetchone()["open"]

    cursor.execute(
        "SELECT COUNT(*) AS in_progress "
        "FROM tickets WHERE status = 'In Progress'"
    )
    in_progress = cursor.fetchone()["in_progress"]

    cursor.execute(
        "SELECT COUNT(*) AS resolved "
        "FROM tickets WHERE status = 'Resolved'"
    )
    resolved = cursor.fetchone()["resolved"]

    cursor.execute(
        "SELECT COUNT(*) AS critical "
        "FROM tickets WHERE priority = 'Critical'"
    )
    critical = cursor.fetchone()["critical"]

    cursor.close()
    connection.close()

    return render_template(
        "admin.html",
        total=total,
        open_tickets=open_tickets,
        in_progress=in_progress,
        resolved=resolved,
        critical=critical
    )


# =========================
# TICKET DETAILS
# =========================

@app.route("/ticket/<int:ticket_id>")
def ticket_details(ticket_id):

    if "username" not in session:
        return redirect("/login")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT *
        FROM tickets
        WHERE id = %s
    """

    cursor.execute(
        query,
        (ticket_id,)
    )

    ticket = cursor.fetchone()

    cursor.close()
    connection.close()

    if not ticket:
        return "Ticket not found", 404

    return render_template(
        "ticket_details.html",
        ticket=ticket,
        username=session["username"],
        role=session["role"]
    )


# =========================
# LOGOUT
# =========================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# =========================
# RUN APPLICATION
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
