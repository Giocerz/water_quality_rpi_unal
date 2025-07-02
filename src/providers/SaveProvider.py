class SaveProvider:
    _instance = None  # Singleton

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(cls).__new__(cls)
            cls._instance._prev_view = None  # Inicialmente sin valor
            #cls._instance.filter = MovingAverageFilter(num=25)  # Filtro con 25 valores
        return cls._instance

    def get_prev_view(self):
        """Devuelve la vista previa actual, si está disponible."""
        return self._prev_view

    def set_prev_view(self, view):
        """Asigna la vista previa actual."""
        self._prev_view = view

        