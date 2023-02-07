import numpy as np
test = np.array( [[34,43,73],[82,22,12],[53,94,66]] )
newColumn = np.array([[10,10,10]])
deleted = np.delete(test,1,axis=1)
print(f'deleting the 2nd coloumn {deleted}')
deleted = np.insert(deleted,1,newColumn,axis=1)
print(f'After insert the 2nd coloumn {deleted}')
