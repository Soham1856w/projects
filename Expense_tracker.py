expenses=[]
while True:
    print("========== Welcome to expense tracker..==========")
    print("1. Add expense")
    print("2. show expense")
    print("3. Total expense")
    print("4. Category summary")
    print("5. exit....")

    choice=int(input("Enter your choice"))
    if choice==1:
        name=input("Enter item name:")
        amount=float(input("Enter amount :"))
        category=input("Enter category:")

        expense={"Name":name,
                 "Amount":amount,
                 "Category":category}
        expenses.append(expense)
    

    elif choice ==2:
        if len(expenses)==0:
            print("There is no expenses..")
        else:
            print("expense list..")
            for e in expenses:
                print(f"{e['name']} | {e['amount']} | {e['category']}")
    
    elif choice == 3:
        total=0
        for e in expenses:
            total=total + e['amount']
    
    
    elif choice == 4:
        if len(expenses)==0:
            print("no expenses found")
        else:
            summry={}
            for e in expenses:
                cat= e["category"]
                if cat in summry:
                    summry[cat]=summry[cat] + e["amount"]
                else:
                    summry[cat]=e["amount"]
            print("category summary")
            for key,value in summry.items():
                print(f"{key} : {value}")
    
    
    elif choice ==5 :
        print("Exting program....")
        break

    else:
        print("invalid choice")