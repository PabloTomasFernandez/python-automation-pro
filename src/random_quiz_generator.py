# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key

import random
import json
from pathlib import Path
from typing import Final

# State: Capital
CapitalData = dict[str, str]
# List of province names
ProvinceList = list[str]

# Configuration constant
NUM_QUIZZES: Final[int] = 35

# --- Routing Logic ---
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / 'capitales_argentina.json'
OUTPUT_DIR = BASE_DIR / 'quizzes'

# Create the folder for exams if it doesn't exist
OUTPUT_DIR.mkdir(exist_ok=True)


# The quiz data. Keys are states and values are thei capitals.
# Upload the file
def load_data(data_path) -> CapitalData:
    "Upload the JSON file privately."
    try:
        with open(data_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {data_path.name}")
        return {}
    
capitals: CapitalData = load_data(DATA_PATH)


for quiz_num in range(NUM_QUIZZES):
    
    quiz_filename = OUTPUT_DIR / f'capitalsquiz{quiz_num + 1}.txt'
    answer_filename = OUTPUT_DIR / f'capitalsquiz_answers{quiz_num + 1}.txt'
    
    
    with open(quiz_filename, 'w', encoding='utf-8') as quiz_file, \
         open(answer_filename, 'w', encoding='utf-8') as answer_file:
    
        # Write out the header for the quiz.
        quiz_file.write(f'Nombre: {"_" * 30} Fecha: {"_" * 10} Curso: {"_" * 10}\n\n')
        quiz_file.write((' ' * 20) + f'Examen de Capitales (Formulario {quiz_num + 1})\n\n')
        quiz_file.write('=' * 60 + '\n\n')
        
        # Answer sheet header
        answer_file.write(f'CLAVE DE RESPUESTAS - FORMULARIO {quiz_num + 1}\n')
        answer_file.write('=' * 40 + '\n')
        
        # Shuffle the order of the states.
        states: ProvinceList = list(capitals.keys())
        random.shuffle(states)
        
        # Loop through all states, making a question for each.
        for num, state in enumerate(states, start=1):
            correct_answer: str = capitals[state]
            all_capitals: list[str] = list(capitals.values())
            wrong_answers: list[str] = [c for c in all_capitals if c != correct_answer]
            wrong_answers = random.sample(wrong_answers, 3)
            
            answer_options: list[str] = wrong_answers + [correct_answer]
            random.shuffle(answer_options)
            
            # Write the question and the answer options to the quiz file.
            quiz_file.write(f'{num}. ¿Cuál es la capital de {state}?\n')
            
            for i, char in enumerate('ABCD'):
                quiz_file.write(f"      {char}. {answer_options[i]}\n")
            quiz_file.write('\n')
            
            # Write the answer key to a file.
            correct_letter: str = 'ABCD'[answer_options.index(correct_answer)]
            answer_file.write(f"Pregunta {num:2}: {correct_letter}\n")

print("Proceso completado con éxito.")