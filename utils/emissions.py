def calculate_footprint(transport_km, electricity_kwh, fuel_litre):
    transport_factor = 0.12    # CO₂ per km
    electricity_factor = 0.45  # CO₂ per kWh
    fuel_factor = 2.31         # CO₂ per litre
    
    total = (
        transport_km * transport_factor +
        electricity_kwh * electricity_factor +
        fuel_litre * fuel_factor
    )
    return total


def lifestyle_footprint(transport, diet, energy, shopping):
    factors = {
        "transport": {"Car": 2.0, "Bus": 1.2, "Bike": 1.0, "Cycle/Walk": 0.1},
        "diet":      {"Meat-heavy": 3.0, "Mixed": 2.0, "Vegetarian": 1.5, "Vegan": 1.0},
        "energy":    {"Coal": 3.0, "Electric": 2.0, "Renewable": 0.5},
        "shopping":  {"Frequent": 2.0, "Moderate": 1.0, "Minimal": 0.5},
    }

    total = (
        factors["transport"][transport] +
        factors["diet"][diet] +
        factors["energy"][energy] +
        factors["shopping"][shopping]
    )
    return total
