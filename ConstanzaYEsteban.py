import requests

def obtener_info_viaje(origen, destino, api_key):
    url = f"https://graphhopper.com/api/1/route?point={origen}&point={destino}&vehicle=car&locale=es&calc_points=false&key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        distancia_km = data['paths'][0]['distance'] / 1000 
        duracion_segundos = data['paths'][0]['time'] / 1000  
        return distancia_km, duracion_segundos
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None, None
def convertir_tiempo(segundos):
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segundos_restantes = int(segundos % 60)
    return horas, minutos, segundos_restantes


def calcular_combustible(distancia_km, consumo_litros_km=0.12):
    return distancia_km * consumo_litros_km


def main():
    api_key = "57b39598-a396-449e-b040-1447ca08ffa1"  
    while True:
        origen = input("Ingrese la Ciudad de Origen (o 'q' para salir): ")
        if origen.lower() == 'q':
            break
        destino = input("Ingrese la Ciudad de Destino: ")
        
        distancia_km, duracion_segundos = obtener_info_viaje(origen, destino, api_key)
        
        if distancia_km is not None and duracion_segundos is not None:
            # Convertir la duración a horas, minutos y segundos
            horas, minutos, segundos = convertir_tiempo(duracion_segundos)
            
            # Calcular el combustible requerido (usando 12 litros por cada 100 km, por ejemplo)
            combustible_litros = calcular_combustible(distancia_km)

            # Imprimir resultados
            print(f"\nNarrativa del viaje de {origen} a {destino}:")
            print(f"Distancia: {distancia_km:.2f} km")
            print(f"Duración del viaje: {horas} horas, {minutos} minutos, {segundos} segundos")
            print(f"Combustible requerido: {combustible_litros:.2f} litros\n")
        else:
            print("No se pudo calcular la ruta, intente de nuevo.\n")

# Ejecutar el programa
if __name__ == "__main__":
    main()

