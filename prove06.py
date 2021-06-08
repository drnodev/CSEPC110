"""
File:check01.py
Author: NO

Purspose:  Prove: Milestone
"""
value = 20
while value < 20:
    value = value + 1
print(value)

answer = ""
question = "Wha t do you what to do?\n"
my_house = "You realize that Yuki is not there, you only see his leash pointing north, immediately you see some footprints in the opposite direction. "
ralf_house = "You walk for hours and ask your neighbors, but you can't find any trace of Yuki.\nFinally, someone seemed to see her enter old Ralf's house.\nOld Ralf is known to hate children and eats dogs"
left_ralf = "Old Ralf opens the door, you realize that he is a very kind person, you ask him if he saw your dog,\nhe answers that Yuki was hanging out with her dogs but then she left, in the direction of your house."
talk = "You ask him if the stories of old Ralf are true, he tells you they are false, he loves dogs and likes to talk to children.\nHe invites you to his house next weekend, it is the birthday of one of his puppies. "
stealthily = "You enter old Ralf's house and see several dogs in his garden, the dogs are playing and having fun, the opposite of the stories. Old Ralf appears. "
run = "You run scared to your house, when you arrive you find Yuki :)"
say_bye = "You say goodbye to old Ralf :)  \nThe dog is at home. "
freeze = "You get scared, but after all old Ralf is a good person. "

my_house_op = "Follow leash direction LEASH or Follow FOOTPRINTS: "
ralf_house_op = "Ringing the DOORBELL or Entering the house STEALTHILY: "
left_ralf_op = "Run HOME or TALK to Old Ralf: "
talk_op = "Confirm your ATTENDANCE or APOLOGIZE, you must clean your room: "
stealthily_op = "RUN or FREEZE"

print("\n")
print("********************************************************************************")
print("                                 YUKI o.O ")
print("********************************************************************************")
print("Yuki is a husky, since she was a little pet she was quite curious and explorer. ")
print("One day she ran away from home, since then nothing is known about her. ")
print("\n")
print("     |\_/|")
print("     | @ @   Woof!")
print("     |   <>              _ ")
print("     |  _/\------____ ((| |))")
print("     |               `--' |   ")
print(" ____|_       ___|   |___.' ")
print("/_/_____/____/_______|")
print("\n")

print("Let's find her. ")
print("\n")
print(my_house)
print("\n")
answer = input(question + my_house_op).lower()
print("\n")
if answer == "leash":
    print("\n")
    print(ralf_house)
    print("\n")
    answer = input(question + ralf_house_op).lower()
    if answer == "doorbell":
        print("\n")
        print(left_ralf)
        print("\n")
        answer = input(question + left_ralf_op).lower()
        if answer == "talk":
            print("\n")
            print(talk)
            answer = input(question + talk_op).lower()
            print(say_bye)
        elif answer == "home":
            print("\n")
            print(say_bye)
        else:
            print("\n")
            print("You go home and your dog is there. ")
    elif answer == "stealthily":
        print("\n")
        print(stealthily)
        answer = input(question + stealthily_op).lower()
        print("\n")
        if answer == "freeze":
            print("\n")
            print(freeze + talk + say_bye)
        else:
            print("\n")
            print(run)
            print("\n")
    else:
        print("go Home She is there")
elif answer == "footprints":
    print("\n")
    print("You follow the footprints and finally find your dog at the back of the yard. ")
    print("\n")
else:
    print("Sorry the option is not valid, please restart the game.")


print("Good bye.")
