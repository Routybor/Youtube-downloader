from flask import Flask, request, jsonify, send_from_directory
from main import process_link


app = Flask(__name__)


@app.route('/get-audio', methods=['POST'])
async def run_script():
    data = request.get_json()
    if 'link' not in data or 'option' not in data:
        return jsonify({'error': 'Data not provided'}), 400
    link = data['link']
    option = data['option']
    try:
        audio = await process_link(link, option)
        return jsonify({'audio_url': str(audio)}), 200
    except Exception as e:
        return jsonify({'error': f'Error executing script: {e}'}), 500


@app.route('/media/<path:filename>', methods=['GET'])
def get_file(filename):
    try:
        return send_from_directory('media', filename, as_attachment=True)
    except Exception as e:
        return jsonify({'error': f'Error retrieving file: {e}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
