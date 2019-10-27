def convert_grade(letter):
    grades = {
        'a': 4.0,
        'b': 3.0,
        'c': 2.0,
        'd': 1.0,
        'f': 0.0
    }

    grade = letter.lower()
    if grade in grades:
        return grades[grade]
    else:
        raise KeyError(f'{letter} is invalid')


convert_grade('A')
convert_grade('B')
convert_grade('C')
convert_grade('D')
convert_grade('F')
convert_grade('G')
