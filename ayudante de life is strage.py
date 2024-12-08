import os
import json
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Ruta base de recursos
BASE_DIR = r"c:\Users\jesus\OneDrive - Universidad CNCI de México, S.C\Sumblimacion\resources"

# Diccionarios de contenido
DECISIONES_CLAVE = {
    1: [
        "Salvar a Chloe o dejarla morir.",
        "Reportar a Nathan o mantener silencio.",
        "Ayudar a Alyssa o ignorarla.",
        "Firmar la petición de la academia o no.",
        "Hacer que David culpe a Chloe o a Nathan."
    ],
    2: [
        "Confortar a Kate o dejarla sola.",
        "Revelar la verdad o mentir sobre el video de Kate.",
        "Decidir si Kate vive o muere.",
        "Ayudar a Alyssa nuevamente o no.",
        "Robar dinero del fondo de la escuela o no."
    ],
    3: [
        "Decidir si Chloe toma la culpa por el robo.",
        "Elegir entre besar a Chloe o no.",
        "Ayudar a Alyssa por tercera vez o ignorarla.",
        "Guardar la información sobre Rachel o revelarla.",
        "Decidir si dañar o no la casa de Frank."
    ],
    4: [
        "Salvar a Victoria o dejarla que entre en peligro.",
        "Confrontar a Jefferson o esperar.",
        "Aceptar o rechazar el destino de Chloe.",
        "Usar la foto para cambiar el pasado o no.",
        "Decidir si expones a Jefferson en público."
    ],
    5: [
        "Decidir entre salvar a Arcadia Bay o salvar a Chloe.",
        "Confrontar a Jefferson en el pasado.",
        "Decidir si ayudas a Alyssa por última vez.",
        "Elegir entre abandonar o regresar al tornado.",
        "Revivir momentos clave del juego a través de fotografías."
    ]
}

CONSECUENCIAS = {
    1: [
        "Si salvas a Chloe, fortaleces la relación con ella. Si la dejas morir, cambia el curso del juego.",
        "Reportar a Nathan hará que Jefferson te observe. Mantener silencio reduce tensiones inmediatas.",
        "Ayudar a Alyssa mejora tu relación con ella. Ignorarla no tiene impacto significativo.",
        "Firmar la petición influye en la visión de tus compañeros sobre ti.",
        "Culpar a David puede afectarlo emocionalmente. Culpar a Nathan aumenta su hostilidad."
    ],
    2: [
        "Confortar a Kate mejora tu relación con ella. Dejarla sola la hará sentir abandonada.",
        "Revelar la verdad ayuda a Kate, pero puede causar problemas con Nathan.",
        "Si Kate vive, ella será clave en el futuro. Si muere, genera consecuencias emocionales.",
        "Ayudar a Alyssa fortalece tu vínculo con ella. Ignorarla no tiene consecuencias significativas.",
        "Robar dinero afecta tu relación con la escuela y con Chloe."
    ],
    3: [
        "Si Chloe toma la culpa, su relación con Max mejora. Si no, otros personajes reaccionan de forma distinta.",
        "Besar a Chloe fortalece su vínculo emocional. No hacerlo mantiene una relación platónica.",
        "Ayudar a Alyssa mejora tu relación con ella.",
        "Revelar información sobre Rachel puede causar tensiones.",
        "Dañar la casa de Frank puede tener consecuencias graves más adelante."
    ],
    4: [
        "Salvar a Victoria puede evitar su muerte. Dejarla en peligro afecta tu relación con ella.",
        "Confrontar a Jefferson altera cómo se desarrollan los eventos del episodio.",
        "Aceptar el destino de Chloe puede cambiar el curso del juego.",
        "Usar la foto para cambiar el pasado tiene efectos inesperados.",
        "Exponer a Jefferson públicamente cambia la percepción de otros personajes."
    ],
    5: [
        "Salvar a Arcadia Bay destruye tu relación con Chloe. Salvar a Chloe sacrifica la ciudad.",
        "Confrontar a Jefferson puede cambiar el final del juego.",
        "Ayudar a Alyssa refuerza tu papel como héroe del pueblo.",
        "Abandonar el tornado afecta tu percepción del destino.",
        "Revivir momentos clave da un cierre emocional al juego."
    ]
}

COLECCIONABLES = {
    1: [
        {"nombre": "Foto de un mural", "detalle": "Ubicación: Cerca del faro al inicio del episodio."},
        {"nombre": "Foto de un ciervo", "detalle": "Ubicación: En el bosque, justo antes del faro."},
        {"nombre": "Foto de la pizarra", "detalle": "Ubicación: En el aula de fotografía de Jefferson."},
        {"nombre": "Foto del espejo", "detalle": "Ubicación: En el baño de chicas, toma la foto al espejo."},
        {"nombre": "Foto del automóvil", "detalle": "Ubicación: En el estacionamiento, cerca del auto de Nathan."}
    ],
    2: [
        {"nombre": "Foto de un conejo", "detalle": "Ubicación: En la habitación de Kate, cerca de su ventana."},
        {"nombre": "Foto de dos aves", "detalle": "Ubicación: En el tejado de la escuela."},
        {"nombre": "Foto de graffiti", "detalle": "Ubicación: En el baño de los chicos, en una de las puertas."},
        {"nombre": "Foto de un cuadro", "detalle": "Ubicación: En el cuarto de arte, cerca de los caballetes."},
        {"nombre": "Foto de una planta", "detalle": "Ubicación: En el dormitorio de Max, junto a la ventana."}
    ],
    3: [
        {"nombre": "Foto de una polaroid", "detalle": "Ubicación: En la habitación de Chloe, cerca de la ventana."},
        {"nombre": "Foto de una cinta de cassette", "detalle": "Ubicación: En la sala de Chloe, junto a la televisión."},
        {"nombre": "Foto de un barco", "detalle": "Ubicación: Cerca del puerto de Arcadia Bay."},
        {"nombre": "Foto de una estatua", "detalle": "Ubicación: En la escuela, cerca del aula de Jefferson."},
        {"nombre": "Foto de una ardilla", "detalle": "Ubicación: En el parque, cerca del banco central."}
    ],
    4: [
        {"nombre": "Foto de una mariposa", "detalle": "Ubicación: En el dormitorio de Max, junto a la ventana."},
        {"nombre": "Foto de una cámara", "detalle": "Ubicación: En la habitación de Chloe, en el estante superior."},
        {"nombre": "Foto de un trofeo", "detalle": "Ubicación: En el aula de Jefferson."},
        {"nombre": "Foto de un reloj", "detalle": "Ubicación: En el salón de entrada de la escuela."},
        {"nombre": "Foto de una lámpara", "detalle": "Ubicación: En el cuarto oscuro."}
    ],
    5: [
        {"nombre": "Foto de un tornado", "detalle": "Ubicación: En la playa de Arcadia Bay."},
        {"nombre": "Foto de una pareja", "detalle": "Ubicación: En la cafetería de Two Whales."},
        {"nombre": "Foto de una guitarra", "detalle": "Ubicación: En el dormitorio de Max."},
        {"nombre": "Foto de un coche antiguo", "detalle": "Ubicación: En el garaje de Chloe."},
        {"nombre": "Foto de una fogata", "detalle": "Ubicación: En el bosque cerca del faro."}
    ]
}

PUZLES = {
    1: [
        {"nombre": "Rompecabezas del candado", "detalle": "Ubicación: En el baño, adivina el código del candado (código: 451)."},
        {"nombre": "Rompecabezas del álbum de fotos", "detalle": "Ubicación: En la habitación de Chloe, encuentra las fotos ocultas."},
        {"nombre": "Rompecabezas del mapa del faro", "detalle": "Ubicación: Encuentra la ubicación del faro en el mapa de Arcadia Bay."}
    ],
    2: [
        {"nombre": "Rompecabezas de los pájaros", "detalle": "Ubicación: Encuentra las tres aves escondidas en el tejado."},
        {"nombre": "Rompecabezas del diario de Kate", "detalle": "Ubicación: Encuentra el diario de Kate y descubre sus pensamientos."},
        {"nombre": "Rompecabezas del cuarto oscuro", "detalle": "Ubicación: Descifra las pistas para acceder al cuarto oscuro."}
    ]
}

PROGRESO_COLECCIONABLES = {episodio: [False] * len(COLECCIONABLES.get(episodio, [])) for episodio in range(1, 6)}

def cargar_progreso():
    """
    Carga el progreso desde un archivo JSON.
    """
    global PROGRESO_COLECCIONABLES
    try:
        with open("progreso.json", "r") as archivo:
            PROGRESO_COLECCIONABLES = json.load(archivo)
    except FileNotFoundError:
        print("No se encontró el archivo de progreso. Se iniciará desde cero.")

def guardar_progreso_automatico():
    """
    Guarda el progreso automáticamente en un archivo JSON.
    """
    try:
        with open("progreso.json", "w") as archivo:
            json.dump(PROGRESO_COLECCIONABLES, archivo)
            print("Progreso guardado automáticamente.")
    except Exception as e:
        print(f"Error al guardar el progreso: {e}")


# Aquí integran la funcionalidad completa del menú principal, decisiones, coleccionables, y más.

# Si necesitas el resto listo, lo detallo para integrarlo por completo. 😊
def cargar_progreso():
    """
    Carga el progreso desde un archivo JSON.
    """
    global PROGRESO_COLECCIONABLES
    try:
        with open("progreso.json", "r") as archivo:
            PROGRESO_COLECCIONABLES = json.load(archivo)
    except FileNotFoundError:
        print("No se encontró el archivo de progreso. Se iniciará desde cero.")

def guardar_progreso_automatico():
    """
    Guarda el progreso automáticamente en un archivo JSON.
    """
    try:
        with open("progreso.json", "w") as archivo:
            json.dump(PROGRESO_COLECCIONABLES, archivo)
            print("Progreso guardado automáticamente.")
    except Exception as e:
        print(f"Error al guardar el progreso: {e}")

# Funciones para manejo de imágenes
def encontrar_imagen(nombre_archivo):
    ruta_imagen = os.path.join(BASE_DIR, nombre_archivo)
    return ruta_imagen if os.path.exists(ruta_imagen) else None

def cargar_imagen(ruta_imagen, tamaño=(80, 80)):
    try:
        img = Image.open(ruta_imagen)
        img = img.resize(tamaño)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error al cargar la imagen {ruta_imagen}: {e}")
        return None

# Interfaz gráfica y funcionalidades
def mostrar_menu_principal():
    root = tk.Tk()
    root.title("Life is Strange Helper")
    root.geometry("600x400")
    tk.Label(root, text="Life is Strange Helper", font=("Arial", 18), fg="purple").pack(pady=10)

    icons_frame = tk.Frame(root)
    icons_frame.pack(pady=20)
    crear_boton_icono(icons_frame, "Episodios", encontrar_imagen("episodios.png"), mostrar_episodios, 0, 0)
    crear_boton_icono(icons_frame, "Movimiento", encontrar_imagen("movimiento.png"), mostrar_movimiento, 0, 1)

    root.mainloop()

def mostrar_episodios():
    window = tk.Toplevel()
    window.title("Episodios")
    tk.Label(window, text="Selecciona un Episodio", font=("Arial", 16)).pack(pady=10)
    for episodio in range(1, 6):  # Episodios 1 a 5
        tk.Button(window, text=f"Episodio {episodio}", font=("Arial", 12),
                  command=lambda ep=episodio: mostrar_detalles_episodio(ep)).pack(pady=5)
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def mostrar_detalles_episodio(episodio):
    """
    Muestra las opciones del episodio seleccionado.
    """
    window = tk.Toplevel()
    window.title(f"Episodio {episodio}")

    main_frame = tk.Frame(window)
    main_frame.pack(pady=10)

    izquierda_frame = tk.Frame(main_frame)
    izquierda_frame.grid(row=0, column=0, padx=20)
    derecha_frame = tk.Frame(main_frame)
    derecha_frame.grid(row=0, column=1, padx=20)

    # Buscar la carátula del episodio
    ruta_imagen_episodio = encontrar_imagen(f"EP{episodio}.jpg")
    if not ruta_imagen_episodio:
        ruta_imagen_episodio = encontrar_imagen(f"EP{episodio}.png")

    if ruta_imagen_episodio:
        img_episodio = cargar_imagen(ruta_imagen_episodio, tamaño=(300, 300))
        if img_episodio:
            tk.Label(izquierda_frame, image=img_episodio).pack()
            window.image = img_episodio  # Guardar referencia para evitar que se elimine
    else:
        tk.Label(izquierda_frame, text="(Carátula no disponible)", font=("Arial", 12), fg="red").pack()

    tk.Label(derecha_frame, text=f"Opciones del Episodio {episodio}", font=("Arial", 16)).pack(pady=10)
    agregar_opcion(derecha_frame, "Decisiones Clave", encontrar_imagen("decisiones.png"), lambda: mostrar_decisiones(episodio))
    agregar_opcion(derecha_frame, "Coleccionables", encontrar_imagen("coleccionables.png"), lambda: mostrar_coleccionables(episodio))
    agregar_opcion(derecha_frame, "Puzles", encontrar_imagen("puzzles.png"), lambda: mostrar_puzles(episodio))
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def agregar_opcion(frame, texto, ruta_imagen, comando):
    """
    Crea un botón con texto e imagen, y lo agrega a un frame.
    """
    opcion_frame = tk.Frame(frame)
    opcion_frame.pack(pady=10, anchor="w")

    img_opcion = cargar_imagen(ruta_imagen, tamaño=(50, 50))
    if img_opcion:
        boton = tk.Button(opcion_frame, image=img_opcion, command=comando, bg="white", borderwidth=0)
        boton.image = img_opcion  # Necesario para evitar que se elimine la referencia
        boton.pack()
    tk.Button(opcion_frame, text=texto, command=comando, font=("Arial", 12)).pack()


def mostrar_puzles(episodio):
    """
    Muestra la lista de puzles del episodio seleccionado.
    """
    window = tk.Toplevel()
    window.title(f"Puzles - Episodio {episodio}")
    tk.Label(window, text=f"Puzles - Episodio {episodio}", font=("Arial", 16)).pack(pady=10)

    puzles = PUZLES.get(episodio, [])
    for i, puzle in enumerate(puzles):
        frame = tk.Frame(window)
        frame.pack(pady=5, anchor="w")
        tk.Label(frame, text=f"- {puzle['nombre']}", font=("Arial", 12), wraplength=500).pack(side="left")
        tk.Button(frame, text="Detalles", font=("Arial", 10),
                  command=lambda idx=i: mostrar_detalles_puzle(episodio, idx)).pack(side="left", padx=10)
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def mostrar_detalles_puzle(episodio, indice):
    """
    Muestra los detalles de un puzle específico.
    """
    window = tk.Toplevel()
    window.title(f"Detalles del Puzle - Episodio {episodio}")
    tk.Label(window, text=f"Detalles del Puzle", font=("Arial", 16)).pack(pady=10)

    detalle = PUZLES.get(episodio, [])[indice]["detalle"]
    tk.Label(window, text=detalle, font=("Arial", 12), wraplength=500).pack(pady=10)
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def mostrar_decisiones(episodio):
    window = tk.Toplevel()
    window.title(f"Decisiones Clave - Episodio {episodio}")
    tk.Label(window, text=f"Decisiones Clave - Episodio {episodio}", font=("Arial", 16)).pack(pady=10)

    decisiones = DECISIONES_CLAVE.get(episodio, [])
    consecuencias = CONSECUENCIAS.get(episodio, [])
    for i, decision in enumerate(decisiones):
        frame = tk.Frame(window)
        frame.pack(pady=5, anchor="w")
        tk.Label(frame, text=f"- {decision}", font=("Arial", 12), wraplength=500).pack(side="left")
        tk.Button(frame, text="Consecuencias", font=("Arial", 10),
                  command=lambda idx=i: mostrar_consecuencias(episodio, idx)).pack(side="left", padx=10)
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def mostrar_consecuencias(episodio, indice):
    window = tk.Toplevel()
    window.title(f"Consecuencias - Episodio {episodio}")
    tk.Label(window, text=f"Consecuencias de la decisión:", font=("Arial", 16)).pack(pady=10)

    consecuencias = CONSECUENCIAS.get(episodio, [])
    tk.Label(window, text=consecuencias[indice], font=("Arial", 12), wraplength=500).pack(pady=10)
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def mostrar_coleccionables(episodio):
    window = tk.Toplevel()
    window.title(f"Coleccionables - Episodio {episodio}")
    tk.Label(window, text=f"Coleccionables - Episodio {episodio}", font=("Arial", 16)).pack(pady=10)

    coleccionables = COLECCIONABLES.get(episodio, [])
    progreso = PROGRESO_COLECCIONABLES.get(episodio, [False] * len(coleccionables))
    check_vars = [tk.BooleanVar(value=estado) for estado in progreso]

    for i, coleccionable in enumerate(coleccionables):
        frame = tk.Frame(window)
        frame.pack(pady=5, anchor="w")
        tk.Checkbutton(frame, text=f"- {coleccionable['nombre']}", variable=check_vars[i]).pack(side="left", padx=5)
        tk.Button(frame, text="Detalles",
                  command=lambda idx=i: mostrar_detalles_coleccionable(episodio, idx)).pack(side="left", padx=10)
    tk.Button(window, text="Guardar Progreso", command=lambda: guardar_progreso(episodio, check_vars)).pack(pady=10)
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def mostrar_detalles_coleccionable(episodio, indice):
    window = tk.Toplevel()
    window.title(f"Detalles - Episodio {episodio}")
    tk.Label(window, text=f"Detalles del Coleccionable:", font=("Arial", 16)).pack(pady=10)
    detalle = COLECCIONABLES[episodio][indice]["detalle"]
    tk.Label(window, text=detalle, font=("Arial", 12), wraplength=500).pack(pady=10)
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def mostrar_puzles(episodio):
    """
    Muestra la lista de puzles del episodio seleccionado.
    """
    window = tk.Toplevel()
    window.title(f"Puzles - Episodio {episodio}")
    tk.Label(window, text=f"Puzles - Episodio {episodio}", font=("Arial", 16)).pack(pady=10)

    puzles = PUZLES.get(episodio, [])
    for i, puzle in enumerate(puzles):
        frame = tk.Frame(window)
        frame.pack(pady=5, anchor="w")
        tk.Label(frame, text=f"- {puzle['nombre']}", font=("Arial", 12), wraplength=500).pack(side="left")
        tk.Button(frame, text="Detalles", font=("Arial", 10),
                  command=lambda idx=i: mostrar_detalles_puzle(episodio, idx)).pack(side="left", padx=10)
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def mostrar_detalles_puzle(episodio, indice):
    """
    Muestra los detalles de un puzle específico.
    """
    window = tk.Toplevel()
    window.title(f"Detalles del Puzle - Episodio {episodio}")
    tk.Label(window, text=f"Detalles del Puzle", font=("Arial", 16)).pack(pady=10)

    detalle = PUZLES.get(episodio, [])[indice]["detalle"]
    tk.Label(window, text=detalle, font=("Arial", 12), wraplength=500).pack(pady=10)
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)


def guardar_progreso(episodio, check_vars):
    global PROGRESO_COLECCIONABLES
    PROGRESO_COLECCIONABLES[episodio] = [var.get() for var in check_vars]
    guardar_progreso_automatico()
    messagebox.showinfo("Progreso Guardado", f"Progreso del Episodio {episodio} guardado automáticamente.")

def mostrar_movimiento():
    window = tk.Toplevel()
    window.title("Movimiento")
    tk.Label(window, text="Controles del Juego", font=("Arial", 16)).pack(pady=10)

    CONTROLES = [
        {"acción": "Moverse", "tecla": "W/A/S/D"},
        {"acción": "Caminar rápido", "tecla": "Shift"},
        {"acción": "Interactuar", "tecla": "Botón izquierdo del ratón"},
        {"acción": "Rebobinar el tiempo", "tecla": "Botón derecho del ratón"},
        {"acción": "Abrir diario", "tecla": "Tab"},
        {"acción": "Pausa", "tecla": "Esc"}
    ]

    for control in CONTROLES:
        tk.Label(window, text=f"{control['acción']}: {control['tecla']}", font=("Arial", 12)).pack(pady=2, anchor="w")
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def crear_boton_icono(frame, texto, ruta_imagen, comando, fila, columna):
    icon_frame = tk.Frame(frame)
    icon_frame.grid(row=fila, column=columna, padx=20, pady=10)

    img_tk = cargar_imagen(ruta_imagen)
    if img_tk:
        button = tk.Button(icon_frame, image=img_tk, command=comando, bg="white", borderwidth=0)
        button.image = img_tk
        button.pack()
    tk.Label(icon_frame, text=texto, font=("Arial", 12)).pack()

if __name__ == "__main__":
    cargar_progreso()
    mostrar_menu_principal()
    guardar_progreso_automatico()