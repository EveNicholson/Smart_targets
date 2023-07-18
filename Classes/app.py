from person import Person


client = Person("Ewelina", 500)
print(client.name)

list = ["bread", "milk", "coffe"]
print(client.shopping_list)


client.add_item_to_the_shopping_list("water")
print(client.shopping_list)
client.remove_item_from_the_shopping_list("water")
print(client.shopping_list)

client.add_item_to_the_shopping_list(list)
for item in list:
    print(item)

print(client.shopping_list)