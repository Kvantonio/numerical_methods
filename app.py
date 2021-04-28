from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)


def generate_form(n, A, B) -> object:
    res = ''
    j = n
    if not A:
        A = [0 for _ in range(n * n)]
        B = [0 for _ in range(n)]
    for i in range(n*n):

        print('A ', A[i])
        print('B ', A[round(j / n)-1])
        if i == j:
            res += f" = <input type='number' value='{B[round(j/n)-1]}' name='mat_b' max='99' min='-99' class='nums dop'>"
            res += '<br>'
            j += n
        res += f"<input type='number' name='mat_a' max='99' min='-99' class='nums' value='{int(A[i])}'>"
    res += f" = <input type='number' value='{int(B[round(j/n)-1])}' name='mat_b' max='99' min='-99' class='nums dop'>"
    res += '<br>'
    res += '<button type="submit">Calculate</button>'
    return res

methods = ['/kramer/']


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        print(f)
        f.save('./uploads/uploaded_file.txt')


@app.route('/method/<int:method>/size/<int:size>', methods=['GET', 'POST'])
def methods(method, size):
    if request.method == 'POST':
        print(request.form.getlist('mat_a'))
        print(request.form.getlist('mat_b'))
        method = request.form.get('sel-method')
        #return render_template('method.html', text=generate_form(size,request.form.getlist('mat_a'),request.form.getlist('mat_b'))
    if request.method == 'GET':
        return render_template('method.html', text=generate_form(size))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        method = request.form.get('sel-method')
        size = request.form.get('sel-size')
        #print(request.form.getlist('my_checkbox'))
        return redirect(f'/method/{int(method)}/size/{int(size)}')

    return render_template('index.html')
