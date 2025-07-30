#a kivy app to create a quiz application while using a dictionary. 3 levels- easy, medium, hard. Using dictionary to store questions and answers.
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.clearcolor = (0.05, 0.1, 0.2, 1)  # dark blue background
Window.raise_window()

quiz_data = {
    "easy": [
        {"question": "Which of the following methods is used to remove a key-value pair from a Python dictionary?\na) remove()\nb) delete()\nc) pop()\nd) None of the above", "answer": "c"},
       {
  "question": "Which of the following statements about dictionaries in Python is true?\na) Dictionaries are ordered collections\nb) Dictionaries can contain duplicate keys\nc) Dictionaries are indexed by integers\nd) Dictionaries are immutable",
  "answer": "b"
    },
    {
  "question": "What arithmetic operators cannot be used with strings in Python?\na) *\nb) –\nc) +\nd) All of the mentioned",
  "answer": "b"
},{
  "question": "What are the two main types of functions in Python?\na) System function\nb) Custom function\nc) Built-in function & User defined function\nd) User function",
  "answer": "c"
},
{
  "question": "Which of the following is used to define a block of code in Python language?\na) Indentation\nb) Key\nc) Brackets\nd) All of the mentioned",
  "answer": "a"
}
    ],
    "medium": [
        {
  "question": "What will be the output of the following Python code?\n\nmy_dict = {\"x\": 10}\nprint(my_dict.get(\"y\", \"Key Not Found\"))\nprint(my_dict.get(\"x\", \"Key Not Found\"))\n\na) Key Not Found\n   10\nb) None\n   10\nc) Key Not Found\n   Key Not Found\nd) Error",
  "answer": "a"
}
,
        {
  "question": "Select the correct ways to get the value of marks key.\n\nstudent = {\n\t\"name\": \"Emma\",\n\t\"class\": 9,\n\t\"marks\": 75\n}\n\nm = student.get(2)\nm = student.get('marks')\nm = student['marks'])\n\nA. m = student.get(2)\nB. m = student.get('marks')\nC. m = student['marks']\nD. Both B and C",
  "answer": "D"
}
,
{
  "question": "Please select the correct way to empty the following dictionary:\n\nstudent = {\n\t\"name\": \"Emma\",\n\t\"class\": 9,\n\t\"marks\": 75\n}\n\ndel student\ndel student[0:2]\nstudent.clear()\n\nA. del student\nB. del student[0:2]\nC. student.clear()\nD. Both A and C",
  "answer": "C"
},
{
  "question": "What will be the output of the following Python code?\n\ndict1 = {\"key1\": 1, \"key2\": 2}\ndict2 = {\"key2\": 2, \"key1\": 1}\nprint(dict1 == dict2)",
  "answer": "True"
},
{
  "question": "Which method is used to get the value associated with a given key, returning\nNone or a specified default if the key is not found?\n\ndict.get(key)\ndict.find(key)\ndict.value(key)\ndict.lookup(key)\n\nA. dict.get(key)\nB. dict.find(key)\nC. dict.value(key)\nD. dict.lookup(key)",
  "answer": "A"
},
{
  "question": "Which of the following is NOT a valid way to create a Python dictionary?\n\n{\"key\": \"value\"}\ndict(name=\"Alice\", age=30)\ndict([(\"a\", 1), (\"b\", 2)])\ndict(1=\"one\", 2=\"two\")\n\nA. {\"key\": \"value\"}\nB. dict(name=\"Alice\", age=30)\nC. dict([(\"a\", 1), (\"b\", 2)])\nD. dict(1=\"one\", 2=\"two\")",
  "answer": "D"
}

    ],
    "hard": [
        {
  "question": "Given d = {'a': 1, 'b': 2, 'c': 3}, which of the following correctly inverts the\ndictionary so that values become keys, and multiple keys with the same value are grouped in a\nlist?\nA.\nrev = {v: k for k, v in d.items()}\nB.\nrev = {}\nfor k, v in d.items():\n\trev[v] = k\nC.\nrev = {}\nfor k, v in d.items():\n\trev.setdefault(v, []).append(k)\nD.\nrev = {k: [v] for k, v in d.items()}",
  "answer": "C"
}
,
        {
  "question": "What is the output of the following function call char_freq(\"Hello, World!\")?\n\nfrom collections import defaultdict\ndef char_freq(s):\n\tfreq = defaultdict(int)\n\tfor c in s.lower():\n\t\tif c.isalpha():\n\t\t\tfreq[c] += 1\n\treturn dict(freq)\n\nA. {'H': 1, 'E': 1, 'L': 3, 'O': 2, 'W': 1, 'R': 1, 'D': 1}\nB. {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}\nC. {'h': 1, 'e': 1, 'l': 3, 'o': 2}\nD. {'l': 3, 'o': 2, 'w': 1}",
  "answer": "B"
}
,
{
  "question": "What is the result of the following code?\n\ndata = {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}, 'c': {'x': 5,\n'y': 6}}\ntotal = sum(v for inner in data.values() for v in inner.values())\nprint(total)\n\nA. 15\nB. 21\nC. 10\nD. 6",
  "answer": "B"
},
{
  "question": "Which line of code will create a new dictionary from d = {'a': 1, 'b': 'two', 'c':\n3.0, 'd': [4], 'e': 5} containing only items where the value is an integer?\n\nA.\nnew_d = {k: v for k, v in d.items() if type(v) == int}\nB.\nnew_d = {k: v for k, v in d.items() if isinstance(v, int)}\nC.\nnew_d = {k: v for k, v in d.items() if v.is_integer()}\nD.\nnew_d = {k: v for k, v in d.items() if isinstance(v, str)}",
  "answer": "B"
},
{
  "question": "Given d = {'p': 3, 'q': 1, 'r': 3, 's': 2, 't': 3}, which of the following\ncorrectly finds the most frequent value and the keys that have that value?\n\nA.\nfrom collections import Counter\nvalue_counts = Counter(d)\nmost_common_value = value_counts.most_common(1)[0][0]\n\nB.\nmost_common_value = max(d.values())\nkeys = [k for k, v in d.items() if v == most_common_value]\n\nC.\nfrom collections import Counter\nvalue_counts = Counter(d.values())\nmost_common_value = value_counts.most_common(1)[0][0]\nkeys = [k for k, v in d.items() if v == most_common_value]\nprint(most_common_value, keys)\n\nD.\nkeys = [k for k in d if d[k] == 1]",
  "answer": "C"
}


    ]
}

class QuizWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        self.level = None
        self.question_index = 0
        self.score = 0
        self.questions = []
        self.show_home()

    def show_home(self, *args):
        self.clear_widgets()
        main_layout = BoxLayout(orientation='vertical', size_hint=(0.7, 0.7), pos_hint={'center_x': 0.5, 'center_y': 0.5}, spacing=18)
        lbl = Label(
            text="🏫 [b]Quiz App[/b]",
            markup=True,
            font_size=32,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.3),
            halign="center",
            valign="middle"
        )
        lbl.bind(size=lbl.setter('text_size'))
        main_layout.add_widget(lbl)
        btn_layout = BoxLayout(
            orientation='vertical',
            spacing=14,
            size_hint=(1, 0.7),
            pos_hint={'center_x': 0.5}
        )
        for lvl in quiz_data.keys():
            btn = Button(
                text=lvl.capitalize(),
                font_size=20,
                background_color=(0.1, 0.4, 0.8, 1),
                color=(1, 1, 1, 1),
                size_hint=(1, None),
                height=48,
                border=(16, 16, 16, 16)
            )
            btn.bind(on_press=self.select_level)
            btn_layout.add_widget(btn)
        main_layout.add_widget(btn_layout)
        self.add_widget(Widget(size_hint=(1, 0.15)))  # Spacer
        self.add_widget(main_layout)
        self.add_widget(Widget(size_hint=(1, 0.15)))  # Spacer

    def select_level(self, instance):
        self.level = instance.text.lower()
        self.questions = quiz_data[self.level]
        self.question_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        self.clear_widgets()
        main_layout = BoxLayout(orientation='vertical', size_hint=(0.7, 0.7), pos_hint={'center_x': 0.5, 'center_y': 0.5}, spacing=14)
        lbl = Label(
            text=f"[b]{self.level.capitalize()} Level[/b]\n\nQ{self.question_index+1}: {self.questions[self.question_index]['question']}",
            markup=True,
            font_size=22,
            color=(0.8, 0.9, 1, 1),
            size_hint=(1, 0.3),
            halign="center",
            valign="middle"
        )
        lbl.bind(size=lbl.setter('text_size'))
        main_layout.add_widget(lbl)
        self.txt = TextInput(
            hint_text="Your answer",
            multiline=False,
            font_size=18,
            size_hint=(1, None),
            height=40,
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(0.8, 0.9, 1, 1),
            padding=(10, 10)
        )
        main_layout.add_widget(self.txt)
        btn_layout = BoxLayout(
            orientation='horizontal',
            spacing=14,
            size_hint=(1, None),
            height=40,
            pos_hint={'center_x': 0.5}
        )
        submit_btn = Button(
            text="Submit",
            font_size=16,
            background_color=(0.1, 0.4, 0.8, 1),
            color=(1, 1, 1, 1),
            border=(16, 16, 16, 16),
            size_hint=(0.5, 1)
        )
        submit_btn.bind(on_press=self.check_answer)
        home_btn = Button(
            text="Home",
            font_size=16,
            background_color=(0.05, 0.1, 0.2, 1),
            color=(1, 1, 1, 1),
            border=(16, 16, 16, 16),
            size_hint=(0.5, 1)
        )
        home_btn.bind(on_press=self.show_home)
        btn_layout.add_widget(submit_btn)
        btn_layout.add_widget(home_btn)
        main_layout.add_widget(btn_layout)
        self.add_widget(Widget(size_hint=(1, 0.15)))  # Spacer
        self.add_widget(main_layout)
        self.add_widget(Widget(size_hint=(1, 0.15)))  # Spacer

    def check_answer(self, instance):
        user_ans = self.txt.text.strip().lower()
        correct_ans = self.questions[self.question_index]["answer"].lower()
        if user_ans == correct_ans:
            self.score += 1
            msg = "[color=00ff00]Correct![/color]"
        else:
            msg = f"[color=ff0000]Wrong![/color] Correct answer: {correct_ans.capitalize()}"
        self.show_feedback(msg)

    def show_feedback(self, msg):
        self.clear_widgets()
        main_layout = BoxLayout(orientation='vertical', size_hint=(0.7, 0.7), pos_hint={'center_x': 0.5, 'center_y': 0.5}, spacing=14)
        lbl = Label(
            text=msg,
            markup=True,
            font_size=20,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.5),
            halign="center",
            valign="middle"
        )
        lbl.bind(size=lbl.setter('text_size'))
        main_layout.add_widget(lbl)
        btn_layout = BoxLayout(
            orientation='horizontal',
            spacing=14,
            size_hint=(1, None),
            height=40,
            pos_hint={'center_x': 0.5}
        )
        next_btn = Button(
            text="Next",
            font_size=16,
            background_color=(0.1, 0.4, 0.8, 1),
            color=(1, 1, 1, 1),
            border=(16, 16, 16, 16),
            size_hint=(0.5, 1)
        )
        next_btn.bind(on_press=self.next_question)
        home_btn = Button(
            text="Home",
            font_size=16,
            background_color=(0.05, 0.1, 0.2, 1),
            color=(1, 1, 1, 1),
            border=(16, 16, 16, 16),
            size_hint=(0.5, 1)
        )
        home_btn.bind(on_press=self.show_home)
        btn_layout.add_widget(next_btn)
        btn_layout.add_widget(home_btn)
        main_layout.add_widget(btn_layout)
        self.add_widget(Widget(size_hint=(1, 0.15)))  # Spacer
        self.add_widget(main_layout)
        self.add_widget(Widget(size_hint=(1, 0.15)))  # Spacer

    def next_question(self, instance):
        self.question_index += 1
        if self.question_index < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.clear_widgets()
        main_layout = BoxLayout(orientation='vertical', size_hint=(0.7, 0.7), pos_hint={'center_x': 0.5, 'center_y': 0.5}, spacing=14)
        lbl = Label(
            text=f"[b]Quiz Finished![/b]\n\nYour score: [color=00ff00]{self.score}[/color]/[color=00ff00]{len(self.questions)}[/color]",
            markup=True,
            font_size=24,
            color=(0.8, 0.9, 1, 1),
            size_hint=(1, 0.3),
            halign="center",
            valign="middle"
        )
        lbl.bind(size=lbl.setter('text_size'))
        main_layout.add_widget(lbl)
        btn_layout = BoxLayout(
            orientation='horizontal',
            spacing=14,
            size_hint=(1, None),
            height=40,
            pos_hint={'center_x': 0.5}
        )
        retry_btn = Button(
            text="Retry",
            font_size=16,
            background_color=(0.1, 0.4, 0.8, 1),
            color=(1, 1, 1, 1),
            border=(16, 16, 16, 16),
            size_hint=(0.5, 1)
        )
        retry_btn.bind(on_press=lambda x: self.select_level(Button(text=self.level.capitalize())))
        home_btn = Button(
            text="Home",
            font_size=16,
            background_color=(0.05, 0.1, 0.2, 1),
            color=(1, 1, 1, 1),
            border=(16, 16, 16, 16),
            size_hint=(0.5, 1)
        )
        home_btn.bind(on_press=self.show_home)
        btn_layout.add_widget(retry_btn)
        btn_layout.add_widget(home_btn)
        main_layout.add_widget(btn_layout)
        self.add_widget(Widget(size_hint=(1, 0.15)))  # Spacer
        self.add_widget(main_layout)
        self.add_widget(Widget(size_hint=(1, 0.15)))  # Spacer

class QuizApp(App):
    def build(self):
        return QuizWidget()

if __name__ == "__main__":
    QuizApp().run()