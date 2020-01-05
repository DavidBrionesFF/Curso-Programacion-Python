
class NombreVacioError(Exception):
    pass

    def __init__(self, mensaje, *args):
        super(NombreVacioError, self).__init__(mensaje, args)


def imprmir_nombre(nombre):
    if nombre == "":
        raise NombreVacioError("El nombre esta vacio")
    print(nombre)

try:
    3 / 0
    imprmir_nombre("")
except NombreVacioError:
    print("Hay un error")
except ZeroDivisionError:
    print("Hay una division invalida")