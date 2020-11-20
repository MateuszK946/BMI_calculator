from flask import Flask, request
from flask import render_template
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def bmi():
    if request.method =='POST' and 'weight' in request.form and 'height' in request.form and request.form.get('weight') != '' and request.form.get('height') != '':
        w = float(request.form.get('weight'))
        h = float(request.form.get('height'))
        if h>0 and w>0:
            bmi = w/((h/100)**2)
            if (bmi < 17):
                text = "Wychudzenie!"
            elif (bmi >= 17 and bmi < 18.5):
                text = "Niedowaga!"
            elif (bmi >= 18.5 and bmi < 25):
                text = "Waga prawidłowa!"
            elif (bmi >= 25 and bmi < 30):
                text = "Nadwaga!"
            elif (bmi >= 30 and bmi < 40):
                text = "Otyłość!"
            elif (bmi >= 40):
                text = "Skrajna otyłość!"
            return render_template('bmi_form.html', bmi=bmi, w=w, h=h, text=text)
        else:
            text = 'Waga i wzrost muszą być dodatnie! Podane wartości są nieprawidłowe!'
            return render_template('bmi_form.html', text=text)
    return render_template('bmi_form.html')
if __name__ == '__main__':
    app.run(debug=True)