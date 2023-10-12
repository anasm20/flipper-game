import random
import tkinter as tk


#### To use flipperGUI please use the Terminal (python3 flipperGUI.py) ####

class Zustand:
    NoCredit = 0
    Ready = 1
    Playing = 2
    EndState = 3

class FlipperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Flipperautomat")

        self.credit = 0
        self.balls = 3
        self.state = Zustand.NoCredit

        self.label = tk.Label(root, text="State: NoCredit\nBalls left: 3\nCredit: 0")
        self.label.pack()

        self.insert_coin_button = tk.Button(root, text="Insert Coin", command=self.insert_coin)
        self.insert_coin_button.pack()

        self.press_start_button = tk.Button(root, text="Press Start", command=self.press_start)
        self.press_start_button.pack()

        self.play_button = tk.Button(root, text="Play", command=self.play)
        self.play_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()

    def insert_coin(self):
        if self.state == Zustand.NoCredit:
            self.credit += 1
            self.state = Zustand.Ready
        else:
            self.label.config(text="You already have credit.")

        self.update_label()

    def press_start(self):
        if self.state == Zustand.Ready:
            self.state = Zustand.Playing
        elif self.state == Zustand.NoCredit:
            self.label.config(text="No credit. Insert coin.")
        else:
            self.label.config(text="Game is already in progress.")

        self.update_label()

    def play(self):
        if self.state == Zustand.Playing:
            self.balls -= 1
            if self.balls == 0:
                self.label.config(text="Game over.")
                self.state = Zustand.NoCredit
            else:
                score = random.randint(1, 100)
                self.credit += score
                self.label.config(text=f"You scored {score} points. Credit: {self.credit}")
                if self.credit >= 1000:
                    self.label.config(text="You win a free game!")
                    self.credit -= 1000
        elif self.state == Zustand.NoCredit:
            self.label.config(text="No credit. Insert coin first.")
        else:
            self.label.config(text="Pressing start during the game shows credits.")

        self.update_label()

    def update_label(self):
        state_names = {
            Zustand.NoCredit: "NoCredit",
            Zustand.Ready: "Ready",
            Zustand.Playing: "Playing",
            Zustand.EndState: "EndState"
        }
        state_name = state_names[self.state]
        self.label.config(text=f"State: {state_name}\nBalls left: {self.balls}\nCredit: {self.credit}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlipperGUI(root)
    root.mainloop()
