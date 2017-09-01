from flask import jsonify
from flask import request
from FlaskWebProject import app

empDB=[
 {
 'id':'101',
 'name':'Manoj Kumar',
 'title':'Technical Leader'
 },
 {
 'id':'201',
 'name':'Amit Singh',
 'title':'Sr Software Engineer'
 }
 ]


@app.route('/api/employee',methods=['GET'])
def getAllEmp():
    return jsonify({'emps':empDB})


@app.route('/api/employee/<empId>',methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId) ] 
    return jsonify({'emp':usr})


@app.route('/api/employee/<empId>',methods=['PUT'])
def updateEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if 'name' in request.json : 
        em[0]['name'] = request.json['name']
    if 'title' in request.json:
        em[0]['title'] = request.json['title']
    return jsonify({'emp':em[0]})


@app.route('/api/employee',methods=['POST'])
def createEmp():
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'title':request.json['title']
    }
    empDB.append(dat)
    return jsonify(dat)


@app.route('/api/employee/<empId>',methods=['DELETE'])
def deleteEmp(empId):
    em = [ emp for emp in empDB if (emp['id'] == empId) ]
    if len(em) == 0:
       abort(404)
    empDB.remove(em[0])
    return jsonify({'response':'Success'})
