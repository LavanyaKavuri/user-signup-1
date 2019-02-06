from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('login_form.html')

@app.route("/login", methods=['POST'])
def login():
    user_name = request.form['user_name']
    return render_template('welcome.html', name=user_name)


@app.route("/form-inputs")
def display_form_inputs():
    return form
form = """
<!DOCTYPE html>
<html>
<body>
    <style>
        br{margin-bottom : 20px}
    </style>
    <form method='POST'>
        <label>Username
            <input name="user-name" type="text" />
        </label>
        <br>
        <label>Password
            <input name="user-password" type="password" />
        </label>
        <br>
        <label>Verify Password
            <input name="password-verify" type="password" />
        </label>
        <br>
        <label>Email
            <input name="user-email" type="email" />
        </label>
        <br>
    </form>
</body>

</html>
"""

@app.route("/form-inputs", methods=['POST'])
def print_form_values():
    resp=""
    for field in request.form.keys():
        resp += "<b>{key}</b>: {value}<br>".format(key=field, value=request.form[field])
        return resp

app.run()