# database.py

# Función para agregar un riesgo a la "base de datos" (en este caso, un archivo de texto)
def guardar_riesgo(nombre, impacto, probabilidad, riesgo):
    with open("riesgos.txt", "a") as file:
        file.write(f"{nombre} | Impacto: {impacto} | Probabilidad: {probabilidad} | Riesgo: {riesgo}\n")

# Función para listar los riesgos desde la "base de datos" (archivo de texto)
def obtener_riesgos():
    try:
        with open("riesgos.txt", "r") as file:
            riesgos = file.readlines()
        # Parsear los datos del archivo
        riesgos = [line.strip().split(" | ") for line in riesgos]
        riesgos = [(r[0], r[1], float(r[2].split(":")[1]), float(r[3].split(":")[1]), float(r[4].split(":")[1])) for r in riesgos]
        return riesgos
    except FileNotFoundError:
        return []

