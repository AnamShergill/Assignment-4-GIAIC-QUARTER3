#Write a program to solve this age-related riddle!

#Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

#Anton is 21 years old.

#Beth is 6 years older than Anton.

#Chen is 20 years older than Beth.

#Drew is as old as Chen's age plus Anton's age.

#Ethan is the same age as Chen.

def main():

# Assigning ages based on the given relationships
    Anton = 21
    Beth = Anton + 6
    Chen = Beth + 20
    Drew = Anton + Chen
    Ethan = Chen

    # Printing the names and ages in the required format
    print(f"Anton is {Anton}")
    print(f"Beth is {Beth}")
    print(f"Chen is {Chen}")
    print(f"Drew is {Drew}")
    print(f"Ethan is {Ethan}")

if __name__ == '__main__':
    main()