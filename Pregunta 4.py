class UnidadRadiologia:
    """Sistema de gestión para la Unidad de Radiología de una Clínica en Caracas"""
    
    def __init__(self):
        """Inicializa el sistema con contadores y acumuladores"""
        # Diccionarios para almacenar contadores y montos por tipo de estudio
        self.contador_estudios = {"Ultrasonido": 0, "Tomografía": 0, "Resonancia": 0}
        self.monto_total = 0
        self.clientes = []

    def calcular_precio_base(self, tipo_estudio, edad):
        """Calcula el precio base según el tipo de estudio y la edad"""
        if tipo_estudio == "Ultrasonido":
            return 8.90 + (edad * 10)
        elif tipo_estudio == "Tomografía":
            return 12.64 + (edad * 10)
        elif tipo_estudio == "Resonancia":
            return 15.60 + (edad * 10)
        else:
            raise ValueError("Tipo de estudio no válido")

    def calcular_descuento(self, precio_base, tiene_seguro, sexo, edad):
        """Calcula el descuento aplicable según las condiciones del cliente"""
        # Inicializamos el porcentaje de descuento en 0
        porcentaje_descuento = 0
        
        # Si tiene seguro, aplicamos 80% de descuento
        if tiene_seguro:
            porcentaje_descuento += 80
        
        # Aplicamos descuentos adicionales por edad y sexo
        if sexo == "F" and edad > 70:
            porcentaje_descuento += 20
        elif sexo == "M" and edad > 80:
            porcentaje_descuento += 15
            
        # Calculamos el monto del descuento
        descuento = (porcentaje_descuento / 100) * precio_base
        
        return descuento

    def registrar_cliente(self, cedula, edad, sexo, tiene_seguro, tipo_estudio):
        """Registra un nuevo cliente y calcula el monto a pagar"""
        # Validamos el sexo (solo puede ser M o F)
        if sexo not in ["M", "F"]:
            raise ValueError("El sexo debe ser 'M' o 'F'")
        
        # Validamos el tipo de estudio
        if tipo_estudio not in self.contador_estudios:
            raise ValueError("Tipo de estudio no válido")
        
        # Calculamos el precio base
        precio_base = self.calcular_precio_base(tipo_estudio, edad)
        
        # Calculamos el descuento
        descuento = self.calcular_descuento(precio_base, tiene_seguro, sexo, edad)
        
        # Calculamos el monto neto a pagar
        monto_neto = precio_base - descuento
        
        # Actualizamos los contadores y acumuladores
        self.contador_estudios[tipo_estudio] += 1
        self.monto_total += monto_neto
        
        # Guardamos la información del cliente
        cliente = {
            "cedula": cedula,
            "edad": edad,
            "sexo": sexo,
            "tiene_seguro": tiene_seguro,
            "tipo_estudio": tipo_estudio,
            "monto_neto": monto_neto
        }
        
        self.clientes.append(cliente)
        
        return cliente

    def imprimir_recibo(self, cliente):
        """Imprime un recibo con la información del cliente"""
        print("\n" + "=" * 40)
        print("RECIBO - UNIDAD DE RADIOLOGÍA")
        print("=" * 40)
        print(f"Cédula de Identidad: {cliente['cedula']}")
        print(f"Edad: {cliente['edad']} años")
        print(f"Sexo: {cliente['sexo']}")
        print(f"Tipo de Estudio: {cliente['tipo_estudio']}")
        print(f"Tiene Seguro: {'Sí' if cliente['tiene_seguro'] else 'No'}")
        print(f"Monto Neto a Pagar: ${cliente['monto_neto']:.2f}")
        print("=" * 40 + "\n")

    def generar_reporte_diario(self):
        """Genera un reporte con los totales del día"""
        print("\n" + "=" * 50)
        print("REPORTE DIARIO - UNIDAD DE RADIOLOGÍA")
        print("=" * 50)
        print("Cantidad de Clientes por Tipo de Estudio:")
        for tipo, cantidad in self.contador_estudios.items():
            print(f"- {tipo}: {cantidad} cliente(s)")
        
        print(f"\nMonto Total Neto Facturado: ${self.monto_total:.2f}")
        print("=" * 50 + "\n")


# Ejemplo de uso del sistema
def main():
    # Inicializamos el sistema
    unidad = UnidadRadiologia()
    
    # Menú interactivo para registrar clientes
    while True:
        print("\n--- UNIDAD DE RADIOLOGÍA - REGISTRO DE CLIENTES ---")
        print("1. Registrar un nuevo cliente")
        print("2. Generar reporte diario")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            # Solicitamos los datos del cliente
            cedula = input("Cédula de Identidad: ")
            
            try:
                edad = int(input("Edad: "))
                if edad <= 0:
                    print("La edad debe ser un número positivo.")
                    continue
            except ValueError:
                print("La edad debe ser un número entero.")
                continue
            
            sexo = input("Sexo (M/F): ").upper()
            if sexo not in ["M", "F"]:
                print("El sexo debe ser 'M' o 'F'.")
                continue
            
            tiene_seguro_input = input("¿Pertenece a un seguro? (S/N): ").upper()
            tiene_seguro = tiene_seguro_input == "S"
            
            print("\nTipos de Estudio disponibles:")
            print("1. Ultrasonido")
            print("2. Tomografía")
            print("3. Resonancia")
            
            tipo_estudio_opcion = input("Seleccione el tipo de estudio: ")
            
            if tipo_estudio_opcion == "1":
                tipo_estudio = "Ultrasonido"
            elif tipo_estudio_opcion == "2":
                tipo_estudio = "Tomografía"
            elif tipo_estudio_opcion == "3":
                tipo_estudio = "Resonancia"
            else:
                print("Opción no válida.")
                continue
            
            try:
                # Registramos al cliente
                cliente = unidad.registrar_cliente(cedula, edad, sexo, tiene_seguro, tipo_estudio)
                
                # Imprimimos el recibo
                unidad.imprimir_recibo(cliente)
                
            except ValueError as e:
                print(f"Error: {e}")
                
        elif opcion == "2":
            # Generamos el reporte diario
            unidad.generar_reporte_diario()
            
        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
            
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()