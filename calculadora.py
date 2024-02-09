import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
import sys

script_directory = os.path.dirname(os.path.abspath(__file__))

def calculate_cv():
    try:
        crit_dmg = float(crit_dmg_entry.get())
        crit_rate = float(crit_rate_entry.get())

        crit_value = crit_dmg + (crit_rate * 2)

        result_label.config(text=f"Tu CV es: {crit_value}")

        img_src = get_image_src(crit_value)
        load_and_display_image(img_src)

    except ValueError:
        result_label.config(text="Ingresa valores numéricos en CRIT DMG y CRIT RATE")

def get_image_src(crit_value):
    image_folder = os.path.join(script_directory, "images")
    if 0 <= crit_value <= 5:
        return os.path.join(image_folder, "imagen-1.jpg")
    elif 5 < crit_value <= 10:
        return os.path.join(image_folder, "imagen-1.png")
    elif 11 <= crit_value <= 20:
        return os.path.join(image_folder, "imagen-2.png")
    elif 21 <= crit_value <= 30:
        return os.path.join(image_folder, "imagen-3.png")
    elif 31 <= crit_value <= 40:
        return os.path.join(image_folder, "imagen-4.png")
    elif 41 <= crit_value <= 50:
        return os.path.join(image_folder, "imagen-5.png")
    elif 51 <= crit_value <= 60:
        return os.path.join(image_folder, "imagen-6.png")
    elif 61 <= crit_value <= 70:
        return os.path.join(image_folder, "imagen-7.png")
    elif 71 <= crit_value <= 80:
        return os.path.join(image_folder, "imagen-8.png")
    elif 81 <= crit_value <= 90:
        return os.path.join(image_folder, "imagen-9.png")
    elif 91 <= crit_value <= 100:
        return os.path.join(image_folder, "imagen-10.png")
    elif 101 <= crit_value <= 1000:
        return os.path.join(image_folder, "imagen-god.png")

def load_and_display_image(img_src):
    print(f"Intentando abrir la imagen en la ruta: {img_src}")
    image = Image.open(img_src)
    image.thumbnail((200, 200))
    photo = ImageTk.PhotoImage(image)

    image_label.config(image=photo)
    image_label.image = photo

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calcula de CV")

# Configurar el icono de la aplicación
icon_path = os.path.join(script_directory, "icono.ico")
root.iconbitmap(icon_path)

# Crea un estilo temático utilizando el tema Yaru
style = ThemedStyle(root)
style.set_theme("yaru")

frame = ttk.Frame(root, padding="20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

crit_dmg_label = ttk.Label(frame, text="CRIT DMG:")
crit_dmg_label.grid(column=0, row=0, sticky=tk.W)

crit_dmg_entry = ttk.Entry(frame)
crit_dmg_entry.grid(column=1, row=0, sticky=tk.W)

crit_rate_label = ttk.Label(frame, text="CRIT RATE:")
crit_rate_label.grid(column=0, row=1, sticky=tk.W)

crit_rate_entry = ttk.Entry(frame)
crit_rate_entry.grid(column=1, row=1, sticky=tk.W)

calculate_button = ttk.Button(frame, text="Calcular", command=calculate_cv)
calculate_button.grid(column=0, row=2, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=3, columnspan=2)

image_label = ttk.Label(frame, text="Resultado de imagen")
image_label.grid(column=0, row=4, columnspan=2)

# Ejecutar la aplicación
root.mainloop()
