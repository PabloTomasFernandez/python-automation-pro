# Funciones para sumar, restar y dividir

def add(a: float, b: float) -> float:
    """Sum of 2 numbers
    
    Args:
        a (float): First operand
        b (float): Second operand
    
    Returns:
        float: the sum of a and b
    """
    return a + b

    
def subtract(a: float, b: float) -> float:
    """Subtraction of 2 numbers

    Args:
        a (float): First operand
        b (float): Second operand

    Returns:
        float: the difference of a and b
    """
    return a - b

    
def divide(a: float, b: float) -> float | None:
    """Divide two numbers safely.
    Returns None if the divisor is 0.

    Args:
        a (float): First operand
        b (float): Second operand

    Returns:
        float : The result of division if b is not 0.
        None: If b is 0.
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        return None
    
def main() -> None:
    """Función principal para pruebas manuales."""
    print(f"Suma (1 + 5): {add(1, 5)}")
    print(f"Resta (10 - 2): {subtract(10, 2)}")
    print(f"División (10 / 2): {divide(10, 2)}")
    print(f"División por cero: {divide(5, 0)}")
    
if __name__ == "__main__":
    main()