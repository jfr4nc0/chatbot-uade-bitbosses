import csv
import os

class FilesUtils:
    @staticmethod
    def get_resource_path(file_name):
        """Get the full path to a file in the resources directory."""
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        return os.path.join(base_dir, 'src/resources', file_name)

    @staticmethod
    def load_questions(file_name):
        """Load questions and answers from a CSV file."""
        file_path = FilesUtils.get_resource_path(file_name)
        questions = {}
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:  # Ensure each row has a question and an answer
                        question, answer = row
                        questions[question.strip().lower()] = answer.strip()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        return questions

    @staticmethod
    def save_question(file_name, question, answer):
        """Save a new question and answer to the CSV file."""
        file_path = FilesUtils.get_resource_path(file_name)
        try:
            with open(file_path, mode='a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file, lineterminator='.\n')
                writer.writerow([question, answer])
        except Exception as e:
            print(f"Error saving question: {e}")