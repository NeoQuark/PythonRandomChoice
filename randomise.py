import os, sys, random

list = []

def quit():
	print("\rBye! 👋")
	try:
		sys.exit(0)
	except SystemExit:
		os._exit(0)

def commands(command):
	if command == "/q":
		quit()
	elif command == "/help":
		print("\n----------\nYou may insert each element in the list whenever it is prompted to you and press \"Enter\" while leaving the input as blank so the program makes a choice in the list.\n\nHere are some examples of commands you can type :\n- /help		->	Display help\n- /print list	->	Print items of the list\n- /empty list	->	Makes the list empty\n- /q		->	Quit\n\n")
	elif command == "/print list":
		if len(list) == 0:
			print("\nYour list is empty\n")
		else:
			if len(list) == 1:
				print("\nYour list contains {} item :\n".format(len(list)))
			else:
				print("\nYour list contains {} items :\n".format(len(list)))
			for item in list:
				print("• {}".format(item))
	elif command == "/empty list":
		del list[:]
		print("\nThe list is now empty!\n")

def main():
	while True:
		item = input("\nType the name of the item to append to the list.\nSimply press \"Enter\" to end your list.\nType \"/help\" to display help.\n")
		if item != "":
			if item[0] == "/":
				commands(item)
			else:
				list.append(item)
		else:
			if len(list) < 2:
				print("\nSorry, the list doesn't containe enough items.\nType \"/help\" to display help.\n")
			else:
				print("\nThis is the chosen item : {}\n".format(random.choice(list)))
				break

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		quit()
