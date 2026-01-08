"""
Módulo para procesar y limpiar logs de servidor.
"""
from typing import TypeAlias, List, Dict

# Simulación de un log crudo
RAW_LOGS = """
   [INFO]    System booted successfully   | 2023-01-01
[WARN] Low memory warning | 2023-01-02  
   [ERROR]   Critical   disk failure   | 2023-01-03
[INFO] User admin logged out |    2023-01-04
"""

LogEntry: TypeAlias = Dict[str, str]

def process_logs(raw_text: str) -> List[LogEntry]:
    """
    Procesa un texto de logs crudos y devuelve una lista de diccionarios limpios.
    """
    processed_data: List[LogEntry] = []
    
    # 1. Separar por líneas y limpiar espacios externos
    # Usamos strip() en raw_text para evitar líneas vacías al inicio/final
    lines = raw_text.strip().split('\n')
    
    for line in lines:
        # Validación defensiva: Si una línea está vacía, saltarla
        if not line.strip():
            continue

        # 2. Tuple Unpacking: Asignamos nombres inmediatamente
        # El argumento maxsplit=1 asegura que solo corte en la primera barra (por si el mensaje tiene barras)
        try:
            log_part, date_part = line.split('|', maxsplit=1)
        except ValueError:
            continue # Si la línea no tiene pipe |, la saltamos
        
        # 3. Procesamiento del mensaje (Izquierda)
        # log_part es algo como "[INFO]   System..."
        # Vamos a separar por el primer espacio para sacar el nivel
        # Primero limpiamos espacios de los lados
        log_part = log_part.strip()
        
        # Encontramos donde cierra el corchete
        bracket_index = log_part.find(']')
        
        if bracket_index == -1:
            continue # Log mal formado

        # Slicing: Desde el caracter 1 (saltando '[') hasta el corchete de cierre
        level = log_part[1:bracket_index]
        
        # El mensaje es todo lo que sigue después del corchete
        msg = log_part[bracket_index+1:].strip()

        # 4. Construcción
        entry: LogEntry = {
            "level": level,
            "msg": msg,
            "date": date_part.strip()
        }
        processed_data.append(entry)

    return processed_data

def main() -> None:
    print("--- Procesando Logs ---")
    clean_logs = process_logs(RAW_LOGS)
    
    for entry in clean_logs:
        print(f"[{entry['level']}] Date: {entry['date']} -> {entry['msg']}")

if __name__ == "__main__":
    main()