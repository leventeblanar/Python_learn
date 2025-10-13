from unit_convert import UnitConvert

LENGTH = {
    "millimeter": 0.001,   # m
    "centimeter": 0.01,    # m
    "meter": 1.0,          # m
    "kilometer": 1000.0,   # m
    "inch": 0.0254,        # m
    "foot": 0.3048,        # m
    "yard": 0.9144,        # m
    "mile": 1609.34,       # m
}

WEIGHT = {
    "milligram": 1e-6,     # kg
    "gram": 1e-3,          # kg
    "kilogram": 1.0,       # kg
    "ounce": 0.028349523125,  # kg
    "pound": 0.45359237,      # kg
}

ALIASES = {
    # length
    "mm": "millimeter", "millimeter": "millimeter",
    "cm": "centimeter", "centimeter": "centimeter",
    "m": "meter", "meter": "meter",
    "km": "kilometer", "kilometer": "kilometer",
    "in": "inch", "inch": "inch",
    "ft": "foot", "foot": "foot",
    "yd": "yard", "yard": "yard",
    "mi": "mile", "mile": "mile",
    # weight
    "mg": "milligram", "milligram": "milligram",
    "g": "gram", "gram": "gram",
    "kg": "kilogram", "kilogram": "kilogram",
    "oz": "ounce", "ounce": "ounce",
    "lb": "pound", "lbs": "pound", "pound": "pound",
    # temperature
    "c": "celsius", "°c": "celsius", "celsius": "celsius",
    "f": "fahrenheit", "°f": "fahrenheit", "fahrenheit": "fahrenheit",
    "k": "kelvin", "kelvin": "kelvin",
}

def normalize_unit(u: str) -> str:
    key = (u or "").strip().lower()
    if key in ALIASES:
        return ALIASES[key]
    return key