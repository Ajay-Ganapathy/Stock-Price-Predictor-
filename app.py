from flask import Flask,render_template,request
import utils

app = Flask(__name__)
@app.route("/")

def home():
  return render_template("index.html")


@app.route('/predict/', methods=['GET', 'POST']) 
def predict(): 
    if request.method == 'POST': 
        open = int(request.form.get('Open'))
        high = int(request.form.get('High'))
        volume = int(request.form.get('Volume'))
        low = int(request.form.get('Low') )
        adj_close = int(request.form.get("adj_close"))

    prediction = utils.preprocessdata(open,high,volume,low,adj_close) 

    return render_template('predict.html', prediction=prediction) 

if __name__ == "__main__":
  app.run(debug=True)