from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)


@app.route("/pokered", methods=['GET','POST'])
def sugar():
    if request.method == 'POST':
        nome = request.form["nome"]
        mw = request.form["mw"]
        return render_template('index1.html',nome=nome,mw=mw)
    
    return render_template('index2.html')


@app.route("/komi", methods=['GET','POST'])
def komi():

    res = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/788/penha-sc').content
    soup = BeautifulSoup(res,'html.parser')
    max_temp = soup.find(id='max-temp-1').get_text()
    min_temp = soup.find(id='min-temp-1').get_text    ()

    return render_template('index3.html',max_temp=max_temp,min_temp=min_temp)



if __name__ == '__main__':
    app.run(debug=True)
