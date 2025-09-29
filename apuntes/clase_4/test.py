from cafeteria import *  # Asegúrate de que Pedido esté definido en cafeteria.py

def testPagar():
    pedido1 = Pedido()
    producto1 = Producto("Arroz", 2)

    pedido1.añadirProducto(producto1)
    # Comprueba si el método pagar no retorna nada (es decir, retorna None)
    resultado = pedido1.pagar(2)
    assert resultado is None  # True si pagar() no retorna nada
