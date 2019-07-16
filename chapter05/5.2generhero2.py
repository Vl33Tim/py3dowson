#gener hero

attrbutes = 30 

attr = [0,0,0,0]
health strenght intelegence agility = attr

rules = ("""

    Welcome to Generator of heroes
    chose attribute

    0 - exit
    1 - health
    2 - strenght
    3 - intelegence
    4 - agility

    5 - show state

    
""")
print(rules)
decision = input("make your choice")

while decision != "0":
    if decision == "1":
        while decision != "b":
            decision = input("enter number of 'b'-back to previous menu")
            if  decision == "+":
                health += "#"
                attrbutes -= 1
            elif decision == "-":
                health.remove("#")
                attrbutes += 1
            elif decision ==
            else:
                print("incorrect choice")