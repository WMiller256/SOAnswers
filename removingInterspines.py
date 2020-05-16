# Question: https://stackoverflow.com/questions/61648477/
import numpy as np
import matplotlib.pyplot as plt
import math 

plt.style.use('miller')

ratios = [5, 5, 7]
lim = [[-0.3, 0.3], [-1, 1], [-12,4]]
labels = [['' if (e != (ratios[j] - 1) / 2) else 0 for e in range(ratios[j]-1)]+[lim[j][1]] for j in range(len(ratios))]
fig, axs = plt.subplots(3, 1, sharex=True, gridspec_kw={'height_ratios': ratios})
def initial(): 
    #obtain inital parameters
    dt = .04
    g = 9.8
    l = 9.8
    q = 0.5
    f_d = 1.2 #driving force
    frequency = 0.667 #frequency of driving force
    theta_start = 0.2
    omega_start = 0
    time_stop = 60
    return dt, g, l, q, frequency, theta_start, omega_start, time_stop

def rk_2(dt, g, l, q, frequency, theta_start, omega_start, time_stop): 
    forces = [0, 0.5, 1.2]

    for j in range(3):
        f_d = forces[j]
        theta = [] 
        omega = []
        time = [np.array([0])]
        theta = np.append(theta, theta_start)
        omega = np.append(omega, omega_start)
        i = 0
        while time[i] < time_stop:
            theta_prime = theta[i] + 0.5*omega[i]*dt
            omega_prime = omega[i] + 0.5*((-g/l)*math.sin(theta[i]) - q*omega[i] + 
                                          f_d*math.sin(frequency*time[i]))*dt
            time_prime = time[i] + 0.5*dt

            theta_new = theta[i] + omega_prime*dt
            omega_new = omega[i] + ((-g/l)*math.sin(theta_prime) - q*omega[i] + 
                                    f_d*math.sin(frequency*time_prime))*dt
            time_new = time[i] + dt

            theta = np.append(theta, theta_new)
            omega = np.append(omega, omega_new)
            time = np.append(time, time_new)
            i = i + 1
        axs[j].plot(time, theta)
        if j != 0: axs[j].spines['top'].set_visible(False)
        if j != 2: 
            axs[j].spines['bottom'].set_visible(False)
            axs[j].tick_params(bottom=False)
        axs[j].tick_params(axis='y', direction='in')
        axs[j].set_ylim(lim[j])
       	axs[j].set_yticks(np.linspace(lim[j][0], lim[j][1], ratios[j]))
       	axs[j].set_yticklabels(labels[j])
    plt.subplots_adjust(hspace=0)
    plt.figtext(0.08, 0.5, 'Angle [rad]', rotation = 90, ha='center', va='center')
    plt.xlabel('Time [s]')
    plt.savefig('./plot_without_interspines.png', bbox_inches='tight', dpi=300)
    plt.show()

    return theta, omega, time

def main():
    dt, g, l, q, frequency, theta_start, omega_start, time_stop = initial()
    theta, omega, time = rk_2(dt, g, l, q, frequency, theta_start, omega_start, time_stop)

main()
