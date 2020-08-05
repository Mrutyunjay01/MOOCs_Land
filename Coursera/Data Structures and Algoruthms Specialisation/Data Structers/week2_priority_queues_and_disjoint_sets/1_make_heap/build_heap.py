# python3
def parent(j):
    return int((j-1)/2)

def makeHeap(arr):
    swap_set = []
    
    for i in range(len(arr)-1, 0, -1):
        
        while arr[i] < arr[parent(i)]:
            swap_set.append((parent(i), i))
            arr[parent(i)], arr[i] = arr[i], arr[parent(i)]
            i = parent(i)

    return swap_set

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = makeHeap(data)
    
    print(len(swaps))
    if len(swaps):
        for i, j in swaps:
            print(i, j)

if __name__ == "__main__":
    main()
