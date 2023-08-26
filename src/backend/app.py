from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/build', methods=['POST'])
def build_endpoint():
    try:
        data = request.json
        if data is None:
            return jsonify({"error": "Invalid JSON data"}), 400
        
        # Assuming you want to process the data from the POST request
        # You can replace this with your actual processing logic
        response_data = {"message": "Received POST request", "data": data}
        #response_data = {"message": "Received POST request", "data": ""}
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
