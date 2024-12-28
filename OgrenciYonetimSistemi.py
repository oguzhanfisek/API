from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-OBLTQPD;"  
    "Database=OgrenciYonetimSistemi;" 
    "Trusted_Connection=yes;"  
)

cursor = connection.cursor()

@app.route("/ogrenciyonetimsistemi", methods=["GET"])
def get_Table1():
    cursor.execute("SELECT * FROM Table1")  
    students = [
        {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "email": row[3],
            "enrollment_date": row[4],
        }
        for row in cursor.fetchall()
    ]
    return jsonify(students)

@app.route("/ogrenciyonetimsistemi", methods=["POST"])
def add_Student():
    if not request.is_json: 
        return jsonify({"message": "Content-Type must be 'application/json'"}), 415

    data = request.get_json()  

    try:
        cursor.execute(
            """
            INSERT INTO Table1 (first_name, last_name, email, enrollment_date)
            VALUES (?, ?, ?, ?)
            """,
            data["first_name"], data["last_name"], data["email"], data["enrollment_date"]
        )
        connection.commit()  
        return jsonify({"message": "Yeni öğrenci başarıyla eklendi!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/ogrenciyonetimsistemi/<int:id>", methods=["PUT"])
def update_Student(id):
    data = request.get_json()  

    try:
        cursor.execute(
            """
            UPDATE Table1
            SET first_name = ?, last_name = ?, email = ?, enrollment_date = ?
            WHERE id = ?
            """,
            data["first_name"], data["last_name"], data["email"], data["enrollment_date"], id
        )
        connection.commit()
        return jsonify({"message": "Öğrenci başarıyla güncellendi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/ogrenciyonetimsistemi/<int:id>", methods=["DELETE"])
def delete_Student(id):
    try:
        cursor.execute("DELETE FROM Table1 WHERE id = ?", id)  
        connection.commit()
        return jsonify({"message": "Öğrenci başarıyla silindi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
