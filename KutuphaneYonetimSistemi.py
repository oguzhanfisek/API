from flask import Flask, request, jsonify
import pyodbc

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-OBLTQPD;"
    "Database=Kutuphaneyonetimsistemi;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()
print("sql bağlantısı oldu", cursor)

app = Flask(__name__)

@app.route("/kutuphaneyonetimsistemi", methods=["GET"])
def get_Kitaplar():
    cursor.execute("SELECT * FROM Kitaplar")
    Kitaplar = [
        {
            "id": row[0],
            "ad": row[1],
            "yazar": row[2],
            "kategori": row[3],
            "adet": row[4]
        }
        for row in cursor.fetchall()
    ]
    return jsonify(Kitaplar)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/kutuphaneyonetimsistemi", methods=["POST"])
def add_Kitap():
    data = request.get_json() 

    cursor.execute(
        """
        INSERT INTO Kitaplar (ad, yazar, kategori, adet)
        VALUES (?, ?, ?, ?)
        """, 
        data["ad"], data["yazar"], data["kategori"], data["adet"]
    )
    connection.commit()  

    return jsonify({"message": "Yeni kitap başarıyla eklendi!"}), 201

@app.route("/kutuphaneyonetimsistemi/<int:id>", methods=["PUT"])
def update_Kitap(id):
    data = request.get_json() 

    cursor.execute(
        """
        UPDATE Kitaplar
        SET ad = ?, yazar = ?, kategori = ?, adet = ?
        WHERE id = ?
        """, 
        data["ad"], data["yazar"], data["kategori"], data["adet"], id
    )
    connection.commit() 

    return jsonify({"message": "Kitap başarıyla güncellendi!"})

@app.route("/kutuphaneyonetimsistemi/<int:id>", methods=["DELETE"])
def delete_Kitap(id):
    cursor.execute("DELETE FROM Kitaplar WHERE id = ?", id)
    connection.commit() 

    return jsonify({"message": "Kitap başarıyla silindi!"})

