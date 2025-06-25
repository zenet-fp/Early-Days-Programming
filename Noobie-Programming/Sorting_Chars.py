unordered = ["b","c","g","a","i","k"]
ordered = ["a", "b", "c", "g", "i", "k"]

def main():
    for x in range(len(unordered) - 1):
        c = False
        while True:
            if unordered[x] != ordered[x]:
                unordered[x], unordered[x + 1] = unordered[x + 1], unordered[x]
                unordered[x], unordered[-x] = ordered[x], ordered[-x]
            if not c:
                print(unordered)
                break
              
if __name__ == '__main__':
    main()
