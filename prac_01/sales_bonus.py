"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""

print("Please start to count your sales bonus")
again_or_not = 0
while again_or_not >=0 :
    sales = float(input("Enter sales: $"))
    sales_bonus_rate=0
    if sales < 1000:
        sales_bonus =  0.10
    elif sales >= 1000:
        sales_bonus_rate =  0.15
    sales_bonus = sales_bonus_rate * sales
    print(f"Result: The bonus is {sales_bonus}.")
    print("Do you want continue? If you want continue press 0, if not press -1")
    again_or_not = float(input())
print("Thank you.")
