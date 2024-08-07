from flask import Flask, request, render_template, jsonify, send_file
import os
import requests
import hack2
import hack

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index_bkp.html')

@app.route('/main_bkp.html')
def main_bkp():
    return render_template('main_bkp.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            print(f"File name: {file.filename}")
            print(f"File path: {file_path}")
            resp = hack.generate(file_path)


            response_file_path = os.path.join(UPLOAD_FOLDER, "response.txt")
            with open(response_file_path, "w") as response_file:
                for response in resp:
                    response_file.write(response.text + "\n")

            # Return the file as a downloadable file
            return send_file(response_file_path, as_attachment=True, download_name="response.txt")

    except requests.exceptions.RequestException as e:
        print(f"Error making request to Gemini API: {e}")
        return jsonify({"error": "Error making request to Gemini API"}), 500

    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({"error": "Unexpected error occurred"}), 500

@app.route('/upload2', methods=['POST'])
def upload_file2():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            print(f"File name: {file.filename}")
            print(f"File path: {file_path}")
            resp = hack2.generate(file_path)


            response_file_path = os.path.join(UPLOAD_FOLDER, "response2.txt")
            with open(response_file_path, "w") as response_file:
                for response in resp:
                    response_file.write(response.text + "\n")

            # Return the file as a downloadable file
            return send_file(response_file_path, as_attachment=True, download_name="response2.txt")

    except requests.exceptions.RequestException as e:
        print(f"Error making request to Gemini API: {e}")
        return jsonify({"error": "Error making request to Gemini API"}), 500

    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({"error": "Unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)