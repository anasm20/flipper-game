import random
import pyfiglet

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
    def __init__(self, spieler):
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

# Abstrakte Fabrik für die Erzeugung von ASCII-Art-Text
class ASCIIArtFactory:
    def create_art(self, text):
        pass

# Konkrete Fabrik für Flipper
class FlipperASCIIArtFactory(ASCIIArtFactory):
    def create_art(self, text):
        ascii_art = pyfiglet.Figlet(font='bigmoney-ne').renderText(text)
        return ascii_art

# Flipperautomat mit ASCII-Art-Text
class FlipperAutomat:
    def __init__(self):
        self.credit = 0
        self.balls = 3
        self.state = Zustand.NoCredit
        self.selected_player = 1
        self.ascii_art_factory = FlipperASCIIArtFactory()

    def insert_coin(self):
        if self.state == Zustand.NoCredit:
            self.credit += 1
            self.state = Zustand.Ready
        else:
            print("You already have credit.")

    def press_start(self):
        if self.state == Zustand.Ready:
            self.state = Zustand.Playing
            self.show_playing_ascii_art()
        elif self.state == Zustand.NoCredit:
            print("No credit. Insert coin.")
        else:
            print("Game is already in progress.")

    def show_playing_ascii_art(self):
        if self.state == Zustand.Playing:
            ball_type = random.choice(["#", " "])  # Beispielhaft: Zufällig ein Balltyp
            ascii_art = self.ascii_art_factory.create_art(ball_type)
            print(ascii_art)

    # Rest des Codes bleibt unverändert

if __name__ == "__main__":
    flipper = FlipperAutomat()
    
    while True:
        print("\nOptions:")
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
            element = Hole("Sample Hole")
            commands = element.hit()
            for command in commands:
                command.execute(flipper)
        elif choice == "4":
            flipper.check_status()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
