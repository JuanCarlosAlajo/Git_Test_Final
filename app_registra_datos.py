import json
from flask import Flask, Response, request
from utils import get_last_price
from cnx_base_datos import MongoDriver
from datetime import datetime




app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h2>Hola.. Mi pais Ecuador!</h2>"

#--
@app.route("/api/stock")
def get_stock_price():
    company_ticker = request.args.get("ticker")
    mongodb = MongoDriver()
    try:
        last_price = get_last_price(ticker=company_ticker)
    except ValueError as error:
        return {"company_ticker": company_ticker, "price": None, 'error': str(error)}

    response_raw = {
            "INSTITUCION": company_ticker,
            "AVALUO": last_price,
            "FECHA_REGISTRO": datetime.now()
            }

    mongodb.insert_record(record=response_raw, username="REGISTROS")

    return Response(json.dumps(response_raw), mimetype='application/json')



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)