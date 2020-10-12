from Controller import *
from flask import *


app = Flask(__name__)


@app.route('/')
def index():
    data = get_ad()

    return render_template('index.html', rows=data)


@app.route('/learnmore/<int:ad_id>', methods=['POST'])
def learnmore(ad_id):
    data = get_ad_by_id_foreign_keys(ad_id)

    return render_template('learnMore.html', row=data)


if __name__ == '__main__':
    app.run(debug=True)
