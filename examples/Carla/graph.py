import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

import glob
        
def read_data(file_name):
    # Read the file
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Parse the data
    steer = [float(x) for x in lines[0].strip().split(':')[1].strip().strip('[]').split(',')]
    acceleration = [float(x) for x in lines[1].strip().split(':')[1].strip().strip('[]').split(',')]
    brake = [float(x) for x in lines[2].strip().split(':')[1].strip().strip('[]').split(',')]

    return steer, acceleration, brake

def interpolate_data(master_data, data):
    # Make sure the arrays are the same size
    if len(master_data) != len(data):
        # Interpolate the smaller array to the size of the larger one
        x = np.linspace(0, 1, len(data))
        f = interpolate.interp1d(x, data)
        xnew = np.linspace(0, 1, len(master_data))
        data = f(xnew)
    
    return master_data, data


# Read data from all files
master_steer, master_acceleration, master_brake = read_data('examples\\Carla\\Data\\master_t_5.txt')  # Master file

# Get all 'cog' and 'num' files
cog_files = sorted(glob.glob('output\\bb.txt'))
num_files = sorted(glob.glob('output\\aa.txt'))

# Make sure we have an equal number of 'cog' and 'num' files
assert len(cog_files) == len(num_files), "Mismatch in number of 'cog' and 'num' files"

# Iterate over pairs of 'cog' and 'num' files
for cog_file, num_file in zip(cog_files, num_files):
    with open(cog_file, 'r') as cog_f, open(num_file, 'r') as num_f:        
        steer2, acceleration2, brake2 = read_data(num_file)
        steer3, acceleration3, brake3 = read_data(cog_file)

        # Interpolate data to make them the same size
        master_steer, steer2 = interpolate_data(master_steer, steer2)
        master_steer, steer3 = interpolate_data(master_steer, steer3)

        master_acceleration, acceleration2 = interpolate_data(master_acceleration, acceleration2)
        master_acceleration, acceleration3 = interpolate_data(master_acceleration, acceleration3)

        master_brake, brake2 = interpolate_data(master_brake, brake2)
        master_brake, brake3 = interpolate_data(master_brake, brake3)

        # Plot the data
        plt.figure(figsize=(12, 8))

        plt.subplot(3, 1, 1)
        plt.plot(master_steer, label='Master Steer')
        plt.plot(steer2, label='Steer 2')
        plt.plot(steer3, label='Steer 3')
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(master_acceleration, label='Master Acceleration')
        plt.plot(acceleration2, label='Acceleration 2')
        plt.plot(acceleration3, label='Acceleration 3')
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(master_brake, label='Master Brake')
        plt.plot(brake2, label='Brake 2')
        plt.plot(brake3, label='Brake 3')
        plt.legend()

        plt.tight_layout()
        plt.show()

        # Calculate the Euclidean distances
        steer_distance2 = np.linalg.norm(np.array(master_steer) - np.array(steer2))
        steer_distance3 = np.linalg.norm(np.array(master_steer) - np.array(steer3))

        acceleration_distance2 = np.linalg.norm(np.array(master_acceleration) - np.array(acceleration2))
        acceleration_distance3 = np.linalg.norm(np.array(master_acceleration) - np.array(acceleration3))

        brake_distance2 = np.linalg.norm(np.array(master_brake) - np.array(brake2))
        brake_distance3 = np.linalg.norm(np.array(master_brake) - np.array(brake3))

        print(f"The Euclidean distance between the master steer data and steer data of file 2 is: {steer_distance2}")
        print(f"The Euclidean distance between the master steer data and steer data of file 3 is: {steer_distance3}")

        print(f"The Euclidean distance between the master acceleration data and acceleration data of file 2 is: {acceleration_distance2}")
        print(f"The Euclidean distance between the master acceleration data and acceleration data of file 3 is: {acceleration_distance3}")

        print(f"The Euclidean distance between the master brake data and brake data of file 2 is: {brake_distance2}")
        print(f"The Euclidean distance between the master brake data and brake data of file 3 is: {brake_distance3}")

        f = open("experiment_data.txt", "a")
        f.write(f"The Euclidean distance between the master steer data and steer data of file 2 is: {steer_distance2}\n")
        f.write(f"The Euclidean distance between the master steer data and steer data of file 3 is: {steer_distance3}\n")

        f.write(f"The Euclidean distance between the master acceleration data and acceleration data of file 2 is: {acceleration_distance2}\n")
        f.write(f"The Euclidean distance between the master acceleration data and acceleration data of file 3 is: {acceleration_distance3}\n")

        f.write(f"The Euclidean distance between the master brake data and brake data of file 2 is: {brake_distance2}\n")
        f.write(f"The Euclidean distance between the master brake data and brake data of file 3 is: {brake_distance3}\n")
        f.write(f"\n\n")
        f.close()
 