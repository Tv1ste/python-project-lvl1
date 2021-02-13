#!/usr/bin/env python
from brain_games.cli import welcome_user


def greeting(welcome):
    print(welcome)


def main():
    greeting('Welcome to the Brain Games!')
    greeting(welcome_user())


if __name__ == '__main__':
    main()
