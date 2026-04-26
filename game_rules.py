import random
from utils import choices
def comp_choice():
    return random.choice(choices)
def logic(p,c):
    if p==c:
        return "--Tie--"
    rules={'rock':'scissors','paper':'rock','scissors':'paper'}
    if rules[p]==c:
        return "--You won--"
    else:
        return "--I won--"