
from puzzle1 import predict_next


def main():
    with open('puzzle_input.txt', 'r') as f:
        lines = [line.strip().split(' ') for line in f]
    readings = [[int(n) for n in line] for line in lines]
    total = sum([predict_next(reading, 'backwards') for reading in readings])
    print('The sum of all predicted values is:', total)





if __name__ == "__main__":
    main()