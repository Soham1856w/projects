students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Topper")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))

        student = {
            "name": name,
            "marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No students found.")
        else:
            print("\n--- Student List ---")
            for s in students:
                print(f"Name: {s['name']} | Marks: {s['marks']}")

    elif choice == 3:
        search = input("Enter name to search: ")

        found = False
        for s in students:
            if s["name"].lower() == search.lower():
                print(f"Student Found -> Name: {s['name']} | Marks: {s['marks']}")
                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == 4:
        if len(students) == 0:
            print("No students available.")
        else:
            topper = students[0]

            for s in students:
                if s["marks"] > topper["marks"]:
                    topper = s

            print(f"Topper is {topper['name']} with {topper['marks']} marks.")

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")