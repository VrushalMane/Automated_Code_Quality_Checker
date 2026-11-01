
def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid Marks"

    elif marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 60:
        return "C"    

    elif marks >= 40:
        return "D"

    else:
        return "F"


if __name__ == "__main__":
    print(calculate_grade(85))
    print(calculate_grade(30))
    print(calculate_grade(120))
    print(calculate_grade(65))
