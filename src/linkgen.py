import random, string

def generate_random_symbols(l): 
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(l)])
