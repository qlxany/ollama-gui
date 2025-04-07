from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.json['input']
    try:
        # Replace 'ollama run gemma:2b' with your actual command to run the model
        result = subprocess.run(['ollama', 'run', 'gemma:2b', user_input], capture_output=True, text=True, encoding='utf-8')
        output = result.stdout
    except Exception as e:
        output = f"Error: {str(e)}"
        
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)