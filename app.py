from flask import *

app = Flask(__name__)

@app.route('/login',methods = ['GET'])
def login():
      uname=request.args.get('uname')
      passwrd=request.args.get('pass')
      if uname=="siva" and passwrd=="python":
          return "Welcome %s" %uname
      else:
            return "invalid %s" %uname      

if __name__ == "__main__":
 
   app.run(debug = True)