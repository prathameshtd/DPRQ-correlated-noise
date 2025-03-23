import numpy as np
import corr_matrix
import cascade
import time
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal 
from scipy.stats import linregress
from matplotlib.ticker import MaxNLocator


def generate_gaussian_vector(C, k):
    mean_vector = np.zeros(2**k)  # Zero mean for the Gaussian vector
    gaussian_vector = multivariate_normal(mean_vector, C)
    return gaussian_vector

# here we use scipy's internal function to generate gaussian noises
k_values = range(2, 16)
average_speeds = []

for k in k_values:
    C_k =  corr_matrix.construct_matrix_C_k(k)
    run_times = []
    print(time.time())
    print(k)
    for _ in range(2):
        start_time = time.time()
        tree = generate_gaussian_vector(C_k, k)
        this_time = time.time() - start_time
        run_times.append(this_time)
    average_speeds.append(np.mean(run_times))





# now we implement the cascade sampling to a range of k and test the speed
k_values_td = range(2, 26)
average_speeds_td = []

for k in k_values_td:
    run_times = []
    print(k)
    for _ in range(10):
        start_time = time.time()
        tree = cascade.create_tree(k)
        run_times.append(time.time() - start_time)
    average_speeds_td.append(np.mean(run_times))

# Now that we have the average speeds for both methods, let's plot them on a line chart

plt.figure(figsize=(18, 6))  # Adjust the figure size as needed

# Create the first subplot (1 row, 2 columns, first subplot)
plt.subplot(1, 2, 1)
# Add plotting commands for the first plot
# For example: plt.plot(x1, y1)
plt.plot(np.power(2, k_values_td[1:]), average_speeds_td[1:], marker='o', linestyle='-')
plt.title('Speed of Gaussian generation',fontsize=20)
plt.xlabel('Number of leaf nodes',fontsize=16)
plt.ylabel('Time (seconds)',fontsize=16)
plt.grid(True)
plt.annotate('', xy=(100000, 10), xytext=(8000000, 190),
             arrowprops=dict(facecolor='black', shrink=0.01))

# We customize the x-axis to show the labels as 2^k
plt.xticks(np.power(2, k_values_td[18:]), [r'$2^{{{}}}$'.format(k) for k in k_values_td[18:]])
a = plt.axes([.16, .56, .15, .3], facecolor='y')
plt.scatter(k_values_td[1:13], average_speeds_td[1:13], marker='o', s = 20, label = 'Cascade sampling')
plt.scatter(k_values[1:], average_speeds[1:], marker='x', s = 20, label = 'scipy gaussian', color = 'red')
plt.legend(loc = 'upper left',fontsize=12)
plt.xlabel('Tree Depth (k)',fontsize=12)
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

# Create the second subplot (1 row, 2 columns, second subplot)
plt.subplot(1, 2, 2)
# Add plotting commands for the second plot
# For example: plt.plot(x2, y2)

slope1, intercept1, r_value1, p_value1, std_err1 = linregress(k_values_td[1:], np.log2(average_speeds_td[1:]))
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(k_values[1:], np.log2(average_speeds[1:]),)

plt.scatter(k_values_td[1:], np.log2(average_speeds_td[1:]), marker='o', label = 'Cascade sampling')
plt.scatter(k_values[1:], np.log2(average_speeds[1:]), marker='x', label = 'scipy gaussian', color = 'red')
plt.plot(k_values_td[1:], k_values_td[1:] * slope1 + intercept1)
plt.text(max(k_values_td[1:]) - 4, max(np.log2(average_speeds_td[1:])) - 8, f'Slope: {slope1:.2f}', fontsize=16, verticalalignment='bottom')

plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))




plt.title('log-log plot: speed of Gaussian generation',fontsize=20)
plt.xlabel(r'Tree Depth = $log_2$(Number of leaf nodes)',fontsize=16)
plt.ylabel( r'$log_2$(Time) (seconds)',fontsize=16)
plt.legend(fontsize=16)

plt.grid(True)

# Display the plots
plt.show()

