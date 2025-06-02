def get_name():
    return input("Enter your name: ")

def get_age():
    return int(input("Enter your age: "))

def get_class():
    return input("Enter your class: ")

def get_grade():
    return input("Enter your grade: ")

def get_reputation():
    return input("Your reputation: ")

def get_favorite_subject():
    return input(" Favorite subject? ")

def likes_school():
    response = input("Do you like school? (yes or no): ")
    return response == "yes"

def display_student_info(name, age, class_level, grade, reputation, subject, likes):
    print("\n--- Student Profile ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Class: {class_level}")
    print(f"Grade: {grade}")
    print(f"Reputation: {reputation}")
    print(f"Favorite Subject: {subject}")
    print(f"Likes School:")

def main():
    name = get_name()
    age = get_age()
    class_level = get_class()
    grade = get_grade()
    reputation = get_reputation()
    subject = get_favorite_subject()
    likes = likes_school()

    display_student_info(name, age, class_level, grade, reputation, subject, likes)

if __name__ == "__main__":
    main()
