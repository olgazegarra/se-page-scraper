from data import Kappa
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/api/commands', methods=["GET"])
def parse_commands():    
    caller = Kappa()
    result = caller.get_commands()
    return jsonify(result=result)

if __name__ == "__main__":
    app.run()
