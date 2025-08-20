class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso: ${monto}. Nuevo saldo: ${self.saldo}")
        else:
            print("El monto a depositar debe ser mayor a 0.")

    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes.")
        elif monto <= 0:
            print("El monto a retirar debe ser mayor a 0.")
        else:
            self.saldo -= monto
            print(f"Retiro exitoso: ${monto}. Nuevo saldo: ${self.saldo}")

    def consultar_saldo(self):
        print(f"Saldo actual de {self.titular}: ${self.saldo}")


# Ejemplo de uso
if __name__ == "__main__":
    cuenta1 = CuentaBancaria("Miguel", 1000)

    cuenta1.consultar_saldo()
    cuenta1.depositar(500)
    cuenta1.retirar(200)
    cuenta1.retirar(2000)  # caso de fondos insuficientes
    cuenta1.consultar_saldo()