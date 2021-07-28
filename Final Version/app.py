import pickle
from flask import Flask, render_template, request


app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))



@app.route('/')
def html_linkage():
    return render_template('index.html')


@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":


        parents = request.form['Parents Behaviour']

        if (parents == "Usual"):
            Parents = 2
        elif (parents == "Pretentious"):
            Parents = 1
        elif (parents == "Very Pretentious"):
            Parents = 0

        nursery = request.form['Nursery Status']

        if (nursery == "Critical"):
            Nursery = 0
        elif (nursery == "Improper"):
            Nursery = 1
        elif (nursery == "Not very proper"):
            Nursery = 2
        elif (nursery == "Proper"):
            Nursery = 3
        elif (nursery == "Very Critical"):
            Nursery = 4

        form = request.form['Form']

        if (form == "Complete"):
            Form = 0
        elif (form == "Completed"):
            Form = 1
        elif (form== "Incomplete"):
            Form = 3
        elif (form == "Foster"):
            Form = 2

        children = request.form['Children']

        if (children == "1"):
            Children = 1
        elif (children == "2"):
            Children = 2
        elif (children == "3"):
            Children = 3
        elif (children == "More"):
            Children = 4

        housing = request.form['Housing']

        if (housing == "Convenient"):
            Housing = 0
        elif (housing == "Less Convenient"):
            Housing = 2
        elif (housing == "Critical"):
            Housing = 1

        finance = request.form['Finance']

        if (finance == "Convenient"):
            Finance = 0
        elif (finance == "Inconvenient"):
            Finance = 1

        social = request.form['Social']

        if (social == "Problematic"):
            Social = 1
        elif (social == "Non-Problematic"):
            Social = 0
        elif (social == "Slightly Problematic"):
            Social = 2

        health = request.form['Health']

        if (health == "Recommended"):
            Health = 2
        elif (health == "Priority"):
            Health = 1
        elif (health == "Not Recommended"):
            Health = 0

        prediction = model.predict([
            Parents,
            Nursery,
            Form,
            Children,
            Housing,
            Finance,
            Social,
            Health])
        return render_template('after.html',data = prediction)













if __name__ == '__main__':
    app.run(debug = True)



