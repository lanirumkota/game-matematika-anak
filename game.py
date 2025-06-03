import tkinter as tk
import random
import time

class MathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Matematika bapak")
        self.root.geometry("450x400")
        self.root.configure(bg="#FFF8DC")  # Latar belakang pastel cerah

        self.time_limit = 30
        self.score = 0
        self.start_time = None

        self.question_label = tk.Label(
            root,
            text="Tekan tombol mulai untuk bermain!",
            font=('Comic Sans MS', 18, 'bold'),
            bg="#FFF8DC",
            fg="#FF5733"
        )
        self.question_label.pack(pady=20)

        input_frame = tk.Frame(root, bg="#FFF8DC")
        input_frame.pack(pady=10)

        self.answer_entry = tk.Entry(input_frame, font=('Comic Sans MS', 18), width=10, state='disabled', justify='center')
        self.answer_entry.grid(row=0, column=0, padx=5)
        self.answer_entry.bind('<Return>', self.check_answer)

        self.submit_button = tk.Button(
            input_frame,
            text="Jawab 🎯",
            font=('Comic Sans MS', 14),
            bg="#FFD700",
            activebackground="#FFEC8B",
            state='disabled',
            command=self.check_answer_button
        )
        self.submit_button.grid(row=0, column=1, padx=5)

        self.start_button = tk.Button(
            root,
            text="Mulai 🚀",
            font=('Comic Sans MS', 14),
            command=self.start_game,
            bg="#90EE90",
            activebackground="#7CCD7C"
        )
        self.start_button.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=('Comic Sans MS', 14), bg="#FFF8DC")
        self.feedback_label.pack(pady=5)

        self.score_label = tk.Label(root, text="Skor: 0", font=('Comic Sans MS', 14), bg="#FFF8DC", fg="#008B8B")
        self.score_label.pack(pady=2)

        self.timer_label = tk.Label(root, text="Waktu: 30 detik", font=('Comic Sans MS', 14), bg="#FFF8DC", fg="#8B0000")
        self.timer_label.pack(pady=2)

    def start_game(self):
        self.score = 0
        self.start_time = time.time()
        self.answer_entry.config(state='normal')
        self.submit_button.config(state='normal')
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus()
        self.start_button.config(state='disabled')
        self.feedback_label.config(text="")
        self.update_score()
        self.update_timer()
        self.next_question()

    def update_timer(self):
        elapsed = int(time.time() - self.start_time)
        remaining = self.time_limit - elapsed
        self.timer_label.config(text=f"Waktu: {remaining} detik")

        if remaining <= 0:
            self.end_game()
        else:
            self.root.after(1000, self.update_timer)

    def next_question(self):
        self.a = random.randint(1, 10)
        self.b = random.randint(1, 10)
        self.op = random.choice(['+', '-', '*'])

        if self.op == '+':
            self.correct_answer = self.a + self.b
        elif self.op == '-':
            self.correct_answer = self.a - self.b
        elif self.op == '*':
            self.correct_answer = self.a * self.b

        self.question_label.config(text=f"Berapakah {self.a} {self.op} {self.b}?")
        self.answer_entry.delete(0, tk.END)

    def check_answer(self, event):
        self.process_answer()

    def check_answer_button(self):
        self.process_answer()

    def process_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
        except ValueError:
            self.feedback_label.config(text="⚠️ Masukkan angka!", fg="orange")
            return

        if int(time.time() - self.start_time) >= self.time_limit:
            self.end_game()
            return

        if user_answer == self.correct_answer:
            self.feedback_label.config(text="🎉 Benar!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text=f"😞 Salah. Jawaban: {self.correct_answer}", fg="red")

        self.update_score()
        self.next_question()

    def update_score(self):
        self.score_label.config(text=f"Skor: {self.score}")

    def end_game(self):
        self.answer_entry.config(state='disabled')
        self.submit_button.config(state='disabled')
        self.question_label.config(text="⏰ Waktu habis!")
        self.feedback_label.config(text=f"🏁 Skor akhir kamu: {self.score}", fg="blue")
        self.start_button.config(state='normal')
        self.timer_label.config(text="Waktu: 0 detik")


# Program utama
if __name__ == "__main__":
    root = tk.Tk()
    game = MathGame(root)
    root.mainloop()
   

