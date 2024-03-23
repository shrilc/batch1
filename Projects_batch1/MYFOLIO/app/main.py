from flask import Flask, render_template

app = Flask('MyFolio')

# Routes
# decorators


@app.route('/')  # This serves root path
def index():
    return render_template("index.html")


@app.route('/resume')
def download_resume():
    return render_template("download_resume.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


if __name__ == "__main__":
    app.run(debug=True)

