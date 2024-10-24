from flask import Flask, render_template, request, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'spk_secret_key'


def main():
    return render_template('main.html')



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')