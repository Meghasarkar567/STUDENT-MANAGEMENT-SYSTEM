def save_data():
    with open("students.json", "w") as file:
        json.dump(student, file, indent=4)
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"
import json
import os
import csv

if os.path.exists("students.json"):

    with open("students.json","r") as file:

        student = json.load(file)

else:

    student = {}


while True:
    print("\n-----STUDENT MANAGEMENT SYSTEM-----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Check Result")
    print("7. Show Ranking")
    print("8. Show Topper")
    print("9. Show Statistics")
    print("10. Export Student Report")
    print("11. Exit")

    choice = input("Enter your choice: ")
    
    # add student
    if choice == "1":
        name = input("Enter student name:")
        if name in student:
            print("Student already exists!")
            continue
        age = int(input("Enter Age: "))
        if age <= 0:
            print("Invalid Age!")
            continue
        course = input("Enter Course: ")
        marks = int(input("Enter Marks: "))
        if marks < 0 or marks > 100:
            print("Invalid Marks!")
            continue
        student[name] = {
            "Age" : age,
            "Course" : course,
            "Marks" : marks
        }
        print(f"{name} Successfully Added!")

   # view student
    elif choice == "2":
        if not student:
            print("No student found!")
        else:
            for name, details in student.items():
                print("------------------------")
                print("Name :", name)
                print("Age :", details["Age"])
                print("Course :", details["Course"])
                print("Marks :", details["Marks"])
                print("Grade :", calculate_grade(details["Marks"]))


    # Scarch student
    elif choice == "3":

        name = input("Enter Student Name: ")
        if name in student:

            details = student[name]

            print("------------------------")
            print("Name :", name)
            print("Age :", details["Age"])
            print("Course :", details["Course"])
            print("Marks :", details["Marks"])
            print("Grade :", calculate_grade(details["Marks"]))
            print("---------------------------")
        else:
            print("Student Not Found")


    #update student
    elif choice == "4":
        name = input("Enter Student Name: ")

        if name in student:

            age = int(input("New Age: "))
            course = input("New Course: ")
            marks = int(input("New Marks: "))
            if marks < 0 or marks > 100:
                print("Invalid Marks!")
                continue

            student[name]["Age"] = age
            student[name]["Course"] = course
            student[name]["Marks"] = marks

            print("Updated Successfully")

        else:

            print("Student Not Found")
   

    # delete students
    elif choice == "5":
        name = input("Enter Student Name: ")
        confirm = input("Are you sure? (Y/N): ").upper()
        if name in student:
            del student[name]
            print("Deleted Succesfully")

        else:

            print("Student Not Found")


   # check result
    elif choice == "6":
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]["Marks"]

            grade = calculate_grade(marks)

            print("--------------------")
            print("Marks :", marks)
            print("Grade :", grade)

            if marks >= 40:
                print("Status : PASS")
            else:
                print("Status : FAIL")

        else:
            print("Student Not Found!")


    # show ranking
    elif choice == "7":
        ranking = sorted(
            student.items(),
            key=lambda x: x[1]["Marks"],
            reverse=True
        )
        
        rank = 1
        for name, details in ranking:
            print(
                rank,
                ".",
                name,
                "| Marks:",
                details["Marks"],
                "| Grade:",
                calculate_grade(details["Marks"])
            )

            rank += 1


    #show topper
    elif choice == "8":
        topper = max(student.items(), key=lambda x: x[1]["Marks"])
        print("\n------ TOPPER ------")
        print("Topper :", topper[0])
        print("Course :", topper[1]["Course"])
        print("Marks :", topper[1]["Marks"])
        print("Grade :", calculate_grade(topper[1]["Marks"]))


    # Show statistics
    elif choice == "9":

        if not student:
            print("No Student Found!")

        else:

            marks = []

            passed = 0

            for details in student.values():

                marks.append(details["Marks"])

                if details["Marks"] >= 40:
                    passed += 1

            failed = len(student) - passed

            print("\n------ CLASS STATISTICS ------")
            print("Total Students :", len(student))
            print("Highest Marks :", max(marks))
            print("Lowest Marks :", min(marks))
            print("Average Marks :", round(sum(marks)/len(marks),2))
            print("Passed :", passed)
            print("Failed :", failed)


    # export student report
    elif choice == "10":

        with open("students_report.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["Name", "Age", "Course", "Marks", "Grade"])

            for name, details in student.items():

                writer.writerow([
                    name,
                    details["Age"],
                    details["Course"],
                    details["Marks"],
                    calculate_grade(details["Marks"])
                ])

        print("Student report exported successfully!")


   
    # exit
    elif choice == "11":
        print("Exiting.....")
        with open("students.json","w") as file:

            json.dump(student,file,indent=4)
        break

    else:
        print("In-valid input")