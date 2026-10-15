from flask import Flask, render_template
app = Flask(__name__)

movies = [
    {"title": "The Shawshank Redemption", "year": 1994, "note": 9.3},
    {"title": "The Godfather", "year": 1972, "note" : 9.2 },
    {"title": "The Dark Knight", "year": 2008, "note": 9.1 },
    {"title": "12 Angry Men", "year": 1957, "note": 9.0},
    {"title": "Schindler's List", "year": 1993, "note" : 9.0 }
]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies')
def movies_page():
    return render_template('movies.html', movies=movies)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
