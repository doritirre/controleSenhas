from flask import Flask, render_template, request, redirect


app = Flask(__name__)
x = 0
lista = [1,2,3]


@app.route('/teste', methods=['GET','POST'])
def index2():
    return render_template('senhas.html', n1=lista[0], n2=lista[1], total=lista[2])

@app.route('/mudar', methods=['POST'])
def request_data():
    return render_template('senhas.html', n1=lista[0]+1, n2=lista[1], total=lista[2])


#@app.route('/inicio')
#def index():
#    return render_template('inicio.html', titulo='Controle de Senhas')



if __name__== '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)