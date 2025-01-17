import random

alphabet = ['A','T','C','G']
swap_A = ['T','C','G']
swap_T = ['A', 'C','G']
swap_C = ['A','T','G']
swap_G = ['A','T','C']

def gen_string(n):
    string = []
    for i in range(n):
        string += [random.choice(alphabet)]
    return string

def swap(x):
    options = None
    if x == 'A':
        options = swap_A
    if x == 'T':
        options = swap_T
    if x == 'C':
        options = swap_C
    if x == 'G':
        options = swap_G
    return random.choice(options)
        
def permute_string(V_in, percentage):
    V = V_in.copy()
    num_indices = int(len(V) * percentage)
    indices = random.sample(range(0, len(V)), num_indices)
    for idx in indices:
        V[idx] = swap(V[idx])
    return V

def get_subset(V_in, percentage):
    V = V_in.copy()
    num_indices = int(len(V) * percentage)
    indices = random.sample(range(0, len(V)), num_indices)
    V_out = [V[i] for i in indices]
    return V_out

V_10 = gen_string(10)
V_100 = gen_string(100)
V_1000 = gen_string(1000)

V_10_P = permute_string(V_10, .2)
V_100_P = permute_string(V_100, .2)
V_1000_P = permute_string(V_1000, .2)

U_8 = get_subset(V_10, .8)
U_80 = get_subset(V_100, .8)
U_800 = get_subset(V_1000, .8)

U_8_P = permute_string(U_8, .2)
U_80_P = permute_string(U_80, .2)
U_800_P = permute_string(U_800, .2)


V_100 = ''.join(V_100)
V_1000 = ''.join(V_1000)
V_10_P = ''.join(V_10_P)
V_100_P = ''.join(V_100_P)
V_1000_P = ''.join(V_1000_P)
V_80 = ''.join(U_80)
V_800 = ''.join(U_800)
V_8_P = ''.join(U_8_P)
V_80_P = ''.join(U_80_P)
V_800_P = ''.join(U_800_P)

V_10000 = gen_string(10000)
V_10000_P = permute_string(V_10000, .2)
V_8000 = get_subset(V_10000, .8)
V_8000_P = permute_string(V_8000, .2)
V_10000 = ''.join(V_10000)
V_10000_P = ''.join(V_10000_P)
V_8000 = ''.join(V_8000)
V_8000_P = ''.join(V_8000_P)