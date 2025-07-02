class SaveProvider:
    _instance = None  # Singleton

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._prev_view = []  # Initially no value
            #cls._instance.filter = MovingAverageFilter(num=25)  # Filtro con 25 valores
        return cls._instance

    def get_prev_view(self):
        """Returns the current previous view, if available."""
        prev_preview = self._prev_view[-1] if self._prev_view else None
        self._prev_view.pop()
        return prev_preview

    def set_prev_view(self, view):
        """Assigns the current previous view."""
        self._prev_view.append(view)

        