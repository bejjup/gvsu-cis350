class File:
    def __init__(self):
        self._title = "Assets/Title_text.png"
        self._map = "Assets/Mappy  (1).jpg"
        self._music = "Assets/01. Battle Royal (Guitar Theme).mp3"
        self._dice = "Assets/dice.png"
        self._roll_effect = "Assets/dice-142528.mp3"
        self._start = "Assets/start_button.jpg"
        self._nog_ops = "Assets/nog_ops.jpg"
        self._jonesy = "Assets/jonesy.jpg"
        self._raven = "Assets/Raven.jpg"
        self._john_wick = "Assets/John_wick.jpg"
        self._materials = "Assets/Materials.png"

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
    @property
    def start(self):
        return self._start
    @property
    def nog_ops(self):
        return self._nog_ops
    @property
    def jonesy(self):
        return self._jonesy
    @property
    def raven(self):
        return self._raven
    @property
    def john_wick(self):
        return self._john_wick
    @property
    def materials(self):
        return self._materials


