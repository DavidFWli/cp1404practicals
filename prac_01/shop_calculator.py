MENU = """
    A - Check total price
    Q - Quit
"""



while True:
    print(MENU)
    choice = input(">>> ").upper()
    if choice == "A":
        total_price=0
        items = int(input("Number of items: "))
        for i in range(0,items):
            price = float(input("Price of item: "))
            total_price = total_price + price
        if total_price >=100:
            total_price = total_price*0.9              
        print(f"Total price for {items} items is ${total_price:.2f}")
    elif choice =="Q":
        print("Thank you.")
        break
    else:
        print("Invalid option")
