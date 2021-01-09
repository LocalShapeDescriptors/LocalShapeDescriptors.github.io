import pandas as pd
import sys

data = pd.read_csv(sys.argv[1], header=None)

loc = data.iloc[:,0:3]
off = data.iloc[:,3:6]
ortho = data.iloc[:,6:9]
diag = data.iloc[:,9:12]
size = data.iloc[:,12:13]

off = pd.concat([loc,off],axis=1)
ortho = pd.concat([loc,ortho],axis=1)
diag = pd.concat([loc,diag],axis=1)
size = pd.concat([loc,size],axis=1)

off.to_csv('fib_offsets.csv',header=False,index=False)
ortho.to_csv('fib_ortho.csv',header=False,index=False)
diag.to_csv('fib_diag.csv',header=False,index=False)
size.to_csv('fib_size.csv',header=False,index=False)
