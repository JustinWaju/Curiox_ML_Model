import random
#x-accelerometer, y-accelerometer, z-accelerometer, x-gyro, y-gyro, z-gyro
def generate_data(movement, count):
    data = []
    for _ in range(count):
        if movement == 'right-to-left-swing':
            values = [-round(random.uniform(3, 6), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2),
                      round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2)]
        elif movement == 'left-to-right-swing':
            values = [round(random.uniform(3, 6), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2),
                      round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2)]
        elif movement == 'down-to-up-swing':
            values = [round(random.uniform(1, 5), 2), round(random.uniform(3, 6), 2), round(random.uniform(1, 5), 2),
                      round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2)]
        elif movement == 'up-to-down-swing':
            values = [round(random.uniform(1, 5), 2), -round(random.uniform(3, 6), 2), round(random.uniform(1, 5), 2),
                      round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2)]
        elif movement == 'back-to-forth-swing':
            values = [round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), -round(random.uniform(3, 6), 2),
                      round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2)]
        elif movement == 'forth-to-back-swing':
            values = [round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), round(random.uniform(3, 6), 2),
                      round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2)]
        elif movement == 'lean-left':
            values = [round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2),
                      -round(random.uniform(3, 6), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2)]
        elif movement == 'lean-right':
            values = [round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2),
                      round(random.uniform(3, 6), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2)]
        elif movement == 'lean-up':
            values = [round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2),
                      round(random.uniform(1, 5), 2), round(random.uniform(3, 6), 2), round(random.uniform(1, 5), 2)]
        elif movement == 'lean-down':
            values = [round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2),
                      round(random.uniform(1, 5), 2), -round(random.uniform(3, 6), 2), round(random.uniform(1, 5), 2)]
        elif movement == 'lean-back':
            values = [round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2),
                      round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), -round(random.uniform(3, 6), 2)]
        elif movement == 'lean-forth':
            values = [round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2),
                      round(random.uniform(1, 5), 2), round(random.uniform(1, 5), 2), round(random.uniform(3, 6), 2)]

        values.append(movement)
        data.append(values)

    return data

# Set the number of lines for each movement
lines_per_movement = 2000 // 12

# Generate data for each movement
data = []
movements = ['right-to-left-swing', 'left-to-right-swing', 'down-to-up-swing', 'up-to-down-swing',
             'back-to-forth-swing', 'forth-to-back-swing', 'lean-left', 'lean-right',
             'lean-up', 'lean-down', 'lean-back', 'lean-forth']

for movement in movements:
    data.extend(generate_data(movement, lines_per_movement))

# Sort the generated data by movement
data.sort(key=lambda x: x[-1])

# Write data to a file (2000 entries)
with open('generated_data_sorted.txt', 'w') as file:
    for line in data:
        file.write(','.join(map(str, line)) + '\n')

# Write a subset of data to a verification file (500 entries)
verification_data = random.sample(data, 500)
verification_data.sort(key=lambda x: x[-1])

with open('generated_data_sorted_verification.txt', 'w') as file:
    for line in verification_data:
        file.write(','.join(map(str, line)) + '\n')

print("Data generation complete. Check 'generated_data_sorted.txt' and 'generated_data_sorted_verification.txt'")
