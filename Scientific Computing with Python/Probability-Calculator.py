import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **ball_colors_and_number):
        self.ball_colors_and_number = ball_colors_and_number
        self.contents = []
        for key in self.ball_colors_and_number:
            for values in range(0,self.ball_colors_and_number.get(key)):
                self.contents.append(key)

    def draw(self,num_to_draw):
        tempNum = num_to_draw
        balls_drawn = []
        if num_to_draw > len(self.contents):
            return self.contents
        while tempNum > 0:
            ball_chosen = random.choice(self.contents)
            balls_drawn.append(ball_chosen)
            str(self.contents.remove(ball_chosen))
            tempNum -= 1
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    tempNum = num_experiments
    num_predicted = 0
    tempContents = hat.contents.copy()
    tempBalls_drawn_dict = {}
    tempNum_correct = 0
    while tempNum > 0:
        balls_drawn = hat.draw(num_balls_drawn)
        for i in balls_drawn:
            if i in tempBalls_drawn_dict:
                tempBalls_drawn_dict[i] = tempBalls_drawn_dict[i] + 1
            else:
                tempBalls_drawn_dict[i] = 1
        for x in tempBalls_drawn_dict:
            if x in expected_balls:
                if tempBalls_drawn_dict[x] >= expected_balls[x]:
                    tempNum_correct += 1
                    if tempNum_correct == len(expected_balls):
                        print("yay")
                        num_predicted += 1 
        hat.contents = tempContents.copy()
        tempNum -= 1
        tempBalls_drawn_dict = {}
        tempNum_correct = 0
    return num_predicted/num_experiments