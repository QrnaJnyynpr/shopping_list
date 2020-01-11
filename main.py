help_text = """
======================================================================
                            SHOPPING LIST
- To view shopping list, type 'view'
- To add an item, type 'add' followed by the item name
- To remove an item, type 'remove' followed by the item name
======================================================================"""

print(help_text)

shopping = eval(open("shoppinglist.txt").read())
while True:
	def write():
		with open('shoppinglist.txt', 'w') as f:
			print(shopping, file=f)

	def add(query):
		element = query[4:]
		shopping.append(element)
		print(f"\n- {element} added")
		write()

	def remove(query):
		element = query[7:]
		if element in shopping:
			shopping.remove(element)
			print(f"\n- {element} removed")
		else:
			print("Item not found!")
		write()

	def view():
		if shopping == []:
			print("\nShopping list is empty!\nType 'add' followed by the item description to add some items.")
		else:
			print("\n==========================\nShopping List\n==========================")
			for i in shopping:
				print(f"- {i}")
			print("==========================")

	query = input("\nEnter command:\n")
	if "add " in query:
		add(query)
	elif "remove " in query:
		remove(query)
	elif "view" in query:
		view()
	else:
		print("Please enter a valid command!")