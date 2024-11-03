import pyfiglet  # Importa la biblioteca pyfiglet para generar arte ASCII a partir de texto
import os, sys, subprocess, keyboard  # Importa módulos para manejo del sistema y teclado

# Se obtiene la lista de fuentes disponibles en pyfiglet
FONTS = pyfiglet.FigletFont.getFonts()
INDEX = 32  # Índice inicial de la fuente seleccionada
TEST_TEXT = "Hola"  # Texto de prueba predeterminado

def clean_cmd():
    """Limpia la consola, ejecutando el comando correspondiente según el sistema operativo."""
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)

def simulate_enter():
    """Simula una presión y liberación de la tecla 'enter' para limpiar la entrada."""
    keyboard.press('enter')
    keyboard.release('enter')

def config_font():
    """Configura la fuente utilizada para el arte ASCII."""
    
    def gui():
        """Muestra la interfaz gráfica para la selección de fuentes."""
        global TEST_TEXT, FONTS, INDEX
        clean_cmd()  # Limpia la consola
        print("#" * 100)
        print(pyfiglet.figlet_format(TEST_TEXT, font=FONTS[INDEX]))  # Muestra el texto en la nueva fuente
        print(f'Fuente --> Nombre: {FONTS[INDEX]} , Indice: {INDEX}')
        print(f'Presiona  "a" o "d" para ver las fuentes, "s" para establecer fuente, "esc" para salir ')
        print(f"Fuente establecida :  Nombre: {FONTS[tmp_index]} , Indice: {tmp_index} ")
        print("#" * 100)
    
    global FONTS, INDEX  # Hace referencia a las variables globales FONTS e INDEX
    tmp_change_index = INDEX  # Guarda el índice actual de la fuente
    tmp_index = INDEX  # Índice temporal de la fuente
    tmp_save_index = False  # Indica si se ha guardado un nuevo índice de fuente
    tmp_a = True  # Variable para evitar múltiples presiones rápidas de la tecla 'a'
    tmp_d = True  # Variable para evitar múltiples presiones rápidas de la tecla 'd'
    gui()  # Muestra la interfaz inicial

    while True:  # Bucle para gestionar la selección de fuentes
        if keyboard.is_pressed('a'):
            if INDEX > 0 and tmp_a:  # Verifica si puede cambiar a la fuente anterior
                INDEX -= 1
            tmp_a = False
        else:
            tmp_a = True    
        if keyboard.is_pressed("d"):
            if INDEX < len(FONTS) - 1 and tmp_d:  # Verifica si puede cambiar a la fuente siguiente
                INDEX += 1
            tmp_d = False
        else:
            tmp_d = True

        if tmp_change_index != INDEX:  # Si el índice ha cambiado, actualiza la vista
            tmp_change_index = INDEX
            gui()  # Redibuja la interfaz

        if keyboard.is_pressed("s"):  # Al presionar 's', se guarda la configuración de la fuente
            tmp_save_index = True
            tmp_index = INDEX  # Guarda el índice actual como temporal
            gui()  # Redibuja la interfaz para mostrar la fuente guardada
            
        if keyboard.is_pressed("escape"):  # Al presionar 'escape', sale de la configuración
            if not tmp_save_index:
                INDEX = tmp_index  # Restaura el índice anterior si no se guardó
            simulate_enter()  # Simula la pulsación de 'enter' para limpiar la entrada
            break

def config_text():
    """Permite al usuario configurar el texto de prueba."""
    global TEST_TEXT  # Hace referencia a la variable global TEST_TEXT
    clean_cmd()  # Limpia la consola
    print("#" * 100)
    print("")
    TEST_TEXT = input("Introduce el texto de prueba: ")  # Pide al usuario que introduzca un nuevo texto de prueba

def text_generator():
    """Genera y muestra arte ASCII basado en el texto introducido por el usuario."""
    clean_cmd()  # Limpia la consola
    while True: 
        print("#" * 100)
        text = input("Introduce el texto: ")  # Solicita al usuario un texto
        clean_cmd()  # Limpia la consola
        print("")        
        ascii_art = pyfiglet.figlet_format(text, font=FONTS[INDEX])  # Genera arte ASCII con el texto y la fuente seleccionada
        print(ascii_art)  # Muestra el arte ASCII
        print("")
        print('Escribe "salir", para salir del programa')  # Instrucción para salir del bucle
        if text.lower() == "salir":  # Sale si el usuario escribe "salir"
            break

def menu_gui():
    """Muestra el menú principal de la aplicación."""
    clean_cmd()  # Limpia la consola
    print("#" * 100)
    print("Letras gigantes ASCII")  # Título del programa
    print("1 --> Generar texto ascii")  # Opción para introducir texto
    print("2 --> Configurar fuente")  # Opción para configurar la fuente
    print("3 --> Configurar texto")  # Opción para configurar el texto
    print("4 --> Salir ...")  # Opción para salir del programa
    print("#" * 100)

def main():
    """Función principal que ejecuta el programa."""
    while True:
        menu_gui()  # Muestra el menú principal
        option = input("Introducir opcion: ")  # Solicita al usuario que elija una opción
        if option.lower() == "1":
            text_generator()  # Llama a la función para generar texto
        elif option.lower() == "2":
            config_font()  # Llama a la función para configurar la fuente
        elif option.lower() == "3":
            config_text()  # Llama a la función para configurar el texto
        elif option.lower() == "4":
            sys.exit()  # Sale del programa

# Llama a la función principal para iniciar el programa
main()
