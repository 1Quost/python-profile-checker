#project ass1:

#input name and check if it is empty

name=input("Enter your name: ")
while True:
    if name.strip() == "":
        name = input("Name cannot be empty. Please enter your name: ")
    else:
        break

#input age and check if it is negative
age=int(input("Enter your age: "))

while True:
    if age < 1:
        age = int(input("Age cannot be negative. Please enter a valid age: "))
    else:
        break

#input GPA and check if it is between 0 and 5
while True:
    gpa=float(input("Enter your GPA (0-5): "))
    if gpa>=0 and gpa<=5:
        break


#input field of interest and check if it is empty
field = input("Enter your field of interest: ")
while True:
    if field.strip() == "":
        field = input("Field of interest is required and cannot be empty. Please enter your field of interest: ")
    else:
        break


#input graduated and check if it is yes or no
while True:
    graduated=input("Have you graduated? (yes/no): ")
    if graduated.lower() in ["yes", "no"]:
        break
    else:
        print("Please enter 'yes' or 'no'.")

#Print detail info of the user
print("\n--- Profile  ---")
print("Name:", name)
print("Age:", age)
print("GPA:", gpa)
print("Field of Interest:", field)
print("Graduated:", graduated)

# Eligibility checks
#scholarship eligibility:
if age < 25 and gpa >= 3.5 and graduated == "yes":
    print("You are eligible for a scholarship.")
# internship eligibility:
if age < 30 and gpa >= 2.5:
    print("You are eligible for an internship.")
# If neither is eligible
if  not (age < 25 and gpa >= 3.5 and graduated == "yes") and not (age < 30 and gpa >= 2.5):
    print("You are not eligible for a scholarship or internship at this time. I recommend you to apply again later.")




