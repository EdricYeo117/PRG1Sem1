friends = ["Izzat", "Bryan", "Dalton", "Ethan", "Isaac"]
new_friend = str(input("Enter the name of the new friend: "))
friends.append(new_friend)
print(friends)

delete_friend = str(input("Enter the name of friend to delete: "))
delete_friend in friends 
index = friends.index(delete_friend)
print(str("{} is at index {} in the friendslist".format(delete_friend, index)))
friends.pop(index)
print(friends)
