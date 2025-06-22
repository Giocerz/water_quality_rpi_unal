class AppConstants:
    SOFTWARE_VERSION = '1.0.3'

    PARAMS_ATTRIBUTES = {
    "conductivity": {
        "name": "Conductividad Eléctrica",
        "maxValue": 2000.0,
        "minValue": 0.0,
        "lowerLimit": None,
        "upperLimit": 1000.0,
        "unit": "µS/cm",
        "significant_figures": 0
    },
    "oxygen": {
        "name": "Oxigeno Disuelto",
        "maxValue": 10.0,
        "minValue": 0.0,
        "lowerLimit": None,
        "upperLimit": None,
        "stableTolerance": 0.1,
        "unit": ["mg/L", "%"],
        "significant_figures": 2
    },
    "ph": {
        "name": "pH",
        "maxValue": 14.0,
        "minValue": 0.0,
        "lowerLimit": 6.5,
        "upperLimit": 8.5,
        "stableTolerance": 0.1,
        "unit": "pH",
        "significant_figures": 2
    },
    "tds": {
        "name": "Sólidos Totales Disueltos",
        "maxValue": 1000.0,
        "minValue": 0.0,
        "lowerLimit": None,
        "upperLimit": 500.0,
        "stableTolerance": 2.0,
        "unit": "ppm",
        "significant_figures": 0
    },
    "temperature": {
        "name": "Temperatura",
        "maxValue": 40.0,
        "minValue": 0.0,
        "lowerLimit": None,
        "upperLimit": 30.0,
        "unit": ["°C", "°F", "K"],
        "significant_figures": 1
    },
    "turbidity": {
        "name": "Turbidez",
        "maxValue": 3000.0,
        "minValue": 0.0,
        "lowerLimit": None,
        "upperLimit": 42.0,
        "unit": "NTU",
        "significant_figures": 0
    },
    }

    MONITORING_STABLE_TDS = {
        'window': 6,
        'threshold': 10.0,
        'repeat': 3,
    }
    
    MONITORING_STABLE_PH = {
        'window': 6,
        'threshold': 0.01,
        'repeat': 2,
    }
    
    MONITORING_STABLE_DO = {
        'window': 6,
        'threshold': 0.1,
        'repeat': 3,
    }
    
    MONITORING_STABLE_TURBIDITY = {
        'window': 6,
        'threshold': 30.0,
        'repeat': 3,
    }

    MEASURE_OFF_VALUE = -14563.0

    WATER_SOURCES = [
    'Acuífero',
    'Arroyo',
    'Depósito de agua',
    'Embalse',
    'Estanque',
    'Fuente',
    'Llave',
    'Lago',
    'Lluvia recolectada',
    'Manantial',
    'Planta de tratamiento de agua',
    'Pozo',
    'Río',
    'Tanque de almacenamiento',
    'Torre de agua',
    'Otro'
  ]

