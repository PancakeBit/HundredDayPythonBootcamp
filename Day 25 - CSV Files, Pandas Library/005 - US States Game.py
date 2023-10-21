import turtle
import pandas

# I hate pandas now
# The dataframe object is obscure and hard to understand
# the syntax is the opposite of intuitive
# you throw out what you learned from SQL
# it sucks

# Notes to change for improvement:
# 1. if statement for answer returns error if answer is left blank
# 2. try catch statement should be fixed to not need try catch
# 3. Dataframe object returns string WITH OBJECT NAME AND TYPE WTH IS UP WITH THAT WHY
class Writer(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.score = 0
        self.hideturtle()
        self.up()
        self.goto(-290, 250)

    def writeto(self, state, x, y):
        self.goto(x, y)
        self.write(f"{state}", move=False, align='center', font=("Courier", 10, "normal"))


screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")
# Instructions are to use the "addshape" method of turtle, but this makes more sense to me
screen.bgpic('blank_states_img.gif')

gamestart = True
states = pandas.read_csv('50_states.csv')

writer = Writer()
correctstates = []
while gamestart == True:
    # Score is tracked by the length of correctstates
    answer = screen.textinput(f"{len(correctstates)}/50 States Correct", "What is a name of a US State?")
    # If that correct answer hasn't been given yet
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!! returns an error if answer is left blank !!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if answer.lower() not in correctstates:
        # AND if that answer is in the state column of the file
        if answer.lower() in str(states['state'].values).lower():
            # Add the answer to the correctstates
            # Get the dataframe row of the answer converted to title case because case sensitive
            try:
                correctans = states[states['state'] == answer.title()]
                correctstates.append(answer)
                # convert to list that is flattened
                state = correctans.values.flatten().tolist()
                print(correctans.x)
                writer.writeto(state[0], state[1], state[2])
            except:
                pass
    if len(correctstates) == 50:
        writer.write("Congratulations! You win the game", 0, 0)
        gamestart = False

screen.mainloop()

# -------- IMPORTANT --------------------------------
# 'in' keyword also notices substrings, incomplete inputs also return true
# This causes an error in which line ~50 attempts to pull a dataframe but cannot find that key
# I'll just enclose that small block in a try catch, it's cheating but it works
# Should this be any other case i'll rewrite the code to not use 'in' but that would take more time
