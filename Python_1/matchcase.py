#Program for match case
#matchcase.py
wkn=input("Enter Week Name:")
match(wkn):
	case "monday":
		print("{} is Working Day".format(wkn))
	case "tuesday":
		print("{} is Working Day".format(wkn))
	case "wednesday":
		print("{} is Working Day".format(wkn))
	case "thursday":
		print("{} is Working Day".format(wkn))
	case "friday":
		print("{} is Working Day".format(wkn))
	case "saturday":
		print("{} is Week End".format(wkn))
	case "sunday":
		print("{} is HoliDay".format(wkn))
	case _:
		print("{} is not a week day:".format(wkn))