from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Welcome():
    return "Try adding /play/*number of your choice*/*color of your choice* !:)"

@app.route('/play')
def index():
    return render_template("index.html", times = 3, background_color = 'skyblue')

@app.route('/play/<number>')
def repeat(number):
    return render_template("index.html", times = int(number), background_color = 'skyblue')

@app.route('/play/<number>/<color>')
def colorChange(number, color):
    return render_template("index.html", times = int(number), background_color = color)


# Left it here just because. 
@app.errorhandler(404) # only works for error 404, page not found 404 status explicitly
def page_not_found(e):
    return ('Sorry! No response. Double check your url and try again :)'), 404

if __name__=="__main__":
    app.run(debug=True)