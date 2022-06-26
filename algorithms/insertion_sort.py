"""Algorithm for Insertion Sort."""


def insertion_sort(shuffled):
    """Algorithm for Insertion Sort."""
    for i in range(1, len(shuffled)):
        key = shuffled[i]
        j = i - 1
        while j >= 0 and shuffled[j] > key:
            shuffled[j + 1] = shuffled[j]
            j = j - 1
        shuffled[j + 1] = key
