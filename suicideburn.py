import gym
from time import sleep
from gym import wrappers
env = gym.make('LunarLander-v2')
env = wrappers.Monitor(env, './')
env.seed(0)

g = 1.0
delta_t = 1.0/50.0
action = 0

state = env.reset()

y0 = state[1]
v0 = 0
cut_off = 0.01

for t in range(3000):
	env.render()
	state, reward, done, _  = env.step(action)
	y = state[1]
	v = (y - y0)/delta_t
	if done or y < 0 or v == 0.001:
	    break

	alt_burn = (y*g+0.5*v*v)/(13.0 / env.lander.mass * 0.5)

	v0 = v
	y0 = y
	if y < alt_burn and y > cut_off:
		action = 2
	else:
		action = 0

	sleep(1.0/50.0)	
