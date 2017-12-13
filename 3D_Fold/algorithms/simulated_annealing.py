from global_vars import Amino
from utility.score import score
from utility.fold import fold
from algorithms.hillclimber import get_random_value
from algorithms.progress_bar import printProgressBar

import time
import datetime
import os
from random import randint
import copy
import csv
import math

import global_vars
global_vars.init()

def simulated_annealing():

    global_vars.protein.winning_score = current_score = 0

    length = len(global_vars.protein.protein_string)
    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
    global_vars.protein.winning_coordinates = copy.deepcopy(global_vars.protein.coordinates)

    # initialize iterations, begin and end temperature
    N = 10000
    T0 = Ti = 1
    Tn = 0

    # store algorithm in file, write a header
    global_vars.csvfile.algorithm = "Simulated Annealing"

    # generate a filepath
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    global_vars.csvfile.filepath = "data\hillclimber\hc_" + str(date) + ".csv"

    # store data in .csv
    with open(global_vars.csvfile.filepath, 'w', newline='') as csvfile:
        datawriter = csv.writer(csvfile)
        datawriter.writerow(["# This is a datafile generated for protein: " + str(global_vars.protein.protein_string)])
        datawriter.writerow(["# It is generated with a" +  global_vars.csvfile.algorithm + "algorithm."])

        # do N times 10 random folds and keep track of the best value
        for i in range(N):

            printProgressBar(i, N)

            # write score and iteration to a csv file
            datawriter.writerow([i] + [current_score])

            # do random folds
            for j in range(10):
                random_value = get_random_value()
                return_code = fold(random_value[0], random_value[1])

            old_score = current_score
            # calculate stability of the protein
            current_score = score()

            # if the score is lower save that particular grid in winning grid
            if current_score <= global_vars.protein.winning_score:
                global_vars.winning_grid = copy.deepcopy(global_vars.grid)
                global_vars.protein.winning_coordinates = copy.deepcopy(global_vars.protein.coordinates)

                # update winning_score
                global_vars.protein.winning_score = current_score

            # if the score is higher, calculate acceptance chance
            else:
                # calculate acceptance chance
                difference = global_vars.protein.winning_score - current_score
                acceptance_chance = math.exp(difference / Ti)

                # generate random compare value
                value = randint(1,10000)/10000

                # if acceptance_chance <= value, the deterioration is not accepted
                if acceptance_chance < value:

                    # if not accepted, restore the old grid
                    global_vars.grid = copy.deepcopy(global_vars.winning_grid)
                    global_vars.protein.coordinates = copy.deepcopy(global_vars.protein.winning_coordinates)
                    current_score = old_score

                # if accepted
                else:
                    # update changes anyway in the grid
                    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
                    global_vars.protein.winning_coordinates = copy.deepcopy(global_vars.protein.coordinates)

            # cool system linear
            Ti = T0 - (i * (T0 - Tn) / N)


def simulated_annealing_control():
    global_vars.protein.winning_score = current_score = 0

    length = len(global_vars.protein.protein_string)
    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
    global_vars.protein.winning_coordinates = copy.deepcopy(global_vars.protein.coordinates)

    # initialize iterations, begin and end temperature
    N = 5000
    T0 = Ti = 1
    Tn = 0

    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filepath = "data\simulated_annealing\sa_" + str(date) + ".csv"
    global_vars.filepath = filepath

    # store data in .csv
    with open(filepath, 'w', newline='') as csvfile:
        datawriter = csv.writer(csvfile)
        datawriter.writerow(["# This is a datafile generated for protein: " + str(global_vars.protein.protein_string)])
        datawriter.writerow(["# It is generated with a Simulated Annealing algorithm."])

        # do N times 3 random folds and keep track of the best value
        for i in range(N):

            printProgressBar(i, N)

            # write score and iteration to a csv file
            datawriter.writerow([i] + [current_score])

            # do .. random folds and check each fold for a better score
            for j in range(10):
                # initial random value
                random_value = get_random_value()

                while fold(random_value[0], random_value[1]) == "collision":
                    random_value = get_random_value()

                old_score = current_score
                # calculate stability of the protein
                current_score = score()

                # if the score is lower save that particular grid in winning grid
                if current_score < global_vars.protein.winning_score:
                    global_vars.winning_grid = copy.deepcopy(global_vars.grid)
                    global_vars.protein.winning_coordinates = copy.deepcopy(global_vars.protein.coordinates)
                    global_vars.protein.winning_score = current_score

                else:
                    # calculate acceptance chance
                    difference = global_vars.protein.winning_score - current_score
                    acceptance_chance = math.exp(difference / Ti)

                    # generate random compare value
                    value = randint(1,10000)/10000

                    # if acceptance_chance <= value, the deterioration is not accepted
                    if acceptance_chance < value:

                        # if not accepted, restore the old grid
                        global_vars.grid = copy.deepcopy(global_vars.winning_grid)
                        global_vars.protein.coordinates = copy.deepcopy(global_vars.protein.winning_coordinates)
                        current_score = old_score

                    # if accepted
                    else:
                        # update changes anyway in the grid
                        global_vars.winning_grid = copy.deepcopy(global_vars.grid)
                        global_vars.protein.winning_coordinates = copy.deepcopy(global_vars.protein.coordinates)

            # cool system linear
            Ti = T0 - (i * (T0 - Tn) / N)
