Proyecto: Life is Strange Helper

Este proyecto es una herramienta interactiva creada en Python para mejorar la experiencia de los jugadores de Life is Strange. Proporciona detalles sobre decisiones clave, consecuencias, coleccionables, y puzles de cada episodio, además de opciones de seguimiento de progreso.

Características Principales

Interfaz Gráfica: Diseñada con tkinter, permite una navegación fácil e intuitiva.

Seguimiento de Decisiones y Consecuencias: Muestra las decisiones clave de cada episodio y sus implicaciones.

Gestión de Coleccionables: Lista los coleccionables por episodio y permite registrar su progreso.

Resolución de Puzles: Proporciona detalles sobre los puzles del juego.

Guardado Automático del Progreso: Registra automáticamente el estado actual del usuario en un archivo JSON.

Soporte Multimodal: Incluye imágenes y botones gráficos para una experiencia más inmersiva.

Requisitos del Sistema

Sistema Operativo: Windows

Python: Versión 3.7 o superior

Librerías Python:

tkinter (integrado en Python estándar)

Pillow

Instalación

Asegúrate de tener Python instalado en tu sistema. Descárgalo desde python.org.

Instala las dependencias necesarias ejecutando:

pip install pillow

Clona o descarga este repositorio en tu sistema.

Uso

Ejecuta el script:

Abre una terminal en el directorio del script y ejecuta:

python life_is_strange_helper.py

Interacción:

Desde el menú principal, navega por episodios, coleccionables, decisiones clave, y puzles.

Haz clic en los botones para explorar más detalles.

Guardado Automático:

El progreso se guarda automáticamente en un archivo progreso.json.

Estructura del Código

1. mostrar_menu_principal()

Propósito: Crea y muestra el menú principal de la herramienta.

Detalles:

Ofrece opciones como "Episodios" y "Movimiento".

2. mostrar_episodios()

Propósito: Muestra la lista de episodios disponibles.

Detalles:

Permite seleccionar episodios del 1 al 5.

3. mostrar_detalles_episodio(episodio)

Propósito: Muestra las opciones de un episodio específico.

Detalles:

Incluye carátulas de episodios, decisiones clave, coleccionables, y puzles.

4. guardar_progreso_automatico()

Propósito: Guarda automáticamente el estado actual del usuario.

5. mostrar_decisiones(episodio)

Propósito: Lista las decisiones clave de un episodio junto con sus consecuencias.

6. mostrar_coleccionables(episodio)

Propósito: Muestra los coleccionables de un episodio y permite marcar el progreso.

Personalización

Imágenes y Recursos: Asegúrate de que las imágenes de los episodios y botones estén ubicadas en resources.

Carpetas de Progreso: Cambia la ruta de progreso.json si deseas almacenarlo en otra ubicación.

Notas Importantes

Las imágenes deben estar en formatos compatibles (.png, .jpg).

Si algún recurso falta, aparecerán mensajes de error en la consola.

Para restaurar el progreso, elimina o edita manualmente el archivo progreso.json.

