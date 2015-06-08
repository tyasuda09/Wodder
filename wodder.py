from flask import Flask, render_template, session, url_for 

# create the application object 
app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/welcome/')
def welcome(): 
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)