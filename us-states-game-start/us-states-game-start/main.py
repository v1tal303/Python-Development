import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("U.S. Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
s_data = pandas.read_csv("50_states.csv")
state_number = 0
answer_list = []


#
# def get_moust_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_moust_click_coor)
# turtle.mainloop()


# print(answer_state)
#
# print(s_data["state"].str.contains(answer_state))
# print(any(s_data["state"].str.contains(answer_state).to_list()))
# answer_check = any(s_data["state"].str.contains(answer_state).to_list())
while state_number < 50:
    answer_state = screen.textinput(title=f"Guess the State: {state_number}/50", prompt="What's another state's name?").title()
    answer_check = any(s_data["state"].str.contains(answer_state).to_list())
    if answer_state == "Exit":
        break
    if answer_check and answer_state not in answer_list:
        s_xcor = int(s_data[s_data.state == answer_state].x)
        y_xcor = int(s_data[s_data.state == answer_state].y)
        Turtle_State = State(s_xcor, y_xcor, answer_state)
        state_number += 1
        answer_list.append(answer_state)
    elif answer_state in answer_list:
        print("You already guessed that")
    else:
        print("Wrong state name")

print(answer_list)
#
# s_data.drop("Alabama")

# print(s_data[s_data.state != answer_list[0]])

index_check = s_data[s_data.state.isin(answer_list)].index
unanswered = s_data.drop(index_check)

unanswered.to_csv("unanswered_states.csv")






# Test_State = State(s_xcor,y_xcor,answer_state)


turtle.mainloop()