from units import LENGTH, WEIGHT, normalize_unit

def convert_length(value: float, from_u: str, to_u: str) -> float:
    f = normalize_unit(from_u)
    t = normalize_unit(to_u)
    if f not in LENGTH or t not in LENGTH:
        raise ValueError(f"Ismeretlen hossz mértékegység: {from_u} vagy {to_u}")

    in_base = value * LENGTH[f]
    out_val = in_base / LENGTH[t]
    return out_val

def convert_weight(value: float, from_u: str, to_u: str) -> float:
    f = normalize_unit(from_u)
    t = normalize_unit(to_u)
    if f not in WEIGHT or t not in WEIGHT:
        raise ValueError(f"Ismeretlen hossz mértékegység: {from_u} vagy {to_u}")

    in_base = value * WEIGHT[f]
    out_val = in_base / WEIGHT[t]
    return out_val

def convert_temperature(value: float, from_u: str, to_u: str) -> float:
    f = normalize_unit(from_u)
    t = normalize_unit(to_u)

    if      f == "celsius":     c = value
    elif    f == "fahrenheit":  c = (value -32) * 5.0/9.0
    elif    f == "kelvin":      c = value - 273.15
    else:
        raise ValueError(f"Ismeretlen hőmérsékleti egység: {from_u}")

    if      t == "celsius":     return c
    elif    t == "fahrenheit":  return c * 5.0/9.0 + 32
    elif    t == "kelvin":      return c + 273.15
    else:
        raise ValueError(f"Ismeretlen hőmérsékleti egység: {to_u}")

def convert(kind: str, value: float, from_unit: str, to_unit: str) -> float:
    k = (kind or "").strip().lower()
    if k in ("length", "distance"):
        return convert_length(value, from_unit, to_unit)
    elif k in ("weight", "mass"):
        return convert_weight(value, from_unit, to_unit)
    elif k in ("temperature", "temp"):
        return convert_temperature(value, from_unit, to_unit)
    else:
        raise ValueError(f"Ismeretlen kategória: {kind}")