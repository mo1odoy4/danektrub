def is_unique(x):
    x = [(i, type(1)) for i in x]
    return len(x) == (set(x))

if __name__ == '__main__':
    print(is_unique(input()))
    
