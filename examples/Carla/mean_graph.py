import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
df = pd.read_csv('experiment_data.csv')

# Define a function to filter distances based on the full text
def filter_distances(column_text):
    filtered_df = df[df['Column1'] == column_text]
    return filtered_df['Column2'].astype(float).tolist()  # Convert the distance values to float for plotting

# Get the distances using specific text filters
steer2_distance = filter_distances('The Euclidean distance between the master steer data and steer data of file 2 is')
steer3_distance = filter_distances('The Euclidean distance between the master steer data and steer data of file 3 is')
acceleration2_distance = filter_distances('The Euclidean distance between the master acceleration data and acceleration data of file 2 is')
acceleration3_distance = filter_distances('The Euclidean distance between the master acceleration data and acceleration data of file 3 is')
brake2_distance = filter_distances('The Euclidean distance between the master brake data and brake data of file 2 is')
brake3_distance = filter_distances('The Euclidean distance between the master brake data and brake data of file 3 is')

# Create an x-axis array that matches the length of your data arrays
x_values = range(len(steer2_distance))

# Calculate the deviations
steer_deviation = [abs(a - b) for a, b in zip(steer3_distance, steer2_distance)]
acceleration_deviation = [abs(a - b) for a, b in zip(acceleration3_distance, acceleration2_distance)]
brake_deviation = [abs(a - b) for a, b in zip(brake3_distance, brake2_distance)]

# Calculate average deviations
avg_steer_deviation = sum(steer_deviation) / len(steer_deviation)
avg_acceleration_deviation = sum(acceleration_deviation) / len(acceleration_deviation)
avg_brake_deviation = sum(brake_deviation) / len(brake_deviation)

print(f'Average Steer Deviation: {avg_steer_deviation}')
print(f'Average Acceleration Deviation: {avg_acceleration_deviation}')
print(f'Average Brake Deviation: {avg_brake_deviation}')

# Plot for steer data
plt.figure(figsize=(20, 15))
plt.subplot(131)
plt.plot(x_values, steer2_distance, label='master to numerical nav', marker='o', color='#ff7f0e')
plt.plot(x_values, steer3_distance, label='master to cognitive nav', marker='o', color='#2ca02c')
plt.title(f'Steer Data Euclidean Distances\nAverage Deviation: {avg_steer_deviation:.2f}')
plt.ylabel('Distance')
plt.xlabel('Experiment Index')
plt.legend()

# Plot for acceleration data
plt.subplot(132)
plt.plot(x_values, acceleration2_distance, label='master to numerical nav', marker='o', color='#ff7f0e')
plt.plot(x_values, acceleration3_distance, label='master to cognitive nav', marker='o', color='#2ca02c')
plt.title(f'Acceleration Data Euclidean Distances\nAverage Deviation: {avg_acceleration_deviation:.2f}')
plt.ylabel('Distance')
plt.xlabel('Experiment Index')
plt.legend()

# Plot for brake data
plt.subplot(133)
plt.plot(x_values, brake2_distance, label='master to numerical nav', marker='o', color='#ff7f0e')
plt.plot(x_values, brake3_distance, label='master to cognitive nav', marker='o', color='#2ca02c')
plt.title(f'Brake Data Euclidean Distances\nAverage Deviation: {avg_brake_deviation:.2f}')
plt.ylabel('Distance')
plt.xlabel('Experiment Index')
plt.legend()

plt.tight_layout()
plt.show()
