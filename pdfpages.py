import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

pdf = PdfPages('out.pdf')
for i in range(5):
	fig, ax = plt.subplots(figsize=(20, 10))
	plt.plot(np.random.random(10), linestyle=None, marker='.')
	pdf.savefig(fig)

pdf.close()
