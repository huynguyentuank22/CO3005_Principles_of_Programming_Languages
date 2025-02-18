def flatten(lst):
    return [item for sublist in lst for item in sublist]

print(flatten([[1,2,3],[4,5],[6,7]])) # Expected output: [1, 2, 3, 4, 5, 6, 7]