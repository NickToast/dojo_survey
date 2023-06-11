from flask import Flask, render_template, redirect, session, request  # Import Flask to allow us to create our app, if u need render_template
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'life' 	#key goes into here

#SHOW PAGE FOR SURVEY
@app.route('/')
def home():




    return render_template('index.html')

#ACTION PAGE FOR SURVEY
@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    # session['stacks'] = request.form['webfund']
    return redirect('/results')


#SHOW PAGE FOR RESULTS
@app.route('/results')
def results():
    return render_template('results.html')




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.