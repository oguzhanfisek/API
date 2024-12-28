from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-OBLTQPD;" 
    "Database=KategoriYonetimSistemi;" 
    "Trusted_Connection=yes;"  
)

cursor = connection.cursor()

@app.route("/categories", methods=["GET"])
def get_categories():
    cursor.execute("SELECT * FROM categories")  
    categories = [
        {
            "id": row[0],
            "name": row[1],
            "description": row[2]
        }
        for row in cursor.fetchall()
    ]
    return jsonify(categories)

@app.route("/categories", methods=["POST"])
def add_category():
    if not request.is_json: 
        return jsonify({"message": "Content-Type must be 'application/json'"}), 415

    data = request.get_json()  

    try:
        cursor.execute(
            """
            INSERT INTO categories (name, description)
            VALUES (?, ?)
            """,
            data["name"], data["description"]
        )
        connection.commit()  
        return jsonify({"message": "Yeni kategori başarıyla eklendi!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/categories/<int:id>", methods=["PUT"])
def update_category(id):
    data = request.get_json() 

    try:
        cursor.execute(
            """
            UPDATE categories
            SET name = ?, description = ?
            WHERE id = ?
            """,
            data["name"], data["description"], id
        )
        connection.commit()
        return jsonify({"message": "Kategori başarıyla güncellendi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/categories/<int:id>", methods=["DELETE"])
def delete_category(id):
    try:
        cursor.execute("DELETE FROM categories WHERE id = ?", id)  
        connection.commit()
        return jsonify({"message": "Kategori başarıyla silindi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
