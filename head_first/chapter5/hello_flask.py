from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search4', methods=['GET', 'POST'])
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru,!'))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Returns set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


@app.route('/entry', methods=['GET', 'POST'])
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


app.run(debug=True)
