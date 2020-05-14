# Question: https://stackoverflow.com/questions/61648477/
import matplotlib
from matplotlib import rcParams, rc, rcParamsDefault

# These are the "Tableau 20" colors as RGB.
tab20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
				 (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
				 (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
				 (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
				 (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(tab20)):
	r, g, b = tab20[i]
	tab20[i] = (r / 255., g / 255., b / 255.)

rcParams.update(rcParamsDefault)
rcParams['axes.prop_cycle'] = matplotlib.cycler(color=tab20)
rcParams['figure.figsize'] = 14, 9
rcParams['font.family'] = "Times New Roman"
rcParams['font.size'] = 16
rcParams['figure.dpi'] = 100
rcParams['savefig.dpi'] = 300
rcParams['figure.titlesize'] = 28
rcParams['legend.fontsize'] = 16
rcParams['ytick.labelsize'] = 14
rcParams['xtick.labelsize'] = 14
rcParams['axes.labelsize'] = 20
rcParams['lines.dash_capstyle'] = 'round'
#rcParams['lines.linestyle'] = 0.01,1.5
rcParams['lines.linewidth'] = 1
rcParams['axes.titlepad'] = 10.0
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'
#rcParams['xtick.minor.visible'] = True
#rcParams['ytick.minor.visible'] = True

pgf_with_latex = {
	"text.usetex": True,
	"pgf.rcfonts": False,
	"pgf.preamble": [
			r'\usepackage{color}'
			r'\usepackage{bm}'
		]
	}
matplotlib.rcParams.update(pgf_with_latex)

import numpy as np
import matplotlib.pyplot as plt
import math 

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
