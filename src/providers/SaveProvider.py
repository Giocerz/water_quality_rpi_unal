class SaveProvider:
    _instance = None  # Singleton

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._prev_view = None  # Initially no value
            #cls._instance.filter = MovingAverageFilter(num=25)  # Filtro con 25 valores
        return cls._instance

    def get_prev_view(self):
        """Returns the current preview view, if available."""
        return self._prev_view

    def set_prev_view(self, view):
        """Assigns the current preview view."""
        self._prev_view = view

        