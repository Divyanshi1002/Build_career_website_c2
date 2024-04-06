import logging
from flask import Flask, render_template

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello_world():
    try:
        # Log a debug message indicating that the template rendering process has started
        logging.debug("Rendering 'home.html' template...")
        
        # Attempt to render the template
        return render_template('home.html')
    
    except Exception as e:
        # Log an error message if an exception occurs during template rendering
        logging.exception("Error rendering template:")
        return f"An error occurred while rendering the template: {str(e)}"

@app.route('/act')
def action():
    return 'Hello there!'
if __name__ == '__main__':
    app.run(debug=True)
