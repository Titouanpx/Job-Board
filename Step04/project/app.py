from Controller import *
from flask import *

app = Flask(__name__)


@app.route('/')
def index():
    data = get_ads()

    return render_template('index.html', rows=data)


@app.route('/learnmore/<int:ad_id>', methods=['POST'])
def learnmore(ad_id):
    data = get_ad_by_id_foreign_keys(ad_id)

    return render_template('learnMore.html', row=data)


@app.route('/create')
def create():
    create_new_ad("5000", "title", "description", "1500", "place", "20", "1", "2")

    data = get_ad_by_id(5000)

    return render_template("learnMore.html", row=data)


@app.route('/read')
def read():
    data = get_ad_by_id_foreign_keys(1)

    return render_template("learnMore.html", row=data)


@app.route('/update')
def update():
    update_ad("5000", "titleupdate", "descriptionupdate", "1500", "placeupdate", "20", "1", "2")
    data = get_ad_by_id_foreign_keys(5000)

    return render_template("learnMore.html", row=data)


@app.route('/delete')
def delete():
    delete_ad(5000)

    return "ad deleted"


if __name__ == '__main__':
    app.run(debug=True)
