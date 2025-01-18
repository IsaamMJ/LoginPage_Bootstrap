from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render the index.html file

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
