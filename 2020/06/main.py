if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        lines = f.readlines()
        entries = [[]]
        i = 0
        for line in lines:
            x = line.strip()
            if not x:
                entries.append([])
                i += 1
            else:
                entries[i].append(x)
        print(entries)
