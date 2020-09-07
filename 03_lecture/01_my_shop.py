from store import Store
from category import Category
from data_for_store import cats

# my_store = Store('Bobs Emporium', [Category('False Legs'), Category('Baseball Bats'), Category('Fruit'), Category('Special product')])

my_store = Store('Bobs Emporium', [cats['legs'], cats['fruit'], cats['special'], cats['bats'] ]) # Instantiating the Store Class
print(my_store)
# print("Print with repr: " + repr(my_store))

selection = 0
while selection != len(my_store.categories) + 1:

    selection = input('Please select a number of the department: ')

    try:
        selection = int(selection)

        if selection == len(my_store.categories) + 1:
            print(f'Thank you for shoping at {my_store.name}!')
        elif selection > 0 and selection <= len(my_store.categories):
            print(my_store.categories[selection-1])
        else:
            print('please select a number!')      
    except ValueError:
        print('Please enter an integer!\n')

    print(f'The user selected {selection}')