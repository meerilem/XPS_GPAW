import matplotlib.pyplot as plt
import numpy as np

numberlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def readTheFile(filename):
	m, atomname = [], []
	# notatom=True
	with open(filename) as f:
		count = 0
		for line in f:
			count +=1
			if count > 1 and count%2 == 1:
				m.append(float(line[:-1]))
			elif count > 1 and count%2 == 0:
			    tmp = line.split()
			    atomname.append(tmp[0])
	return m, atomname
					
def gaussian(x, m, s):
  return np.exp(-np.power((x - m), 2.) / (2 * np.power(s, 2.)))

def getListOfAtoms(atom, m, atomname):
	m_atom, atomname_atom = [], []
	for i in range(len(atomname)):
	    if len(atom) == 1:
	        if atomname[i][0] == atom and atomname[i][1] in numberlist:
	            m_atom.append(m[i])
	            atomname_atom.append(atomname[i])
	    else:
	        if atomname[i][0:2] == atom:
	            m_atom.append(m[i])
	            atomname_atom.append(atomname[i])
	
	return m_atom, atomname_atom

def plotAtomSpectra(m, atomname, s):
	t = []
	w = np.linspace(min(m) - 3, max(m) + 3, 201)
	for i in range(len(m)):
	    y_pos = 1.1
	    for j in range(i):
	        if abs(m[i] - m[j]) < 0.3:
	            y_pos += 0.1	        
	for j in range(len(w)):
	  a = 0
	  for i in range(len(m)):
	    a += gaussian(w[j], m[i], s)
	  t.append(a)
	return w, t
	
def plotFinalSpectra(namelist, nr, lineW, dashes, ncolors, plt):
	w, t = [], []
	count = 0
	scale = 6.25
	for name in namelist:
		m, atomname = [], []
		m, atomname = readTheFile('./data/' + name + '/' + name + filename + '.out')
		m_tmp, atomname = getListOfAtoms(atom, m, atomname)
		m2 = [x+aliphatic-min(m_tmp) for x in m_tmp]
		w_tmp, t_tmp = plotAtomSpectra(m2, atomname , s)
		w.append(w_tmp)
		new_list = [x+nr[count]*scale for x in t_tmp]
		t.append(new_list)
		count += 1

	for i in range(len(namelist)):
		plt.plot(w[i], t[i], linewidth=lineW, c=ncolors[i], label=namelist[i], dashes=dashes)

########################################################

# Original palette
# ncolors = [ '#377eb8', 
# 			'#ff7f00', 
# 			'#4daf4a', 
# 			'#f781bf', 
# 			'#a65628', 
# 			'#984ea3', 
# 			'#999999', 
# 			'#e41a1c', 
# 			'#dede00']

# Colorblind-friendly palette
ncolors = [ '#aa0a3c',
			'#fa5078',
			'#8c0a82',
			'#f06ed2',
			'#005ac8',
			'#12c8fa',
			'#036732',
			'#02AD51']

black=['k'] * 8
grey=['#707070'] * 8

s = 0.5
atom = 'C'
anions = ['BCN4', 'TFSI', 'FSI','PF6', 'BF4', 'Cl', 'Br', 'I']

f, (ax0, ax1, ax2) = plt.subplots(1, 3, sharey=True, figsize=(17/2.54,10/2.54))

butane = 289.65
aliphatic = 285.0

cation = 'BMIm'
namelist1 = [cation + anion for anion in anions]
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
filename = ""
plotFinalSpectra(namelist1, numbers, 2.0, [1,0], ncolors, ax1)

nr = [1, 3, 4, 5, 6, 7]
namelist2 = []
for x in nr:
	namelist2.append(cation + anions[x])
filename = "_Villar"
plotFinalSpectra(namelist2, nr, 1.0, [4,1,4,1], black, ax1)

cation = 'Pyr14'
namelist1 = [cation + anion for anion in anions]
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
filename = ""
plotFinalSpectra(namelist1, numbers, 2.0, [1,0], ncolors, ax2)

nr = [1, 3, 7]
namelist2 = []
for x in nr:
	namelist2.append(cation + anions[x])
	
filename = "_Men"
plotFinalSpectra(namelist2, nr, 1.0, [4,1,4,1], black, ax2)

#* Plot from Figure 3 here

namelist1 = ['EMImBCN4', 'EMImTFSI', 'EMImFSI','EMImPF6', 'EMImBF4', 'EMImCl', 'EMImBr', 'EMImI']
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
filename = ""
plotFinalSpectra(namelist1, numbers, 2.0, [1,0], ncolors,ax0)
	
namelist2 = ['EMImTFSI','EMImPF6', 'EMImBF4', 'EMImCl', 'EMImBr', 'EMImI']
nr = [1, 3, 4, 5, 6, 7]
filename = "_Villar"
plotFinalSpectra(namelist2, nr, 1.0, [4,1,4,1], black,ax0)

namelist2 = ['EMImBCN4']
nr = [0]
filename = "_Kruusma"
plotFinalSpectra(namelist2, nr, 1.0, [4,1,1,1], black,ax0)

namelist2 = ['EMImBF4']
nr = [4]
filename ='_Tonisoo'
plotFinalSpectra(namelist2, nr, 1.0, [4,1,1,1], grey,ax0)

namelist2 = ['EMImBCN4', 'EMImTFSI', 'EMImBF4']
nr = [0, 1, 4]
filename = '_Kotz'
plotFinalSpectra(namelist2, nr, 1.0, [1,1], black,ax0)

namelist2 = ['EMImTFSI']
nr = [1]
filename = '_Hammer'
plotFinalSpectra(namelist2, nr, 1.0, [4,1,4,1,1,1], grey,ax0)

namelist2 = ['EMImTFSI']
nr = [1]
filename = '_Reinmoller'
plotFinalSpectra(namelist2, nr, 1.0, [4,1,4,1,1,1,1,1], black,ax0)


ax0.set_xlim(283.8,288.8)
ax0.set_xticks([284,285,286,287,288])
ax0.tick_params(axis='both', which='both', labelsize=7)

ax1.set_xlim(283.8,288.8)
ax1.set_xticks([284,285,286,287,288])
ax1.tick_params(axis='both', which='both', labelsize=7)

ax2.set_xlim(283.8,288.8)
ax2.set_xticks([284,285,286,287,288])
ax2.tick_params(axis='both', which='both', labelsize=7)

#ax0.set_xticks([284.5,285.5,286.5,287.5,288.5],minor=True)
#ax1.set_xticks([284.5,285.5,286.5,287.5,288.5],minor=True)
#ax2.set_xticks([284.5,285.5,286.5,287.5,288.5],minor=True)

#* Figure 3 done

#* Text legends
scale = 6.25
legends = [ [289.0,  0.00, r"B(CN)$_{4}^{-}$"],
			[289.0,  6.26, r"TFSI$^{-}$"],
			[289.0, 12.50, r"FSI$^{-}$"],
			[289.0, 18.74, r"PF$_{6}^{-}$"],
			[289.0, 24.98, r"BF$_{4}^{-}$"],
			[289.0, 31.22, r"Cl$^{-}$"],
			[289.0, 37.46, r"Br$^{-}$"],
			[289.0, 43.70, r"I$^{-}$"]]

for item in legends:
	ax2.text(*item, horizontalalignment='left', rotation=0, size=7, color='k')

# Extra space in string for padding to offset + sign
topnames = [r" EMIm$^{+}$",
			r" BMIm$^{+}$",
			r" BMPyr$^{+}$"]

# Hardcoded xlims, adjust if needed
ax0.text((283.8+288.8)/2,53.75,topnames[0],
			horizontalalignment='center', rotation=0, 
			size=7, color='k')

ax1.text((283.8+288.8)/2,53.75,topnames[1],
			horizontalalignment='center', rotation=0, 
			size=7, color='k')

ax2.text((283.8+288.8)/2,53.75,topnames[2],
			horizontalalignment='center', rotation=0, 
			size=7, color='k')

ax1.tick_params(axis='both', which='both', labelsize=7)
ax2.tick_params(axis='both', which='both', labelsize=7)
ax0.minorticks_on()
ax1.minorticks_on()
ax2.minorticks_on()
ax1.set_yticks([])
ax0.set_ylabel("intensity / arb. units",fontsize=8)
ax0.set_xlabel("binding energy / eV",fontsize=8)
ax1.set_xlabel("binding energy / eV",fontsize=8)
ax2.set_xlabel("binding energy / eV",fontsize=8)
#plt.tick_params(labelsize=16)
plt.tight_layout()
plt.subplots_adjust(wspace=0.05)
plt.savefig('./figures_for_article/figure3.png', format="png", dpi=600)
plt.savefig('./figures_for_article/figure3.svg', format="svg", dpi=600)
# plt.savefig('./figures_for_article/figure4_two_figures_stackedCations.eps', format="eps", dpi=2000, bbox_inches='tight')
#plt.savefig('./figures_for_article/figure_three_columns.png', format="png", dpi=300, bbox_inches='tight')