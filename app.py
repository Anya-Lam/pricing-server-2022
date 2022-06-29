from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

pricing_database = {
    'theritz': '560'
}

reviews_database = {
    'ritz': [2, 4, 6, 7, 6, 5, 7]
}


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hotel/price/<hotel_id>')
@cross_origin(origin='*')
def get_hotel_price(hotel_id):
    return 'No price found :('


@app.route('/hotel/reviews/<hotel_id>')
@cross_origin(origin='*')
def get_hotel_reviews(hotel_id):
    return str(5)


if __name__ == '__main__':
    app.run()
