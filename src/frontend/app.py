from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save-code', methods=['POST'])
def save_code():
    code_data = request.get_json()
    print("Received data:", code_data)  # Print received data
    code = code_data.get('code')
    file_name = code_data.get('fileName', 'default_code_data.json')  # Default to a file name if not provided

    with open(file_name, 'w') as json_file:
        json.dump({'code': code}, json_file)

    return jsonify({"message": "Code saved to JSON"})

@app.route('/build', methods=['POST'])
def build_code():
    try:
        code_data = request.get_json()
        print("Received data post:", code_data)  # Print received data
        code = code_data.get('code')
        file_name = code_data.get('fileName', 'code_data.json')  # Default to a file name if not provided

        # Process the code and build it, you can use the 'code' and 'file_name' parameters

        return jsonify({"message": "Code build successful", "stdout": "standadrd output", "stderr": "standard error"})
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"})

@app.route('/view-data', methods=['GET'])
def view_data():
    try:
        received_data = {
            'save-code': request.get_json(silent=True),
            'build-code': request.get_json(silent=True)
        }
        return jsonify(received_data)
    except:
        return jsonify({"message": "No data received"})

if __name__ == '__main__':
    app.run(debug=True, port=30410)
