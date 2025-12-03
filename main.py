from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

# تنظیمات اولیه
Window.clearcolor = (0.1, 0.1, 0.1, 1)


class CalculatorApp(App):
    def build(self):
        self.equation = ""
        self.last_result = ""
        
        # لایه اصلی
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # نمایشگر
        self.display = TextInput(
            text='',
            multiline=False,
            readonly=True,
            halign='right',
            font_size=50,
            size_hint=(1, 0.2),
            background_color=(0.2, 0.2, 0.2, 1),
            foreground_color=(1, 1, 1, 1)
        )
        main_layout.add_widget(self.display)
        
        # لایه دکمه‌ها
        buttons_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.8))
        
        # لیست دکمه‌ها
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '.', '+',
            '(', ')', '←', '='
        ]
        
        # ایجاد دکمه‌ها
        for button in buttons:
            btn = Button(
                text=button,
                font_size=30,
                background_color=self.get_button_color(button),
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(btn)
        
        main_layout.add_widget(buttons_layout)
        return main_layout
    
    def get_button_color(self, text):
        """تعیین رنگ دکمه بر اساس نوع"""
        if text in ['/', '*', '-', '+', '=', '(', ')']:
            return (1, 0.5, 0, 1)  # نارنجی برای عملگرها
        elif text in ['C', '←']:
            return (1, 0, 0, 1)  # قرمز برای حذف
        else:
            return (0.3, 0.3, 0.3, 1)  # خاکستری برای اعداد
    
    def on_button_press(self, instance):
        current_text = self.display.text
        button_text = instance.text
        
        if button_text == '=':
            try:
                # جایگزینی نمادهای ریاضی
                expression = current_text.replace('×', '*').replace('÷', '/')
                result = str(eval(expression))
                self.display.text = result
                self.last_result = result
            except Exception as e:
                self.display.text = "Error"
                self.last_result = ""
        
        elif button_text == 'C':
            self.display.text = ''
            self.last_result = ''
        
        elif button_text == '←':
            self.display.text = current_text[:-1]
        
        elif button_text == '(' and current_text and current_text[-1].isdigit():
            self.display.text = current_text + '*('
        
        elif button_text == ')' and self.last_result:
            self.display.text = self.last_result
        
        else:
            # برای نمایش زیباتر
            display_text = button_text
            if button_text == '*':
                display_text = '×'
            elif button_text == '/':
                display_text = '÷'
            
            self.display.text = current_text + display_text


if __name__ == '__main__':
    CalculatorApp().run()