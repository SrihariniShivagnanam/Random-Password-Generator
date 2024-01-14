from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


@app.route('/', methods=['GET', 'POST'])
def index():
    generated_password = ''
    if request.method == 'POST':
        password_length = int(request.form.get('password_length', 12))
        generated_password = generate_password(password_length)
    return render_template('index.html', generated_password=generated_password)


if __name__ == "__main__":
    app.run(debug=True)
