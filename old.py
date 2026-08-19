from Connect4_Solver import MonteCarlo
from Connect4_Solver import Connect4Bit        

def alphabetac4(state,depth,a,b,player):
  global count
  temp1 =state.p1board
  temp2 = state.p2board
  p = state.possible()
  point = 0
  if state.won(2):
    return [-100]
  elif state.won(1):
    return [-100]
  if len(p) == 0:
    return [0]
  if depth == 0:
    p1 = state.eval(1)
    p2 = state.eval(2)
    if player == 2:
        return [p2-p1]
    elif player == 1:
        return [p1-p2]
  value = -100
  for node in p:
      count += 1
      state.add(node,player)
      v = -alphabetac4(state,depth-1,-b,-a,3-player)[0]
      if v > value:
        value = v
        point = node
      a = max(a,value)
      state.p1board = temp1
      state.p2board = temp2
      if a >= b:
          return [a,point]
  return value,point
  
if __name__ == "__main__":
  count = 0    
  MCTS = MonteCarlo()
  state = Connect4Bit()
  state.display()
  while 1:
      if state.won(1):
          print('Player 1 (R) wins!!!!!!!!')
          break
      elif state.won(2):
          print('Player 2 (Y) wins!!!!!!!!')
          break
      count = 0
      index = int(input('Your move: ')) #alphabetac4(state,10,-100,100, 1)
      #print('AB: ', index)
      state.add(index,1)
      state.display()
      index = MCTS.main(state, 5000)
      print("MCTS: ", index)
      state.add(index,2)
      state.display()