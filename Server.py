import sqlite3
from flask import Flask,jsonify
from flask import request
import os
import json

import numpy as np
from sklearn.svm import SVR
# import matplotlib.pyplot as plt

app = Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_rbf = SVR(kernel='linear', C=1e3, gamma=0.1)
svr_rbf = SVR(kernel='poly', C=1e3, gamma=0.1)


xtrain=[]
ytrain=[]




@app.route('/register', methods=['POST','GET'])
def test():
     conn = sqlite3.connect('temp.db')
     c = conn.cursor()
     try:
         create_tb_cmd = '''
             CREATE TABLE IF NOT EXISTS TFEST
             (ID INT PRIMARY KEY ,
             NAME           TEXT
             );
             '''

         c.execute(create_tb_cmd)
     except:
         print( "Create table failed")

         return False
     c.execute('''CREATE TABLE TTEST
           (ID INT PRIMARY KEY     ,
           NAME           TEXT

           );''')

     if request.method == 'POST':

        username = request.form["username"]
        # print(len(username))


        c.execute("insert into tfest(name) values ('%s')" % (username[-6:]))


        cursor=c.execute('select name from tfest')

        for row in cursor:
            ytrain.append(int(row[0][0:2],10))
            xtrain.append(int(row[0][2:4],10))
        # print(xtrain)
        # print(ytrain)
        xtrainarray=np.array(xtrain)
        ytrainarray=np.array(ytrain)
        print(xtrainarray)
        print(ytrainarray)
        #
        global y_rbf
        y_rbf=svr_rbf.fit(xtrainarray.reshape(-1,1), ytrainarray)



        # print(type(username))
        # print(values)
        # print(b)

        # conn.commit()

        # return astr[1:3]+"C"

        lw = 2
        # plt.plot(xtrainarray, y_rbf, color='navy', lw=lw, label='RBF model')
        # plt.scatter(50,a)
        # plt.show()
        return "hello"

@app.route('/predict', methods=['POST','GET'])
def predictation():

     if request.method=='POST':


        username = request.form["username"]
        # password = request.form["password"]
        # a = y_rbf.predict(int(username,10))
        predictarray=[]

        # print(len(username))
        # print(username[-4:])
        predictvalue=int(username[-4:])
        predictarray.append(predictvalue)
        predictarray=np.array(predictarray)

        # print(predictarray)
        predicted=y_rbf.predict(predictarray.reshape(-1,1))
        predictedOne=predicted[0]
        # print(predicted)
        print(predictedOne)

        StrPre=str(int(predicted))





        return StrPre
        # return "hello"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=False)


    def UserSimilarity(train):
      W = dict()
        for u in train.keys():
            for v in train.keys():
                if u == v:
                    continue
                W[u][v] = len(train[u] & train[v])
                W[u][v] = /= math.sqrt(len(train[u]) * len(train[v]) * 1.0)
         return W


     def Recommend(user, train, W):
        rank = dict()
         interacted_items = train[user]
         for v, wuv in sorted(W[u].items, key=itemgetter(1), reverse=True)[0:K]:
             for i, rvi in train[v].items:
                 if i in interacted_items:
                     # we should filter items user interacted before
                     continue
             rank[i] += wuv * rvi
         return rank