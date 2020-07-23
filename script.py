from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Creating the Stacks
stacks = []

left_stack = Stack("Left")
middle_stack = Stack('Middle')
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

# this number will push on to the left_stack
#this starts at num_disk and goes down by 1 to o
for disk in range(num_disks, 0, -1):
  left_stack.push(disk)

# this will let the user the mimium amount of moves in order to win
num_optimal_move = (2 ** num_disks) -1
print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_move))

#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]

  while True:
     for i in range(len(stacks)):
       name = stacks[i].get_name()
       letter = choices[i]
       print("Enter {0} for {1}".format(letter, name))
    #once options display use will be prompted to pick a choice 
     user_input = input("")

     # this will check which stack the user chose.
     if user_input in choices:
      for i in range(len(stacks)):
        return stacks[i]
