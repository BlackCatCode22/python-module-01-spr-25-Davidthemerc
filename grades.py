# Accept grade score as input
gradeScore = input("Enter score: ")

try:

    gradeScore = float(gradeScore)

    if gradeScore > 1:
        print("Score value too high. Please review.")
    elif gradeScore >= 0.9:
        print("A")
    elif gradeScore >= 0.8:
        print("B")
    elif gradeScore >= 0.7:
        print("C")
    elif gradeScore >= 0.6:
        print("D")
    elif gradeScore < 0.6:
        print("F")

except:
    print("Invalid score value. Please review.")
