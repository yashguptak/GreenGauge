import random

TIPS = [
    "Switch to LED bulbs to cut electricity use.",
    "Use public transport to lower emissions.",
    "Reduce meat meals for a smaller carbon footprint.",
    "Turn off chargers when not in use.",
    "Walk or cycle for short trips instead of driving.",
    "Plant a tree to absorb CO2.",
    "Use a reusable water bottle instead of single-use plastic.",
    "Compost food scraps to reduce landfill waste.",
    "Take shorter showers to save water and energy.",
    "Unplug electronics when not in use to save energy."
]

def random_tip():
    return random.choice(TIPS)
