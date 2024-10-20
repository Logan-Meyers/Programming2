
import psrock
import importlib
importlib.reload(psrock)

import team1, team2, team3, team4, team5  # These are file names in this folder     
# The reload() statement is needed for each team because import 
# will only compile source code once to create the pyc file and store in memory.
# Without reload(), changes to the .py file will be ignored unless the pyc 
# file is deleted and the kernel restarted. 
importlib.reload(team1) 
importlib.reload(team2)
importlib.reload(team3)
importlib.reload(team4)
importlib.reload(team5)

import teamLogan
importlib.reload(teamLogan)
import TL3Pattern
importlib.reload(TL3Pattern)
import TLPossibilities
importlib.reload(TLPossibilities)
                        
# The first argument of round_robin() specifies the number of 
# rounds to be played by each pair of strategies. 
# Change the other arguments to use more teams, fewer teams, or different teams
short_report, long_report = psrock.round_robin(2000, team1, team2, team3, team4, team5, teamLogan, TL3Pattern, TLPossibilities)

for team in long_report:
    print('-'*80)
    print(long_report[team])
    
print(short_report)