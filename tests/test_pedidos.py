import unittest
from ejemplo1 import Pedido, EstadoPedido

class TestPedido(unittest.TestCase):

    def test_creacion_pedido_valido(self):
        articulos = {"Procesador": 2, "Memoria RAM": 4}
        pedido = Pedido(1, "Juan", articulos)
        self.assertEqual(pedido.id, 1)
        self.assertEqual(pedido.cliente, "Juan")
        self.assertEqual(pedido.estado, EstadoPedido.PENDIENTE)
        self.assertEqual(pedido.articulos["Procesador"], 2)

    def test_confirmar_pedido(self):
        articulos = {"Disco Duro": 1}
        pedido = Pedido(2, "Maria", articulos)
        pedido.confirmar()
        self.assertEqual(pedido.estado, EstadoPedido.EN_PROCESO)
        self.assertIsNotNone(pedido.id_guia)

    def test_entregar_pedido(self):
        articulos = {"Tarjeta Gráfica": 1}
        pedido = Pedido(3, "Carlos", articulos)
        pedido.confirmar()
        pedido.entregar()
        self.assertEqual(pedido.estado, EstadoPedido.ENTREGADO)

    def test_cancelar_pedido(self):
        articulos = {"Fuente de Poder": 1}
        pedido = Pedido(4, "Ana", articulos)
        pedido.cancelar("Cliente no disponible")
        self.assertEqual(pedido.estado, EstadoPedido.CANCELADO)

    def test_error_cliente_vacio(self):
        with self.assertRaises(ValueError):
            Pedido(5, "", {"Placa Madre": 1})

    def test_error_articulos_vacios(self):
        with self.assertRaises(ValueError):
            Pedido(6, "Luis", {})

if __name__ == "__main__":
    unittest.main()