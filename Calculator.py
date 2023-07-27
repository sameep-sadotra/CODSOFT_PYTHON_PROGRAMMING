import tkinter as tk
import math

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("400x600")
        self.configure(bg="white")

        self.result_var = tk.StringVar()

        self.create_widgets()
        self.previous_calculations = []

    def create_widgets(self):
        # Entry widget to display the result
        result_entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 20), justify='right')
        result_entry.pack(pady=10, padx=10, fill=tk.BOTH)

        # Frame to hold buttons
        button_frame = tk.Frame(self, bg='white')
        button_frame.pack()

        # Buttons for numbers and operations
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '+'),
            ('sqrt', 'square', 'C', 'History')
        ]

        for row in buttons:
            frame = tk.Frame(button_frame, bg='white')
            frame.pack()

            for btn_text in row:
                btn = tk.Button(frame, text=btn_text, font=("Arial", 12), width=8, height=3, command=lambda text=btn_text: self.on_button_click(text))
                btn.pack(side=tk.LEFT, padx=5, pady=5)

        # Equal button
        equal_btn = tk.Button(button_frame, text='=', font=("Arial", 12), width=8, height=3, command=self.on_equal_click)
        equal_btn.pack(side=tk.LEFT, padx=5, pady=5)

        # History Textbox
        self.history_textbox = tk.Text(self, font=("Arial", 12), width=30, height=10)
        self.history_textbox.pack(padx=10, pady=5)

    def on_button_click(self, text):
        current_value = self.result_var.get()
        if text == 'C':
            self.result_var.set('')
        elif text == 'sqrt':
            try:
                num = float(current_value)
                if num >= 0:
                    result = math.sqrt(num)
                    self.result_var.set(result)
                else:
                    self.result_var.set("Error")
            except ValueError:
                self.result_var.set("Error")
        elif text == 'square':
            try:
                num = float(current_value)
                result = num ** 2
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif text == 'History':
            self.show_history()
        else:
            self.result_var.set(current_value + text)

    def on_equal_click(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
            self.previous_calculations.append(f"{self.result_var.get()} = {result}")
            self.update_history()
        except Exception as e:
            self.result_var.set("Error")

    def update_history(self):
        self.history_textbox.delete(1.0, tk.END)
        for calc in self.previous_calculations:
            self.history_textbox.insert(tk.END, calc + "\n")

    def show_history(self):
        history_window = tk.Toplevel(self)
        history_window.title("History")
        history_window.geometry("400x400")
        history_window.configure(bg="white")

        history_label = tk.Label(history_window, text="History of Calculations", font=("Arial", 14), bg="white")
        history_label.pack(pady=10)

        history_textbox = tk.Text(history_window, font=("Arial", 12), width=40, height=10)
        history_textbox.pack(padx=10, pady=5)

        for calc in self.previous_calculations:
            history_textbox.insert(tk.END, calc + "\n")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()

