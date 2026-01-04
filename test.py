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




def retr_data():
    import os
    print(f"{"-"*10}Profiles{"-"*10}")
    print("1.Ajeet\n2.Rahul\n3.Akash\n4.Rudra\n5.Rakesh")
    user=input("Choose Name from above names: ")
    if user in files:
        print(f"{"-"*10}Categories{"-"*10}")
        print("1.Food\n2.Exercise")
        categories=int(input("Enter the categories: "))

        file_name=files[user][categories]

        if os.path.exists(file_name):
            with open(file_name, "r") as r:
                print(f"{"-"*10}Stored Data{"-"*10}")
                print(r.read())
        else:
            print(f"You have nothing in '{file_name}' to show")
    else:
        print("Profile not found! Please Enter an existing Profile Name")

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