# Question: https://stackoverflow.com/questions/61278228/
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

col_names = ["this", "that","the other","4","5","6"]
data = np.random.randint(100, size=(40,6)).astype('str')

fig, ax = plt.subplots(1, figsize=(10,10))
ax.axis('off')
_table = plt.table(cellText=data, colLabels=col_names, loc='center', edges='open', colLoc='right')

pdf = PdfPages('test.pdf')
pdf.savefig(fig)
plt.savefig('./PDFTableCentering.png', bbox_inches='tight', dpi=400)
pdf.close()
