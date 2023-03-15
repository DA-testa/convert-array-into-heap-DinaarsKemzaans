#Dinārs Kemzāns 221RDB321 17.grupa


def build_heap(info):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    option = str(input())
    if "I" in option:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
        return
    if "F" in option:
        file = str(input())
        file = "test/" + str(file)
        with open(file, 'r') as pakete:
            n = int(pakete.readLine())
            data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
        return   

if __name__ == "__main__":
    main()
