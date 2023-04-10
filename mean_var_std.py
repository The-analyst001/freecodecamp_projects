import numpy as np

def calculate(list):

  a = np.array(list)
  if len(a) != 9:
    raise ValueError("List must contain nine numbers.")
  else : 
    print (a)
    d = a.reshape(3,3)
    dic = {
'mean' : [[d[:,i].mean() for i in range(3)], [d[i].mean() for i in range (3) ] , d.mean() ],
'variance': [[d[:,i].var() for i in range(3)], [d[i].var() for i in range (3) ] , d.var()],
'standard deviation': [[d[:,i].std() for i in range(3)], [d[i].std() for i in range (3) ] , d.std()],
'max': [[d[:,i].max() for i in range(3)], [d[i].max() for i in range (3) ] , d.max()], 
'min': [[d[:,i].min() for i in range(3)], [d[i].min() for i in range (3) ] , d.min()],
'sum': [[d[:,i].sum() for i in range(3)], [d[i].sum() for i in range (3) ] , d.sum()]
  }
    return dic

