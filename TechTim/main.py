def get_weather(temp):
    if temp > 20:
        return "It's warm outside."
    elif temp > 10:
        return "It's a bit chilly outside."
    else:
        return "It's cold outside."
    
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b