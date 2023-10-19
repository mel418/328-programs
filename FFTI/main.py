def max_subsequence_sum(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

def main(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            # Assuming the file contains a list of numbers enclosed in curly braces.
            nums = [int(x) for x in data.strip('{}').split(', ')]
            result = max_subsequence_sum(nums)
            print(f"Maximum subsequence sum of {filename}: {result}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    filename = "10.txt"  # Replace with the actual filename containing your numbers
    main(filename)
