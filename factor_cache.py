import json
import os.path

def memoize(func):
    if os.path.isfile('cached_facs.json'):
        with open('cached_facs.json','r+') as infile:
            cached_facs = json.load(infile)
    else:
        cached_facs = {}
    def checker(int_array_input):
        int_array_input.sort()
        if str(tuple(int_array_input)) in cached_facs:
            print('Found it')
            out_dict = cached_facs[str(tuple(int_array_input))]
            #turn the string keys into int keys for more intuitive print()
            out_dict = {int(key) : out_dict[key] for key in out_dict}
        else:
            out_dict = func(int_array_input)
            cached_facs.update({str(tuple(int_array_input)) : out_dict})
            with open('cached_facs.json', 'w+') as outfile:
                json.dump(cached_facs, outfile, indent = 4)
        return out_dict
    return checker

@memoize
def factor_cache(int_array_input):

    if len(int_array_input) == 0:
        return None
    '''
    this is the naive implementation that takes a sorted int_array
    from memoize (O(n log n)) time, and then takes on average 1/4 n^2
    time to find all the factors because it might recalculate them
    '''
    out_dict = {key : [] for key in int_array_input}

    for x in range(0, len(int_array_input)):
        out_dict[str(int_array_input[x])] = []
        y = 0
        while int_array_input[y] * 2 <= int_array_input[x]:
            if int_array_input[x] % int_array_input[y] == 0:
                out_dict[str(int_array_input[x])].append(int_array_input[y])
                #the following reverses the functionality
                #out_dict[str(int_array_input[y])].append(int_array_input[x]) 
            y += 1
            
    return out_dict

def main():

    A = [10, 2, 5, 20]
    B = [10, 2, 20, 5]
    C = [10, 5, 2, 20]
    D = [1,4,8,10]

    print(factor_cache(A))
    print(factor_cache(B))
    print(factor_cache(C))
    print(factor_cache(D))

if __name__ == '__main__':
    main()
