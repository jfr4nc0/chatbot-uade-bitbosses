from src.utils.FilesUtils import FilesUtils

def main():
    file_name = 'preguntas_y_respuestas.csv'

    # Load questions and answers from the CSV file
    questions = FilesUtils.load_questions(file_name)

    print("Hola! Soy un asistente de F1! Ingrese su pregunta o 'exit' para salir.")
    print("Puede ingresar una pregunta y una respuesta para agregarla a la base de datos con 'agregar pregunta'.")

    while True:
        user_input = input("User: ").strip().lower()

        if user_input == 'exit':
            print("Vuelva pronto!")
            break
        if user_input == 'agregar pregunta':
            question = input("Ingrese la pregunta: ").strip().lower()
            answer = input("Ingrese la respuesta: ").strip().lower()
            FilesUtils.save_question(file_name, question, answer)
            questions = FilesUtils.load_questions(file_name)
            print("Pregunta agregada exitosamente!")
            continue

        # Search for the question in the loaded dictionary
        answer = questions.get(user_input)

        if answer:
            print(f"Chatbot: {answer}")
        else:
            print("Chatbot: No tengo la suficiente información para responder a esa pregunta.")


if __name__ == "__main__":
    main()