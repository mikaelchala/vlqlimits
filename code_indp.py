#!/usr/bin/env python


import sys
import os.path
from scipy.interpolate import griddata
import numpy as np

def grid(x, y, z, grid_x, grid_y):
	Z = griddata(np.array(zip(x, y)), np.array(z), (grid_x, grid_y), method = 'linear')

	return Z

# READ THE TABLE FILE
###############################################################################
file = ".tables"
data = np.loadtxt(file, comments = "%")
x = data[:, 0]
y = data[:, 1]
X, Y = np.mgrid[min(x): max(x):1j * 11, min(y): max(y):1j * 4]
dict = {}
k = -1
for line in open(file).readlines():
	if "%" in line:
		for word in line.split():
			if word != "%":
				dict[word] = grid(x, y, data[:, k], X, Y)
			k = k + 1

def f(char, m1, m2):
	return dict[char][np.searchsorted(X[:,0], m1), np.searchsorted(Y[0, :], m2)]
###############################################################################

# READ THE INPUT FILE
###############################################################################
vecM = []
vecmS = []
veci = []
vecj = []
veck = []
vecl = []

BRless1 = 0
BRmore1 = 0
if len(sys.argv) < 2:
	print "ERROR: SET AN INPUT FILE"
else:
	input = sys.argv[1]
	if not os.path.isfile(input):
		print "ERROR: INPUT FILE DOES NOT EXIST"
	else:
		try:
			for line in open(input).readlines():
				if "%" not in line:
					vecM.append(float(line.split()[0]))
					vecmS.append(float(line.split()[1]))
					veci.append(float(line.split()[2]))
					vecj.append(float(line.split()[3]))
					veck.append(float(line.split()[4]))
					vecl.append(float(line.split()[5]))
		except:
			print "WRONG FORMAT"
			vecM = []

###############################################################################
L08 = 20000.
L13 = 14000.
Nsignal_ht = 0.
Nsignal_wb = 0.
Nsignal_zt = 0.
Nsignal_c1 = 0.
Nsignal_c2 = 0.
xsec_wbwb2 = 0.
xsec_htht2 = 0.

excl = 0
###############################################################################
for p in range(0, len(vecM)):
	M = vecM[p]
	mS = vecmS[p]
	i = veci[p]
	j = vecj[p]
	k = veck[p]
	l = vecl[p]
###############################################################################
	x08   = f("xsec08", M, mS)
	x13   = f("xsec13", M, mS)
	htht  = f("htht", M, mS)
	htzt  = f("htzt", M, mS)
	htwb  = f("htwb", M, mS)
	wbwb  = f("wbwb", M, mS)
	ztzt  = f("ztzt", M, mS)
	ztht  = f("ztht", M, mS)
	ztwb  = f("ztwb", M, mS)
	stht  = f("stht", M, mS)
	stzt  = f("stzt", M, mS)
	stwb  = f("stwb", M, mS)
	stst1 = f("stst1", M, mS)
	stst2 = f("stst2", M, mS)
	wblim = f("wbwblim", M, mS)
	htlim = f("hthtlim", M, mS)
###############################################################################
	Nsignal_ht = Nsignal_ht + x08 * L08 * (j**2*htht + 2.*j*k*htzt + 2.*j*i*htwb)
	Nsignal_wb = Nsignal_wb + x08 * L08 * (i**2*wbwb)
	Nsignal_zt = Nsignal_zt + x13 * 36000. * (k**2*ztzt + 2.*k*j*ztht + 2.*k*i*ztwb + 2.*l*j*stht + 2.*l*k*stzt + 2.*l*i*stwb)
	Nsignal_c1 = Nsignal_c1 + x13 * L13 * (l**2*stst1)
	Nsignal_c2 = Nsignal_c2 + x13 * L13 * (l**2*stst2)

	ratio_wb = (i**2*x13)/wblim
	ratio_ht = (j**2*x13)/htlim

	if ratio_wb > 1:
		excl = 1
	if ratio_ht > 1:
		excl = 1

if Nsignal_ht > 22:
		excl = 1
if Nsignal_wb > 15:
		excl = 1
if Nsignal_zt > 6:
		excl = 1
if Nsignal_c1 > 13:
		excl = 1
if Nsignal_c2 > 5:
		excl = 1

#################################
if len(vecM) != 0:
	print excl
