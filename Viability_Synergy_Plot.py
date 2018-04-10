'''
=========================
Viability synergy plot
by
Yunkai Zhang
=========================
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from mpl_toolkits.mplot3d import Axes3D

#Parameters
Drug_X = 'Osimertinib'
Drug_Y = 'Erdafitinib'
Data_File = 'test.xlsx'
colormap = 'BuGn'

#import data
df_Zr = pd.read_excel(Data_File, sheet_name = 'Zr', header = None)
df_X = pd.read_excel(Data_File, sheet_name = 'X', header = None)
df_Y = pd.read_excel(Data_File, sheet_name = 'Y', header = None)
df_Zp = pd.read_excel(Data_File, sheet_name = 'Z_p', header = None)
df_Zp_min = pd.read_excel(Data_File, sheet_name = 'Z_p_min', header = None)

plt.figure(figsize=(10,6))

#Add 3D subplot as first subplot
ax = plt.subplot2grid((2,3), (0,0), colspan=2, rowspan=2, projection='3d')
ax.w_xaxis.set_pane_color((1, 1, 1, 1))
ax.w_yaxis.set_pane_color((1, 1, 1, 1))
ax.w_zaxis.set_pane_color((1, 1, 1, 1))

#Plot scatter and wireframe
ax.scatter(df_X, df_Y, df_Zr, color='k')
ax.plot_wireframe(df_X, df_Y, df_Zp, color='#00b786')

#Plot indicator, red if scatter < wireframe, blue if scatter > wireframe
for a in range(0,df_Zr.shape[0]):
	for b in range(0,df_Zr.shape[1]):
		if df_Zp.iloc[a,b] > df_Zr.iloc[a,b]:
			ax.plot([df_X.iloc[a,b], df_X.iloc[a,b]],[df_Y.iloc[a,b], df_Y.iloc[a,b]],[df_Zp.iloc[a,b], df_Zr.iloc[a,b]], color='#ff4242')
		if df_Zp.iloc[a,b] < df_Zr.iloc[a,b]:
			ax.plot([df_X.iloc[a,b], df_X.iloc[a,b]],[df_Y.iloc[a,b], df_Y.iloc[a,b]],[df_Zp.iloc[a,b], df_Zr.iloc[a,b]], color='#545cff')

#Format 3D plot
ax.set_xlabel(Drug_X + ' (μM)')
ax.set_ylabel(Drug_Y + ' (μM)')
ax.set_zlabel('Viability')
zticks = mtick.FormatStrFormatter('%d%% ')
ax.zaxis.set_major_formatter(zticks)
ax.set_zlim(bottom = 0)
ax.view_init(40, 45)
ax.yaxis.set_ticks(range(1,7))
ax.xaxis.set_ticks(range(1,6))
ax.yaxis.set_ticklabels(['a','b','c','d','e','f'])
ax.xaxis.set_ticklabels(['a','b','c','d','e'])

#2D Plot
#Plot two 2D subplots
ax2 = plt.subplot2grid((2,3),(0,2))
ax2.contourf(df_X, -df_Y, df_Zr, 10, alpha=.75, cmap=colormap)
ax3 = plt.subplot2grid((2,3),(1,2))
ax3.contourf(df_X, -df_Y, df_Zp, 10, alpha=.75, cmap=colormap)

#Format 2D subplots
ax2.set_title('Real Z')
ax3.set_title('Synergy Z')
ax2.set_xlabel(Drug_X)
ax2.set_ylabel(Drug_Y)
ax3.set_xlabel(Drug_X)
ax3.set_ylabel(Drug_Y)
ax2.set_xticks(())
ax2.set_yticks(())
ax3.set_xticks(())
ax3.set_yticks(())

plt.tight_layout()
plt.show()