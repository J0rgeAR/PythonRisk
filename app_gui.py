import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import ttkbootstrap as tb
import pandas as pd
import plotly.express as px
from db import guardar_riesgo, obtener_riesgos

# Lista de riesgos actualizada
CATEGORIAS = {
    "Riesgos Naturales": [
        ("Inundaciones", "Construcción de diques y drenajes, monitoreo de lluvias."),
        ("Caída de ceniza", "Instalación de filtros de aire y mantenimientos de ventilación."),
        ("Incendios forestales", "Implementación de sistemas de detección temprana, equipos de extinción."),
        ("Erosión de suelos", "Plantación de vegetación en áreas críticas, control de actividades agrícolas."),
        ("Desertificación", "Proyectos de reforestación y restauración de suelos."),
        ("Fenómenos geológicos", "Monitoreo sísmico y evaluación de riesgos geológicos."),
    ],
    "Riesgos Humanos": [
        ("Saqueo", "Refuerzo de las barreras físicas y sistemas de alarmas."),
        ("Robos", "Cámaras de seguridad, control de acceso, refuerzo de cerraduras."),
        ("Tráfico de bienes", "Control de inventarios, rastreo de productos, colaboración con autoridades."),
        ("Vandalismo", "Monitoreo constante y sistemas de vigilancia."),
        ("Contaminación", "Inspección de procesos industriales, cumplimiento de normas ambientales."),
        ("Explosiones", "Detección de gases, control de equipos y capacitación del personal."),
    ],
    "Riesgos Físicos": [
        ("Robos", "Instalación de cámaras y alarmas, capacitación en manejo de riesgos."),
        ("Asaltos", "Contratación de seguridad privada y simulacros."),
        ("Secuestros", "Medidas preventivas, control de acceso y vigilancia."),
        ("Incendios", "Sistemas de detección de incendios y simulacros periódicos."),
        ("Sabotajes", "Inspección de equipos, control de acceso."),
        ("Destrozos", "Supervisión constante de equipos y sistemas."),
    ],
    "Riesgos Cibernéticos": [
        ("Vulneración de información confidencial", "Implementación de seguridad informática, encriptación de datos."),
        ("Ataques a la reputación", "Gestión de crisis y control de redes sociales."),
    ],
    "Riesgos Internos": [
        ("Falta de cumplimiento de responsabilidades", "Definición de roles, auditorías internas periódicas."),
    ]
}

# Configuración de la ventana principal con ttkbootstrap
root = tb.Window(themename="cosmo")
root.title("GERI - Gestión de Riesgos")
root.geometry("900x600")

# Variables
categoria_var = tk.StringVar()
nombre_riesgo_var = tk.StringVar()
impacto_var = tk.StringVar()
probabilidad_var = tk.StringVar()
analista_var = tk.StringVar()
busqueda_var = tk.StringVar()

# Función para actualizar la lista de riesgos
def actualizar_nombres_riesgos(*args):
    categoria = categoria_var.get()
    nombres_riesgos = [r[0] for r in CATEGORIAS.get(categoria, [])]
    if nombres_riesgos:
        nombre_riesgo_var.set(nombres_riesgos[0])
    else:
        nombre_riesgo_var.set("")
    menu_nombres_riesgos["menu"].delete(0, "end")
    for riesgo in nombres_riesgos:
        menu_nombres_riesgos["menu"].add_command(label=riesgo, command=tk._setit(nombre_riesgo_var, riesgo))

# Función para agregar riesgo
def agregar_riesgo():
    categoria = categoria_var.get()
    nombre = nombre_riesgo_var.get()
    impacto = impacto_var.get()
    probabilidad = probabilidad_var.get()
    analista = analista_var.get()
    
    try:
        impacto = int(impacto)
        probabilidad = float(probabilidad)
    except ValueError:
        messagebox.showerror("Error", "Impacto y probabilidad deben ser numéricos.")
        return
    
    nivel_riesgo = impacto * probabilidad
    guardar_riesgo(categoria, nombre, impacto, probabilidad, nivel_riesgo, analista)
    messagebox.showinfo("Éxito", f"Riesgo '{nombre}' guardado con nivel {nivel_riesgo:.2f}.")

# Creación de la interfaz gráfica
frame_registro = ttk.Frame(root)
frame_registro.pack(pady=20)

ttk.Label(frame_registro, text="Categoría:").pack()
categoria_menu = ttk.OptionMenu(frame_registro, categoria_var, *CATEGORIAS.keys(), command=actualizar_nombres_riesgos)
categoria_menu.pack()

ttk.Label(frame_registro, text="Nombre del Riesgo:").pack()
menu_nombres_riesgos = ttk.OptionMenu(frame_registro, nombre_riesgo_var, "")
menu_nombres_riesgos.pack()

ttk.Label(frame_registro, text="Impacto (1-10):").pack()
ttk.Entry(frame_registro, textvariable=impacto_var).pack()

ttk.Label(frame_registro, text="Probabilidad (0-1):").pack()
ttk.Entry(frame_registro, textvariable=probabilidad_var).pack()

ttk.Label(frame_registro, text="Analista:").pack()
ttk.Entry(frame_registro, textvariable=analista_var).pack()

boton_guardar = ttk.Button(frame_registro, text="Guardar Riesgo", command=agregar_riesgo)
boton_guardar.pack(pady=10)

root.mainloop()


