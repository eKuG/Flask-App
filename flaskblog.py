from flask import Flask, render_template, jsonify
# from flask_assets import Bundle, Environment
app = Flask(__name__)

# js= Bundle('home.js', output='gen/main.js')

# assets = Environment(app)
# assets.register('main.js', js)
posts = [
  {
    'author' : 'J K Rowling',
    'title'  :  'Blog Post 1',
    'content':  'First post content',
    'dated'  :  'May 1 2019'
  },

 { 'author' : 'Dan Brown',
    'title'  :  'Blog Post 2',
    'content':  'Second post content',
     'dated'  :  'May 2 2019'
 }
]

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html' )

@app.route("/about")
def about():
    return render_template('about.html',title = 'About')    

if __name__ == '__main__':
  app.run(debug=True)  
