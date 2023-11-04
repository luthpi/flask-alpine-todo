from flask import Flask, jsonify, render_template, request, redirect, json
from datetime import date

app = Flask(__name__)
app.json.sort_keys = False

def load_data():
    with open('./data.json') as file:
        return json.load(file)

def save_data(json_data):
    with open('./data.json', 'w') as file:
        json.dump(json_data, file, indent=4)

@app.route("/")
def home():
    return render_template('index.html')
    
todos = load_data()
        
@app.route("/data")
def data():
	return jsonify(todos)

@app.route("/json")
def jsonDatas():
	return load_data()
	
@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        todos.append({
            "id": len(todos) + 1,
        	"todo": request.form['todo_input'],
      	  "done": False
        })
        save_data(todos)
    else: 
        redirect("/")
    return redirect("/")
  
@app.route("/delete/<int:id>")
def delete(id):
    for x in todos:
    	if x["id"] == id:
    		todos.remove(x)
    		break
    save_data(todos)
    return redirect("/")
    
@app.route("/deleteall")
def deletall():
    todos.clear()
    save_data(todos)
    return redirect("/")
    
@app.route("/done/<int:id>")
def done(id):
    for x in todos:
    	if x["id"] == id:
    		x["done"] = not x["done"]
    		break
    save_data(todos)
    return redirect("/")