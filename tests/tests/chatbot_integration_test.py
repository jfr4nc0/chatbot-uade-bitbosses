import unittest
import os
from unittest.mock import patch
from src.assistant_simple.assistant import main

class TestChatbotIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a test CSV file in the tests/resources directory
        cls.resources_dir = 'tests/resources'
        os.makedirs(cls.resources_dir, exist_ok=True)
        cls.test_csv = os.path.join(cls.resources_dir, 'formula_1_dataset.csv')
        with open(cls.test_csv, 'w') as f:
            f.write("Quien gano la Mundial de pilotos en 2023?,El ganador fua Max Verstappen.\n")

    @classmethod
    def tearDownClass(cls):
        # Remove the test CSV file and directory after tests
        if os.path.exists(cls.test_csv):
            os.remove(cls.test_csv)
        if os.path.exists(cls.resources_dir) and not os.listdir(cls.resources_dir):
            os.rmdir(cls.resources_dir)

    @patch('builtins.input', side_effect=['Quien gano la Mundial de pilotos en 2023?', 'exit'])
    @patch('builtins.print')
    def test_chatbot_with_actual_csv(self, mock_print, mock_input):
        # Run the main function
        main()

        # Verify the chatbot's response
        mock_print.assert_any_call("Chatbot: El ganador fue Max Verstappen.")
        mock_print.assert_any_call("Vuelva pronto!")

if __name__ == '__main__':
    unittest.main()