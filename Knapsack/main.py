import re

# Open and read the input file
with open('10.txt', 'r') as file:
    input_text = file.read()

# Extract the values using regular expressions
values = re.findall(r'\d+', input_text)

# Parse the values
max_weight = int(values[0])
bricks = [(int(values[i]), int(values[i + 1]), int(values[i + 2])) for i in range(1, len(values), 3)]

print(f"Maximum Allowable Weight: {max_weight}")
print("Bricks:")
for brick in bricks:
    print(brick)

# Function to calculate the maximum total potential profit
def max_profit(weights, values, max_weight):
    n = len(weights)
    dp = [0] * (max_weight + 1)

    for i in range(n):
        for w in range(max_weight, 0, -1):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[max_weight]

weights = [brick[1] for brick in bricks]
values = [brick[0] for brick in bricks]

max_profit = max_profit(weights, values, max_weight)

print(f"Maximum Total Potential Profit: {max_profit}")
