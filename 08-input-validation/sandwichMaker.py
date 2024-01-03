#! python3
# sandwichMaker.py - Sandwich Maker project that uses pyinputplus module.

import pyinputplus as pyip

prices = {
        'wheat': 4,
        'white': 3,
        'sourdough': 5,
        'chicken': 10,
        'turkey': 12,
        'ham': 8,
        'tofu': 7,
        'cheddar': 6,
        'Swiss': 6.5,
        'mozzarella': 5.5,
        'mayo': 1.5,
        'mustard': 1.8,
        'lettuce': 2,
        'tomato': 2.5
    }

sandwichCost = 0

# Ask for break type:
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
sandwichCost += prices[bread]

# Ask for protein type:
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
sandwichCost += prices[protein]

# Ask if they want cheese:
if 'yes' == pyip.inputYesNo('Do you want cheese?'):
    # Ask for cheese type:
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
    sandwichCost += prices[cheese]

# Ask if they want mayo, mustard, lettuce or tomato:
if 'yes' == pyip.inputYesNo('Do you want mayo?'):
    sandwichCost += prices['mayo']
if 'yes' == pyip.inputYesNo('Do you want mustard?'):
    sandwichCost += prices['mustard']
if 'yes' == pyip.inputYesNo('Do you want lettuce?'):
    sandwichCost += prices['lettuce']
if 'yes' == pyip.inputYesNo('Do you want tomato?'):
    sandwichCost += prices['tomato']

# Ask how many sandwiches:
sandwiches = pyip.inputInt('How many sandwiches do you want?', min=1)
sandwichCost *= sandwiches

# Display total cost:
print(f'Total cost for your selections is: {sandwichCost}')
