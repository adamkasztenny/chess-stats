import pgn
import glob

pgn_text = ''
print('Opening pgn files')

# the example on https://github.com/renatopp/pgnparser for large pgn files did not work
# as a result, this is pretty slow (even with only 1 1mb pgn file)

# thanks to http://stackoverflow.com/questions/5013532/open-file-by-filename-wildcard
path = "data/*.pgn"
for filename in glob.glob(path):
        with open(filename, 'r') as f:
            pgn_text += f.read()

pgn_games = pgn.PGNGame()
games = pgn.loads(pgn_text)
number_of_games = len(games)

print(str(number_of_games) + " number of games loaded.\n")

results = map(lambda x: x.result, games)
print(results)

def win_rate(result): return len(filter(lambda x: x == result, results)) / number_of_games

white_wins = win_rate('1-0')
black_wins = win_rate('0-1')
draws = win_rate('1/2-1/2')

print("White wins " + str(white_wins) + "%")
print("Black wins " + str(black_wins) + "%")
print("Draws " + str(draws) + "%")
