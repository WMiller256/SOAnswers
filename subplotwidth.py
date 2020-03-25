import matplotlib.pyplot as plt
import numpy as np

KWS = dict(weight='bold', fontsize=14)

def plot_auto(mat, vec):
	fig, axes = plt.subplots(1, 2)
	plt.suptitle("AUTO", **KWS)
	axes[0].imshow(mat, aspect='auto')
	axes[1].imshow(vec, aspect='auto')
	plt.show()

def plot_equal(mat, vec, smallvec):
	fig, axes = plt.subplots(1, 2)
	plt.suptitle("EQUAL", **KWS)
	axes[0].imshow(mat, aspect='auto')
	axes[1].imshow(vec, aspect=(smallvec.shape[0] / smallvec.shape[1]) / (vec.shape[0] / vec.shape[1]))
	plt.savefig('./SubplotWidths.png', bbox_inches='tight', dpi=300)
	plt.show()

def plot_smallvec(smallvec):
	plt.imshow(smallvec)
	plt.title("SMALLVEC", **KWS)

np.random.seed(0)
mat = np.random.randn(500, 500)
vec = np.random.randn(500, 1)
smallvec = np.random.randn(25, 1)

plot_auto(mat, vec)
plot_equal(mat, vec, smallvec)
