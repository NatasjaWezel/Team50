# holds all the globals and stuff we need in every file

def init():
    global grid
    grid = []
    global winning_grid
    winning_grid = []
    global amount
    amount = 0

    global csvfile
    csvfile = File("", "", "")

    global protein
    protein = Protein("", [], [], 0, [])


class File():
    def __init__(self, filepath, protein_input, algorithm):
        self.filepath = filepath
        self.protein_name = protein_input
        self.algorithm = algorithm


    # def generate_filepath():
    #     date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        
    #     filepath = "data\hillclimber\hc_" + str(date) + ".csv"
    #     File.filepath = filepath

    # def generate_header():
    #     with open(File.filepath, 'w', newline='') as csvfile:
    #         datawriter = csv.writer(csvfile)
    #         datawriter.writerow(["# This is a datafile generated for protein: " + str(global_vars.protein.protein_string)])
    #         datawriter.writerow(["# It is generated with a" +  File.algorithm + "algorithm."])




class Protein():
    def __init__(self, protein_string, coordinates, winning_coordinates,
        winning_score, aminos):
        self.protein_string = protein_string
        self.coordinates = coordinates
        self.winning_coordinates = winning_coordinates
        self.winning_score = winning_score
        self.aminos = aminos

    # def initialize(): string aminos omzetten in lijst


class Amino():
    def __init__(self, num_id, letter):
        self.num_id = num_id
        self.letter = letter
