# importing modules-> you can make your own one and can import from standard library

print('imported my_module ...')

test = ' test string'


def find_index(to_search, target):
 # finds the indexd of a valuein a sequence
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
