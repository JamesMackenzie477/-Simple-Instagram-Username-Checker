import requests

# prompts user for the list name
user_list = input("Please enter the name of the list: ")

# imports usernames as list
with open(user_list, "r") as f:
	usernames = f.read().split("\n")

# checks each username
for user in usernames:
	r = requests.get("https://www.instagram.com/" + user)
	if r.status_code == 404: # if page returns a 404 the username is available
		print("{} is available".format(user))
# stops program from quitting
input("")