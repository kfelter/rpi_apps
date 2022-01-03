from flask import Flask, jsonify
import sense_hat, datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify(
        time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        temp_c=sense_hat.temperature,
        humidity_rh=sense_hat.humidity,
        pressure_millibars=sense_hat.pressure,
    )
print('sensor api deamon running on port 8000')

app.run(port=8000)

