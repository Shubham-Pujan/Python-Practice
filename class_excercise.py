import numpy as np
np.set_printoptions(threshold=np.nan)
import pandas as pd
rollno = [109,102,105,106,103,110,101,107, 104,111,108]
rollno
name=["meena","apporva","kaustav","shubham","goldie","hitesh","shruti",      "vijay"  ,"achal","lalit","varun"]

genderl=["m","m","f","f","m","f","m","f","m","m","f"]

pythonL=np.random.randint(60,100,11)
pythonL

sasL=np.random.randint(60,100,11)
sasL

nameS=pd.Series(name,rollno)
nameS


112 in nameS
111 in nameS
nameS.index
nameS.keys()
nameS.items
nameS.values
