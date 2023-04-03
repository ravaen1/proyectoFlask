from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_HOST'] = 'localhost'
app.config['SQLALCHEMY_USER'] = 'root'
app.config['SQLALCHEMY_PASSWORD'] = ''
app.config['SQLALCHEMY_DB'] = 'mapaica'  #revisar

db = SQLAlchemy(app)

@app.route('/')
def index():
   # return "saguela alesso"

   return render_template('index.html')
    

if __name__=='__main__':
    app.run(debug=True, port=5000)
