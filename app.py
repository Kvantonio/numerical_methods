import os  # noqa: I201

import numpy as np  # noqa: I201
from flask import Flask, abort, redirect, render_template, \
    request  # noqa: I201, I100
from werkzeug.utils import secure_filename  # noqa: I201, I100

from diff import Euler, rungeKuttaFourth, \
    rungeKuttaSecond, rungeKuttaThird  # noqa: I201, I100
from dop import checkRoots, generateIntegration, generate_rand, \
    graph, normaliseSets, parse_file  # noqa: I201, I100
from gauss import gauss  # noqa: I201, I100
from generates import generateErrors, generateIntegrateTable, generateTable, \
    generate_form  # noqa: I201, I100
from integrate import Simpson, centralRectangle, leftRectangle, \
    rightRectangle, trapezium  # noqa: I201, I100
from setsOperations import difference, entrance, merge, \
    symmetricalDifference, traversal  # noqa: I201, I100
from jacobi import jacobi  # noqa: I201, I100
from jordan_gauss import jordan_gauss  # noqa: I201, I100
from kramer import kramer  # noqa: I201, I100
from zadel import zadel  # noqa: I201, I100

from nums import Graph  # noqa: I201, I100



from graphviz import Digraph



app = Flask(__name__)

UPLOAD_FOLDER = './upload/'
ALLOWED_EXTENSIONS = {'txt'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

methods = ['Kramer', 'Gauss', 'Zadel', 'Jordan-Gauss', 'Jacobi']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/sprint02/integrate_method/', methods=['GET', 'POST'])
def integrate():
    if request.method == 'POST':
        method = int(request.form.get('sel-method'))
        func = int(request.form.get('sel-func'))
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        n = int(request.form.get('n'))

        if a > b:
            a, b = b, a

        functions = [(lambda x: 1 / np.log(x)), (lambda x: np.exp(-x)),
                     (lambda x: np.sin(x)), (lambda x: np.exp(pow(-x, 2))),
                     (lambda x: np.exp((-4 * x) - pow(x, 3)))]

        if method == 0:
            res = leftRectangle(functions[func], a, b, n)
        elif method == 1:
            res = rightRectangle(functions[func], a, b, n)
        elif method == 2:
            res = centralRectangle(functions[func], a, b, n)
        elif method == 3:
            res = trapezium(functions[func], a, b, n)
        elif method == 4:
            res = Simpson(functions[func], a, b, n)
        elif method == 5:
            res = [
                leftRectangle(functions[func], a, b, n),
                rightRectangle(functions[func], a, b, n),
                centralRectangle(functions[func], a, b, n),
                trapezium(functions[func], a, b, n),
                Simpson(functions[func], a, b, n)
            ]
            return render_template('integrate.html',
                                   data=True,
                                   graphJSON=generateIntegrateTable(res),
                                   image=generateIntegration(
                                       a, b, functions[func]),
                                   a=a, b=b, n=n
                                   )

        return render_template('integrate.html',
                               res=res,
                               image=generateIntegration(
                                   a, b, functions[func]
                               ),
                               a=a, b=b, n=n
                               )

    return render_template('integrate.html', a=0, b=0, n=0)


@app.route('/sprint02/diff_method/', methods=['GET', 'POST'])
def diff():
    if request.method == 'POST':
        method = int(request.form.get('sel-method'))
        func = int(request.form.get('sel-func'))
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        y0 = float(request.form.get('y'))
        n = int(request.form.get('n'))

        if a > b:
            a, b = b, a

        functions_d = [(lambda x, y: -1 * (x * y)),
                       (lambda x, y: x + y),
                       (lambda x, y: (3 * x - 12 * x * x) * y),
                       (lambda x, y: pow(x, 2) - (y * 2))
                       ]

        if method == 0:
            Y = Euler(functions_d[func], a, b, y0, n)
        elif method == 1:
            Y = rungeKuttaSecond(functions_d[func], a, b, y0, n)
        elif method == 2:
            Y = rungeKuttaThird(functions_d[func], a, b, y0, n)
        elif method == 3:
            Y = rungeKuttaFourth(functions_d[func], a, b, y0, n)

        h = (b - a) / n
        x = [round(item, 5) for item in np.arange(a, b + h, h)]
        return render_template('diff.html',
                               data=True,
                               graphJSON=generateTable(a, b, n, Y),
                               image=graph(x, Y),
                               a=a, b=b, n=n, y0=y0
                               )

    return render_template('diff.html', a=0, b=0, n=0, y0=0)


@app.route('/sprint02/methods/', methods=['GET', 'POST'])
def methods_menu_s2():
    return render_template('s2_methods_menu.html')


# Sprint01
@app.route('/sprint01/methods/', methods=['GET', 'POST'])
def methods_menu():
    if request.method == 'POST':
        method = request.form.get('sel-method')
        size = request.form.get('sel-size')
        if int(method) == 0 and int(size) > 4:
            err = "matrix > 4 use another method"
            return render_template('methods_menu.html', err=err)
        else:
            return redirect(f'/method/{int(method)}/size/{int(size)}')

    return render_template('methods_menu.html')


# Sprint01
@app.route('/method/<int:method>/size/<int:size>', methods=['GET', 'POST'])
def methods_logic(method, size):
    if size > 10:
        abort(404)

    if method == 0:
        if size > 4:
            abort(404)

    if request.method == 'POST':
        if request.form.get('rand'):
            A, B = generate_rand(size, -10, 10)
        else:
            B = [int(i) for i in request.form.getlist('mat_b')]
            A = [int(i) for i in request.form.getlist('mat_a')]
            A = [A[i:i + len(B)] for i in range(0, len(A), len(B))]

        rd = int(request.form.get('round'))
        if not rd:
            rd = 3
        file = request.files['fil']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            size, A, B = parse_file('upload/' + filename)

        X = None
        haveAnswer = True
        if method == 0:
            X = kramer(A.copy(), B.copy(), rd)
        elif method == 1:
            X = gauss(A.copy(), B.copy(), rd)
        elif method == 2:
            it = int(request.form.get('iter'))
            haveAnswer, X = zadel(A.copy(), B.copy(), rd, it)
        elif method == 3:
            X = jordan_gauss(A.copy(), B.copy(), rd)
        elif method == 4:
            it = int(request.form.get('iter'))
            haveAnswer, X = jacobi(A.copy(), B.copy(), rd, it)

        if X == -1:
            answer = 'Matrix is degenerate'
        elif not haveAnswer:
            answer = generateErrors(X, methods[method])
        else:
            answer = [f' X{i} = {x} <br>' for i, x in enumerate(X)]
            answer = ''.join(answer)
            if request.form.get('checkRoots'):
                if checkRoots(A, B, X):
                    answer += '<br>Roots is true'
                else:
                    answer += '<br>Roots is false'

        return render_template('method.html',
                               text=generate_form(
                                   size,
                                   method=method,
                                   A=A,
                                   B=B,
                                   rd=rd),
                               title=methods[method], answer=answer)
    else:
        return render_template('method.html',
                               text=generate_form(size, method=method),
                               title=methods[method])


@app.route('/dm/', methods=['GET', 'POST'])
def dm():
    if request.method == 'POST':
        data_A, data_B = request.form.get('set_a'), request.form.get('set_b')
        A, B = normaliseSets(data_A, data_B)
        method = int(request.form.get('meth'))

        if method == 0:
            res = entrance(A.copy(), B.copy())
            res = [str(res)]
        elif method == 1:
            res = merge(A.copy(), B.copy())
        elif method == 2:
            res = traversal(A.copy(), B.copy())
        elif method == 3:
            res = difference(A.copy(), B.copy())
        elif method == 4:
            res = difference(B.copy(), A.copy())
        elif method == 5:
            res = symmetricalDifference(B.copy(), A.copy())
        elif method == 6:
            res = entrance(B.copy(), A.copy())
            res = [str(res)]

        if res:
            res = ', '.join(res)
        else:
            res = 'Empty'
        return render_template('dm.html', A=data_A, B=data_B, data=res)

    return render_template('dm.html')


@app.route('/dm2/', methods=['GET', 'POST'])
def dm2():
    if request.method == 'POST':
        graph = Graph()
        data = request.form.get('data')

        graph.parseGraph(data)
        degree = graph.calcDegree()
        im = graph.getGraph()
        preim = graph.getPreimage()
        adMatrix = graph.adjacencyMatrixToTable()
        inMatrix = graph.incidenceMatrixToTable()
        t = graph.drawGraph()
        image = graph.graphImgToBytes(t)



        return render_template('dm2.html',
                               data=True,
                               degree=degree,
                               im=im,
                               preim=preim,
                               adMatrix=adMatrix,
                               inMatrix=inMatrix,
                               image=image)

    return render_template('dm2.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
