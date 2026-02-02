import shelve
from pathlib import Path

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


¡Vaya cambio de ritmo! Has saltado directamente a la Sesión 3 (Persistencia / Archivos) usando el módulo shelve (Capítulo 10 del libro).

Me gusta que estés explorando la persistencia de datos, pero como tu Tech Lead, debo mantener el orden. Tenemos un ticket crítico abierto (el validador de Regex) y me has entregado código de base de datos.

Voy a revisar este snippet rápidamente porque tiene errores de concepto y estilo, y luego necesito que volvamos al Regex, porque sin validar los datos, no deberíamos estar guardándolos en ninguna base de datos (GIGO: Garbage In, Garbage Out).

🔍 Code Review: persist_list
1. Imports Fantasma (Critical): Estás usando shelve y Path sin importarlos. El código fallará con NameError.

2. Inconsistencia de Idioma (Style): Volvemos al "Spanglish".

Variable: ruta_db -> Debería ser db_path.

Clave del diccionario: "inventario" -> Debería ser "inventory".

Regla: Si el código está en inglés, las claves de la base de datos también.

3. Hardcoding (Design): Estás definiendo la clave "inventario" dentro de la función. Si mañana quieres guardar "usuarios", tienes que reescribir la función. Hazla agnóstica.

4. El Comentario [cite: 2719, 2721]: reference Veo que referencias el libro. shelve es genial para scripts rápidos, pero ten cuidado: crea archivos binarios que solo Python puede leer. Si quieres compartir datos con otro lenguaje (Javascript, C#), esto no sirve. (Veremos JSON después para eso).

🛠️ Refactor Profesional
Aquí tienes cómo se escribe esa función en un entorno de producción:

Python
import shelve
from pathlib import Path
from typing import List

# Definimos constantes para nombres de archivo/claves
DB_FILENAME = "warehouse_db"
INVENTORY_KEY = "inventory"

def save_inventory(items: List[str], db_name: str = DB_FILENAME) -> None:
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




