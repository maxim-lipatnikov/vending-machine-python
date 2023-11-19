
# Vending Machine

itemnumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
itemname = ["Snickers", "Mars", "Bounty", "Twix", "Coca-Cola 0.33l", "Fanta 0.33l", \
            "Aqua Minerale 0.5l", "Orange Juice 0.33l", "Cheetos", "Lay's"]
itemprice = [50, 45, 45, 50, 55, 55, 35, 33, 52, 76]
itemquantity = [3, 5, 6, 2, 1, 4, 4, 7, 2, 3]
banknotes = [50, 100, 200, 500]
banknotecount = [0, 0, 0, 0]
coincount = [400, 400, 400, 400]

print('### Welcome To Vending Machine ###')
print('Banknotes supported: 50p, 100p, 200p, 500p')


# Functions


def InsertBanknotes():
    print('Please insert the banknotes and type "1" when finished')
    totalmoney = 0
    count = 0
    money = 0
    while money != 1:
        money = int(input('Please insert the banknotes: '))
        if money in banknotes:
            count = banknotes.index(money)
            banknotecount[count] += 1
            totalmoney += money
        elif money == 1:
            break
        else:
            print('Banknote not supported')
    print('50p:', banknotecount[0], '100p:', banknotecount[1], '200p', banknotecount[2], '500p', \
          banknotecount[3])
    return totalmoney


def ListOfItems():
    for count in range(len(itemquantity)):
        if itemquantity[count] > 0:
            print('Item:', itemnumber[count], itemname[count], 'Price:', itemprice[count], \
                  'Available:', itemquantity[count])


def ListOfItemsToBeBought():
    for count in range(len(itemquantity)):
        if itemquantity[count] > 0:
            if totalmoney >= itemprice[count]:
                print('Item:', itemnumber[count], itemname[count], 'Price:', itemprice[count],
                      'Available:', itemquantity[count])
        else:
            break


def ChangeInCoins(totalmoney):
    ten = 0
    five = 0
    two = 0
    one = 0
    while totalmoney >= 10 and coincount[0] != 0:
        totalmoney -= 10
        ten += 1
        coincount[0] -= 1
    while totalmoney >= 5 and coincount[1] != 0:
        totalmoney -= 5
        five += 1
        coincount[1] -= 1
    while totalmoney >= 2 and coincount[2] != 0:
        totalmoney -= 2
        two += 1
        coincount[2] -= 1
    while totalmoney >= 1 and coincount[3] != 0:
        totalmoney -= 1
        one += 1
        coincount[3] -= 1
    print("# Your change is #")
    print("10's: ", ten, "Five's: ", five, "Two's: ", two, "One's: ", one)


# Inserting money


totalmoney = InsertBanknotes()
print('You inserted: ', totalmoney)

# Showing available items

print('# Items available #')
print(ListOfItems())

# Showing only the items a user can buy

print('# You can buy #')
print(ListOfItemsToBeBought())

# Selecting and buying an item, getting change

number = 0
count = 0
while totalmoney > 0:
    number = int(input('Enter the number of an item or type "11" to get change: '))
    if number in itemnumber:
        count = itemnumber.index(number)
        if itemquantity[count] > 0:
            if itemprice[count] <= totalmoney:
                itemquantity[count] -= 1
                totalmoney -= itemprice[count]
                print("Selected items left: ", itemquantity[count])
                print("Money left: ", totalmoney)
            else:
                a = int(input('Not enough money. Would you like to select another item (type any\
 number), add more money (type "1") or to get change(type "2")? '))
                if a == 1:
                    totalmoney += InsertBanknotes()
                elif a == 2:
                    ChangeInCoins(totalmoney)
                    break
        else:
            b = int(input('There are no selected items left. Select another item (press any button)\
 or type "11" to get change: '))
            if b == 11:
                ChangeInCoins(totalmoney)
                break
    else:
        ChangeInCoins(totalmoney)
        break
print('### Thank you for using Vending Machine! ###')

