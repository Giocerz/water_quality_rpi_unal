class SaveProvider:
    _instance = None  # Singleton

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._prev_view = []  # Initially no value
            cls._instance._oxygen_list = []
            cls._instance._ph_list = []
            cls._instance._temperature_list = []
            cls._instance._tds_list = []
            cls._instance._conductivity_list = []
            cls._instance._turbidity_list = []
            cls._instance._battery_list = []
            cls._instance._timestamp_list = []

            cls._instance._sample_name = None
            cls._instance._it_rained = None
            cls._instance._origin = None
            cls._instance._location = {
                'latitude': None,
                'longitude': None,
            }
        return cls._instance

    def get_prev_view(self):
        """Returns the current previous view, if available."""
        prev_preview = self._prev_view[-1] if self._prev_view else None
        self._prev_view.pop()
        return prev_preview

    def set_prev_view(self, view):
        """Assigns the current previous view."""
        self._prev_view.append(view)
    
    def add_oxygen(self, value):
        """Adds a value to the oxygen list."""
        self._oxygen_list.append(value)
    
    def add_ph(self, value):
        """Adds a value to the pH list."""
        self._ph_list.append(value)
    
    def add_temperature(self, value):
        """Adds a value to the temperature list."""
        self._temperature_list.append(value)
    
    def add_tds(self, value):
        """Adds a value to the TDS list."""
        self._tds_list.append(value)
    
    def add_conductivity(self, value):
        """Adds a value to the conductivity list."""
        self._conductivity_list.append(value)
    
    def add_turbidity(self, value):
        """Adds a value to the turbidity list."""
        self._turbidity_list.append(value)
    
    def add_battery(self, value):
        """Adds a value to the battery list."""
        self._battery_list.append(value)
    
    def add_timestamp(self, value):
        """Adds a value to the timestamp list."""
        self._timestamp_list.append(value)
    
    def get_parameters_lists(self):
        """Returns the lists of parameters."""
        return {
            'oxygen_list': self._oxygen_list,
            'ph_list': self._ph_list,
            'temperature_list': self._temperature_list,
            'tds_list': self._tds_list,
            'conductivity_list': self._conductivity_list,
            'turbidity_list': self._turbidity_list,
            'battery_list': self._battery_list,
            'timestamp_list': self._timestamp_list
        }

    def set_sample_name(self, sample_name):
        """Sets the sample name."""
        self._sample_name = sample_name
    
    def get_sample_name(self):
        """Returns the sample name."""
        return self._sample_name
    
    def set_it_rained(self, it_rained):
        """Sets whether it rained."""
        self._it_rained = it_rained

    def get_it_rained(self):
        """Returns whether it rained."""
        return self._it_rained

    def set_origin(self, origin):
        """Sets the origin."""
        self._origin = origin
    
    def get_origin(self):
        """Returns the origin."""
        return self._origin
    
    def set_location(self, latitude, longitude):
        """Sets the location."""
        self._location['latitude'] = latitude
        self._location['longitude'] = longitude
    
    def get_location(self):
        """Returns the location."""
        return self._location
    
    def clear_only_form_data(self):
        """Clears only the form data, keeping the lists intact."""
        self._prev_view.clear()
        self._sample_name = None
        self._it_rained = None
        self._origin = None
        self._location = {
            'latitude': None,
            'longitude': None,
        }

    def clear(self):
        """Clears all saved data."""
        self._prev_view.clear()
        self._oxygen_list.clear()
        self._ph_list.clear()
        self._temperature_list.clear()
        self._tds_list.clear()
        self._conductivity_list.clear()
        self._turbidity_list.clear()
        self._battery_list.clear()
        self._timestamp_list.clear()

        self._sample_name = None
        self._it_rained = None
        self._origin = None
        self._location = {
            'latitude': None,
            'longitude': None,
        }
        