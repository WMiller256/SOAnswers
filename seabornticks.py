import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_json(
'{"contract":{"0":"cu2003","1":"cu2003","2":"cu2003","3":"cu2003","4":"cu2003","5":"cu2003","6":"cu2003","7":"cu2003","8":"cu2004","9":"cu2004","10":"cu2004","11":"cu2004","12":"cu2004","13":"cu2004","14":"cu2004","15":"cu2004","16":"cu2005","17":"cu2005","18":"cu2005","19":"cu2005","20":"cu2005","21":"cu2005","22":"cu2005","23":"cu2005","24":"cu2006","25":"cu2006","26":"cu2006","27":"cu2006","28":"cu2006","29":"cu2006","30":"cu2006","31":"cu2006","32":"cu2007","33":"cu2007","34":"cu2007","35":"cu2007","36":"cu2007","37":"cu2007","38":"cu2007","39":"cu2007","40":"cu2008","41":"cu2008","42":"cu2008","43":"cu2008","44":"cu2008","45":"cu2008","46":"cu2008","47":"cu2008","48":"cu2009","49":"cu2009","50":"cu2009","51":"cu2009","52":"cu2009","53":"cu2009","54":"cu2009","55":"cu2009","56":"cu2010","57":"cu2010","58":"cu2010","59":"cu2010","60":"cu2010","61":"cu2010","62":"cu2010","63":"cu2010","64":"cu2011","65":"cu2011","66":"cu2011","67":"cu2011","68":"cu2011","69":"cu2011","70":"cu2011","71":"cu2011","72":"cu2012","73":"cu2012","74":"cu2012","75":"cu2012","76":"cu2012","77":"cu2012","78":"cu2012","79":"cu2012","80":"cu2101","81":"cu2101","82":"cu2101","83":"cu2101","84":"cu2101","85":"cu2101","86":"cu2101","87":"cu2101","88":"cu2102","89":"cu2102","90":"cu2102","91":"cu2102","92":"cu2102","93":"cu2102","94":"cu2102","95":"cu2102"},"time_interval_between_concsecutive_transactions_bucket":{"0":"less than 1s","1":"between 1s and 2s","2":"between 2s and 3s","3":"between 3s and 4s","4":"between 4s than 8s","5":"between 8s and 60s","6":"between 60s and 120s","7":"more than 120s","8":"less than 1s","9":"between 1s and 2s","10":"between 2s and 3s","11":"between 3s and 4s","12":"between 4s than 8s","13":"between 8s and 60s","14":"between 60s and 120s","15":"more than 120s","16":"less than 1s","17":"between 1s and 2s","18":"between 2s and 3s","19":"between 3s and 4s","20":"between 4s than 8s","21":"between 8s and 60s","22":"between 60s and 120s","23":"more than 120s","24":"less than 1s","25":"between 1s and 2s","26":"between 2s and 3s","27":"between 3s and 4s","28":"between 4s than 8s","29":"between 8s and 60s","30":"between 60s and 120s","31":"more than 120s","32":"less than 1s","33":"between 1s and 2s","34":"between 2s and 3s","35":"between 3s and 4s","36":"between 4s than 8s","37":"between 8s and 60s","38":"between 60s and 120s","39":"more than 120s","40":"less than 1s","41":"between 1s and 2s","42":"between 2s and 3s","43":"between 3s and 4s","44":"between 4s than 8s","45":"between 8s and 60s","46":"between 60s and 120s","47":"more than 120s","48":"less than 1s","49":"between 1s and 2s","50":"between 2s and 3s","51":"between 3s and 4s","52":"between 4s than 8s","53":"between 8s and 60s","54":"between 60s and 120s","55":"more than 120s","56":"less than 1s","57":"between 1s and 2s","58":"between 2s and 3s","59":"between 3s and 4s","60":"between 4s than 8s","61":"between 8s and 60s","62":"between 60s and 120s","63":"more than 120s","64":"less than 1s","65":"between 1s and 2s","66":"between 2s and 3s","67":"between 3s and 4s","68":"between 4s than 8s","69":"between 8s and 60s","70":"between 60s and 120s","71":"more than 120s","72":"less than 1s","73":"between 1s and 2s","74":"between 2s and 3s","75":"between 3s and 4s","76":"between 4s than 8s","77":"between 8s and 60s","78":"between 60s and 120s","79":"more than 120s","80":"less than 1s","81":"between 1s and 2s","82":"between 2s and 3s","83":"between 3s and 4s","84":"between 4s than 8s","85":"between 8s and 60s","86":"between 60s and 120s","87":"more than 120s","88":"less than 1s","89":"between 1s and 2s","90":"between 2s and 3s","91":"between 3s and 4s","92":"between 4s than 8s","93":"between 8s and 60s","94":"between 60s and 120s","95":"more than 120s"},"counts":{"0":58309,"1":11996,"2":5821,"3":3437,"4":5045,"5":1705,"6":3,"7":26,"8":107450,"9":17426,"10":6022,"11":2680,"12":2508,"13":383,"14":3,"15":26,"16":84459,"17":15043,"18":6176,"19":3007,"20":3780,"21":935,"22":4,"23":26,"24":62479,"25":12210,"26":5252,"27":3038,"28":4588,"29":1845,"30":4,"31":26,"32":41701,"33":8244,"34":4068,"35":2493,"36":4423,"37":3044,"38":6,"39":26,"40":22636,"41":4583,"42":2301,"43":1604,"44":3543,"45":4071,"46":31,"47":28,"48":19049,"49":3566,"50":2146,"51":1323,"52":2925,"53":3573,"54":147,"55":46,"56":21468,"57":3121,"58":2001,"59":1175,"60":2399,"61":3344,"62":151,"63":59,"64":24253,"65":3310,"66":2034,"67":1176,"68":2423,"69":3211,"70":170,"71":57,"72":22188,"73":3055,"74":1940,"75":1110,"76":2346,"77":3252,"78":182,"79":63,"80":25472,"81":2930,"82":1730,"83":1025,"84":2099,"85":3240,"86":191,"87":52,"88":32094,"89":2471,"90":1621,"91":807,"92":1589,"93":2231,"94":263,"95":124},"contract_code":{"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":1,"9":1,"10":1,"11":1,"12":1,"13":1,"14":1,"15":1,"16":2,"17":2,"18":2,"19":2,"20":2,"21":2,"22":2,"23":2,"24":3,"25":3,"26":3,"27":3,"28":3,"29":3,"30":3,"31":3,"32":4,"33":4,"34":4,"35":4,"36":4,"37":4,"38":4,"39":4,"40":5,"41":5,"42":5,"43":5,"44":5,"45":5,"46":5,"47":5,"48":6,"49":6,"50":6,"51":6,"52":6,"53":6,"54":6,"55":6,"56":7,"57":7,"58":7,"59":7,"60":7,"61":7,"62":7,"63":7,"64":8,"65":8,"66":8,"67":8,"68":8,"69":8,"70":8,"71":8,"72":9,"73":9,"74":9,"75":9,"76":9,"77":9,"78":9,"79":9,"80":10,"81":10,"82":10,"83":10,"84":10,"85":10,"86":10,"87":10,"88":11,"89":11,"90":11,"91":11,"92":11,"93":11,"94":11,"95":11}}'
)
fig, axs = plt.subplots(3, 4, figsize = (15,8), sharex = True)

fig.subplots_adjust(hspace=0.5, wspace=.5, bottom=0.2)

props = {'rotation' : 45, 'ha' : 'right'}

for i in range(3):

	for j in range(4):

		contract_code = i + j

		contract = df.query('contract_code == @contract_code').contract.unique()[0]

		sns.barplot(x = 'time_interval_between_concsecutive_transactions_bucket', y = 'counts', 
					data = df.query('contract_code == @contract_code'), ax = axs[i, j])
		axs[i,j].set_title(f'Contract: {contract}')
		axs[i,j].set_xlabel('')
		plt.setp(axs[i,j].get_xticklabels(), **props)

plt.figtext(0.02, 0.5, 'Time interval between consecutive transactions', 
		    rotation = 'vertical', size = 20, va='center')
plt.figtext(0.5, 0, 'Number of Transactions', size = 20, ha='center')
plt.savefig('./SeabornTicklabels.png', dpi=300)
plt.show()
