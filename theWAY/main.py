from message import message
from input_string import input_string
from print_protein import fancy_print_protein
from print_protein import print_protein
from update_grid import update_grid
from fold import fold
from score import score
from hillclimber import hillclimber
from algo_brute_force import algo_brute_force
from plotdata import plotdata
import csv

# Import all the global variables.
import global_vars
global_vars.init()

message("This is a protein-fold-optimizer by Team50")

# Get the user's choice of protein.
input_string()

message("Protein received")

# Print starting configuration of the protein
print_protein()

message("Protein initiated, starting algorithm.")

message("Folding summary:")

""">>>>>> UNCOMMENT THE ALGORITHM YOU WANT TO USE BELOW <<<<<<"""

with open('optimum.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    for i in range(4, 15):
        # algo_brute_force()

        print(i)
        forloop = 5
        for j in range(forloop):
            hillclimber(i)
            writer.writerow([i] + [global_vars.winning_score])




# Print the best solution.
print_protein()

plotdata()
