FishType = input('What kind of Fish do you have? "Carnivorous", "Salt Water", or Community?": ')

if __name__ == '__main__':

	if FishType == "Carnivorous" or FishType == "Salt Water" or FishType == "Community": 
		pass
	
	else:
		print("I don't think that's a type of fish. Maybe you're looking for a lizard?")
	
	if FishType == "Carnivorous":
		Size = input('Do you have a smaller fish?(Yes/No): ')
		if Size == "No":
			print('Great! Enjoy!')
			
		if Size == "Yes":
			print("This is a bad idea! It'll eat your little ones!")
			

	if FishType == "Salt Water":
		print("Wow, you're a fancy fish parent!")

	if FishType == "Community":
		try:
			Amount = int(input("How many fish of that kind do you have?:"))
			if Amount < 3:
				print("You should get more then one!")
	
			if Amount >= 3:
				print("Yay more fish friends enjoy!")
		
		except  ValueError:
			print("Please give a number")