################################
# Kinley Dolkar
# BE ECE
# 02220118
################################
# REFERENCES
# File Opration : https://www.youtube.com/watch?v=Uh2ebFW8OYM
# Rock-Paper-Scissor Sample Game: https://realpython.com/python-rock-paper-scissors/
# Python Crash Course: https://www.youtube.com/watch?v=JJmcL1N2KQs
################################
# SOLUTION
# Your Solution Score: 49843
################################
# Read the input_8_cap1.txt file
def read_input():
    rounds = []
    with open("input_8_cap1.txt", "r") as file:
        for line in file:
            line = line.strip().split()
            rounds.append(line)
    return rounds

def calculate_score():
    rounds = read_input()
    score = 0

    # Iterating each user list 
    for round in rounds:
        opponent_choice = round[0] # i.e A,B,C
        end = round[1] # i.e X,Y,Z
        rock_point, paper_point, scissor_point = [1,2,3]
        lose_point, draw_point, win_point = [0,3,6]

        # A : rock, B : paper, C : scissor
        #  X : lose, Y : draw, Z : win
        if end == "X":
            if opponent_choice == "A":
                score += scissor_point  # rock defeats scissor
            elif opponent_choice == "B":
                score +=  rock_point # paper defeats rock
            elif opponent_choice == "C":
                score += paper_point  # scissor defeats paper
            score += lose_point
        elif end == "Y":
            if opponent_choice == "A":
                score += rock_point  # rock draw with rock
            elif opponent_choice == "B":
                score += paper_point  # paper draw with paper
            elif opponent_choice == "C":
                score += scissor_point  # scissor draw with scissor
            score += draw_point
        elif end == "Z":
            if opponent_choice == "A":
                score += paper_point  # rock loses to paper
            elif opponent_choice == "B":
                score += scissor_point  # paper loses to scissor
            elif opponent_choice == "C":
                score += rock_point  # scissor loses to rock
            score += win_point
    print(f"The total score is: {score}")

# Run the program
calculate_score()