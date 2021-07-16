import pandas as pd
import mysql.connector
import operator




df = pd.read_csv(r"C:\xampp\htdocs\Mini_project_2021\state_final.csv")
res = pd.read_csv(r"C:\xampp\htdocs\Mini_project_2021\new_register_statewise.csv")

# f=open('profile.html','w')
# msg="""<!DOCTYPE html>
# <html lang="en" dir="ltr">
# <html>
# <head>
#     <meta charset="utf-8">
#     <title>Disrtibution</title>
#     <link rel="stylesheet" href="login.html">
#     <style>
#
#         p {text-align: center;}
#         p {font-size: 30px;}
#         p {color: #3b77bb;}
#
#
#
#         .button{
#             border: none;
#             color :rgba(10, 10, 10, 0.726);
#             padding: 16px 32px;
#             text-align: center;
#             text-decoration: none;
#             display: inline-block;
#             font-size: 16px;
#             margin-top: 4px 2px ;
#             transition-duration: 0.4s;
#             cursor: pointer;
#             border-radius: 12px;
#             position:relative;
#             left:550px;
#             font-style: normal;
#
#         }
#
#
#
#         .button1{
#             position:relative;
#             top: 100px;
#             left:650px;
#             background-color: azure;
#             border-color:#3b77bb ;
#             border-style: double;
#
#         }
#         .button1:hover {
#             background-color: #3b77bb;
#             color: white;
#         }
#         .button2{
#             position:relative;
#             top:200px;
#             left:420px;
#             background-color: azure;
#             border-color:#3b77bb ;
#             border-style: double;
#
#         }
#         .button2:hover {
#             background-color: #3b77bb;
#             color: white;
#         }
#         body{
#             background-image: url("https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/slideshows/covid19_myths_you_shouldnt_believe_slideshow/1800x1200_covid19_myths_you_shouldnt_believe_slideshow.jpg?resize=*:350px");
#             background-repeat: no-repeat;
#             background-size: cover;
#             position : relative;
#         }
#         .arse{
#             font-size: x-small;
#         }
#         .space{
#         position:relative;
#         left:500px;
#         }
#
#      </style>
#     </head>
#     <body>
#
#           <header>
#           <p style="font-style:oblique">" Dawai bhi, kadai bhi"</p>
#           <p > (Yes to Vaccine , Yes to Caution)</p>
#
#           <div class="arse">
#           <p>for corona updates
#           <a href="https://www.aarogyasetu.gov.in/">https://www.aarogyasetu.gov.in</a></p>
#           </div>
#         </header>
#          <form name="search" action="/cgi-bin/main_program.py" method="get">
#         v: <input type="text" name="variable">
#         <input type="submit" value="Submit">
#         </form>
#           <button onclick="window.location.href='http://localhost/Mini_project_2021/state.php';"  class="button button1" >State wise Distribution</button>
#           <button onclick="window.location.href='http://localhost/Mini_project_2021/fetch.php';" class="button button2">District wise Distribution</button>
#     </body>
# </html>
# """
# f.write(msg)
# f.close()
# form = cgi.FieldStorage()
# vaccines= form.getvalue('searchbox')
# print(vaccines)
#webbrowser.open_new_tab('http://localhost:63342/python_loginpage/templates/profile.html')

# if form.getvalue('variable'):
#    vaccines = form.getvalue('variable')
# else:
#     vaccines = "Not entered"

#vaccines = int(input("Enter no of vaciines:"))



dic = {}
length = len(df)
for i in range(length):
    dic[df.State[i]] = df.Active[i]
sort_dic = (sorted(dic.items(), key=lambda kv: (kv[1], kv[0])))
sorted_d = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))
l = len(sorted_d)

reg = {}
lengthr = len(res)
for i in range(lengthr):
    reg[res.States[i]] = res.register[i]

myconn = mysql.connector.connect(host="localhost", user="root", password="", database="vaccines")
cur = myconn.cursor()
k = sorted_d.keys()
kd = dic.keys()
for i in k:
    t = vaccines * (10/100)
    if i in reg:
        if reg[i] < t:
            sql = "UPDATE vaccines.state_final SET NO_of_vaccines= %s WHERE State=%s"
            val = (reg[i], i)
            cur.execute(sql, val)
            myconn.commit()
            vaccines = vaccines-reg[i]
        else:
            sql = "UPDATE vaccines.state_final SET NO_of_vaccines= %s WHERE State=%s"
            val = (t, i)
            cur.execute(sql, val)
            myconn.commit()
            vaccines = vaccines-t