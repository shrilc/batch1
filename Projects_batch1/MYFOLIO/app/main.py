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
    cards = [
        {
            'title': 'Project1',
            'image': 'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=500&h=300&dpr=2',
            'description': 'Some desc'
        },
        {
            'title': 'Project2',
            'image': 'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=500&h=300&dpr=2',
            'description': 'Some desc'
        },
        {
            'title': 'Project3',
            'image': 'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=500&h=300&dpr=2',
            'description': 'Some desc'
        },
        {
            'title': 'Project3',
            'image': 'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=500&h=300&dpr=2',
            'description': 'Some desc'
        },
        {
            'title': 'Project3',
            'image': 'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=500&h=300&dpr=2',
            'description': 'Some desc'
        },
        {
            'title': 'Project3',
            'image': 'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=500&h=300&dpr=2',
            'description': 'Some desc'
        }
    ]
    return render_template("projects.html", cards=cards)


if __name__ == "__main__":
    app.run(debug=True)

