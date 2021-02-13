import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    hello = ('Hello, {}!')
    return hello.format(name)
