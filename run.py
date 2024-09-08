def get_shopping_list():
    """
    Get items to buy input from the user.
    Run a while loop to collect a valid string of items from the user
    via the terminal, each beginning with prompt > . 
    The loop will repeatedly request data, until the user type DONE
    to terminate it and print shopping list.

    """

    #create a list to keep new items
    grocery_shopping_list = []

    #guide on how to use this simple shopping list app    
    print("Type what do I need to buy")
    print("Enter 'DONE' to stop adding items")

    while True:
            #enter new items
            new_item = input("> ")

            #list complete and end the app
            if new_item == 'DONE':
                break
            #add items to shopping list
            grocery_shopping_list.append(new_item)

    #introduce shopping list
    print("My grocery shopping list:")

    #print out items from final shopping list
    for item in grocery_shopping_list:
        print(item)

def main():
    """
    Run program function
    """
    get_shopping_list()
    
main()