from flask import Flask, request, jsonify
from funcs import *
app = Flask(__name__)

allowed = ['decimal', 'hexadecimal', 'binary', 'octadecimal']

@app.route("/")
def hello():
    return "Hello World!"


def check_required_args(required_args):
    missing_args = []
    for arg in required_args:
        if not request.args.get(arg):
            missing_args.append(arg)
    return missing_args

conversion_functions = {
    ('decimal', 'binary'): decimal_to_binary,
    ('decimal', 'octal'): decimal_to_octal,
    ('decimal', 'hexadecimal'): decimal_to_hex,
    ('binary', 'decimal'): binary_to_decimal,
    ('binary', 'octal'): binary_to_octal,
    ('binary', 'hexadecimal'): binary_to_hex,
    ('octal', 'decimal'): octal_to_decimal,
    ('octal', 'binary'): octal_to_binary,
    ('octal', 'hexadecimal'): octal_to_hexa,
    ('hexadecimal', 'decimal'): hexa_to_decimal,
    ('hexadecimal', 'binary'): hexa_to_binary,
    ('hexadecimal', 'octal'): hexa_to_octal
}


@app.route("/convert")
def convert():
    required_args = ['data','from', 'to']
    missing_args = check_required_args(required_args)

    
    if missing_args:
        return jsonify({
            'error': 'Missing required parameters',
            'missing_parameters': missing_args
        }), 400
    
    v_from = request.args.get("from")
    v_to = request.args.get("to")
    number = request.args.get("data")
    try:
        if v_from not in allowed:
            return jsonify({"error": "Invalid input format"}), 400
        if v_to not in allowed:
            return jsonify({"error": "Invalid output format"}), 400
        if v_from == v_to:
            return jsonify({"error": "Input and Output formats cannot be the same"}), 400
        if not number:
            return jsonify({"error": "Data should not be empty"}), 400
        
        conversion_func = conversion_functions.get((v_from, v_to))

        if v_from == 'decimal':
            number = int(number)
        else:
            number = str(number)

        converted = conversion_func(number)
        return jsonify({
            "status": "success",
            "input": f"{number} ({v_from})",
            "converted": f"{converted} ({v_to})"
        }), 200
        

    except ValueError:
        return jsonify({"error": "Invalid number format"}), 400
    except Exception as e:
        return jsonify({"error": f"An unknown error occurred: {str(e)}"}), 500

    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
