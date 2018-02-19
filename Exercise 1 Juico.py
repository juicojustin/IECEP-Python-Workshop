price = input("Please input how much is the price of the thing you want to buy: ")
money = input("Please input your money: ")
print "Your current money is:", money
print "With this money, you can afford", money/price, "of the thing you want to buy"
print "You will need to have", price-(money%price), "to get the thing you want to buy"

