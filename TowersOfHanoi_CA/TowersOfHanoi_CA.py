
###TOWERS OF HANOI###

from stackClass import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks

stack = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stack.append(left_stack)
stack.append(middle_stack)
stack.append(right_stack)


#Set up the Game

num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    int(input("Enter a number greater than or equal to 3\n"))

#populating stacks

for i in range(num_disks, 0, -1):
    left_stack.push(i)

#calculating optimal game time

optMoves = 2 ** num_disks - 1
print("\nThe fastest you can solve this game is in {0} moves".format(optMoves))



#Get User Input

def getInput():
    choices = [s.get_name()[0] for s in stack]
    while True:
        for i in range(len(stack)):
            name = stack[i].get_name()
            letter = choices[i]
            print("\nEnter {0} for {1}".format(letter,name))
        userInput = input("")
        if userInput in choices:
            for i in range(len(stack)):
                if userInput == choices[i]:
                    return stack[i]
        
#Play the Game

userMoves = 0
while(right_stack.get_size() != num_disks):
    print("\n\n\n...Current Stacks...")

    for s in stack:
        s.print_items()
    
    while True:
        print("\nWhich stack do you want to move from?\n")
        fromStack = getInput()
        print("\nWhich stack do you want to move to?\n")
        toStack = getInput()

        if fromStack.get_size() == 0:
            print("\n\nInvalid Move. Try Again")
        elif toStack.get_size() == 0 or fromStack.peek() < toStack.peek():
            disk = fromStack.pop()
            toStack.push(disk)
            userMoves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(userMoves,optMoves))








