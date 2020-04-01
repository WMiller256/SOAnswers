import matplotlib
matplotlib.use('pgf')
import matplotlib.pyplot as plt
from PyPDF2 import PdfFileMerger
import os

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rcParams['pgf.preamble'] = [r'\usepackage{hyperref} \hypersetup{hidelinks,'
							    'colorlinks=true, urlcolor=cyan}', ]

merger = PdfFileMerger()
for i in range(5):
	plt.figure()
	plt.text(0.5, 0.5, r'\href{https://stackoverflow.com/questions/}{StackOverflow '+str(i)+'}')

	out = './out.'+str(i)+'.pdf'
	plt.savefig(out)
	merger.append(out)
	os.remove(out)

merger.write('./out.pdf')
merger.close()
