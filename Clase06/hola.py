lista=[1,2,3]
n=2
try:
   for k in range(10): 
    if k<n and lista[k]==3:
        print('caso1')
except Exception:
    print('caso2')