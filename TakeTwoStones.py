stones = int(input())

def winner(stones):
    if stones % 2 == 0:
        print('Bob')
    else:
        print('Alice')

winner(stones)
