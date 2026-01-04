def main():
    print(f"{"-"*20}HEALTH MANAGEMENT SYSTEM{"-"*20}")

    operation={
        1: store_data, 
        2: retr_data
    }
    
    print("1.Store the data\n2.Retrieve the data")
    choice=int(input("Enter your choice: "))
    
    if choice in operation:
        operation[choice]()
    else:
        print("Invalid Input")