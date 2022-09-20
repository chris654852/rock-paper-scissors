#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

from mimetypes import init
import random


moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        m = input("Enter your choice [choose from rock, paper or scissors]: ")
        # if theres a typo, ask for another move
        if m == "quit":
            return m
        while m not in moves:
            print("Invalid input")
            m = input(
                "Enter your choice [choose from rock, paper or scissors]: ")

        return m


class RandomPlayer(Player):
    def move(self):
        randomNumber = random.randint(0, 2)
        return moves[randomNumber]


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()  # = self.score = 0
        self.lastMove = None

    def move(self):
        # if lastmove is none just do random move
        if self.lastMove is None:
            randomNumber = random.randint(0, 2)
            return moves[randomNumber]
        return self.lastMove

    def learn(self, my_move, their_move):
        self.lastMove = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.lastmove = None

    def move(self):
        # If it played 'rock' this round
        # it should play 'paper' in the next round.
        if self.lastmove is None:
            randomNumber = random.randint(0, 2)
            return moves[randomNumber]
        if self.lastmove == 'rock':
            return 'paper'
        if self.lastmove == 'paper':
            return 'scissors'
        if self.lastmove == 'scissors':
            return 'rock'

    def learn(self, my_move, their_move):
        # We are learning our moves
        self.lastmove = my_move


# class CyclePlayer:
#     def init


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2, max_rounds):
        self.p1 = p1
        self.p2 = p2
        self.max_rounds = max_rounds

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if "quit" in [move1, move2]:
            return "quit"
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2) is True:
            print("Player 1 won!")
            self.p1.score += 1
        elif beats(move2, move1) is True:
            print("Player 2 won!")
            self.p2.score += 1
        else:
            print("Tie")

        print(
            f"Player 1 score: {self.p1.score} | \
Player 2 score: {self.p2.score}")
        print()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        round = 1
        m = ""
        # for round in range(3) = 0,1,2
        while m != "quit" and round <= self.max_rounds:
            print(f"Round {round}:")
            m = self.play_round()
            round += 1
        print("Game over!")
        print(
            f"Player 1 score: {self.p1.score} | \
Player 2 score: {self.p2.score}")

        if self.p1.score > self.p2.score:
            print("Player 1 won!")
        elif self.p1.score == self.p2.score:
            print("It's a tie")
        elif self.p2.score > self.p1.score:
            print("Player 2 won!")

        # print("Player {...} won!")

    def KeepScore(self):
        beats()


if __name__ == '__main__':
    print()
    game = Game(CyclePlayer(), ReflectPlayer(), 5)
    game.play_game()
    print()
