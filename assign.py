# Question 1
def convert_to_indian_currency_notation(number):
    # Convert the number to a string
    num_str = str(number)

    # Determine the position to insert commas
    length = len(num_str)
    comma_positions = [i for i in range(length - 1, 0, -2)]

    # Insert commas at appropriate positions
    for position in comma_positions:
        num_str = num_str[:position] + ',' + num_str[position:]

    return num_str

# Example usage:
input_number = 504678
output_currency_notation = convert_to_indian_currency_notation(input_number)
print("Input:", input_number)
print("Output:", output_currency_notation)

#question2
S = int(input())
res = []

for _ in range(T):
    count = 0
    n, m = list(map(int, input().split()))
    heights = list(map(int, input().split()))

    for h in heights:
        if h > m:
            count += 1

    res.append(count)

# Print the results as integers
for result in res:
    print(result)
