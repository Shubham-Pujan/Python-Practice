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
namelist=list(nameS.items())
type(namelist)
namelist[10]="sdscas"
namelist
namelist[10]=(108,"jain")
namelist
nameS[108]="varun jain"
nameS

nameS[:5]
nameS.iloc[0:5]
nameS.iloc[0]
nameS.loc[0]
nameS.loc[108]
nameS[nameS=="meena"]
nameS.loc[103:110]


rollnoS=pd.Series(rollno)
rollnoS
nameS=pd.Series(name)
pythonS=pd.Series(pythonL)
sasS=pd.Series(sasL)
genderS=pd.Series(genderl)
df=pd.concat([rollnoS,nameS,pythonS,sasS,genderS],axis=1)
df
df.index=rollno
df
df1=pd.DataFrame({"rollno":rollno,"name":name,"gender":genderl,"python":pythonL,"sas":sasL},columns=["rollno","name","gender","python","sas"])
df1
df2=df1[["name","sas","rollno"]]
df2

df1.dtypes
df1.T
df1[1]
df1[[1]]
df1
df1[3:4]
df1.loc(1)
type(df1.iloc[0])
type(df1[["name"]])
df1.iloc[:3,:2]
df1[:4,:2]
df1["total"]=df1["sas"]+df1["python"]
df1
df1.iloc[:5,:3]
df1[df1["total"]>150]






#%% pivot tables


rollno = [109,102,105,106,103,110,101,107, 104,111,108]
rollno
name=["meena","apporva","shubham","shubham","goldie","hitesh","shruti",      "vijay"  ,"achal","lalit","varun"]

gender=["m","m","f","f","m","f","m","f","m","m","f"]

python=np.random.randint(60,100,11)
python

sas=np.random.randint(60,100,11)
hadoop=np.random.randint(60,100,11)
fees=np.random.randint(100000,150000,11)
hostel=[True,False,True,False,True,True,False,False,True,True,False]
hadoop
fees
hostel

sass=pd.Series(sas)
feess=pd.Series(fees)
namess=pd.Series(name)
pythons=pd.Series(python)
hadoops=pd.Series(hadoop)
rollnos=pd.Series(rollno)
genders=pd.Series(gender)
hostels=pd.Series(hostel)
df2=pd.concat([rollnos,namess,genders,hostels,feess,sass,pythons,hadoops],axis=1)
df2.columns=["rollno","name","gender","hostel","fees","sas","python","hadoop"]
df2
type(df2)
df2["total"]=df2.sas+df2.python+df2.hadoop
student=df2
type(student)
student.to_csv("student.csv",index=False)
df2.columns
student.groupby("gender")[["sas","hadoop"]].mean()
classes=["C1","C2","C3"]
df2["class"]=np.random.choice(classes,11)
df2
type(df2)
df2.to_csv("student1.csv",index=False)
df2

pd.pivot_table(df2,index=["name"])
pd.pivot_table(df2,index=["name","class"])
pd.pivot_table(df2,index=["class","gender"],values=["total","python"])

df3=pd.read_csv("student1.csv")
df3

pd.pivot_table(df3,index=["class","gender"],values=["total","python"],aggfunc=[np.sum,np.mean,len])
course=pd.Series(["msc","pg","msc","msc","msc","pg","msc","pg","pg","pg","msc"])
# df3.drop(labels="class",axis=1,inplace=True)
df3
df3["course"]=course
type(df3)
df3=df3[["rollno","name","gender","class","course","hostel","fees","sas","python","hadoop","total"]]
df3
df3.to_csv("studentnew.csv",index=False)
data=pd.read_csv("studentnew.csv")
data
data.groupby("course")["python"].describe()
pd.pivot_table(data,index=["gender"],values=["python"],aggfunc=[np.sum,np.mean,len])






rng=np.random.RandomState(42)
rng
marks=pd.Series(rng.randint(50,100,11))
marks1=pd.Series(rng.randint(50,100,11))
marks
marks1
marks
marks.sum()
marks.std()

dict(x=1,y=4,z=3)
dict(x=1,y="hello",z=[3,4])



A=pd.Series(rng.randint(0,10,6))
B=pd.Series(rng.randint(0,10,6))
df=pd.concat([A,B],axis=1)
df.sum(axis=1)
df.sum(axis=0)
df.describe()
df.columns=["A","B"]
df


["A","B","C"]*2
np.repeat(["a","b","c"],2)
np.repeat(["a","b","c"],[1,2,3])

df=pd.DataFrame({"key":["a","b","c"]*2,"data1":range(6),"data2":rng.randint(0,10,6)},columns=["key","data1","data2"])
df
df.groupby("key")
df.groupby("key").mean()
grouped=df.groupby("key")
grouped
grouped.sum()
df.groupby("key").aggregate(["min","max","median"])
df.groupby("key").aggregate({"data1":"min","data2":["max","median"]})

df
df.filter(items=["data1"])
df.filter(like="0",axis=0)
df.filter(like="y",axis=1)
df
df["data2"].mean()
grouped.filter(lambda x:x['data2'].mean() > 1)
grouped.transform(lambda x:x-x.mean())

prodct = lambda x,y : x*y
prodct(4,5)

df
grouped.apply(lambda x:x["data2"]*2)

df2=df.set_index("key")
df2

newmap={"a":"pg","b":"msc","c":"bsc"}
df2.groupby(newmap).sum()

df2.groupby(str.lower).mean()
df2.groupby([newmap,str.lower]).mean()

df.groupby("key").sum().unstack()


