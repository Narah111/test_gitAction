from dev import hello


def check(text):
    if isinstance(text, str):
        print("nice work!")
    else:
        print("try again!")


check(hello())