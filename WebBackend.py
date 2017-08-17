import pygal
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/bob')
def bob():
    file = open("130/130.txt", "r")
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    date = []
    total = [a, b, c, d, e, f]
    lst = file.readlines()
    file.close()
    count = 0
    for i in lst:
        total[count].append(int(i.replace("\n","").replace(".","")))
        count += 1
        if count==6:
            count = 0
    for i in range(len(a)):
        date.append("1/" + str(i + 1))
    graph = pygal.Line()
    graph.title = 'Emotional Status by Day for Bob'
    graph.x_labels = date
    graph.add('Joy', a)
    graph.add('Sadness', b)
    graph.add('Disgust', c)
    graph.add('Anger', d)
    graph.add('Surprise', e)
    graph.add('Fear', f)
    graph_data = graph.render_data_uri()
    file2 = open("130/130Social.txt", "r")
    number = file2.readline()
    return render_template("graphing.html", graph_data=graph_data) + number

@app.route('/alice')
def alice():
    file = open("16/16.txt", "r")
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    date = []
    total = [a, b, c, d, e, f]
    lst = file.readlines()
    file.close()
    count = 0
    for i in lst:
        total[count].append(int(i.replace("\n","")))
        count += 1
        if count==6:
            count = 0
    for i in range(len(a)):
        date.append("1/" + str(i + 1))
    graph = pygal.Line()
    graph.title = 'Emotional Status by Day for Alice'
    graph.x_labels = date
    graph.add('Joy', a)
    graph.add('Sadness', b)
    graph.add('Disgust', c)
    graph.add('Anger', d)
    graph.add('Surprise', e)
    graph.add('Fear', f)
    graph_data = graph.render_data_uri()
    file2 = open("16/16Social.txt", "r")
    number = file2.readline()
    return render_template("graphing.html", graph_data=graph_data) + number

if __name__ == "__main__":
    app.run(debug=True)
