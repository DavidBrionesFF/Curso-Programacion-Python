from log4p import GetLogger

def mensaje_bienvenida():
    LOGGER = GetLogger(__name__).create()

    LOGGER.info("Bienvenido al curso de Python que te lo pases muy bien!!")
    LOGGER.error("Ups es un error generado :3")

    LOGGER.info("Secciones")

    LOGGER.info("Capitulo 1. Variables")
    LOGGER.info("Capitulo 2. Datos Complejos")
    LOGGER.info("Capitulo 3. Entrada y Salida")
    LOGGER.info("Capitulo 4. Estructuras de Control")
    LOGGER.info("Capitulo 5. Modulos y Paquetes")
    LOGGER.info("Capitulo 6. Funciones")
    LOGGER.info("Capitulo 7. Programacion Orientada a Objetos")
    LOGGER.info("Capitulo 8. Cadenas de Caracteres")
    LOGGER.info("Capitulo 9. Manejo de Excepciones")
    LOGGER.info("Capitulo 10. Instalacion de librerias")
