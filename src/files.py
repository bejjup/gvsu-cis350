class File:
    def __init__(self):
        self._title = "Assets/Title_text.png"
        self._map = "Assets/Mappy .jpg"
        self._music = "Assets/01. Battle Royal (Guitar Theme).mp3"
        self._dice = "Assets/dice.png"
        self._roll_effect = "Assets/dice-142528.mp3"

    @property
    def title(self):
        return self._title
    @property
    def map(self):
        return self._map
    @property
    def music(self):
        return self._music
    @property
    def dice(self):
        return self._dice
    @property
    def roll_effect(self):
        return self._roll_effect


