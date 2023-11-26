data="""Col1    Col2    Col3   NewCol4
A       ABC     100    ABC
B       BCD     200    BCD
C       CDA     300    CDA_1
D       CDA     400    CDA_2
E       CDA     500    CDA_3
F       EFG     600    EFG
G       XYZ     700    XYZ_1
H       XYZ     800    XYZ_2
I       PQR     900    PQR"""

df = pd.read_csv(StringIO(data), sep="\s+")

grouped=df.groupby('Col2')['Col3']

index=[]
values=[]
def count_consecutive(df):
    index.append(df.index)
    values.append(df.values)

grouped.apply(count_consecutive)        
#[print(x) for x in index]
#[print(x) for x in values]

for x in index:
    count=0
    old_value=0
    for i in x:
        field=df.loc[i,'Col2']
        value=df.loc[i,'Col3']
        #print(value)
        if value>old_value:
            count+=1
        df.loc[i,'NewCol4']=field+"_"+str(count)
        old_value=value
    
print(df)
