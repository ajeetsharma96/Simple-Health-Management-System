def getdate():
    import datetime
    return datetime.datetime.now()

files={
    "Ajeet":{1:"ajeet_food.txt",2:"ajeet_exercise.txt"},
    "Rahul":{1:"Rahul_food.txt",2:"Rahul_exercise.txt"},
    "Akash":{1:"akash_food.txt",2:"akash_exercise.txt"},
    "Rudra":{1:"rudra_food.txt",2:"rudra_exercise.txt"},
    "Rakesh":{1:"rakesh_food.txt",2:"rakesh_exercise.txt"}
}






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

main()