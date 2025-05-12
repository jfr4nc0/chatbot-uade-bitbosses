# chatbot-uade-bitbosses

## Description

This project is a chatbot application designed to answer questions based on a dataset. It uses a CSV file as its knowledge base and provides responses to user queries.

## Requirements

- Python 3.8 or higher
- `pip` (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chatbot-uade-bitbosses.git
   cd chatbot-uade-bitbosses
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

<!--
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
-->

## Running the Program

1. Ensure the dataset file `preguntas_y_respuestas.csv` is located in the `src/resources` directory.

2. Run the chatbot:
   ```bash
   python main.py
   ```

3. Interact with the chatbot by typing your questions. To exit, type `exit`.

<!--
## Running Tests

To ensure the program works as expected, you can run the integration tests:

1. Run the tests using `unittest`:
   ```bash
   python -m unittest discover tests
   ```
-->

## Project Structure

- `main.py`: Entry point of the application.
- `src/`: Contains the chatbot logic and resources.
<!--
- `tests/`: Contains integration tests for the chatbot.
-->
## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```