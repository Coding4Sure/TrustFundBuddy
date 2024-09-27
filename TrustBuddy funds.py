# Trust Fund Buddy - Bad
# Demonstrates a logical error (the issue was a concatenation string and needs
#string text to convert into integer
print( """ Trust Fund Buddy Totals your monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).
Please enter the requested, monthly costs. Since you're rich, ignore
pennies and use only dollar amounts.""")

car = input("Lamborghini Tune-Ups: ")
car = int(car)
rent = int(input("Manhattan Apartment: "))
jet = int(input("Private Jet Rental: "))
gifts = input("Gifts: ")
gifts = int(gifts)
food = input("Dining Out: ")
food = int(food)
staff = input("Staff (butlers, chef, driver, assistant): ")
staff = int(staff)
guru = input("Personal Guru and Coach: ")
guru = int(guru)
games = input("Computer Games: ")
games = int(games)

total = car + rent + jet + gifts + food + staff + guru + games
print("\nGrand Total:", total)

input("\n\nPress the enter key to exit.")
