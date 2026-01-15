# Text Pattern Matching with Regular
import re

'''
 Escribe una función pequeña llamada find_hex_color que:

1. Reciba un texto (str).

2. Use un patrón global compilado para buscar un código de color Hex (ej: #FFFFFF). Usa r'#[0-9A-Fa-f]{6}'.

3. Devuelva el texto encontrado o None.

4. Requisito Clave: Usa Type Hints estrictos (Python 3.10+) para el patrón, la variable de match y el retorno.
'''

HEX_COLOR_PATTERN: re.Pattern = re.compile(r'#[0-9A-Fa-f]{6}')

def extract_hex_color(text: str) -> str | None:
    """
    Busca el primer código de color hexadecimal (ej: #FFFFFF) en el texto.
    """
    # Usamos la constante global directamente (Principio de Cohesión)
    match_result: re.Match[str] | None = HEX_COLOR_PATTERN.search(text)
    
    # Defensive Programming: Manejo explícito de None
    if match_result is None:
        return None
    
    return match_result.group()

'''
Escribe una función extract_emails que:

1. Reciba un texto.

2. Use una Regex con re.VERBOSE para capturar emails simples (Formato: usuario + @ + dominio).

3. Usa Grupos: Quiero que la función devuelva una lista de tuplas [(usuario, dominio), ...].

4. Tipado: Define correctamente el retorno.
'''

EMAIL_PATTERN: re.Pattern = re.compile(r'''
    ([a-zA-Z0-9._%+-]+)      # Grupo 1: Usuario (Capturado)
    @                        # Separador literal (No capturado)
    ([a-zA-Z0-9.-]+)         # Grupo 2: Dominio completo (Capturado, incluye .com.ar)
''', re.VERBOSE)


def extract_all_email(text: str) -> list[tuple[str,str]]:
    """
    Extrae emails y separa usuario del dominio.
    Retorna: [('usuario', 'dominio.com.ar'), ...]
    """
    return EMAIL_PATTERN.findall(text)
