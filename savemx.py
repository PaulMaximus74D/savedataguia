from flask import Flask, request
import csv
import os

app = Flask(__name__)

@app.route('/save_data', methods=['POST'])
def save_to_csv():
    data = request.json
    file_exists = os.path.isfile('RESUMEN.csv')

    with open('RESUMEN.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            # Escribir el encabezado solo si el archivo no existe
            writer.writerow(data.keys())
        
        # Escribir los datos
        writer.writerow(data.values())

    return {'message': 'Datos guardados exitosamente'}

if __name__ == '__main__':
    app.run(debug=True)
