from django.shortcuts import render
from joblib import load

model = load('./savedModels/model.joblib')

def predictor(request):
    if request.method == 'POST':
        sepal_lenght = request.POST['sepal_length']
        sepal_width = request.POST['sepal_width']
        petal_lenght = request.POST['petal_length']
        petal_width = request.POST['petal_width']

        y_pred = model.predict([[sepal_lenght, sepal_width, petal_lenght, petal_width]])
        # print(y_pred)
        if y_pred[0] == 0:
            y_pred = 'Setosa'
        elif y_pred[0] == 1:
            y_pred = 'Verscicolor'
        else:
            y_pred = 'Verginica'
        return render(request, 'main.html',{'result':y_pred})
    return render(request, 'main.html')