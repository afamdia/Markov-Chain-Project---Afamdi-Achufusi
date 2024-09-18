"""
Name: Afamdi Achufusi

Markov Chain Project

PROJECT IDEA (Ball Handling Workout):
    - My project uses a Markov Chain to create different basketball moves/workouts for kids to try. A lot of kids aren't able to afford basketball trainers and may struggle to find a sense of direction in temrs of how to structure their basketball workouts. This project essentially structures a ball handling workout for young basketball players to follow.
    - The ball handling workout can be split into 10 sections (each section is one minute, so its a 10 minute workout)
    - The markov chain will come up with combo moves for the player to spend each minute on
    - To get extra creative, I can try to record myself doing each move, so then it will show me demonstrating the combo moves when the Markov chain runs

Dependencies: numpy, matplotlib, pillow

"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


class MarkovWorkoutGenerator:
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.moves = list(transition_matrix.keys())

    def next_move(self, current_move):
        """
        Decides which dribble move to do next.
      
        Args: 
            - current_move (str) - the current dribble move being performed.
        """
        return np.random.choice(self.moves, p=[self.transition_matrix[current_move][next_move] for next_move in self.moves])
    
    def combo_move(self, current_move="pound", move_array=[]):
        """
        Creates a 3-part combo move for the user to perform.
      
        Args: 
            - current_move (str) - the current dribble move being performed.
            - move_array (array) - this will get populated with three dribble moves, turning it into a single 3-part combo move.
        """
        if (len(move_array) == 3):
            return move_array
        else:
            added_move = self.next_move(current_move)
            move_array.append(added_move)
            return self.combo_move(added_move, move_array)


def main():
    print("Let's go through a ball handling workout!")

    # The weights for this transition matrix were very carefully selected based on what dribble moves are realistic/common in real life.
    # For example, you will never see a player do a hesitation dribble (hesi) into another hesitation dribble, so I gave that transition a probability of 0.
    bball_workout_maker = MarkovWorkoutGenerator({"cross" : {"cross": 0.1, "between": 0.3, "behind": 0.3, "spin": 0.2, "in_and_out": 0.0, "retreat": 0.1, "pound": 0.0, "hesi": 0.0},
                                  "between" : {"cross": 0.3, "between": 0.1, "behind": 0.3, "spin": 0.2, "in_and_out": 0.0, "retreat": 0.1, "pound": 0.0, "hesi": 0.0},
                                  "behind" : {"cross": 0.3, "between": 0.1, "behind": 0.1, "spin": 0.2, "in_and_out": 0.1, "retreat": 0.1, "pound": 0.0, "hesi": 0.1},
                                  "spin" : {"cross": 0.3, "between": 0.0, "behind": 0.1, "spin": 0.0, "in_and_out": 0.2, "retreat": 0.3, "pound": 0.0, "hesi": 0.1},
                                  "in_and_out" : {"cross": 0.2, "between": 0.1, "behind": 0.1, "spin": 0.2, "in_and_out": 0.1, "retreat": 0.2, "pound": 0.0, "hesi": 0.1},
                                  "retreat" : {"cross": 0.1, "between": 0.1, "behind": 0.1, "spin": 0.3, "in_and_out": 0.1, "retreat": 0.0, "pound": 0.0, "hesi": 0.3},
                                  "pound" : {"cross": 0.2, "between": 0.2, "behind": 0.2, "spin": 0.1, "in_and_out": 0.1, "retreat": 0.1, "pound": 0.0, "hesi": 0.1},
                                  "hesi" : {"cross": 0.2, "between": 0.2, "behind": 0.2, "spin": 0.1, "in_and_out": 0.2, "retreat": 0.1, "pound": 0.0, "hesi": 0.0}})

    # Assigning variable names for the images
    cross = Image.open("crossover_dribble.jpeg")
    between = Image.open("between_the_legs_dribble.jpg")
    behind = Image.open("behind_the_back.jpeg")
    spin = Image.open("spin_move_dribble.jpg")
    in_and_out = Image.open("in_and_out_dribble.jpeg")
    retreat = Image.open("retreat_dribble.jpg")
    pound = Image.open("pound_dribble.png")
    hesi = Image.open("hesitation-dribble.jpg")

    # Initializing the figure and subplots
    fig, axes = plt.subplots(1, 3, figsize=(12, 12))

    # Giving the figure a title
    fig.suptitle('BALL-HANDLING WORKOUT!\n All three of these moves combined make up one 3-part combo move. So make sure to do them CONSECUTIVELY (one right into the next)!\n Perform this 3-part combo move repeatedly for ONE MINUTE STRAIGHT to get a good burn in your arms.\n Then run the code again for a new move.\n Begin!', fontweight='bold')
    
    # Giving the figure a background color (I chose tan because this is the color of most basketball courts)
    fig.set_facecolor('tan')

    # Declaring which cases each image will be displayed in
    for n, move in enumerate(bball_workout_maker.combo_move()):
        if move == "cross":
            axes[n].imshow(cross, extent=[-1, 1, -1, 1])
            axes[n].title.set_text("CROSSOVER")
            axes[n].set_xticks([])
            axes[n].set_yticks([])
            axes[n].set_xlabel("(Get low and dribble the ball across to\n your other hand in one hard bounce.)")
        elif move == "between":
            axes[n].imshow(between, extent=[-1, 1, -1, 1])
            axes[n].title.set_text("BETWEEN")
            axes[n].set_xticks([])
            axes[n].set_yticks([])
            axes[n].set_xlabel("(Get low and dribble the ball across to\n your other hand in one hard bounce\n between your legs.)")
        elif move == "behind":
            axes[n].imshow(behind, extent=[-1, 1, -1, 1])
            axes[n].title.set_text("BEHIND")
            axes[n].set_xticks([])
            axes[n].set_yticks([])
            axes[n].set_xlabel("(Get low and dribble the ball across to\n your other hand in one hard bounce\n behind your back.)")
        elif move == "spin":
            axes[n].imshow(spin, extent=[-1, 1, -1, 1])
            axes[n].title.set_text("SPIN")
            axes[n].set_xticks([])
            axes[n].set_yticks([])
            axes[n].set_xlabel("(Spin around and let the ball bounce\n mid-spin, picking it up with your other hand.)")
        elif move == "in_and_out":
            axes[n].imshow(in_and_out, extent=[-1, 1, -1, 1])
            axes[n].title.set_text("IN-AND-OUT")
            axes[n].set_xticks([])
            axes[n].set_yticks([])
            axes[n].set_xlabel("(Get low and pretend you are going to\n bounce the ball across to your other hand.\n But right before letting go of the ball,\n turn your hand so that it is on the inside of\n the ball when you dribble. The ball will bounce\n back in the same direction it came from,\n and you will pick it up with the same hand.)")
        elif move == "retreat":
            axes[n].imshow(retreat, extent=[-1, 1, -1, 1])
            axes[n].title.set_text("RETREAT")
            axes[n].set_xticks([])
            axes[n].set_yticks([])
            axes[n].set_xlabel("(Take two hard dribbles and\n side-shuffle backwards as you do so.)")
        elif move == "pound":
            axes[n].imshow(pound, extent=[-1, 1, -1, 1])
            axes[n].title.set_text("POUND")
            axes[n].set_xticks([])
            axes[n].set_yticks([])
            axes[n].set_xlabel("(Just take one hard dribble.)")
        elif move == "hesi":
            axes[n].imshow(hesi, extent=[-1, 1, -1, 1])
            axes[n].title.set_text("HESITATION")
            axes[n].set_xticks([])
            axes[n].set_yticks([])
            axes[n].set_xlabel("(Get low and bounce the ball hard.\n As the ball comes up, you can\n relax back up into an upright stance.\n As soon as the ball touches your hand again,\n get back low and bounce it again.)")

    plt.tight_layout() 
    plt.show()
    

if __name__ == "__main__":
    main()