# Fantasy Game Inventory

from typing import List

def displayInventory(inventory: dict) -> None:
    '''
    Prints the contents of the dictionary <inventory>.
    '''
    print('Inventory:')
    totalItems = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        totalItems += int(v)
    print(f'Total number of items: {totalItems}')

def addToInventory(inventory: dict, addedItems: List[str]) -> None:
    '''
    <inventory> is a dictionary with key=item name and value=how many items.
    <addedItems> is a list of items.
    The function updates the <inventory> item values based on the items added.
    '''
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

# Now let's test it
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print('Initial inventory')
displayInventory(stuff)
print()

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(stuff, dragonLoot)
print('After dragon loot')
displayInventory(stuff)
