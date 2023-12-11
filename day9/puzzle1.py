

# find the next number in the sequence recursively 
def predict_next(reading, direction, depth=0):
    if all([num == 0 for num in reading]): return reading
    length = len(reading)
    diff = [reading[i+1] - reading[i] for i in range(length-1)]
    result = predict_next(diff, direction, depth+1)
    if direction == 'backwards': reading.insert(0, reading[0] - result[0])
    elif direction == 'forwards': reading.append(reading[-1] + result[-1])
    else: raise ValueError(f"Direction muust be 'forwards' or 'backwards', not '{direction}'")
    if depth > 0: return reading
    else: return reading[-1] if direction == 'forwards' else reading[0]


def main():
    with open('puzzle_input.txt', 'r') as f:
        lines = [line.strip().split(' ') for line in f]
    readings = [[int(n) for n in line] for line in lines]
    total = sum([predict_next(reading, 'forwards') for reading in readings])
    print('The sum of all predicted values is:', total)





if __name__ == "__main__":
    main()