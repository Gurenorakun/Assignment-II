def main():
    grades = []

    while True:
        grade = input("Enter a grade (-1 to stop): ")
        if grade == '-1':
            break
        grades.append(int(grade))

    average = int(sum(grades) / len(grades))

    print("Average:", average)

    for grade in grades:
        print(grade)


if __name__ == "__main__":
    main()
