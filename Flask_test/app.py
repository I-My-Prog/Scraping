from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    html = render_template('index.html',a = '20-0401 16:00',b = '2768',c = '双日',d = '267')
    return html

if __name__ == "__main__":
    app.run()