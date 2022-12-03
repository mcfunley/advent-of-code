#!/usr/bin/env python

choice_scores = { 'A': 1, 'B': 2, 'C': 3 }
decoded_outcomes = { 'X': 'lose', 'Y': 'draw', 'Z': 'win' }

outcomes = {
    ('A', 'B'): 0,
    ('A', 'C'): 6,
    ('B', 'A'): 6,
    ('B', 'C'): 0,
    ('C', 'A'): 0,
    ('C', 'B'): 6,
}

losing_moves = { 'A': 'C', 'B': 'A', 'C': 'B' }
winning_moves = { 'A': 'B', 'B': 'C', 'C': 'A' }

def score(opponent_move, move):
    outcome_score = 3 if move == opponent_move else outcomes[(move, opponent_move)]
    return outcome_score + choice_scores[move]

def get_move(opponent_move, encoded_outcome):
    outcome = decoded_outcomes[encoded_outcome]
    if outcome == 'draw':
        return opponent_move
    if outcome == 'win':
        return winning_moves[opponent_move]
    return losing_moves[opponent_move]

prescribed_outcomes = [tuple(l.split()) for l in open('data/q2.dat', 'r').readlines()]
print(sum(score(opponent_move, get_move(opponent_move, outcome))
          for opponent_move, outcome in prescribed_outcomes))
