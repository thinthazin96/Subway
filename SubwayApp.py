from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/train')
def serve_xml():
    return send_from_directory('static', 'SubwayRSSTest.xml', mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True)


