# -*- coding: utf-8 -*-
# Objetos es una cosa
# Propiedades del objeto o atributos de un objeto, la propiedade de un objeto puede ser un objeto
# acciones se le llamaria funciones o metodos
# Ejemplo un carro --> Propiedades: sus llantas, sus puertas, sus vidrios...., acciones o metodos: andar, estacionarse ...
# Herencia, por ejemplo teniendo un carro base poder tener varios tipos de carro que tengan esas mismas propiedades
# Abstraccion es extraer lo mas basico de una idea u objeto
# POO: Programacion Orientada a Objetos

class Persona:
    cedula = "39283928932"
    nombre = "David"
    apellido = "Briones"
    genero = "M"

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.___mostrar_mensaje()

    def ___mostrar_mensaje(self):
        print(f"El objeto se esta construyendo desde un metodo privado {self.nombre}")

    def __del__(self):
        print(f"El objeto se esta destruyendo {self.nombre}")

    def saludar(self):
        return f"Hola me llamo {self.nombre} y estoy hablando"

    def hablar_saludando(self):
        self.hablar(self.saludar())

    def hablar(self, mensaje):
        print(f"{self.nombre} esta hablando")
        print(mensaje)

    def __str__(self):
        return f"nombre={self.nombre}"

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(f"Hola {Persona.pedirle_nombre()}, {mensaje}")

    @staticmethod
    def pedirle_nombre():
        print("Cual es tu nombre?")
        return input()


class Supervisor(Persona):
    planta = ""
    obreros = []

    def __init__(self, planta, nombre, apellido):
        self.planta = planta
        Persona.__init__(self, nombre, apellido)

    def __str__(self):
        return "Esta es un supervisor"

    def agregar_obrero(self, obrero):
        self.obreros.append(obrero)

    def supervisar(self):
        for obrero in self.obreros:
            print(f"Revisando tareas de obrero {obrero.nombre} === {obrero.tareas}")


class Obrero(Persona):
    planta = ""
    tareas = []
    supervisor = None

    def __init__(self, planta, nombre, apellido):
        self.planta = planta
        Persona.__init__(self, nombre, apellido)

    def __str__(self):
        return "Esta es un obrero"

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def ejecutar_tareas(self):
        for tarea in self.tareas:
            print("Ejecutando tarea... " + str(tarea) + " que sera revisada por " + self.supervisor.nombre)

    def set_supervisor(self, supervisor):
        supervisor.agregar_obrero(self)
        self.supervisor = supervisor


class Destreza:
    nombre_destreza = "Programar en Python"

    def __init__(self, nombre):
        self.nombre_destreza = nombre


class Profesional(Obrero, Destreza):
    def __init__(self, destreza, planta, nombre, apellido):
        Obrero.__init__(self, planta, nombre, apellido)
        Destreza.__init__(self, destreza)

    def agregar_tarea(self, tarea):
        print("Soy mas organizado con mis tareas:3")
        self.tareas.append(tarea)

obrero = Obrero("Programacion", "Juanito", "Guzman")
supervisor = Supervisor("Programacion", "David", "Briones")

obrero.hablar_saludando()
supervisor.hablar_saludando()

print(obrero)
print(supervisor)

obrero.agregar_tarea("Programar")
obrero.agregar_tarea("Jugar")
obrero.agregar_tarea("Testear")

obrero.set_supervisor(supervisor)

obrero.ejecutar_tareas()

supervisor.supervisar()

Persona.mostrar_mensaje("soy una persona")

profesional = Profesional("Diseño Grafico", "Experiencia de usuario", "Jacinto", "Perez")

profesional.agregar_tarea("Jugar")
profesional.set_supervisor(supervisor)

profesional.ejecutar_tareas()