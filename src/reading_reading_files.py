import shelve
from pathlib import Path
import os

"""
Micro-Reto 1: Tu jefe te pide un script que cree un archivo llamado notas.txt 
en el directorio actual. Si el archivo ya tiene texto, no debe borrarlo, sino 
añadir una nueva línea que diga: "Sprint finalizado".
"""

# Definimos constantes para nombres de archivo por defecto
DEFAULT_LOG_FILE = "notas.txt"

def registrar_notas(mensaje: str, archivo_destino: str = DEFAULT_LOG_FILE) -> None:
    """
    Agrega una nota al final de un archivo de texto de manera segura.
    
    Args:
        mensaje (str): El contenido a guardar.
        archivo_destino (str, optional): Nombre del archivo. Defaults to "notas.txt".
    """
    
    # Definimos la ruta en el directorio actual (CWD)
    ruta_notas: Path = Path.cwd() / "notas.txt"
    
    try:
        # 'a' (append) agrega al final. 'utf-8' es obligatorio para evitar moji-bake.
        with open(ruta_notas, mode="a", encoding="utf-8") as archivo:
            archivo.write(f"{mensaje}\n")
    except OSError as e:
        print(f"Error crítico al escribir en disco: {e}")
    

"""
Micro-Reto 2: Crea una función llamada persistir_lista que reciba una lista_items: 
list[str]. Debes guardarla en un archivo de shelve llamado mi_bodega bajo la 
llave "inventario".
"""

# Definimos constantes para nombres de archivo/claves
DB_FILENAME = "warehouse_db"
INVENTORY_KEY = "inventory"

def save_inventory(items: list[str], db_name: str = DB_FILENAME) -> None:
    """
    Persiste una lista de items en una base de datos local (shelve).
    
    Args:
        items (List[str]): Lista de strings a guardar.
        db_name (str): Nombre del archivo de base de datos (sin extensión).
    """
    # Construimos la ruta absoluta de forma segura
    db_path = Path.cwd() / db_name
    
    try:
        # Cast a str() es una buena práctica defensiva con librerías antiguas como shelve
        with shelve.open(str(db_path)) as db:
            db[INVENTORY_KEY] = items
            print(f"Success: {len(items)} items saved to '{db_name}'.")
    except OSError as e:
        print(f"Critical Error: Could not save to database. Details: {e}")


## El Archivador de Logs Inteligente
import shelve
import shutil
from pathlib import Path

# Constantes en UPPER_CASE (Clean Code)
PATTERN: str = "*.txt"

def explore_files(pattern: str) -> list[Path]:
    """Explora el CWD buscando archivos que coincidan con el patrón."""
    # glob() devuelve un generador; lo convertimos a lista para facilitar el manejo.
    return list(Path.cwd().glob(pattern))

def save_stats(file_name: str, count: int) -> None:
    """Persiste el conteo de errores en una base binaria."""
    db_path: str = str(Path.cwd() / "estadisticas_db")
    with shelve.open(db_path) as db:
        db[file_name] = count # Asignación correcta al objeto shelve.

def process_logs() -> None:
    """Lógica principal de procesamiento y limpieza de logs."""
    files: list[Path] = explore_files(PATTERN)
    report_path: Path = Path.cwd() / "reporte_critico.txt"
    clean_dir: Path = Path.cwd() / "procesados" / "limpios"

    for file_path in files:
        # Evitar procesar el propio reporte si ya existe
        if file_path.name == report_path.name:
            continue

        errors_found: list[str] = []
        
        try:
            # Uso de Context Manager con encoding explícito.
            with open(file_path, mode="r", encoding="utf-8") as f:
                for line in f:
                    if "error" in line.lower():
                        errors_found.append(line.strip())
            
            if errors_found:
                # 1. Persistencia en TXT (Modo Append).
                with open(report_path, mode="a", encoding="utf-8") as report:
                    for err in errors_found:
                        report.write(f"Archivo: {file_path.name} | {err}\n")
                
                # 2. Persistencia en Shelve.
                save_stats(file_path.name, len(errors_found))
            else:
                # 3. Limpieza: Mover archivos sin errores.
                clean_dir.mkdir(parents=True, exist_ok=True) # Asegurar destino.
                dest_path: Path = clean_dir / file_path.name
                file_path.rename(dest_path) # Mover de forma Pythonica.
                
        except Exception as e:
            print(f"Error procesando {file_path.name}: {e}")

if __name__ == "__main__":
    process_logs()






