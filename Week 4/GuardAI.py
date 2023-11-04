
#Yeo Jin Rong, S10258457C, guard AI 
#input

sees_player = input("Does the guard see the player (y/n): ")


#process

if sees_player == "n":
 print("The guard waits")

elif sees_player == "y":
 dist_from_player = int(input("How far away is the player?: "))

if dist_from_player <=1:
    print("The guard attacks!")
elif dist_from_player >=2 and dist_from_player <= 4:
    print("The guard advances.")
elif dist_from_player >= 5:
    print("The guard waits.")
