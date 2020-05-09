from flask import Flask, render_template, request, copy_current_request_context
from DBcm2 import UseDatabase, MyConnectionError, CredentialsError, SQLError
from threading import Thread

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'port': '8889',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }

def log_request(req: 'flask_request', res: str) -> None:  # noqa: F821
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                (phrase, letters, ip, browser_string, results)
                values
                (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'], 
                            req.form['letters'],
                            req.remote_addr,
                            req.user_agent.browser,
                            res, ))


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
    try:
        # log_request(request, results)
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print('*****Logging failed with the following error:', str(err))
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
def view_log() -> 'html':
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """SELECT phrase, letters, ip, browser_string, results
                    FROM log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
        return render_template('viewlog.html',
                               the_title='View log',
                               the_row_titles=titles,
                               the_data=contents)
    except CredentialsError as err:
        print('Incorrect username / password.  Error: ', str(err))
    except MyConnectionError as err:
        print('Is your database turned on?  Error: ', str(err))
    except SQLError as err:
        print('Is your query correct?  Error: ', str(err))
    except Exception as err:
        print('Something went wrong: ', str(err))
    return 'Error'


if __name__ == '__main__':
    app.run(debug=True)
