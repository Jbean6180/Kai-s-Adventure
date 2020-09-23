from PIL import Image

start = '''
My name is Kai "milk chocolate" Jones; I just left a house party at your friend's house.
I decided I want some cake to nurse my hangover with.
This adventure begins our quest.
'''


print(start)


print("Type 'left' to go left, 'right' to go right, 'straight' to go forward.")
user_input = input()
if user_input == "left":
    print("We go left ...")

if user_input == "straight":
    print("We go straight ...")

elif user_input == "right":
    print("We go right ...")

print("Now first major choice: should we buy a cake or bake a cake?")
print("Type 'buy a cake' to start shopping debacle or 'bake a cake' to start home debacle.")
user_input = input()
if user_input == "buy a cake":
        print("So... we're going to the grocery store...")

        print("there is a mysterious old woman in the sweets aisle...")
        print("Type 'walk into aisle' to be approached by old hag or 'back away slowly' to not get cake.")
        user_input = input()
        if user_input == "walk into aisle":
                print("OMG...shes coming this way")

                print("*she grabs you by your hipster backpack*")

                print("*she yells obscenities at you*")
                print("What do you do? [1] say:at least im not an old hillbilly and stick out tongue or [2] RUN!!")
                user_input = input()
                if user_input == "1":
                        print("Press X to dodge her ashy hands")



                        print("dang, you got beat down by an old lady...out bad..")

                        print("OG out bad ending")# ending

                elif user_input == "2":
                    print("welp, you fell on your face...out bad..")
                    print("forget the cake lets just go home...")

                    print("Out bad no cake ending")# ending

        elif user_input == "back away slowly":
                print("Fwhew,..dodged a bullet there I'm sure..")

                print("YOU'VE OBtained the CakE!!!")

                print("CaKe!! ending")# ending

elif user_input == "bake a cake":
        print("K, lets go home and figure this mess out...")

        print("Ohh jeez, the old crimple from next door is in my driveway")
        print("What do you do? [1] Confront or [2] Run him over")
        user_input = input()
        if user_input == "1":
            print("The old man screams: Where's your boyfriend?")

            print("what?")

            print("old man says: Mountain Dew...Mountain Dew...Mountain Dew...")

            print("what?")

            print("the old man hits you in the head with a..you guessed it ..a mountian dew bottle; He kidnaps you and know you're trapped in the basement....out bad..")



            print("Crazy OLd man/ No cAke ending")# ending
        elif user_input == "2":
            print("Welp, we ran over OLd maN Maguckit")

            print("*goes inside*")

            print("*makes cake*")

            print("*eats cake*")

            print("*naps*")

            print("*ZZZZZZZ*")


            print("Murderer/ CAke ending")# ending
