
from flask import Flask, render_template, jsonify
from flask_ngrok import run_with_ngrok

app = Flask(__name__, template_folder='E:/flask/FlaskWebProject1/')

run_with_ngrok(app)

# Root page
@app.route('/')
def index():
    return "<h1> Welcome </h1> <p> Under Construction </p>"

# returns single page (static)

@app.route('/about')
def about():
    return "About Us"

# returns specific page (static)

@app.route('/profile/mammoth')
def profile():
    return "<h2>Welcome to profile Mammoth</h2>"

# returns dynamic page based off /name

@app.route('/product/<name>')
def product_page(name):
    return "<h3>Product "+name+"</h3>"

# returns dynamic page based off /name/price (differing from the "/<name>" page)

@app.route('/product/<name>/<price>')
def product_information(name,price):
    return "<h4>About " +name+":</h4> <p>Price: " +price+"</p>"

# static template
@app.route('/first-template')
def first_template():
    return render_template('first_template.html')

#dynamic template
@app.route('/profile/<username>')
def show_profile(username):
    return render_template('profile.html',name=username)

# - dictionary to json
Courses = [{'id':1,'title':'Hello Coding','image_url':'https://cdn.pixabay.com/photo/2024/12/09/16/22/boat-9255590_1280.jpg'},
           {'id':2,'title':'Machine Learning for Everyone','image_url':'https://cdn.pixabay.com/photo/2024/12/06/12/23/ai-generated-9248643_640.jpg'},
           {'id':3,'title':'Wall Street Coder','image_url':'https://cdn.pixabay.com/photo/2023/11/08/04/30/girl-8373900_640.jpg'}
]

@app.route('/api/courses')
def api_courses():
    return jsonify(Courses)

# Show all data correctly - create html file, add components/styling as desired
@app.route('/courses')
def courses():
    return render_template('all_courses.html', courses = Courses)


if __name__ == '__main__':
    app.run()


