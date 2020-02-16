from flask import Flask, render_template, request, escape

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:  # noqa: F821
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


# @app.route('/')
# def hello() -> '302':
#     return redirect('/entry')
# return 'Hello world from Flask!'


@app.route('/search4', methods=['GET', 'POST'])
def do_search() -> 'html':  # noqa: F821
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results)


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Returns set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


@app.route('/')
@app.route('/entry', methods=['GET', 'POST'])
def entry_page() -> 'html':  # noqa: F821
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
# def view_log() -> str:
#     with open('vsearch.log') as log:
#         contents = log.read()
#     return escape(contents)
def view_log() -> str:
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View log',
                           the_row_titles=titles,
                           the_data=contents)


if __name__ == '__main__':
    app.run(debug=True)
