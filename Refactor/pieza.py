class Pieza(object):
    def __init__(self, nombre, mov, status, central, cankill, equipo):
        self.nombre = nombre
        self.mov = mov
        self.status = status
        self.central = central
        self.cankill = cankill
        self.equipo = equipo

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getMov(self):
        return self.mov

    def setMov(self, mov):
        self.mov = mov

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getCentral(self):
        return self.central

    def setCentral(self, central):
        self.central = central

    def getCanKill(self):
        return self.cankill

    def setCanKill(self, cankill):
        self.cankill = cankill


class Militante(Pieza):
    pass


class Necromovil(Pieza):
    pass


class Reportero(Pieza):
    pass


class Provocador(Pieza):
    pass


class Lider(Pieza):
    pass


class Asesino(Pieza):
    pass
