import random
from termcolor import colored

# Zustände des Flipperautomaten
class Zustand:
    NoCredit = 0
    Ready = 1
    Playing = 2
    EndState = 3

# Befehlsklasse für die Punktevergabe
class PunkteVerleihen:
    def __init__(self, punkte):
        self.punkte = punkte

    def execute(self, flipper):
        flipper.credit += self.punkte

# Befehlsklasse für die Auswahl des Spielers
class SpielerAuswahl:
    def __init(self, spieler):
        self.spieler = spieler

    def execute(self, flipper):
        flipper.selected_player = self.spieler

# Elemente des Flipper-Spiels
class FlipperElement:
    def __init__(self, name):
        self.name = name

    def hit(self):
        pass

# Ein einfaches Hole-Element, das Punkte vergibt und Spieler auswählt
class Hole(FlipperElement):
    def hit(self):
        punkte_verleihen = PunkteVerleihen(random.randint(10, 50))
        spieler_auswahl = SpielerAuswahl(random.choice([1, 2, 3]))
        return [punkte_verleihen, spieler_auswahl]

# Flipperautomat mit Text in weißer Farbe
class FlipperAutomat:
    def __init__(self):
        self.credit = 0
        self.balls = 3
        self.state = Zustand.NoCredit
        self.selected_player = 1
        self.first_time = True

    def insert_coin(self):
        if self.state == Zustand.NoCredit:
            self.credit += 1
            self.state = Zustand.Ready
        else:
            print("You already have credit.")

    def press_start(self):
        if self.state == Zustand.Ready:
            self.state = Zustand.Playing
            if self.first_time:
                self.show_welcome_message()
                self.first_time = False
            self.show_playing_text()
        elif self.state == Zustand.NoCredit:
            print("No credit. Insert coin.")
        else:
            print("Game is already in progress.")

    def show_welcome_message(self):
        welcome_text = "Welcome to the Best Flipper Game"
        formatted_text = colored(welcome_text, "white", attrs=["bold"])
        print(formatted_text)

    def show_playing_text(self):
        if self.state == Zustand.Playing:
            ball_type = random.choice(["# Ball", " "])  # Beispielhaft: Zufällig ein Balltyp
            white_text = colored(ball_type, "white")
            print(white_text)

    def play(self):
        if self.state == Zustand.Playing:
            if self.balls > 0:
                self.balls -= 1
                if self.balls <= 0:
                    print("Game over.")
                    self.state = Zustand.NoCredit
                else:
                    score = random.randint(1, 100)
                    self.credit += score
                    print(f"You scored {score} points. Credit: {self.credit}")
                    if self.credit >= 1000:
                        print("You win a free game!")
                        self.credit -= 1000
                hit_hole = random.choice(["Hole hit", "Hole not hit"])  # Zufällig wählen, ob das Loch getroffen wurde
                print(hit_hole)
            else:
                print("No balls left. Game over :( .")
        elif self.state == Zustand.NoCredit:
            print("No credit. Insert coin first.")
        else:
            print("Pressing start during the game shows credits.")

    def check_status(self):
        if self.balls <= 0:
            self.balls = 0
        print(f"State: {self.state}, Balls left: {self.balls}, Credit: {self.credit}, Selected Player: {self.selected_player}")

if __name__ == "__main__":
    flipper = FlipperAutomat()

    while True:
        if flipper.first_time:
            flipper.show_welcome_message()
            flipper.first_time = False
        print("\nGame Options:")
        print("1 - Insert coin")
        print("2 - Press start")
        print("3 - Play")
        print("4 - Check status")
        print("5 - Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            flipper.insert_coin()
        elif choice == "2":
            flipper.press_start()
        elif choice == "3":
            flipper.play()
        elif choice == "4":
            flipper.check_status()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
