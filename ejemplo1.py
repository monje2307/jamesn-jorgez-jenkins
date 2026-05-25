import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from enum import Enum
from tabulate import tabulate

class EstadoPedido(Enum):
    PENDIENTE = "PENDIENTE"
    EN_PROCESO = "EN_PROCESO"
    ENTREGADO = "ENTREGADO"
    CANCELADO = "CANCELADO"

class Pedido:
    contador_guia = 1
    pedidos_totales = 0
    pedidos_confirmados = 0
    pedidos_cancelados = 0
    pedidos_entregados = 0

    def __init__(self, id, cliente, articulos):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("El ID debe ser un número entero positivo.")
        if not cliente or not isinstance(cliente, str) or cliente.strip() == "":
            raise ValueError("El cliente debe ser un nombre válido (texto).")
        if not articulos or len(articulos) == 0:
            raise ValueError("Debe seleccionar al menos un artículo.")

        self.id = id
        self.cliente = cliente.strip()
        self.articulos = articulos
        self.estado = EstadoPedido.PENDIENTE
        self.id_guia = None
        Pedido.pedidos_totales += 1

    def mostrar_info(self):
        print("\n📋 Resumen del Pedido de Partes de Computador")
        print("="*60)
        print(f"🆔 ID Pedido: {self.id}")
        print(f"👤 Cliente: {self.cliente}")
        print(f"📌 Estado: {self.estado.value}")
        print("🛍️ Artículos seleccionados:")
        tabla_articulos = [[art, cant] for art, cant in self.articulos.items()]
        print(tabulate(tabla_articulos, headers=["Artículo", "Cantidad"], tablefmt="fancy_grid"))
        print("="*60)

    def confirmar(self):
        self.estado = EstadoPedido.EN_PROCESO
        self.id_guia = str(Pedido.contador_guia).zfill(10)
        Pedido.contador_guia += 1
        Pedido.pedidos_confirmados += 1
        print("\n✅ Pedido confirmado")
        print(f"📦 ID de guía asignado: {self.id_guia}")
        print("🎉 Gracias por su confianza, estamos procesando su pedido con satisfacción.")

    def entregar(self):
        self.estado = EstadoPedido.ENTREGADO
        Pedido.pedidos_entregados += 1
        print("\n📦 Pedido entregado")
        print("🙌 Esperamos que disfrute sus partes de computador. ¡Gracias por elegirnos!")

    def cancelar(self, motivo):
        self.estado = EstadoPedido.CANCELADO
        Pedido.pedidos_cancelados += 1
        print("\n❌ Pedido cancelado")
        print(f"📋 Motivo de cancelación: {motivo}")

def mostrar_indicadores():
    tasa_confirmacion = (Pedido.pedidos_confirmados / Pedido.pedidos_totales) * 100 if Pedido.pedidos_totales else 0
    tasa_cancelacion = (Pedido.pedidos_cancelados / Pedido.pedidos_totales) * 100 if Pedido.pedidos_totales else 0
    tasa_entrega = (Pedido.pedidos_entregados / Pedido.pedidos_totales) * 100 if Pedido.pedidos_totales else 0

    tabla = [
        ["Pedidos Totales", Pedido.pedidos_totales],
        ["Pedidos Confirmados", Pedido.pedidos_confirmados],
        ["Pedidos Cancelados", Pedido.pedidos_cancelados],
        ["Pedidos Entregados", Pedido.pedidos_entregados],
        ["Tasa de Confirmación (%)", f"{tasa_confirmacion:.2f}"],
        ["Tasa de Cancelación (%)", f"{tasa_cancelacion:.2f}"],
        ["Tasa de Entrega (%)", f"{tasa_entrega:.2f}"]
    ]

    print("\n📊 Tabla de Indicadores de Calidad")
    print(tabulate(tabla, headers=["Indicador", "Valor"], tablefmt="fancy_grid"))

def flujo_pedidos():
    id_pedido = 1
    articulos_disponibles = ["Procesador", "Memoria RAM", "Disco Duro", "Tarjeta Gráfica", "Fuente de Poder", "Placa Madre"]

    while True:
        try:
            print("\n🛒 --- Nueva Solicitud de Pedido (Partes de Computador) ---")
            print("="*60)
            cliente = input("👤 Ingrese el nombre del cliente: ")

            print("\n📦 Partes disponibles:")
            for i, art in enumerate(articulos_disponibles, start=1):
                print(f"{i}. {art}")

            articulos_seleccionados = {}
            while True:
                opcion = input("Seleccione el número del artículo (o 'fin' para terminar): ").strip().lower()
                if opcion == "fin":
                    break
                if opcion.isdigit() and 1 <= int(opcion) <= len(articulos_disponibles):
                    articulo = articulos_disponibles[int(opcion) - 1]
                    cantidad = int(input(f"Ingrese cantidad de {articulo}: "))
                    articulos_seleccionados[articulo] = cantidad
                else:
                    print("⚠️ Opción inválida, intente nuevamente.")

            pedido = Pedido(id_pedido, cliente, articulos_seleccionados)
            pedido.mostrar_info()

            confirmar = input("❓ ¿El cliente confirma el pedido? (s/n): ").strip().lower()
            if confirmar == "s":
                pedido.confirmar()
                entregar = input("❓ ¿Desea entregar el pedido ahora? (s/n): ").strip().lower()
                if entregar == "s":
                    pedido.entregar()
                else:
                    print("⏳ El pedido queda en estado EN_PROCESO.")
            else:
                motivo = input("📝 Ingrese el motivo de la cancelación: ")
                pedido.cancelar(motivo)

            mostrar_indicadores()

            continuar = input("\n🔄 ¿Desea registrar otro pedido? (s/n): ").strip().lower()
            if continuar != "s":
                print("\n✅ Finalizando el sistema de pedidos.")
                break
            id_pedido += 1

        except ValueError as e:
            print(f"⚠️ Error al crear el pedido: {e}")

if __name__ == "__main__":
    flujo_pedidos()
