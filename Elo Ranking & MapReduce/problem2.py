from problem1 import elo_rating
import numpy as np
#-------------------------------------------------------------------------
'''
    Problem 2: 
    In this problem, you will use the Elo rating algorithm in problem 1 to rank the NCAA teams.
    You could test the correctness of your code by typing `nosetests test2.py` in the terminal.
'''

#--------------------------
def import_W(filename ='ncaa_results.csv'):
    '''
        import the matrix W of game results from a CSV file.
        In the CSV file, each line contains the result of one game. For example, (i,j) in the line represents the i-th team won, the j-th team lost in the game.
        Input:
                filename: the name of csv file, a string 
        Output: 
                W: the game result matrix, a numpy integer array of shape (n by 2)
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    W = np.array(np.loadtxt(filename, dtype=np.int, delimiter=','))

    #########################################
    return W

#--------------------------
def import_team_names(filename ='ncaa_teams.txt'):
    '''
        import a list of team names from a txt file. Each line of text in the file is a team name.
        Each line of the file contains one team name. For example, the first line contains the name of the 0-th team.
        Input:
                filename: the name of txt file, a string 
        Output: 
                team_names: the list of team names, a python list of string values, such as ['team a', 'team b','team c'].
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    team_names = np.loadtxt(filename, dtype=np.str, delimiter=',').tolist()

    #########################################
    return team_names

#--------------------------
def team_rating(resultfile = 'ncaa_results.csv', 
                teamfile='ncaa_teams.txt',
                K=16.):
    ''' 
        Rate the teams in the game results imported from a CSV file.
        (1) import the W matrix from `resultfile` file.
        (2) compute Elo ratings of all the teams
        (3) return a list of team names sorted by descending order of Elo ratings 

        Input: 
                resultfile: the csv filename for the game result matrix, a string.
                teamfile: the text filename for the team names, a string.
                K: a float scalar value, which is the k-factor of Elo rating system

        Output: 
                top_teams: the list of team names in descending order of their Elo ratings, a python list of string values, such as ['team a', 'team b','team c'].
                top_ratings: the list of elo ratings in descending order, a python list of float values, such as ['600.', '500.','300.'].
        
    '''
    #########################################
    ## INSERT YOUR CODE HERE

    # load game results
    W = import_W(resultfile)
    # load team names
    team_names = import_team_names(teamfile)
    # number of teams
    number_of_teams = len(team_names)
    # compute Elo rating of the teams
    R = elo_rating(W, number_of_teams, K)
    # sort team names
    for i in range(number_of_teams):
        least_index = i
        for j in range(i + 1, number_of_teams):
            if ( R[j] < R[least_index] ):
                least_index = j
        R[i], R[least_index] = R[least_index], R[i]
        team_names[i], team_names[least_index] = team_names[least_index], team_names[i]
    top_teams = team_names[::-1]
    top_ratings = R[::-1]

    #########################################
    return top_teams, top_ratings

