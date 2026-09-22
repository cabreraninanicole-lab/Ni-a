def calculate_average(a1, a2, a3):
    return (a1 + a2 + a3) / 3


def get_status(average):
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "Very Good"
    elif average >= 75:
        return "Passed"
    else:
        return "Failed"


def main():
    
    while True:
        num_students = int(input("How many students? "))
        if num_students >= 3:
            break
        print("Please enter at least 3 students.\n")
    
    print() 
    
    
    for i in range(1, num_students + 1):
        print(f"Student {i}")
        name = input("Enter name: ")
        act1 = int(input("Activity 1: "))
        act2 = int(input("Activity 2: "))
        act3 = int(input("Activity 3: "))
        
        average = calculate_average(act1, act2, act3)
        status = get_status(average)
        
        print(f"\nAverage: {average:.2f}")
        print(f"Status: {status}")
        print()  


if __name__ == "__main__":
    main()