def calculate_progress(current, goal):
    if goal == 0:
        return 0
    return min(100, (goal - current) / goal * 100)
