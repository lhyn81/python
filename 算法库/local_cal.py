import math
Q = 50000
T = 350
V = 13.5
mu = 3e-5
den = 2500
# 建立输出变量
q = Q*(T+273)/273
A = q/3600/V
D0 = (q / 3600 / (1 * 0.44 * 0.21 * V))**0.5
a = D0*0.44
b = D0*0.21
D = 2*(A/math.pi)**0.5
De = D0*0.4
hc = D0*0.5
h = D0*1.4
H = D0*3
D2 = D0*0.4
Cof_ZL = 16*a*b/De**2
den_gz = 1.34*273/(T+273)
DP = Cof_ZL*V**2/2*den_gz
tmp1 = (4*9.8*mu*(den-den_gz)/(3*den_gz**2))**0.33
Vs = 2.991*tmp1*((b/D0)**0.4/(1-b/D0)**0.33)*D0**0.067*V**0.66
Nc=4
d50 = 10**6*(9*mu*b/(2*math.pi*Nc*V*(den-den_gz)))**0.5
vars=locals().copy()
print(vars)
for k,v in vars.items():
    print('%s = %s' % (k,v))
bb = "%.2f" % h
print(bb)
