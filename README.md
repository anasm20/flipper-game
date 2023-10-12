# flipper-game (Flipperautomaten mit Hilfe von Entwurfsmustern)

Überblick über einige wichtige Schritte die im Code umgesetzt würden:

1. Zustandsmuster (State Pattern): Implementieren Sie den Zustandsautomaten des Flipperautomaten unter Verwendung des Zustandsmusters.

2. Befehls- und Kompositmuster (Command and Composite Pattern): Erstellen Sie Flipper-Elemente wie Rampe, Target, Bumper usw., die das Command-Muster verwenden, um die Aktionen zu definieren, die beim Treffen eines Elements ausgeführt werden. Verwenden Sie das Kompositmuster, um komplexe Befehle (Makro-Befehle) zu erstellen.

3. Adaptermuster (Adapter Pattern): Binden Sie inkompatible Flipperelemente oder Befehle in den Flipper mit Hilfe des Adaptermusters ein.

4. Vermittlermuster (Mediator Pattern): Implementieren Sie einen Vermittler, um zu spezifizieren, wie die Flipper-Elemente miteinander interagieren. Zum Beispiel könnte sich eine Rampe öffnen, wenn alle Targets einer Gruppe getroffen wurden.

5. Besuchermuster (Visitor Pattern): Erstellen Sie Besucher, um durch die Liste der abstrakten Flipper-Elemente zu gehen und Funktionen der konkreten Flipper-Elemente aufzurufen. Implementieren Sie einen ResetVisitor und einen PunkteVisitor.

6. Abstrakte Fabrik (Abstract Factory): Verwenden Sie die Abstrakte Fabrik, um die Ausgabe auf dem Flipper in unterschiedlichen Formaten darzustellen, insbesondere beim Wechsel des Zustands des Automaten.

7. Singletonmuster (Singleton Pattern): Verwenden Sie das Singleton-Muster, wo immer es angebracht erscheint. Zum Beispiel könnte ein GameManager oder ein Highscore-Manager ein Singleton sein.

8. GUI mit tkinter: Die grafische Benutzeroberfläche kann mithilfe des tkinter-Frameworks erstellt werden. In Ihrer GUI können Sie Statusanzeigen, Tasten und Anzeigen für Kredit, Bälle usw. erstellen.


Das Spiel:
<img width="1704" alt="Screenshot 2023-10-12 at 14 23 33" src="https://github.com/anasm20/flipper-game/assets/112882511/08bc295c-1eda-4f17-9428-0be9021a0cb7">

GUI:

<img width="210" alt="Screenshot 2023-10-12 at 14 24 06" src="https://github.com/anasm20/flipper-game/assets/112882511/e42b84d0-844e-4716-9bab-774b500ac361">



