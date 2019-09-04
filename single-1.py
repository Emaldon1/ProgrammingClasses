print('Erika','Maldonado-Rosado','emaldon1@uncc.edu')
from flask import Flask, render_template
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)
    
@app.route("/")
def welcome():
    return"<h1>Welcome!</h1>"

@app.route("/home")
def home():
    return "<h2>Hello, this is Erika's home page!</h2>"

@app.route("/AminoAcids")
def AminoAcids():
    aminos = {"Tyrosine" : "Y", "Tryptophan" : "W"}
    return render_template("aminos.html",aminos=aminos)
    
@app.route("/bargraph.png")
def bargraph():
    fig = create_bargraph()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_bargraph():
    from random import seed
    from random import randint
    seed(1)
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x = ['Purple','Yellow','Blue']
    y = [randint(0, 100), randint(0, 100), randint(0, 100)]
    axis.bar(x,y)
    return fig
    
if __name__ == '__main__':
    app.run(debug = True)