from src.utils.FilesUtils import FilesUtils

def main():
    file_name = 'formula_1_dataset.csv'

    # Load questions and answers from the CSV file
    questions = FilesUtils.load_questions(file_name)

    print("Hola! Soy un asistente de F1! Ingrese su pregunta o 'exit' para salir.")

    while True:
        user_input = input("User: ").strip().lower()

        if user_input == 'exit':
            print("Vuelva pronto!")
            break

        # Search for the question in the loaded dictionary
        answer = questions.get(user_input)

        if answer:
            print(f"Chatbot: {answer}")
        else:
            print("Chatbot: No tengo la suficiente información para responder a esa pregunta.")


if __name__ == "__main__":
    main()