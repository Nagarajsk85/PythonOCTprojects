import csv

def write_into_csv(info_list):
    with open('student.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact_Number", "E-Mail ID"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1

    while condition:
        student_info = input("Enter student information for student #{} in the following format (Name Age Contact_Number E-Mail_ID):".format(student_num))

        student_info_list = student_info.split(' ')

        if len(student_info_list) != 4:
            print("Invalid input. Please provide information in the correct format.")
        else:
            print("\nThe entered information is -\nName: {}\nAge: {}\nContact Number: {}\nE-mail ID: {}"
                  .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

            choice_check = input("Is the entered information correct? (yes/no): ")

            if choice_check == "yes":
                write_into_csv(student_info_list)

                condition_check = input("Enter (yes/no) if you want to enter information for another student: ")
                if condition_check == "yes":
                    condition = True
                    student_num += 1
                elif condition_check == "no":
                    condition = False
            elif choice_check == "no":
                print("\nPlease re-enter the values!")

