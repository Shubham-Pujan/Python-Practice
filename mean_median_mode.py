

data1=[49,66,24,98,37,64,98,27,56,93,68,78,22,25,11]
# sum(data1)/len(data1)
def mean(data):
    sum=0
    for i in data:
        sum=sum+i
    return(sum/len(data))
print(mean(data1))
        

data2=[1,2,5,10,-20,30]

data2[1]
def median(data):
    length=len(data)
    sort_data=sorted(data)
    if (length%2==0):
         median=(sort_data[(length//2)]+sort_data[((length//2)-1)])/2
    else :
         median = sort_data[((length-1)//2)]
    return median

print(median(data2))



def mode(data):
    max=0
    for i in data:
        count1=data.count(i)      
       # print(i,count1)
        if count1 > max:            
            max=count1
            mode=i
            #print(mode)
    return mode
data3=[1,1,1,1,2,2,2,4,4,7,7,7,7,7,-10,-10,-10,-10,-10,-10]
print(mode(data3))


#dynamic input

a = [int(x) for x in input().split(",")]
a=input()
a=int(a.split())