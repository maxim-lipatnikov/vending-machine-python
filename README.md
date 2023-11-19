# Vending Machine

This is one of the projects I did during my university studies in Python Programming.
The idea of the project was to implement a simplified logic of a vending machine.

The .py file in this repository.

## Instructions

### General requirements

- Use proper coding style, follow PEP-8 guidelines. Strict PEP-8 validation like the one in PyJudge won’t be performed, however, if the code becomes hard to read because of multiple PEP-8 violations, your grade can be lowered
- Use constants instead of “magic numbers”
- Use functions (and optionally modules) to modularize your program, don’t put all logic in the main program
- Protect against possible program crashes that come as a result of incorrect user actions, e.g. entering a non-valid number and others

### Description of tasks Vending machine capabilities

- The VM accepts the following banknotes: 50RUB, 100RUB, 200RUB and 500RUB. However, you have to design the program code in such a way that the list can be easily extended to other bill types.
- Change is given only in 10RUB, 5RUB, 2RUB and 1RUB coins listed in order of decreasing priority.
- The terminal is capable of physically storing up to 15 items of each product.
- The change dispensing module is capable of physically holding up to 400 coins of each denomination.

### Task

Start by creating an assortment of products for your vending machine. Hardcode it in a data structure in your program (the user does not need to enter this information!). 
In particular, the following information needs to be stored:

- Products: name, price (integer) and remaining quantity of each product
- Accepted cash: number of accepted banknotes of each denomination since the beginning of operation (or for the advanced task - since the last service operation)
- Number of remaining coins of each denomination used to give change

Your VM application should operate in an loop giving the user a choice of the following options on each iteration:

1. Insert a banknote
2. Show available products
3. Select a product
4. Get the change

When the user enters a banknote value, check that it is supported and increase the corresponding counter, give an error message otherwise.

In the second option (show available products) print information about all products that are currently present (quantity > 0).

In the third menu option provide a choice of only those products that are present and can be bought with the current credit. If the user makes a selection, print information about the product and decrease its quantity.

When the “Get change” option is selected, dispense the change using 10,5,2 and 1 RUB coins (print the distribution of coins on the screen). 10RUB coins have the highest priority, followed by 5 RUB, then 2RUB and finally 1RUB.
