"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Welcome!</title>
      </head>
      <body>
        <h1>Hi! This is the home page.</h1>
        <p>Click <a href="/hello">here</a> to go to the hello page.</p>
      </body>
    </html>
    """
@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""
    compliments = ['awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

    options = ""

    for compliment in compliments: 
      option_selection = f'<option value="{compliment}">{compliment}</option>'
      options += option_selection

    html_form = f'''
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
          <br>
          Choose a compliment:
          <select name="compliment">
            {options}
          </select>
          <br>
          <input type="submit" value="Submit">
        </form>



      </body>
    </html>
    '''
    return html_form


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    if not compliment:
        compliment = choice(AWESOMENESS)
    
    greeting = f"Hi, {player}! I think you're {compliment}!"

    

    html_form = f'''
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        <p>{greeting}
      </body>
    </html>
    '''
    return html_form


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0", port=5001)
