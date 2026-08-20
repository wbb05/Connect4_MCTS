import random
import math
        
class Connect4Bit:
  
  def __init__(self):
    self.p1board = 0
    self.p2board = 0
  
  def possible(self):
    mask = self.p1board | self.p2board
    p = []
    list = [3,4,2,5,1,6,0]
    for i in list:
      if not (mask & (1 << 5 << 7 * i)):
        p.append(i)
    return p
  
  def add(self,col,player):
    bottom_bit = 1 << 7 * col
    mask = self.p1board | self.p2board
    pos = mask | (mask + bottom_bit)
    pos ^= mask
    if player == 1:
      self.p1board |= pos
    elif player == 2:
      self.p2board |= pos
    return
  
  def won(self,player):
    if player == 1:
      board = self.p1board
    elif player == 2:
      board = self.p2board
    #Horizontal
    temp = board & (board << 7)
    if temp & (temp << 14):
      return True
    #Vertical
    temp = board & (board << 1)
    if temp & (temp << 2):
      return True

    temp = board & (board << 8)
    if temp & (temp << 16):
      return True
    temp = board & (board << 6)
    if temp & (temp << 12):
      return True
    return False
  
  def eval(self, player):
    if player == 1:
      board = self.p1board
    elif player == 2:
      board = self.p2board
    tally = 0
    temp = board & (board << 1)
    tally += self.popCount(temp & (temp << 1))
    temp = board & (board << 7)
    tally += self.popCount(temp & (temp << 7))
    temp = board & (board << 8)
    tally += self.popCount(temp & (temp <<8))
    temp = board & (board << 6)
    tally += self.popCount(temp & (temp << 6))
    return tally
  
  def popCount(self, bitstring):
    x = bitstring
    count = 0
    while x or count > 100:
      count += 1
      x &= x - 1
    return count
    
  def toArray(self):
    ret_array = [[-1 for i in range(6)] for j in range(7)]
    p1 = bin(self.p1board)[2:]
    p2 = bin(self.p2board)[2:]
    p1 = p1[::-1]
    p2 = p2[::-1]
    
    count = 0
    for i in range(7):
        for j in range(6):
            if count < len(p1) and p1[count] == '1':
                ret_array[i][j] = 1
            elif count < len(p2) and p2[count] == '1':
                ret_array[i][j] = 2
            else:
                ret_array[i][j] = 0
            count += 1
        count += 1
    return ret_array
    
  def display(self):
      a = self.toArray()
      n = len(a[0])
      print('0 1 2 3 4 5 6')
      for i in range(n):
          for j in range(len(a)):
              #a[j][i]
              if a[j][n - i-1] == 1:
                  print('R', end = ' ')
              elif a[j][n - i-1] == 2:
                  print('Y', end = ' ')
              else:
                  print('.', end = ' ')
          print()
        
class Node:
    def __init__(self, parent, board1, board2, player, move):
        self.move = move
        self.board1 = board1
        self.board2 = board2
        self.player = player
        self.count = 1
        self.value = 0
        self.parent = parent
        self.children = []
        
    def best_child(self):
        max = -100
        for child in self.children:
            weight = child.value / child.count
            weight +=  math.sqrt((2 * math.log(self.count))/child.count)
            if weight > max:
                max = weight
                node = child
        return node
        
    def add_child(self, board1,board2, player, move):
        new = Node(self, board1,board2, player, move)
        self.children.append(new)
        return 
            
class MonteCarlo:
    def __init__(self):
        self.parent = None
        self.state = Connect4Bit()
        return
    
    def selection(self):
        node = self.parent
        while len(node.children) != 0:
            node = node.best_child()
        return node
            
    def simulate(self, node):
        #state.board = node.board[:]
        player = node.player
        self.state.p1board = node.board1
        self.state.p2board = node.board2
        won = 0
        if self.state.won(player) == True:
            won = player
        while won == 0:
            p = self.state.possible()
            if len(p) == 0:
                return 0
            move = random.choice(p)
            self.state.add(move,player)
            player = 3 - player
            if self.state.won(player) == True:
                won = player
        return  3-won
    
    def backprop(self,node,value):
        while node:
            node.count += 1
            if value == 0:
                node.value += 0.5
            elif value == node.player:
                node.value += 1
            node = node.parent

        
    def MCTS(self):
        node = self.selection()
        #self.state.board = node.board[:]
        #temp = state.board[:]
        player = node.player
        self.state.p1board = node.board1
        self.state.p2board = node.board2
        p = self.state.possible()
        for a in p:
            self.state.add(a,player)
            node.add_child(self.state.p1board,self.state.p2board, 3 - player, a)
            self.state.p1board = node.board1
            self.state.p2board = node.board2
            #state.board = temp[:]
        if len(p) != 0:
            node = random.choice(node.children)
        for i in range(1):
          value = self.simulate(node)
          self.backprop(node,value)
        return
    
    def check(self):
        max = -100
        for child in self.parent.children:
            if child.count > max:
                max = child.count
                node = child
            elif child.count == max:
                node = random.choice([node,child])
        #print("\n")
        #for child in node.children:
            #print(child.value,child.count)
        return node.move
            
    
    def main(self,stat,n):
        self.parent = Node(None,stat.p1board,stat.p2board,2,0)
        for i in range(n):
            self.MCTS()
        return self.check()

# Interfaces with GUI
class Connect4_Solver():
   def __init__(self):
      self.game = Connect4Bit()
      self.solver = MonteCarlo()
      self.MCTS_iterations = 5000 # Default
      # Define player 1 as player, player 2 as AI

   # Player adds piece
   def add_player_piece(self, col: int):
      self.game.add(col, 1)

   # AI adds piece
   def add_ai_piece(self, col: int):
      self.game.add(col,2)

   # Predicts next ai move
   # Returns col to move
   def ai_predict(self) -> int:
      col = self.solver.main(self.game, self.MCTS_iterations)
      return col

   def reset(self):
      self.game = Connect4Bit()
      self.solver = MonteCarlo()

   
   # Changes number of iterations
   # Accepts Easy, Medium, Hard
   # TODO: Correct number of iterations?
   def change_level(self, level: str):
       if level == "Easy":
          self.MCTS_iterations = 1000
       elif level == "Medium":
          self.MCTS_iterations = 5000
       elif level == "Hard":
          self.MCTS_iterations = 10000
       

