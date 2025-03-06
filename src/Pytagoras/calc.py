# Module to calculate the hypotenuse of right-angle triangle
#will have two functions, one to get the squares of the opp and adj
#One to calculate the square root of those added together
#a**2 + b**2 = c**c
import numpy as np

#Function to get the squares of opp and adj
#Inputs/args: opp and adj (a and b)
#Outputs/returns: a**2 and b**2
def squares (opp, adj):
    opp_sq = opp**2
    adj_sq = adj**2
    return opp_sq, adj_sq



#Function to calculate the sqrt of those added
#Inputs/args: opp and adj squared (a**2 and b**2)
#Output/returns: hypotenuse (c)
def hypot (opp_sq, adj_sq):
    sum_a_a = opp_sq + adj_sq
    hypot_sqrt = np.sqrt(sum_a_a)
    return hypot_sqrt
    
#function to pull these togeter and calculate the hypotenuse given the sides
def slope (opp, adj):
    opp_sq, adj_sq = squares (opp, adj)
    hypot_sqrt = hypot (opp_sq, adj_sq)
    return hypot_sqrt