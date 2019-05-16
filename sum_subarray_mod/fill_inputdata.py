import random

MAX_SIZE = pow(10,5)
MIN_SIZE = 2
MAX_MOD = pow(10,14)
MIN_MOD = 1
MAX_ITEMS = pow(10,18)
MIN_ITEMS = 1

def generate_values():
    N=random.randint(MIN_SIZE, MAX_SIZE)
    M=random.randint(MIN_MOD, MAX_MOD)
    return (N,M)

def write_inputs(T):
    with open('inputs.txt', 'w') as f:
        for inputs in range(1, T+1):
            f.write('%d\n' %inputs)
            (n,m) = generate_values()
            f.write('%li %li\n' % (n, m) )
            for i in range(0, n):
                f.write('%li ' %random.randint(MIN_ITEMS, MAX_ITEMS))
            f.write('\n')
