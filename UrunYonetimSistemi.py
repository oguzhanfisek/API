from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-OBLTQPD;"  
    "Database=UrunYonetimSistemi;" 
    "Trusted_Connection=yes;"  
)

cursor = connection.cursor()

@app.route("/urunyonetimsistemi", methods=["GET"])
def get_Products():
    cursor.execute("SELECT * FROM Table1")  
    products = [
        {
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "price": row[3],
            "stock_quantity": row[4],
        }
        for row in cursor.fetchall()
    ]
    return jsonify(products)

@app.route("/urunyonetimsistemi", methods=["POST"])
def add_Product():
    if not request.is_json: 
        return jsonify({"message": "Content-Type must be 'application/json'"}), 415

    data = request.get_json() 

    try:
        cursor.execute(
            """
            INSERT INTO Table1 (name, description, price, stock_quantity)
            VALUES (?, ?, ?, ?)
            """,
            data["name"], data["description"], data["price"], data["stock_quantity"]
        )
        connection.commit()  
        return jsonify({"message": "Yeni ürün başarıyla eklendi!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/urunyonetimsistemi/<int:id>", methods=["PUT"])
def update_Product(id):
    data = request.get_json()  

    try:
        cursor.execute(
            """
            UPDATE Table1
            SET name = ?, description = ?, price = ?, stock_quantity = ?
            WHERE id = ?
            """,
            data["name"], data["description"], data["price"], data["stock_quantity"], id
        )
        connection.commit()
        return jsonify({"message": "Ürün başarıyla güncellendi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/urunyonetimsistemi/<int:id>", methods=["DELETE"])
def delete_Product(id):
    try:
        cursor.execute("DELETE FROM Table1 WHERE id = ?", id)  
        connection.commit()
        return jsonify({"message": "Ürün başarıyla silindi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
