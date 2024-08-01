def calculate_slope(x1, y1, x2, y2):
    try:
        slope = (y2 - y1) / (x2 - x1)
    except ZeroDivisionError:
        return "Undefined (vertical line)"
    return slope

x1, y1 = 1, 2
x2, y2 = 3, 6
print(f"The slope is: {calculate_slope(x1, y1, x2, y2)}")
