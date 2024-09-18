# Markov-Chain-Project---Afamdi-Achufusi

Title: Markov Ball Handling Working Generator

Description:

  For my project, I used a Markov Chain to create a ball handling workout. To run my code, you can simply download the code to your device, cd into the folder where it is located, and then enter "python3 MarkovWorkoutGenerator.py" in your terminal. 

  This system is personally meaningful to me because I play basketball myself, and I was fortunate enough to have many coaches/trainers in my life who could give me tips and pointers. these days however, trainers and coaches charge a lot of money for instruction, and a lot of people can't afford a lot of them. I wanted to create something that could help people get better at basketball without having to spend money. Hopefully, this project can find someone who doesn't have access to a trainer/coach, and is looking for ways to get better on their own. The aim of this system is to provide people like this with a structure and routine.

  One thing that I found challenging about my work was finding ways to make it realistic and understandable. In terms of making it realistic, I had to be very specific about which Markov transitions would make sense in this case. in other words, I had to be very specific about which combo moves were realistic and actually commonly used in real-life. For example, nobody ever really does a "hesitation dribble" (hesi) into another "hesitation dribble", so I made sure to give that transition a weight of 0. Next was making the moves understandable to people who may be beginners with basketball. I included descriptions under each picture and tried to be very clear about how each move should be performed without including too many words (unless absolutely necessary). This was a very difficult task since I was only limited to pictures (matplotlib doesn't allow for subplots with videos). 

  I believe this system is creative because it comes up with moves that people might not originally think of performing in games. When we think of moves, we normally think of just a crossover, or just a behind-the-back dribble. Defenders normally only think of basic moves like this as well. Most defenders in basketball will usually only anticipate a 2-part combo move at most. So, by creating a system that comes up with realistic, 3-part combo moves that can actually be used in games, this allows the user to get more creative than most other basketball players. And this in turn makes the system creative.

  I would like to credit the following website: https://www.online-basketball-drills.com/. This is where I got the pictures in my project from. I would also like to credit Professor Harmon and Daniel Grant (my partner from the Two to Tango class activity) because I drew some inspiration for code examples that we had worked on in class.
