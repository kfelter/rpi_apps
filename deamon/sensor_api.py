from flask import Flask, jsonify
import sense_hat, datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify(
        time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        temp_c=sense_hat.get_temperature(),
        humidity_rh=sense_hat.get_humidity(),
        pressure_millibars=sense_hat.get_pressure(),
    )
print('sensor api deamon running on port 8000')

app.run(port=8000)

