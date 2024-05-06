4 queen problem
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
        
    for i, j in zip(range(row, -1, -1),range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, 4, 1),range(col,-1,-1)):
        if board[i][j] == 1:
            return False
        
    return True

def solve_queens(board,col):
    if col >= 4:
        return True
    
    for i in range(4):
        if is_safe(board, i, col):
            board[i][col] = 1 

            if solve_queens(board,col + 1):
                return True
            
            board[i][col] = 0

    return False
    
def print_solution(board):
    for i in range(4):
        for j in range(4):
            print(board[i][j],end=" ")
        print()
    
board = [[0 for _ in range(4)] for _ in range(4)]

if solve_queens(board, 0):
    print("solution exists")
    print_solution(board)

else:
    print("Solution does not exist")

hangman game
import random 

word_list = ["python","java","programming"]

def choose_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = " "
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def is_word_completer(word,guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
        
    return True

def play_hangman():
    word = choose_word(word_list)
    guessed_letters=[]
    attempts_left = 4

    print("Welcome to hangman")
    print(display_word(word,guessed_letters))
    while attempts_left > 0:
        guess = input("Guess a letter : ").lower()

        if guess in guessed_letters:
            print("you have already guessed this letter")
        elif guess in word:
            guessed_letters.append(guess)
            print("Correct Guess")
            print(display_word(word,guessed_letters))
            if is_word_completer(word,guessed_letters):
                print("Congratulations")
                break

        else:
            guessed_letters.append(guess)
            attempts_left -= 1
            print(f"Incorrect guess! {attempts_left} attempts left")
            print(display_word(word,guessed_letters))
    
    if attempts_left == 0 :
        print(f"sorry you ran out of attempts. the word was {word}")

play_hangman()

tower of hanoi
def hanoi(n,source,target,aux):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1,source,aux,target)
    print(f"Move disk {n} from {source}to {target}")
    hanoi(n-1,aux,target,source)

n_disks = 3
source_peg= "A"
aux_peg="B"
target_peg="C"
print(f"Solving towers of hanoi with{n_disks}")
hanoi(n_disks,source_peg,target_peg,aux_peg)

water jug problem
from collections import deque

def fill_jug1(state):
    return (jug1_capacity, state[1])

def fill_jug2(state):
    return(state[0],jug2_capacity)

def empty_jug1(state):
    return(0,state[1])

def empty_jug2(state):
    return(state[0],0)

def pour_jug1_to_jug2(state):
    amount_to_pour = min(state[0], jug2_capacity - state[1])
    return(state[0] - amount_to_pour, state[1] + amount_to_pour)

def pour_jud2_to_jug1(state):
    amount_to_pour = min(state[1], jug1_capacity - state[0])
    return(state[0] + amount_to_pour, state[1] - amount_to_pour)

def bfs(initial_state,goal_state):
    visited = set()
    queue = deque([(initial_state,[])])
    while queue:
        state,path = queue.popleft()
        if state == goal_state:
            return path
        if state in visited:
            continue
        visited.add(state)
        for action_name, action_function in actions.items():
            next_state = action_function(state)
            if next_state not in visited:
                queue.append((next_state,path+[action_name]))
    return None
    
jug1_capacity = 4
jug2_capacity = 3

actions ={
    'fill_jug1' : fill_jug1,
    'fill_jug2' : fill_jug2,
    'empty_jug1' : empty_jug1,
    'empty_jug2' : empty_jug2,
    'pour_jug1_to_jug2' : pour_jug1_to_jug2,
    'pour_jug2_to_jug1' : pour_jud2_to_jug1
}

initial_state = (0,0)
goal_state = (2,0)

path = bfs(initial_state,goal_state)
if path:
    print("Solution found")
    for i,action in enumerate(path,1):
        print(f"Step {i}:{action}")
else: 
    print("No solution found")


tic tac toe
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5 )

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
        
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    
    if board[0][2] == board [1][1] == board [2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
        
    return True

def Game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, choose row (0,1,2) : "))
        col = int(input(f"Player {current_player}, choose col (0,1,2) : "))
        if board[row][col] != " ":
            print("The space is already taken")
            continue

        board[row][col] = current_player
        winner = check_winner(board)
        if winner: 
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        elif is_board_full(board):
            print_board(board)
            print("Its a tie")
            break

        current_player = "O" if current_player == "X" else "X"

Game()

breadth first search
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] 
queue = []
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end = " ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

print("Following is the breadth first search\n")
bfs(visited,graph,"5")

visited =set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited,graph,neighbor)

print("following is the depth first search")
dfs(visited,graph,"5")

celcius to farenheit
celcius_to_farenheit(Celcius, Farenheit) :- 
    Farenheit is (Celcius * 9/5) +32.

# fibonacci series
% Factorial predicate
factorial(0,1). % Base case: factorial of 0 is 1
factorial(N,F) :- 
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    F is N * F1.

% Fibonacci predicate
fibonacci(0,0). % Base case : Fibonacci of 0 is 0
fibonacci(1,1). % Base case : Fibonacci of 1 is 1
fibonacci(N, F) :-
    N > 1,
    N1 is N -1,
    N2 is N -2,
    fibonacci(N1, F1),
    fibonacci(N2, F2),
    F is F1 + F2


# define family relationships
%define family relationships
parent(alice,bob).
parent(alice,carol).
parent(carol,david).
parent(carol,eve).
parent(eve,frank).

male(bob).
male(david).
male(frank).
female(alice).
female(carol).
female(eve).

father(Father,child) :- parent(Father,child), male(Father).
mother(Mother,child) :- parent(Mother,child), female(Mother).
child(Child,Parent) :- parent(Parent,Child).
sibling(Sibling1,Sibling2) :- parent(Parent,Sibling1), parent(Parent,Sibling2), Sibling1 \= Sibling2.

father(bob,carol).
sibling(bob,carol).
mother(mother,david).


# bayesian network

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure of the Bayesian Network
model = BayesianNetwork([('Burglary', 'Alarm'), ('Earthquake', 'Alarm'), ('Alarm', 'Mary'), ('Alarm', 'John')])

# Define the conditional probability distributions (CPDs)
cpd_burglary = TabularCPD(variable='Burglary', variable_card=2, values=[[0.999], [0.001]])
cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2, values=[[0.998], [0.002]])
cpd_alarm = TabularCPD(variable='Alarm', variable_card=2, values=[[0.999, 0.71, 0.06, 0.05], [0.001, 0.29, 0.94, 0.95]],
                       evidence=['Burglary', 'Earthquake'], evidence_card=[2, 2])
cpd_mary = TabularCPD(variable='Mary', variable_card=2, values=[[0.95, 0.1], [0.05, 0.9]], evidence=['Alarm'], evidence_card=[2])
cpd_john = TabularCPD(variable='John', variable_card=2, values=[[0.9, 0.05], [0.1, 0.95]], evidence=['Alarm'], evidence_card=[2])

# Add CPDs to the model
model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_mary, cpd_john)

# Check if the model is valid
print("Model is valid:", model.check_model())

# Perform inference
inference = VariableElimination(model)

# Query for the probability of Burglary given Alarm and Mary heard the alarm
result = inference.query(variables=['Burglary'], evidence={'Alarm': 1, 'Mary': 1})
print("Probability of Burglary given Alarm and Mary heard the alarm:")
print(result)

# Query for the probability of Earthquake given John heard the alarm
result = inference.query(variables=['Earthquake'], evidence={'John': 1})
print("\nProbability of Earthquake given John heard the alarm:")
print(result)
