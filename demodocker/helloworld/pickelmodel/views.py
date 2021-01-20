from django.shortcuts import render
import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
from django.http import HttpResponse

# Create your models here.
def savemodeltopickel(request):
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    
    names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    
    dataframes = pandas.read_csv(url, names=names)
    arrays = dataframes.values
    X = arrays[:,0:8]
    Y = arrays[:,8]
    
    test_size = 0.33
    seed  = 7
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
    
    #Fit the model on training set 
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    
    #save the model to disk
    filename = 'finalized_model.sav'
    pickle.dump(model, open(filename, 'wb'))
    return HttpResponse('Hello Kaka!')