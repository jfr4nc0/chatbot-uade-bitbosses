import os
import csv
import re
import string

# --- Constants ---
STOP_WORDS = {
    "el", "la", "los", "las", "un", "una", "unos", "unas",
    "yo", "tú", "él", "ella", "nosotros", "vosotros", "ellos", "ellas",
    "mi", "tu", "su", "nuestro", "vuestro", "sus",
    "qué", "quién", "quiénes", "cuál", "cuáles", "dónde", "cuándo", "cómo", "por", "qué",
    "es", "ser", "estar", "haber", "tener", "hacer", "poder", "decir", "ir", "ver",
    "a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "so", "sobre", "tras",
    "y", "o", "ni", "pero", "más", "si", "cuando", "aunque", "porque", "si",
    "este", "ese", "aquel", "esta", "esa", "aquella", "estos", "esos", "aquellos", "estas", "esas", "aquellas",
    "todo", "cada", "mucho", "poco", "varios", "varias", "alguno", "algunos", "alguna", "algunas", "ninguno", "ninguna",
    "mismo", "misma", "mismos", "mismas", "otro", "otra", "otros", "otras",
    "cualquier", "cualesquiera"
}
DEFAULT_FILE_NAME = 'preguntas_y_respuestas.csv'

# --- Helper Functions ---

def get_resource_path(file_name):
    """
    Determines the absolute path for a file within a 'resources' directory
    located three levels above the current script, and ensures the directory
    and file (with headers if new) exist.

    Args:
        file_name (str): The name of the resource file (e.g., 'data.csv').

    Returns:
        str or None: The absolute path to the resource file if successful,
                     otherwise None if file creation fails.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    resource_dir = os.path.join(base_dir, 'src', 'resources')

    if not os.path.exists(resource_dir):
        os.makedirs(resource_dir)

    file_full_path = os.path.join(resource_dir, file_name)

    if not os.path.exists(file_full_path):
        try:
            with open(file_full_path, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Pregunta', 'Respuesta'])
        except IOError as e:
            print(f"Error creando el archivo '{file_full_path}': {e}")
            return None

    return file_full_path

def filter_key_words(text):
    """
    Processes a text string to extract relevant keywords.
    It removes punctuation, converts text to lowercase, finds whole words,
    and filters out common stop words defined globally.

    Args:
        text (str): The input string (e.g., a user query or a question from CSV).

    Returns:
        list: A list of filtered keywords (strings). Returns an empty list
              if the input is not a string.
    """
    if not isinstance(text, str):
        return []

    text = text.translate(str.maketrans('', '', string.punctuation))
    palabras = re.findall(r'\b\w+\b', text.lower())
    return [palabra for palabra in palabras if palabra not in STOP_WORDS]

# --- Core Logic Functions ---

def save_question(file_path, question, answer):
    """
    Appends a new question, and answer to the specified CSV file.

    Args:
        file_path (str): The absolute path to the CSV file.
        question (str): The question text to save.
        answer (str): The answer text for the question.
    """
    if file_path is None:
        print("Error: No se pudo guardar la pregunta. Ruta de archivo no válida.")
        return
    try:
        with open(file_path, mode='a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([question, answer])
        print("Pregunta agregada exitosamente!")
    except Exception as e:
        print(f"Error guardando pregunta: {e}")

def find_by_key_words(user_input, file_path):
    """
    Reads the CSV file and finds the question whose filtered keywords
    best match the filtered keywords of the user's input. Matching is based
    on the number of shared whole words (keywords).

    Args:
        user_input (str): The user's input question string.
        file_path (str): The absolute path to the CSV file containing questions.

    Returns:
        tuple: A tuple containing the best matching question string and its
               corresponding answer string (str, str) if a match with at least
               one keyword is found. Returns (None, None) otherwise.
    """
    if file_path is None:
         print("Error: No se pudo buscar la pregunta. Ruta de archivo no válida.")
         return None, None

    key_words = set(filter_key_words(user_input))
    max_coincidences = 0
    best_question = None
    best_answer = None

    if not key_words:
        return None, None

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None or not all(col in reader.fieldnames for col in ['Pregunta', 'Respuesta']):
                 print(f"Error: El archivo '{file_path}' está vacío o no tiene los encabezados correctos.")
                 return None, None

            for row in reader:
                if 'Pregunta' in row and 'Respuesta' in row:
                    question_csv_text = row['Pregunta']
                    answer_csv_text = row['Respuesta']

                    key_words_csv = set(filter_key_words(question_csv_text))

                    coincidences = len(key_words.intersection(key_words_csv))

                    if coincidences > max_coincidences:
                        max_coincidences = coincidences
                        best_question = question_csv_text
                        best_answer = answer_csv_text


    except FileNotFoundError:
        print(f"Error: Archivo '{file_path}' no encontrado durante la búsqueda.")
        return None, None
    except Exception as e:
         print(f"Error al leer el archivo CSV '{file_path}' durante la búsqueda: {e}")
         return None, None

    if best_question and max_coincidences > 0:
        return best_question, best_answer
    else:
        return None, None

# --- Main Application Flow ---

def run_assistant():
    """
    Manages the main interaction loop for the F1 assistant.
    Initializes the file path, handles user input, calls functions
    to find or save questions, and prints responses.
    """
    file_name = DEFAULT_FILE_NAME
    file_path = get_resource_path(file_name)

    if file_path is None:
        print("No se pudo inicializar el asistente debido a un error con el archivo de datos.")
        return

    print("""
    ¡Hola! 👋 ¡Soy tu Asistente de F1!

    Estoy aquí para responder tus preguntas sobre el emocionante mundo de la Fórmula 1.
    Solo pregúntame lo que quieras saber.

    Además, ¡puedes ayudarme a aprender!
    Si sabes una pregunta y respuesta que no tengo, puedes agregarla.

    ¿Cómo puedes interactuar?
      - Para preguntar: Simplemente escribe tu pregunta directamente (ej: ¿Quién ganó la última carrera?).
      - Para agregar: Escribe 'agregar pregunta' y sigue las instrucciones.

    Para terminar la conversación, escribe 'exit'.
    """)

    while True:
        user_input = input("User: ").strip()

        if user_input.lower() == 'exit':
            print("¡Vuelva pronto! ¡Adiós! 👋")
            break
        if user_input.lower() == 'agregar pregunta':
            print("Okay, vamos a agregar una nueva pregunta.")
            question = input("Ingrese la pregunta: ").strip()
            answer = input("Ingrese la respuesta: ").strip()
            save_question(file_path, question, answer)
            continue

        question, answer = find_by_key_words(user_input, file_path)

        if question:
            print(f"Chatbot: Pregunta encontrada: {question}")
            print(f"Chatbot: Respuesta: {answer}")
        else:
            print("Chatbot: No tengo la suficiente información para responder a esa pregunta.")

# --- Script Entry Point ---
if __name__ == "__main__":
    run_assistant()