from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/sugar", methods=['GET','POST'])
def sugar():
    if request.method == 'POST':
        nome = request.form["nome"]
        return render_template('index.html',nome=nome)
    
    return render_template('oder.html')



if __name__ == '__main__':
    app.run(debug=True)
