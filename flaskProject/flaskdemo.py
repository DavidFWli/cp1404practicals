from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['search_query']
        try:
            page = wikipedia.page(search_query)
            return render_template('results.html', page=page)
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options
            return render_template('disambiguation.html', options=options)
        except wikipedia.exceptions.PageError:
            return render_template('not_found.html')

    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True)
