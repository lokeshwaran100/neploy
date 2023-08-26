from flask import Flask, request, jsonify
import tempfile
import subprocess
import os

app = Flask(__name__)

@app.route('/build', methods=['POST'])
def build_endpoint():
    try:
        data = request.json
        if data is None or "code" not in data:
            return jsonify({"error": "Invalid request data"}), 400

        code = data["code"]
        temp_filename = data["file"]

        with open(temp_filename, 'wb') as f:
            f.write(code.encode())
        # Save the code to a temporary .py file
        #with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
        #    temp_filename = temp_file.name
        #    temp_file.write(code.encode())

        # Execute the code
        try:
            result = subprocess.run(["neo3-boa", "compile", temp_filename], capture_output=True, text=True)
            os.remove(temp_filename)  # Delete the temporary file

            response_data = {
                "stdout": result.stdout,
                "stderr": result.stderr
            }

            if result.returncode != 0:
                response_data["message"] = "Build Failed"
            elif 'ERROR' in result.stderr:
                response_data["message"] = "Build Failed"
            else:
                response_data["message"] = "Build is Successful"
            return jsonify(response_data), 200
        except Exception as e:
            os.remove(temp_filename)  # Delete the temporary file
            return jsonify({"error": str(e)}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
