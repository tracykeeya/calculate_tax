def calculate_tax(earnings):
    if earnings < 12000:
        return 0

def calculate_tax(earnings):
    if earnings < 12000:
        return 0
    elif 12000 <= earnings < 36000:
        return (earnings - 12000) * 0.20

def calculate_tax(earnings):
    if earnings < 12000:
        return 0
    elif 12000 <= earnings < 36000:
        return (earnings - 12000) * 0.20
    else:
        return (36000 - 12000) * 0.20 + (earnings - 36000) * 0.40
