import random

# Zustände des Flipperautomaten
class Zustand:
    NoCredit = 0
    Ready = 1
    Playing = 2
    EndState = 3

class FlipperAutomat:
    def __init__(self):
        self.credit = 0  # Der Kredit des Spielers
        self.balls = 3  # Die verbleibenden Bälle
        self.state = Zustand.NoCredit  # Anfangszustand ist "NoCredit"

    # Einwurf einer Münze
    def insert_coin(self):
        if self.state == Zustand.NoCredit:
            self.credit += 1
            self.state = Zustand.Ready  # Zustand wechselt in "Ready"
        else:
            print("You already have credit.")

    # Starten des Spiels
    def press_start(self):
        if self.state == Zustand.Ready:
            self.state = Zustand.Playing  # Zustand wechselt in "Playing"
        elif self.state == Zustand.NoCredit:
            print("No credit. Insert coin.")
        else:
            print("Game is already in progress.")

    # Spielen eines Balls
    def play(self):
        if self.state == Zustand.Playing:
            if self.balls > 0:
                self.balls -= 1
                if self.balls == 0:
                    print("Game over.")
                    self.state = Zustand.NoCredit
                else:
                    score = random.randint(1, 100)
                    self.credit += score
                    print(f"You scored {score} points. Credit: {self.credit}")
                    if self.credit >= 1000:
                        print("You win a free game!")
                        self.credit -= 1000
            else:
                print("No balls left. Game over.")
        elif self.state == Zustand.NoCredit:
            print("No credit. Insert coin first.")
        else:
            print("Pressing start during the game shows credits.")

    # Überprüfen des aktuellen Status
    def check_status(self):
        if self.balls < 0:
            self.balls = 0
        print(f"State: {self.state}, Balls left: {self.balls}, Credit: {self.credit}")

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
        elif choice == "4":
            flipper.check_status()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")