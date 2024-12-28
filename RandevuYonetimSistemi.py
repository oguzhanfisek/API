from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-OBLTQPD;" 
    "Database=RandevuYonetimSistemi;" 
    "Trusted_Connection=yes;"  
)

cursor = connection.cursor()

@app.route("/randevuyonetimsistemi", methods=["GET"])
def get_table1():
    cursor.execute("SELECT * FROM table1")  
    rows = cursor.fetchall()  
    print(rows)  
    table1_data = []
    
    for row in rows:
        table1_data.append({
            "id": row[0],
            "user_id": row[1],
            "date": row[2],
            "time": row[3].strftime('%H:%M:%S') if row[3] else None,
            "description": row[4]
        })
    
    return jsonify(table1_data) 

@app.route("/randevuyonetimsistemi", methods=["POST"])
def add_to_table1():
    if not request.is_json:  
        return jsonify({"message": "Content-Type must be 'application/json'"}), 415

    data = request.get_json()  

    try:
        cursor.execute(
            """
            INSERT INTO table1 (user_id, date, time, description)
            VALUES (?, ?, ?, ?)
            """,
            data["user_id"], data["date"], data["time"], data["description"]
        )
        connection.commit()  
        return jsonify({"message": "Yeni randevu başarıyla eklendi!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/randevuyonetimsistemi/<int:id>", methods=["PUT"])
def update_table1(id):
    data = request.get_json() 

    try:
        cursor.execute(
            """
            UPDATE table1
            SET user_id = ?, date = ?, time = ?, description = ?
            WHERE id = ?
            """,
            data["user_id"], data["date"], data["time"], data["description"], id
        )
        connection.commit()
        return jsonify({"message": "Randevu başarıyla güncellendi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/randevuyonetimsistemi/<int:id>", methods=["DELETE"])
def delete_from_table1(id):
    try:
        cursor.execute("DELETE FROM table1 WHERE id = ?", id)  
        connection.commit()
        return jsonify({"message": "Randevu başarıyla silindi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
