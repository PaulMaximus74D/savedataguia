import csv

def save_to_csv(data):
    fieldnames = ['guide-number', 'date', 'sender', 'recipient', 'origin', 'destination', 'city', 'content', 'packages', 'weight', 'amount', 'return']

    try:
        with open('RESUMEN.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Verificar si es la primera vez que se escribe en el archivo
            if csvfile.tell() == 0:
                writer.writeheader()
            
            writer.writerow(data)
        
        print('Datos guardados en RESUMEN.csv')
    
    except Exception as e:
        print(f'Error al guardar los datos: {e}')