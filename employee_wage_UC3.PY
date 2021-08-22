'''
@Author: Nikita Rai
@Date: 2021-08-19 03:10:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-19 03:10:00
@Title : Check Employee is
Present or Absent
- Use ((RANDOM)) for Attendance
Check
'''
import random
from flask_restful import Resource, Api
from flask import Flask,request

app = Flask(__name__)
api = Api(app)
emp_data = []

class employee(Resource):
    def get(self,name):
        '''
            Description:
                get function is use to only read the data 
            Parameter:
                self and name
            Return:
                the data of index matches with the name
        '''
        for i in emp_data:
            if i['Data'] == name:
                return i
        return {'Data': None}

    def post(self,name):
        '''
            Description:
                post function is use to add the data , if employee is present thr calculate the wage
            Parameter:
                self and name
            Return:
                temprary variable in which i can store the data
        '''
        ISPARTTIME = 1
        ISFULLTIME = 2 
        EMP_RATE_PER_DAY = 20 
        randomCheck = random.randint(1,3)
        if ( ISPARTTIME == randomCheck ) :
            emp_Status= "part time" 
            EMPHRS = 4
            salary = int(EMP_RATE_PER_DAY * EMPHRS)
            Tem_emp_data = {'Data':name,'Attendence' : randomCheck,'Status' : emp_Status , 'Salary' : salary
            
            }
        elif(ISFULLTIME == randomCheck):
            emp_Status= "full time" 
            EMPHRS = 8
            salary = int(EMP_RATE_PER_DAY * EMPHRS)
            Tem_emp_data = {'Data':name,'Attendence' : randomCheck,'Status' : emp_Status, 'Salary' : salary}
        else :
            emp_Status= "absent" 
            salary = 0
            Tem_emp_data = {'Data':name,'Attendence' : randomCheck,'Status' : emp_Status, 'Salary' : salary}

        emp_data.append(Tem_emp_data)
        return Tem_emp_data
    
    def delete(self,name):
        '''
            Description:
                delete is a function which is use to delete(pop) the value 
            Parameter:
               self and name
            Return:
                string value
        '''
        for ind,i in enumerate(emp_data):
            if i['Data'] == name:
                Tem_emp_data = emp_data.pop(ind)
                return {'Note':"Deleted"}
 
api.add_resource(employee,'/Employee_wadge/<string:name>')

if __name__ == '__main__':
    app.run(debug = True)