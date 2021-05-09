import json  # noqa: I201

import numpy as np  # noqa: I201
import plotly  # noqa: I201
import plotly.graph_objects as go  # noqa: I201


def generateErrors(X, method):
    res = f'<p>Method {method} could not find a solution because:<p> <ul>'
    if -2 in X:
        res += "<li> Matrix has no diagonally dominant</li>"

    if -3 in X:
        res += "<li> Matrix does not positive-definite matrix</li>"

    if -4 in X:
        res += "<li> Spectral matrix radius > 1</li>"

    res += '</ul>'
    return res


def generate_form(n, method, A=[], B=[], rd=3):
    res = ''
    if not A:
        A = [[0 for _ in range(n)] for _ in range(n)]
        B = [0 for _ in range(n)]
    res += "  <p></p>Round: <input type='number' min='0'" + \
           f" value='{rd}' name='round' class='nums'></p>"
    for i in range(len(A)):
        for j in range(len(A)):
            res += "<input type='number' name='mat_a'" + \
                   f" max='99' min='-99' class='nums' value='{A[i][j]}'>"

        res += f" = <input type='number' value='{B[i]}'" + \
               " name='mat_b' max='99' min='-99' class='nums dop'>"
        res += '<br>'
    if method in (2, 4):
        res += "Iterations: <input type='number' name='iter'" + \
               " max='10000' min='1' class='nums' value='100'>"

    return res


def generateTable(a, b, n, y):
    h = (b - a) / n
    x = [round(item, 5) for item in np.arange(a, b + h, h)]
    fig = go.Figure(data=[go.Table(header=dict(values=['X', 'Y']),
                                   cells=dict(values=[x, y]))
                          ])
    fig.update_layout(width=600)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def generateIntegrateTable(res):
    fig = go.Figure(data=[
        go.Table(header=dict(values=['Method', 'Area']),
                 cells={'values': [
                     ['Left Rectangles', 'Right Rectangles',
                      'Central Rectangles',
                      'Trapeziums', 'Simpson'], res], 'align': 'left'})
    ])
    fig.update_layout(width=550)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
