#!/usr/bin/env python

choice_scores = { 'A': 1, 'B': 2, 'C': 3 }
decoded_moves = { 'X': 'A', 'Y': 'B', 'Z': 'C' }
outcomes = {
    ('A', 'B'): 0,
    ('A', 'C'): 6,
    ('B', 'A'): 6,
    ('B', 'C'): 0,
    ('C', 'A'): 0,
    ('C', 'B'): 6,
}

def score(opponent_move, encoded_move):
    move = decoded_moves[encoded_move]
    outcome_score = 3 if move == opponent_move else outcomes[(move, opponent_move)]
    return outcome_score + choice_scores[move]

moves = [tuple(l.split()) for l in open('data/q2.dat', 'r').readlines()]
print(sum(score(*m) for m in moves))
