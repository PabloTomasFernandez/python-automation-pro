# Funciones para sumar, restar y dividir

def add(a: float, b: float) -> float:
    """Sum of 2 numbers
    
    Args:
        a (float): first number to be passed to the function
    
        b (float): second number to be passed to the function
    
    Returns:
        float: returns a float or None for the sum of a and b
    """
    return a + b

    
def subtract(a: float, b: float) -> float:
    """Subtraction of 2 numbers

    Args:
        a (float): first number they're going to play in the show
        b (float): secind number they're going to play in the show

    Returns:
        float: a float or None from the difference of a and b
    """
    return a - b

    
def dividir(a: float, b: float) -> float | None:
    """Divide two numbers safely.
    Returns None if the divisor is 0.

    Args:
        a (float): first number they're going to play in the show
        b (float): second number they're going to play in the show

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
    print(f"División (10 / 2): {dividir(10, 2)}")
    print(f"División por cero: {dividir(5, 0)}")
    
if __name__ == "__main__":
    main()