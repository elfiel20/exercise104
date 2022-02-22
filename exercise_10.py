#This is the code for exercise 10
#in which i am defining functions

import math

#this is for the circle area
def circ_area(r):
    """
    Given the radius of a circle, calculate the area
    :param r: (float) radius of circle
    :return: (float) area of a circle
    """
    area=math.pi*r**2.0
    return area

#this is a function for the cone volume

def cone_volume(r,h):
    """ Given the height and radius of the cone, calculate the cone's volume
    :param r: (float) radius of cone
    :param h: (float) height of cone
    :return: (float) volume of cone """
    volume=math.pi*r**2*h/3
    return volume

def pop_est(y):
    """Given the amount of years in the future, calculate the estimated population

    :param y:(float) years
    :return:(float) population estimate
    """

    d=y*365

    h=d*24

    m=h*60

    s=m*60

    pop_est=328000000+((s/8)-(s/12)+(s/33))

    return pop_est



#Jacob Dubofki as a collaborator on pop_est




