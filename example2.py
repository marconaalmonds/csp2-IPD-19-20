####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E2'
strategy_name = 'Pattern Finder'
strategy_description = 'Sees if theres a pattern in the opponents move and responds'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    #This attempts to find any variating patterns in their responses, and respond accordingly
    if 'bcbcbc' in their_history:
      return 'b'
    elif 'cbcbcb' in their_history:
      return 'c'
    elif 'bbbbb' in their_history:
      return 'b'
    elif 'ccccc' in their_history:
      return 'c'
    else: 
      return 'c'
