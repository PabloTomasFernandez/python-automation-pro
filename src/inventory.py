"""
Módulo de gestión de inventario usando diccionarios para búsqueda rápida O(1).
"""
from typing import Dict, Union, Any, Tuple, Optional

# Alias de tipos para hacer el código legible
# ProductData es un diccionario que se ve así: {'price': 10.99, 'stock': 50}
ProductData = Dict[str, Union[float, int]]
Inventory = Dict[str, ProductData]

def add_product(inventory: Inventory, name: str, price: float, stock: int) -> bool:
    """
    Agrega un nuevo producto al inventario.
    Retorna True si se agregó, False si ya existía.
    """
    if name in inventory:
        print(f"Error: '{name}' already exists.")
        return False
    
    # Creamos el diccionario del producto
    inventory[name] = {'price': price, 'stock': stock}
    return True

def update_stock(inventory: Inventory, name: str, quantity: int) -> None:
    """
    Actualiza el stock de un producto.
    Si quantity es positivo suma, si es negativo resta (si hay suficiente stock).
    """
    if name not in inventory:
        print(f"Error: '{name}' not found.")
        return

    current_stock = int(inventory[name]['stock']) # Cast a int para seguridad
    new_stock = current_stock + quantity

    if new_stock < 0:
        print(f"Error: Stock insuficiente ({current_stock}). No se puede restar {abs(quantity)}.")
        return

    # Si todo está bien, actualizamos
    inventory[name]['stock'] = new_stock
        
def get_product_info(inventory: Inventory, name: str) -> Optional[Tuple[str, int, float]]:
    """
    Obtiene información del producto.
    Retorna una tupla (nombre, stock, precio) o None si no existe.
    """
    if name not in inventory:
        print(f"Error: Product '{name}' not found.")
        return None

    product = inventory[name]
    # Nota: product['price'] puede ser float o int, Python lo maneja
    return name, int(product['stock']), float(product['price'])
         

def main() -> None:
    # Inicializamos el inventario vacío
    store_inventory: Inventory = {}

    print("--- Agregando Productos ---")
    add_product(store_inventory, "Laptop", 1200.00, 10)
    add_product(store_inventory, "Mouse", 25.50, 50)
    
    # Intento de duplicado
    add_product(store_inventory, "Laptop", 900.00, 5)

    print("\n--- Actualizando Stock ---")
    update_stock(store_inventory, "Mouse", -5)  # Vendimos 5. Stock esperado: 45
    update_stock(store_inventory, "Mouse", -100) # Error esperado

    print("\n--- Consultando Info ---")
    info = get_product_info(store_inventory, "Mouse")
    if info:
        print(f"Producto: {info[0]} | Stock: {info[1]} | Precio: ${info[2]}")
    
    # Verificación final
    print(f"\nInventario Final: {store_inventory}")

if __name__ == "__main__":
    main()