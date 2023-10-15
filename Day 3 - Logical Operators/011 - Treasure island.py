class StartScreen:
    def __init__(self):
        print("""
                                     _..-:-.._
                              _..--''    :    ``--.._
                       _..--''           :           ``--.._
                 _..-''                  :                .'``--.._
          _..--'' `.                     :              .'         |
         |          `.              _.-''|``-._       .'           |
         |            `.       _.-''     |     ``-._.'       _.-.  |
         |   |`-._      `._.-''          |  ;._     |    _.-'   |  |
         |   |    `-._    |     _.-|     |  |  `-.  |   |    _.-'  |  KSR
         |_   `-._    |   |    |   |     |  `-._ |  |   |_.-'   _.-'   ..
           `-._   `-._|   |    |.  |  _.-'-._   `'  |       _.-'   ..::::::..
               `-._       |    |  _|-'  *    `-._   |   _.-'   ..::::::::''
                   `-._   |   _|-'.::. \|/  *    `-.|.-'   ..::::::::''
                       `-.|.-' *`:::::::.. \|/  *      ..::::::::''
                              \|/  *`:::::::.. \|/ ..::::::::''
                                  \|/  *`:::::::.::::::::''
                                      \|/  *`::::::::''
                                          \|/  `:''
A House in the Suburbs
        
Type (1) to Play, Type (2) to Quit""")

        playerinput = input()

        if playerinput == "1":
            Room1()
        elif playerinput == "2":
            exit()
        else:
            StartScreen()


global matchstick
matchstick = False

class Room1:
    def __init__(self):
        print("The lights in your room suddenly go out and you see nothing but a candle on the table, just to the "
              "front of your face")
        print("You can look (Left) or (Right) from here and see what you can use to get out")

        userinput = input()

        if userinput.lower() == "left":
            Room1West()
        elif userinput.lower() == "right":
            Room1East()
        else:
            Room1North()


class Room1North:
    def __init__(self):
        print(
            "You keep looking straight ahead, you see almost nothing but you can make out the faint outline of a door")
        print("You need something to (Light) the candle so you can see")
        print("You can look (Left) or (Right) from here")

        userinput = input()
        global matchstick

        if userinput.lower() == "left":
            Room1West()
        elif userinput.lower() == "right":
            Room1East()
        elif userinput.lower() == "light":
            if matchstick == False:
                print("You don't have anything to light the candle with")
                Room1North()
            elif matchstick == True:
                print("You successfully light the candle and you can turn the knob to get out")
        else:
            Room1North()


class Room1West:
    def __init__(self):
        global matchstick
        if matchstick == False:
            print("There's something on the floor, you can try to (Pick it Up)")
            userinput = input()

            if userinput.lower() == "right":
                Room1North()
            elif userinput.lower() == "pick it up":
                matchstick = True
                Room1West()
            else:
                Room1West()
        else:
            print("You got a matchbook")
            print("From here you can look (Right) again")

            userinput = input()

            if userinput.lower() == "right":
                Room1North()
            else:
                Room1West()

class Room1East():
    def __init__(self):
        print("You looked right, there's a light switch on the wall and it works for some reason? You can get out now, you win!")
        exit()

if __name__ == "__main__":
    StartScreen()
