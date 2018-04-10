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

#import data
df_Zr = pd.read_excel(Data_File, sheet_name = 'Zr', header = None)
df_X = pd.read_excel(Data_File, sheet_name = 'X', header = None)
df_Y = pd.read_excel(Data_File, sheet_name = 'Y', header = None)
df_Zp = pd.read_excel(Data_File, sheet_name = 'Z_p', header = None)

#3D Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
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
ax.xaxis.set_ticks(range(1,7))
ax.yaxis.set_ticks(range(1,6))
ax.xaxis.set_ticklabels(['a','b','c','d','e','f'])
ax.yaxis.set_ticklabels(['a','b','c','d','e'])

#2D Plot
fig2, axes = plt.subplots(nrows=1, ncols=2,figsize = (8,4))

#Plot 2D subplots
axes[0].contourf(df_Y, -df_X, df_Zr, 10, alpha=.75, cmap='Purples')
axes[1].contourf(df_Y, -df_X, df_Zp, 10, alpha=.75, cmap='Purples')

#Format 2D subplots
axes[0].set_title('Real Z')
axes[1].set_title('Syndergy Z')
axes[0].set_xlabel(Drug_X)
axes[0].set_ylabel(Drug_Y)
axes[1].set_xlabel(Drug_X)
axes[1].set_ylabel(Drug_Y)
axes[0].set_xticks(())
axes[0].set_yticks(())
axes[1].set_xticks(())
axes[1].set_yticks(())

plt.show()
