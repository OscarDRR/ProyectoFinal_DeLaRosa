from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_promedio', methods=['POST'])
def calcular_promedio():
    if request.method == 'POST':
        numeros = request.form.get('numeros')
        numeros = [float(num) for num in numeros.split(',')]
        promedio = sum(numeros) / len(numeros) if numeros else 0
        return render_template('resultado.html', promedio=promedio)

if __name__ == '__main__':
    app.run(debug=True)
