class Envio:
    def __init__(self, peso_kg: float, distancia_km: float):
        self.peso_kg = peso_kg
        self.distancia_km = distancia_km

    def calcular_costo(self, monto_base: float) -> float:
      
        raise NotImplementedError("Este método debe ser implementado por las subclases.")


class EnvioEstandar(Envio):
    def calcular_costo(self, monto_base: float) -> float:
       
        return monto_base * 1.05


class EnvioExpress(Envio):
    def calcular_costo(self, monto_base: float) -> float:
   
        return monto_base * 1.15



if __name__ == "__main__":
    print("--- EJERCICIO 2: COTIZACIÓN DE ENVÍOS (POLIMORFISMO) ---")
    
    
    envios = [
        EnvioEstandar(peso_kg=5.0, distancia_km=50.0),
        EnvioExpress(peso_kg=2.0, distancia_km=100.0),
        EnvioEstandar(peso_kg=10.0, distancia_km=20.0),
        EnvioExpress(peso_kg=4.5, distancia_km=250.0)
    ]

    monto_base_prueba = 50000.0  
    print(f"Monto base para cotización: ${monto_base_prueba:,.2f}\n")

 
    for i, envio in enumerate(envios, start=1):
        tipo = "Envío Estándar (+5%)" if isinstance(envio, EnvioEstandar) else "Envío Express (+15%)"
        costo_total = envio.calcular_costo(monto_base_prueba)
        print(f"Paquete {i} ({tipo}) -> Peso: {envio.peso_kg}kg, Distancia: {envio.distancia_km}km | Costo Final: ${costo_total:,.2f}")