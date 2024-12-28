from flask import Flask, request, jsonify
import pyodbc

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-OBLTQPD;"
    "Database=AracKiralamaSistemi;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()
print("sql bağlantısı oldu", cursor)

app = Flask(__name__)

@app.route("/arackiralamasistemi", methods= ["GET"])
def get_AracKiralamaSistemi():
    cursor.execute("SELECT * FROM Araclar")
    Araclar= [
        {
            "id": row[0],
            "marka": row[1],
            "model": row[2],
            "yil": row[3],
        }
        for row in cursor.fetchall()
    ]
    return jsonify(Araclar)

if __name__ =="__main__":
    app.run(debug=True)

@app.route("/arackiralamasistemi", methods=["POST"])
def post_AracKiralamaSistemi():
    data = request.get_json()

    cursor.execute(
        """
        INSERT INTO Araclar (marka, model, yil)
        VALUES (?, ?, ?)
        """,
        data["marka"], data["model"], data["yil"]
    )
    connection.commit()

    return jsonify({"message": "Araç başarıyla eklendi!"}), 201


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/arackiralamasistemi/<int:id>", methods=["PUT"])
def put_AracKiralamaSistemi(id):
    data = request.get_json()

    cursor.execute(
        """
        UPDATE Araclar
        SET marka = ?, model = ?, yil = ?
        WHERE id = ?
        """,
        data["marka"], data["model"], data["yil"], id
    )
    connection.commit()

    return jsonify({"message": "Araç bilgileri başarıyla güncellendi!"})


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/arackiralamasistemi/<int:id>", methods=["DELETE"])
def delete_AracKiralamaSistemi(id):
    cursor.execute(
        "DELETE FROM Araclar WHERE id = ?",
        id
    )
    connection.commit()

    return jsonify({"message": "Araç başarıyla silindi!"})


if __name__ == "__main__":
    app.run(debug=True)
