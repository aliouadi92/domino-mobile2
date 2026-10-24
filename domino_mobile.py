from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class DominoMobileApp(App):
    def build(self):
        self.score1 = 0
        self.score2 = 0
        self.round_num = 1

        root = BoxLayout(orientation='vertical', padding=20, spacing=15)

        root.add_widget(Label(text="🎲 حاسبة الدومينو (أندرويد) 🎲", font_size=22, color=(0.8, 0.9, 1, 1), size_hint_y=None, height=40))

        scores_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=100)
        
        self.lbl_s1 = Label(text="0", font_size=36, color=(1, 1, 1, 1))
        self.lbl_s2 = Label(text="0", font_size=36, color=(1, 1, 1, 1))
        
        box1 = BoxLayout(orientation='vertical')
        box1.add_widget(Label(text="الفريق 1", color=(0.5, 0.7, 1, 1), font_size=16))
        box1.add_widget(self.lbl_s1)
        
        box2 = BoxLayout(orientation='vertical')
        box2.add_widget(Label(text="الفريق 2", color=(0.6, 1, 0.6, 1), font_size=16))
        box2.add_widget(self.lbl_s2)

        scores_layout.add_widget(box1)
        scores_layout.add_widget(Label(text="VS", font_size=20, color=(1, 0.5, 0.5, 1), size_hint_x=None, width=40))
        scores_layout.add_widget(box2)
        root.add_widget(scores_layout)

        inputs_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        self.input1 = TextInput(hint_text="نقاط ف 1", multiline=False, font_size=18, halign='center')
        self.input2 = TextInput(hint_text="نقاط ف 2", multiline=False, font_size=18, halign='center')
        
        inputs_layout.add_widget(self.input1)
        inputs_layout.add_widget(self.input2)
        root.add_widget(inputs_layout)

        btn_add = Button(text="تسجيل الجولة ➕", font_size=18, background_color=(0.3, 0.7, 0.3, 1), size_hint_y=None, height=50)
        btn_add.bind(on_press=self.add_round)
        root.add_widget(btn_add)

        btn_reset = Button(text="لعبة جديدة 🔄", font_size=16, background_color=(0.8, 0.3, 0.3, 1), size_hint_y=None, height=45)
        btn_reset.bind(on_press=self.reset_game)
        root.add_widget(btn_reset)

        root.add_widget(Label(text="سجل الجولات:", font_size=14, color=(0.8, 0.8, 0.8, 1), size_hint_y=None, height=30))
        
        self.history_label = Label(text="", font_size=14, color=(1, 1, 1, 1), valign='top', halign='center')
        self.history_label.bind(size=self.history_label.setter('text_size'))
        
        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.history_label)
        root.add_widget(scroll)

        return root

    def add_round(self, instance):
        try:
            p1 = int(self.input1.text) if self.input1.text.isdigit() else 0
            p2 = int(self.input2.text) if self.input2.text.isdigit() else 0
        except:
            p1, p2 = 0, 0

        if p1 == 0 and p2 == 0:
            return

        self.score1 += p1
        self.score2 += p2

        self.lbl_s1.text = str(self.score1)
        self.lbl_s2.text = str(self.score2)

        current_text = self.history_label.text
        new_line = f"جولة {self.round_num}: فريق 1 (+{p1}) | فريق 2 (+{p2})\n"
        self.history_label.text = new_line + current_text

        self.round_num += 1
        self.input1.text = ""
        self.input2.text = ""

    def reset_game(self, instance):
        self.score1 = 0
        self.score2 = 0
        self.round_num = 1
        self.lbl_s1.text = "0"
        self.lbl_s2.text = "0"
        self.history_label.text = ""

if __name__ == '__main__':
    DominoMobileApp().run()
