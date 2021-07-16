import pandas as pd
import mysql.connector
from dictinary import s_active, s_reg

db = pd.read_csv(r"C:\xampp\htdocs\Mini_project_2021\vaccine_database.csv")
reg = pd.read_csv(r"C:\xampp\htdocs\Mini_project_2021\Register_District.csv")

myconn = mysql.connector.connect(host="localhost", user="root", password="", database="district")
cur = myconn.cursor()

a = []
b = []
for i in s_active:
    a.append(i)

for i in s_reg:
    b.append(i)

for i in range(len(db)):
    var = db.NO_of_vaccines[i]
    for j in a:
        if db.State[i] == j:
            c = s_active[j]
            d = s_reg[j]
            for k in c:
                t = var * 0.1
                for m in d:
                    if k == m:
                        if d[m] < t:
                            sql = "UPDATE district.district_sample SET NO_of_vaccines= %s WHERE District=%s"
                            val = (int(d[m]), m)
                            cur.execute(sql, val)
                            myconn.commit()
                            var = var - d[m]
                        else:
                            sql = "UPDATE district.district_sample SET NO_of_vaccines= %s WHERE District=%s"
                            val = (int(t), m)
                            cur.execute(sql, val)
                            myconn.commit()
                            var = var - t
