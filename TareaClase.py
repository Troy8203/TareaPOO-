class Persona:
    #Atributos de la Clase Persona
    nombre = ''
    apellidoP = ''
    apellidoM = ''
    ci = 0

    #Metodos de la Clase Persona
    def __init__(self, nombre, apellidoP, apellidoM, ci):
        self.nombre = nombre
        self.apellidoP = apellidoP
        self.apellidoM = apellidoM
        self.ci = ci

    def __str__(self):
        return '********************************\n' \
               'Nombre: {} \n' \
               'Apellidos: {} {} \n' \
               'CI: {} \n' \
               '********************************\n'.format(self.nombre, self.apellidoP, self.apellidoM, self.ci)

    def dia_salida(self):
        d = self.ci % 10
        print('El dia de salida es :',end = ' ')
        if d is 1 or d is 2:
            print('Lunes')
        elif d is 3 or d is 4:
            print('Martes')
        elif d is 5 or d is 6:
            print('Miercoles')
        elif d is 7 or d is 8:
            print('Jueves')
        elif d is 9 or d is 0:
            print('Viernes')

    def cambio_apellidoP(self,apellidoP):
        self.apellidoP = apellidoP
        print('Se cambio el Apellido P. al de = ', self.apellidoP)

person0 = Persona('Roy','Ayala','Ruiz',12465760)
print(person0)
person0.dia_salida()
person0.cambio_apellidoP('Perez')

class Automovil:
    color = ''
    modelo = ''
    marca = ''
    placa = ''

    def __init__(self, color, modelo, marca, placa):
        self.color = color
        self.modelo = modelo
        self.marca = marca
        self.placa = placa

    def __str__(self):
        return ('********************************\n'
              'Color: {}\n'
              'Modelo: {}\n'
              'Marca: {}\n'
              'Placa: {}\n'
              '********************************\n'.format(self.color, self.modelo, self.marca, self.placa))
    def cambio_color(self, color):
        self.color = color
        print('Se cambio el color a = ', self.color)

    def cambio_placa(self,placa):
        self.placa = placa
        print('Se cambio la placa a = ', self.placa)

auto0 = Automovil('Rojo', 'CORE SDN2020', 'MAZDA', '123JQK')
print(auto0)
auto0.cambio_color('Azul')
auto0.cambio_placa('1243SEA')
