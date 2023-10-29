import random
import re
from tkinter import *

version = "0.0.3"

TEXT_WDG_WDTH = 69
TEXT_WDG_HGHT = 25


class ChooseBoxSimulation:  # Simulation of BooleanVar for independent test
    def __init__(self):
        self.return_value_bool = True

    def get(self): return self.return_value_bool


without_dot_bool = ChooseBoxSimulation()
without_capital_bool = ChooseBoxSimulation()


def get_separator_for_each_row(inputValue):
    # TODO return separators back
    global each_row_separator
    inputValue_list = list(map(str.strip, re.split(r'\r?\n', inputValue)))


def split_into_list(inputValue):
    # Delete all start line symbols which usual for list as: 1. 1) a) a.
    inputValue = re.sub(r"\b(?:[1-9]\.|[a-z]\)|[a-z]\.|[1-9]\.\s*|\d\)\s*|[a-z]\)\s*)", "", inputValue)

    inputValue_list = list(map(str.strip, re.split(r'\r?\n', inputValue)))  # split it by rows

    return inputValue_list


def get_text_from_input():
    """
    1. Get text from each line
    2. take out a start symbols as 1. 1 1) a-z. a-z)
    3. return it as a list prepared to shuffling
    """
    global text_box_in

    inputValue = text_box_in.get("1.0", "end-1c")

    get_separator_for_each_row(inputValue)

    inputValue_list = split_into_list(inputValue)

    return inputValue_list


def randomise_text(list_with_text_lines):
    global without_dot_bool
    global without_capital_bool

    for position, each_line in enumerate(list_with_text_lines):
        fixed_text = re.sub(r'(\b|\S)\x08{3,}', r' ', each_line)
        each_line_words_list = fixed_text.split()
        shuffled_words_list = each_line_words_list.copy()

        tries_counter = 100
        while each_line_words_list == shuffled_words_list:
            random.shuffle(shuffled_words_list)
            if tries_counter < 0:
                break
            tries_counter -= 1

        string_to_save = " ".join(shuffled_words_list)

        if without_capital_bool.get():
            string_to_save = string_to_save.lower()

        if without_dot_bool.get():
            string_to_save = string_to_save.replace(".", "")

        list_with_text_lines[position] = string_to_save

    return list_with_text_lines


def drop_text_to_output(randomised_text_list):
    global text_box_out

    text_to_show = ""
    for randomised_text in randomised_text_list:
        text_to_show += randomised_text + "\n"

    text_box_out.delete("1.0", "end-1c")

    text_box_out.insert(END, text_to_show)


def shuffle_text_button_call():
    inputValue_list = get_text_from_input()
    randomised_text_list = randomise_text(inputValue_list)
    drop_text_to_output(randomised_text_list)


def drop_info_to_screen():
    global version
    text_to_show = f"version {version}\nWritten by Denys Zakharov\ndeniszaharov19981208@gmail.com/Linkedin:denys-zakharov"

    text_box_in.delete("1.0", "end-1c")
    text_box_out.delete("1.0", "end-1c")

    text_box_in.insert(END, text_to_show)
    text_box_out.insert(END, text_to_show)


if __name__ == "__main__":
    root = Tk()
    root.geometry("1312x423")
    text_box_in = Text(root, height=TEXT_WDG_HGHT, width=TEXT_WDG_WDTH)
    text_box_out = Text(root, height=TEXT_WDG_HGHT, width=TEXT_WDG_WDTH)

    without_dot_bool = BooleanVar()
    without_capital_bool = BooleanVar()

    b1 = Button(root, text="--SHUFFLE-->", command=lambda: shuffle_text_button_call())
    b0 = Button(root, text="?", command=lambda: drop_info_to_screen())

    text_box_in.pack(side="left", expand=True)
    text_box_out.pack(side="right", expand=True)

    C1 = Checkbutton(root, text="Without dot in the end", variable=without_dot_bool, onvalue=1, offvalue=0, height=5,
                     width=20)
    C2 = Checkbutton(root, text="Without capital letters", variable=without_capital_bool, onvalue=1, offvalue=0,
                     height=5,
                     width=20)
    C3 = Checkbutton(root, text="Save list separates", onvalue=1, offvalue=0, height=5, width=20)

    b0.pack(side="bottom")

    C1.pack(side="bottom")
    C2.pack(side="bottom")

    b1.pack(side="bottom")

    root.mainloop()
