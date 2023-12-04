
# find the calibration value in the jumbled 
def find_calibration_value(jumbled: str) -> int:
    numbers = [char for char in jumbled if char.isnumeric()]
    return int(numbers[0] + numbers[-1])



# open file and sum values
def main() -> None:
    with open("puzzle_input.txt", 'r') as f:
        total = sum((find_calibration_value(line) for line in f))
    print(f"The sum of all calibration values is: {total}")
        

# run main
if __name__ == "__main__":
    main()