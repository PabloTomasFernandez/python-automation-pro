'''
Escenario: Trabajas en una Fintech. Te llegan logs "sucios" de transacciones y 
debes limpiarlos para el equipo de Data Science.

Requisitos del Ejercicio:

El Problema: Tienes un texto con fechas en formato USA desordenado 
(MM-DD-YYYY o MM/DD/YYYY).

Escribe un script log_cleaner.py que:

* Defina una Regex DATE_PATTERN con re.VERBOSE que capture:

* Grupo 1: Mes (1 o 2 dígitos).

* Grupo 2: Separador (- o / o .). Tip: Usa una clase de caracteres.

* Grupo 3: Día (1 o 2 dígitos).

* Grupo 4: Separador (mismo que el anterior).

* Grupo 5: Año (4 dígitos).

Tenga una función standardize_dates(text: str) -> str.

Use re.sub con una función auxiliar para transformar todas las fechas al formato 
estándar ISO: YYYY-MM-DD (Asegurando que día y mes tengan 2 dígitos, 
ej: 1-5-2023 -> 2023-05-01).

'''
import re

import main

DATE_PATTERN: re.Pattern = re.compile(r'''
    (\d{1,2})      # Grupo 1: Mes (1 o 2 dígitos)
    ([./-])        # Grupo 2: Separador (- o / o .)
    (\d{1,2})      # Grupo 3: Día (1 o 2 dígitos)
    (\2)           # Grupo 4: Referencia al Grupo 2 (debe ser el mismo separador)
    (\d{4})        # Grupo 5: Año (4 dígitos)
''', re.VERBOSE)

def iso_format_match(match: re.Match) -> str:
    """
    Callback para re.sub. Transforma matches a ISO 8601.
    """
    day_part: str = match.group(3).zfill(2)
    month_part: str = match.group(1).zfill(2)
    year_part: str = match.group(5)
    
    # Logica de ISO Date
    iso_date: str =  f"{year_part}-{month_part}-{day_part}"
    
    return iso_date

def standardize_dates(text: str) -> str:
    """
    Busca fechas en formato US (MM/DD/YYYY) y las convierte a ISO (YYYY-MM-DD).
    """
    return DATE_PATTERN.sub(iso_format_match, text)

# --- Simulación de Test en CI/CD ---
if __name__ == "__main__":
    log_sample = "Error on 5/1/2023 and 10-12-2023. Backup failed."
    clean_log = standardize_dates(log_sample)
    
    print(f"Original: {log_sample}")
    print(f"Clean:    {clean_log}")
    
    # Assert simple para verificar
    assert "2023-05-01" in clean_log
    assert "2023-10-12" in clean_log
    print("✅ Tests Passed")
    
    