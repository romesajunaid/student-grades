student = {"romesa": 85, "asim": 90, "umaima": 76}

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

for name, score in student.items():
    print(f"{name} {score} {grade(score)}")