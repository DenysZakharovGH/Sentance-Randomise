import unittest
from Random_Sentence_Generator import split_into_list, randomise_text


class MyTestCase(unittest.TestCase):
    def test_regular_expression(self):
        test_text = """
        1. Creates an instance of the class tkinter.Tk.
        2) this creates what is called the "root" window. By conventon,
        3)the root window in Tkinter is usually called "root",
        4.but you are free to call it by any other name.
        If you remove the line, the window created will disappear immediately as the script stops running. This will happen so fast
        A LabeFrame that in order to demonstrate the string returned by the
        """

        expected_output = ['', 'Creates an instance of the class tkinter.Tk.',
                           'this creates what is called the "root" window. By conventon,',
                           'the root window in Tkinter is usually called "root",',
                           'but you are free to call it by any other name.',
                           'If you remove the line, the window created will disappear immediately as the script stops running. This will happen so fast',
                           'A LabeFrame that in order to demonstrate the string returned by the', '']

        output_text_in_list = split_into_list(test_text)

        self.assertEqual(expected_output, output_text_in_list)  # add assertion here

    def test_randomise_double_space(self):
        expected_result = ['']
        output = randomise_text(["  "])
        self.assertEqual(expected_result, output)

    def test_randomise_empty(self):
        expected_result = ['']
        output = randomise_text([""])
        self.assertEqual(expected_result, output)

    def test_randomise_character_lose(self):
        test_line = "If you remove the line, the window created will disappear immediately as the script stops running. This will happen so fast"
        expected_list_len = len(test_line.split())
        output = randomise_text([test_line])[0].split()
        self.assertEqual(expected_list_len, len(output))

    def test_check_flag_of_no_dot(self):
        expected_result = ['dot', ""]
        output = randomise_text(['dot. ', ".."])
        self.assertEqual(expected_result, output)

    def test_check_flag_of_capital_letter(self):
        expected_result = ['dot', "capital"]
        output = randomise_text(['DoT. ', "CAPITAL"])
        self.assertEqual(expected_result, output)

    def test_shuffler(self):
        # Explanation: randomise shuffle words until input sentence != output sentence or 100 times,
        # you definitely should play casino tonight, if that test fail.
        expected_result = ['first second', "capital"]
        output = randomise_text(['second first', "capital"])
        self.assertEqual(expected_result, output)


if __name__ == '__main__':
    unittest.main()
