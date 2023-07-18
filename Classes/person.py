class Person:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.shopping_list = []
    
    
    
    def get_person_name(person):
        return person["name"]

    def add_item_to_the_shopping_list(self,thing):
        self.shopping_list.append(thing)

    def remove_item_from_the_shopping_list(self,thing):
        self.shopping_list.remove(thing)

   
