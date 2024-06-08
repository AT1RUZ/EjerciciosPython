class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def getSaldo(self):
        return self.__saldo
    
    def __setSaldo(self, x):
        if(x < self.__saldo):
            self.__saldo -= x
        else:
            print("Lanzar excepcion")

    def depositarDinero(self, cantidad_depositada):
        self.__saldo += cantidad_depositada
        
    def retirarDinero(self, cantidad_retirada):
        self.__setSaldo(cantidad_retirada)
        #Aqui iria el manejo de la excepcion lanzada en caso de que ocurriese

cuenta1 = CuentaBancaria(
    "Hello World",
    1500
)

cuenta1.depositarDinero(1500)
print(cuenta1.getSaldo())
cuenta1.retirarDinero(3100)
print(cuenta1.getSaldo())
cuenta1.retirarDinero(400)
print(cuenta1.getSaldo())