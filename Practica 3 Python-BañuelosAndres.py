"""
Práctica 3: Regresion no lineal

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Andres Martin Bañuelos Elias
Número de control: 21212142
Correo institucional: l21212142@tectijuana.edu.mx

Asignatura: Gemelos Digitales
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
 
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats
import statistics as st
import warnings
warnings.filterwarnings("ignore")

data=pd.read_csv('data.csv')
T=data.iloc[:,0]; to= T.to_numpy()
X1=data.iloc[:,1];x1o=X1.to_numpy()
X2=T=data.iloc[:,2];x2o=X2.to_numpy()
xo=np.mean([x1o,x2o], axis=0)

print(data)

def plotdata(t,x1,x2,xo):
    fig = plt.figure();
    plt.rcParams.update({'font.size':11})
    fig = plt.figure(figsize = (8,4))
    plt.plot(t,x1,linestyle = 'none', marker = 'x', 
             color = [0.30, 0.45, 0.60], label = '$x_1(t)$')
    plt.plot(t,x2,linestyle = 'none', marker = 'x', 
             color = [0.60, 0.00, 0.00], label = '$x_2(t)$')
    plt.plot(t,xo,'-o',linewidth = 0.5, markersize = 3, 
             color = [ 1.00, 0.00, 0.80], label = '$x_o(t)$')
    plt.xlabel('$t$ $[months]$')
    plt.ylabel('x_i(t)$ $[cells]$')
    plt.xlim(0.72)
    xticks = np.arange(0,73,8)
    plt. xticks(xticks)
    plt.ylim(0, 11E8)
    yticks = np.arange(0,12E8,1E8)
    plt.yticks(yticks)
    plt.legend(bbox_to_anchor=(1.01, 1.03), fontsize = 10,
               title="$Experimental$ $data$", frameon = True)
    plt.show()
    fig.tight_layout()
    fig.savefig('python_data.pdf')
    
plotdata(to,x1o,x2o,xo)

def mdl(to,xo,k0,b,S):
    
    def sigmoidal(t,k):
        dt = 1E-1
        n = round(max(t)/dt)
        time = np.linspace(0,max(t),n+1)
        x = np.zeros(n+1); x[0] = xo[0]
        
        def f(x):
            if S == 1:
                dx = k*x*(1-b*x)
            elif S == 2:
                dx = k*x**(2/3)*(1-b*x**(1/3))
            elif S == 3:
                dx = k*x**(3/4)*(1-b*x**(1/4))
            elif S == 4:
                dx = k*x*(1-b*np.log(x))
            elif S== 5:
                dx = k*x*np.log(b/x)
            return dx
        
        for i in range (0,n):
            fx = f(x[i])
            xn = x[i] + fx*dt
            fxn = f(xn)
            x[i+1] = x[i] + (fx + fxn)*dt/2
            
        xi = np.zeros(len(t))
        
        for i in range(0,len(t)):
            k = abs(time-t[i]) < 1E-9
            xi[i] = x[k]
        return xi 
    
    npar = len(k0)
    low = np.ones(npar)*math.inf*(-1)
    sup = np.ones(npar)*math.inf
    
    Estimate,cov = curve_fit(sigmoidal, to, xo, k0, 
                             bounds = (low, sup))
    
    k = Estimate [0]
    xi = sigmoidal(to,k)
            
    return xi,Estimate,cov

k0 = [0.001]
xmax = np.max(xo)
b = [1/xmax, 
     xmax**(-1/3),
     xmax**(-1/4),
     1/np.log(xmax),
     xmax]

def biostatistics(Estimate, cov, xo, xa):
    alpha = 0.05
    dof = len(xo) - len(Estimate)
    tval = scipy.stats.t.ppf(q=1 - alpha / 2, df=dof)
    SE = np.diag(cov) ** 0.5
    pvalue = 2 * scipy.stats.t.sf(np.abs(Estimate / SE), dof)
    MoE = SE * tval
    CI95 = np.zeros([len(Estimate), 2])
    
    for i in range(0, len(Estimate)):
        CI95[i, 0] = Estimate[i] - MoE[i]
        CI95[i, 1] = Estimate[i] + MoE[i]
    
    print('\nStatistics results:\n')
    Parameter = ['k']
    
    df = pd.DataFrame(list(zip(Parameter, Estimate, SE, MoE, CI95, pvalue)),
                      columns=['Parameter', 'Estimate', 'SE', 'MoE', 'CI95', 'pvalue'])
    
    print(df.to_string(index=False))


for i in range(0, len(b)):
    S = i + 1
    xa, Estimate, cov = mdl(to, xo, k0, b[i], S)
    # print('\nk =', Estimate)
    biostatistics(Estimate, cov, xo, xa)
    

def plotresults(t, xo, xa, S):
    fig = plt.figure()
    plt.rcParams.update({'font.size': 11})
    fig = plt.figure(figsize=(8, 4))
    
    colors = ['#FF69B4', '#1E90FF', '#32CD32'] 
    marker_colors = ['#FF1493', '#4169E1', '#228B22']  

    if S == 1:
        sigmoidal = 'Logistic'
        title = 'Logistic Growth Model'
        line_color = colors[0]  
        marker_color = marker_colors[0]  
    elif S == 2:
        sigmoidal = 'AllometricSphere'
        title = 'Allometric Sphere Model'
        line_color = colors[1] 
        marker_color = marker_colors[1]  
    elif S == 3:
        sigmoidal = 'AllometricFractal'
        title = 'Allometric Fractal Model'
        line_color = colors[2] 
        marker_color = marker_colors[2] 
    elif S == 4:
        sigmoidal = 'Gompertz'
        title = 'Gompertz Model'
        line_color = colors[0]  
        marker_color = marker_colors[0]  
    elif S == 5:
        sigmoidal = 'GompertzSimplified'
        title = 'Simplified Gompertz Model'
        line_color = colors[1]  
        marker_color = marker_colors[1]  

    plt.plot(t, xo, linestyle='none', marker='x', color=line_color, markerfacecolor=marker_color, markeredgecolor=marker_color, label='$x_o(t)$')
    plt.plot(t, xa, linewidth=0.5, markersize=3, color=line_color, label='$x_a(t)$ (Model)')
    
    plt.title(title, fontsize=14)
    
    plt.xlabel('$t$ $[months]$')
    plt.ylabel('$x_i(t)$ $[cells]$')
    plt.xlim(0, 72)
    xticks = np.arange(0, 73, 8)
    plt.xticks(xticks)
    plt.ylim(0, 11E8)
    yticks = np.arange(0, 12E8, 1E8)
    plt.yticks(yticks)
    plt.legend(bbox_to_anchor=(1.01, 1.03), fontsize=10, title='$Results$', frameon=True)

    namepdf = 'Python_results_' + sigmoidal + '.pdf'
    fig.savefig(namepdf) 
    plt.show()
    fig.tight_layout()

for i in range(0, len(b)):
    S = i + 1
    xa, Estimate, cov = mdl(to, xo, k0, b[i], S)
    biostatistics(Estimate, cov, xo, xa)
    plotresults(to, xo, xa, S)