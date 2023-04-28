from flask import Flask, render_template, request, send_file
from pydub import AudioSegment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files['file']
    format = request.form['format']

    audio = AudioSegment.from_file(file)
    converted = audio.export(format=format)

    return send_file(converted, as_attachment=True, attachment_filename='converted.' + format)

if __name__ == '__main__':
    app.run(debug=True)