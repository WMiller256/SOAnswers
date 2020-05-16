import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.style.use('miller')

ylabel = plt.ylabel("Y Label")
plt.xlabel("X Label")
ylabel.set_family("DejaVu Serif")

legend = plt.legend(handles = [mpatches.Patch(color='grey', label="Label")])
plt.setp(legend.texts, family="EB Garamond")

plt.savefig("./LabelFonts.png", bbox_inches="tight", dpi=300)
plt.show()
