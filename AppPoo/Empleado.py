from Persona import Persona


class Empleado(Persona):
    def __init__(self, id, nombre, apellido, correo, contrasena, cargo, salario):
        super().__init__(id, nombre, apellido, correo, contrasena)
        self._cargo = cargo
        self._salario = salario

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self):
        return self._cargo

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self):
        return self._salario

    def registrar(self):
        super().registrar()
        self._cargo = input("Ingrese el cargo: ")
        self._salario = input("Ingrese el salario: ")

    def ver_registro(self):
        super().ver_registro()
        print(f"Cargo: {self._cargo} Salario: {self._salario}")

    def iniciar_sesion(self):
        correo_reg= input("Ingrese el correo registrado: ")
        contras_reg= input("Ingrese su contraseña: ")

        if correo_reg == self._correo and contras_reg == self._contrasena:
            print(f"Bienvenido {self.nombre}")
            return True
        else:
            print("Credenciales Invalidas..")
            return False

    def iniciar_negocio_empleado(self, iniciar_sesion, ver_registro):
        init = iniciar_sesion()

        while init == True:
            print("1: Ver datos usuario")
            print("2: Hacer otra cosa")
            print("3: Salir")
            opc= init(input("Seleccione una opcion: "))

            if opc==1:
                print("Ver datos usuario")
                ver_registro()

            elif opc==2:
                print("Hacer otra cosa")
            elif opc==3:
                print("Salir")
                init = False