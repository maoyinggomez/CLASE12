
class Operacion:
    def calcular(self, num1, num2):
        raise NotImplementedError("Este método debe ser implementado por la clase de operación específica.")

class Suma(Operacion):
    def calcular(self, num1, num2):
        return num1 + num2

class Resta(Operacion):
    def calcular(self, num1, num2):
        return num1 - num2

class Multiplicacion(Operacion):
    def calcular(self, num1, num2):
        return num1 * num2

class Division(Operacion):
    def calcular(self, num1, num2):
        if num2 == 0:
            return "Error: División entre cero no permitida"
        return num1 / num2

class GestorOperaciones:
    def __init__(self):
        self.operaciones = {}

    def registrar_operacion(self, nombre, operacion):
        """Registra una operación en el gestor."""
        self.operaciones[nombre] = operacion

    def mostrar_operaciones(self):
        """Muestra todas las operaciones disponibles en el gestor."""
        print("Seleccione una operación:")
        for i, nombre in enumerate(self.operaciones.keys(), start=1):
            print(f"{i}. {nombre}")
        print(f"{len(self.operaciones) + 1}. Salir")  # Añadir opción de salir

    def obtener_operacion(self, seleccion):
        """Devuelve la operación correspondiente a la selección del usuario."""
        if seleccion == len(self.operaciones) + 1:
            return "salir"
        try:
            nombre = list(self.operaciones.keys())[seleccion - 1]
            return self.operaciones[nombre]
        except (IndexError, ValueError):
            print("Opción no válida.")
            return None

class CalculadoraControlador:
    def __init__(self):
        # Inicializa el gestor de operaciones y registra las operaciones
        self.gestor_operaciones = GestorOperaciones()
        self.gestor_operaciones.registrar_operacion("Sumar", Suma())
        self.gestor_operaciones.registrar_operacion("Restar", Resta())
        self.gestor_operaciones.registrar_operacion("Multiplicar", Multiplicacion())
        self.gestor_operaciones.registrar_operacion("Dividir", Division())
        self.num1 = None
        self.num2 = None

    def solicitar_numeros(self):
        """Solicita los números una sola vez."""
        while True:
            try:
                self.num1 = float(input("Ingrese el primer número: "))
                self.num2 = float(input("Ingrese el segundo número: "))
                break  # Solo pide los números una vez y sale del bucle
            except ValueError:
                print("Error: Entrada no válida. Asegúrese de ingresar números.")

    def iniciar(self):
        """Inicia la calculadora solicitando números una vez y repitiendo solo las operaciones."""
        print("Bienvenido a la Calculadora Extendible")
        self.solicitar_numeros()  # Solicita los números solo una vez al inicio

        while True:
            # Mostrar operaciones disponibles y pedir la operación
            self.gestor_operaciones.mostrar_operaciones()
            try:
                opcion = int(input("Ingrese el número de la operación: "))
            except ValueError:
                print("Error: Entrada no válida. Ingrese un número.")
                continue

            # Ejecutar la operación seleccionada
            operacion = self.gestor_operaciones.obtener_operacion(opcion)
            if operacion == "salir":
                print("Gracias por usar la calculadora. ¡Hasta luego!")
                break

            if operacion:
                # Realizar y mostrar el resultado con los mismos números
                resultado = operacion.calcular(self.num1, self.num2)
                print(f"El resultado de {operacion.__class__.__name__} es: {resultado}")

# Ejecución del programa
if __name__ == "__main__":
    calculadora = CalculadoraControlador()
    calculadora.iniciar()

