import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
	
	word = word.lower()
	
	if word in data:
		return data[word]
	
	elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
		yes_no = input("Did you mean %s instead? Enter Y if yes, or N if no. " % get_close_matches(word, data.keys())[0])
		
		if yes_no == "Y" or yes_no == "y":
			return data[get_close_matches(word, data.keys())[0]]
		
		elif yes_no == "N" or yes_no == "n":
			return "The word doesn't exist. Please try another word."
		
		else:
			return "Didn't receive correct response. Please try again."
	
	else:
		return "The word doesn't exist. Please try another word."


word = input("Enter word: ")
output = translate(word)

if type(output) == list:
	for index, item in enumerate(output, start=1):
		print(str(index) + ". " + item)
else:
	print(output)
