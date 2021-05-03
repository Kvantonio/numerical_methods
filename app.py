import os
from flask import Flask, request, redirect, render_template
from werkzeug.utils import secure_filename

from gauss import gauss
from kramer import kramer
from zadel import zadel
from jordan_gauss import jordan_gauss
from jacobi import jacobi
from dop import parse_file, generate_rand

app = Flask(__name__)

UPLOAD_FOLDER = './upload/'
ALLOWED_EXTENSIONS = {'txt'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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
    res += f"  <p></p>Round: <input type='number' min='0' value='{rd}' name='round' class='nums'></p>"
    for i in range(len(A)):
        for j in range(len(A)):
            res += f"<input type='number' name='mat_a' max='99' min='-99' class='nums' value='{A[i][j]}'>"

        res += f" = <input type='number' value='{B[i]}' name='mat_b' max='99' min='-99' class='nums dop'>"
        res += '<br>'
    if method in (2, 4):
        res += f"Iterations: <input type='number' name='iter' max='10000' min='1' class='nums' value='100'>"

    return res


methods = ['Kramer', 'Gauss', 'Zadel', 'Jordan-Gauss', 'Jacobi']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/method/<int:method>/size/<int:size>', methods=['GET', 'POST'])
def methods_logic(method, size):
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

        return render_template('method.html',
                               text=generate_form(size, method=method, A=A, B=B, rd=rd),
                               title=methods[method], answer=answer)
    else:
        return render_template('method.html',
                               text=generate_form(size, method=method),
                               title=methods[method])


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        method = request.form.get('sel-method')
        size = request.form.get('sel-size')
        # print(request.form.getlist('my_checkbox'))
        return redirect(f'/method/{int(method)}/size/{int(size)}')

    return render_template('index.html')
