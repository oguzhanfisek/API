from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-OBLTQPD;"  
    "Database=SiparisYonetimSistemi;"  
    "Trusted_Connection=yes;"  
)

cursor = connection.cursor()

@app.route("/siparisyonetimsistemi", methods=["GET"])
def get_Orders():
    cursor.execute("SELECT * FROM Orders") 
    orders = [
        {
            "id": row[0],
            "product_id": row[1],
            "quantity": row[2],
            "total_price": row[3],
        }
        for row in cursor.fetchall()
    ]
    return jsonify(orders)

@app.route("/siparisyonetimsistemi", methods=["POST"])
def add_Order():
    if not request.is_json:  
        return jsonify({"message": "Content-Type must be 'application/json'"}), 415

    data = request.get_json() 

    try:
        cursor.execute(
            """
            INSERT INTO Orders (id, product_id, quantity, total_price)
            VALUES (?, ?, ?, ?)
            """,
            data["id"], data["product_id"], data["quantity"], data["total_price"]
        )
        connection.commit()  
        return jsonify({"message": "Yeni sipariş başarıyla eklendi!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/siparisyonetimsistemi/<int:id>", methods=["PUT"])
def update_Orders(id):
    data = request.get_json()  

    try:
        cursor.execute(
            """
            UPDATE Orders
            SET product_id = ?, quantity = ?, total_price = ?
            WHERE id = ?
            """,
            data["product_id"], data["quantity"], data["total_price"], id
        )
        connection.commit()
        return jsonify({"message": "Sipariş başarıyla güncellendi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/siparisyonetimsistemi/<int:id>", methods=["DELETE"])
def delete_Orders(id):
    try:
        cursor.execute("DELETE FROM Orders WHERE id = ?", id)  
        connection.commit()
        return jsonify({"message": "Sipariş başarıyla silindi!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
