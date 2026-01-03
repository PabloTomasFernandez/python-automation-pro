"""
Este módulo demuestra el uso de variables tipadas y f-strings.
"""

def main() -> None:
    username: str = "Pablo"
    years_experience: int = 0
    target_role: str = "Automation Engineer"
    
    # Operaciones básicas
    years_experience = years_experience + 1
    
    # Output Usando f-String
    print(f"Hola, soy {username}.")
    print(f"En {years_experience} años seré un {target_role}.")
    
# El Entry Point
if __name__ == "__main__":
    main()
        
    