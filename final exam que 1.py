secret_number =777

n=int(input("""


+=========================================+
|Welcome to my game, muggle!              |                                                                  
|Enter an integer number                  |          
|and guess what number                    |
|i have picked for u.                     |
|So,what is the secret number ?           |                               
|                                         |
+=========================================+
"""))

if n != secret_number: # If statement to check the number is right
    print("you are stuck in loop!")

    if n <secret_number:
        print("your imagination is too low.")
    if n >secret_number:
        print("your imagination is too up.")
        
    while True:

            input("Enter an integer number: ") # Loop never ends...
        
print("Well done, muggle! You are free now,") # If the program made it here,that means the user's number correct
