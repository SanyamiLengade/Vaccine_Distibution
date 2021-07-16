import pandas as pd
import operator

dr=pd.read_csv(r"C:\xampp\htdocs\Mini_project_2021\Register_District.csv")
dw = pd.read_csv(r"C:\xampp\htdocs\Mini_project_2021\district_sample.csv")
db = pd.read_csv(r"C:\xampp\htdocs\Mini_project_2021\vaccine_database.csv")
#for i in range(len(db)):




a=set(dw.State)
a=sorted(a)
b=[]
for i in a:
    d_Active = {}
    for j in range(len(dw)):
        if i==dw.State[j]:
           d_Active[dw.District[j]]=dw.Active[j]
        else:
            continue
    b.append(d_Active)

s_active={}
for i in range(len(a)):
    d=(sorted(b[i].items(), key=lambda kv: (kv[1],kv[0])))
    d = dict(sorted(b[i].items(), key=operator.itemgetter(1), reverse=True))
    s_active[a[i]] = d

c=[]
for i in a:
    d_reg={}
    for j in range(len(dr)):
        if i==dr.State[j]:
            d_reg[dr.District[j]]=dr.Register[j]
        else:
            continue
    c.append(d_reg)
s_reg={}
for i in range(len(a)):
    s_reg[a[i]] = c[i]


a=[]
b=[]
for i in s_active:
   a.append(i)

for i in s_reg:
    b.append(i)

c=s_active['Maharashtra']
d=s_reg['Maharashtra']

print(a)



