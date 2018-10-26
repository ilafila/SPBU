import math


def balls_collide(ball_one, ball_two):
    if ball_one[2] < 0 or ball_two[2] < 0:
        raise ValueError
    if ball_one[2]+ball_two[2] >= math.sqrt((ball_two[0]-ball_one[0])**2-(ball_two[1]-ball_one[1])**2):
        return True
    return False
