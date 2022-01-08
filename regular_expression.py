                                # Regular Expression
import re
'''
re.match()
re.search()
    span()
    string()
    group()
re.findall()
re.split()
re.sub()
re.compile()
'''
str1 = '''Cricket is a bat-and-ball game played between two teams of eleven players each on a field at the centre of which is a 22-yard (20-metre) pitch with a wicket at each end, each comprising two bails balanced on three stumps. The game proceeds when a player on the fielding team, called the bowler, "bowls" (propels) the ball from one end of the pitch towards the wicket at the other end, with an "over" being completed once they have legally done so six times.'''

matches1 = re.findall("bat",str1)
print(matches1)
matches2 = re.search("two",str1)
print(matches2)
matches3 = re.split(str1,"the")
print(matches3)
# matches4 = re.split(str1,"he")
# print(matches4)