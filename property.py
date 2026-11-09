class Producto:
    def __init__(self, nombre: str, precio_inicial: float):
        self.__nombre = nombre
        self.__precios_historicos = []
        
        self.precio = precio_inicial

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        
        if self.__precios_historicos:
            return self.__precios_historicos[-1]
        return 0.0

    @precio.setter
    def precio(self, nuevo_precio: float):
        
        if 0 <= nuevo_precio <= 10000:
            self.__precios_historicos.append(nuevo_precio)
        else:
            print(f"⚠️ Advertencia: El precio ${nuevo_precio} está fuera del rango permitido ($0 - $10,000). No se registró.")

    def calcular_precio_promedio(self) -> float:
        if not self.__precios_historicos:
            return 0.0
        return sum(self.__precios_historicos) / len(self.__precios_historicos)

    def obtener_historial(self):
        return self.__precios_historicos



if __name__ == "__main__":
    print("--- EJERCICIO 1: CONTROL DE INVENTARIO ---")
    prod = Producto("Laptop Básica", 5000.0)
    print(f"Producto creado: {prod.nombre} con precio inicial: ${prod.precio}")

   
    prod.precio = 5500.0
    prod.precio = 4800.0

    prod.precio = -200.0
    prod.precio = 15000.0

    print(f"Historial de precios: {prod.obtener_historial()}")
    print(f"Precio promedio: ${prod.calcular_precio_promedio():.2f}\n")
