from fitness import *
from genetic_algo import *
from eval_network import *

df = open("gamedata.txt","a")

eval_model = simple_eval()
tourno_fitness = fitness

ga = genetic_algorithm()
agent,loss = ga.execute(tourno_fitness,eval_model,pop_size = 10,generations = 10)
df.write(agent.fitness+'\n')

board = chess.Board()

for move in agent.game:
    board.push_san(move)
df.write(board+'\n')
df.write(board.is_checkmate()+'\n')
df.write(agent.game+'\n')