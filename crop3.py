from flask import Blueprint,request,render_template
import pickle
crop3=Blueprint('crop3',__name__)

#importing pickle files
model = pickle.load(open('pickle/classifier.pkl','rb'))
ferti = pickle.load(open('pickle/fertilizer.pkl','rb'))

@crop3.route('/input1')
def input1():
    return render_template('input1.html')

@crop3.route('/predicted',methods=['POST'])
def predicted():
    temp = request.form.get('temp')
    humi = request.form.get('humid')
    mois = request.form.get('mois')
    soil = request.form.get('soil')
    crop = request.form.get('crop')
    nitro = request.form.get('nitro')
    pota = request.form.get('pota')
    phosp = request.form.get('phos')
    input = [int(temp),int(humi),int(mois),int(soil),int(crop),int(nitro),int(pota),int(phosp)]

    res = ferti.classes_[model.predict([input])]

    return render_template('result3.html',x = ('Predicted Fertilizer is {}'.format(res)))

