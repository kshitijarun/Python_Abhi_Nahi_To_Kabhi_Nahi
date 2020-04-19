# Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z

firstName=input("Enter your first name: ")
if(firstName[0]=='A' or firstName[0]=='B'):
    print("Go to room AB")
elif(firstName[0]=='C'):
    print("Go to room CD")
else:
    lastName=input("Enter your last name: ")
    if(lastName[0]=='Z'):
        print("Go to room Z")
    else:
        print("Go to room OTHER")
