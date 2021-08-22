'''
@Author: Nikita Rai
@Date: 2021-08-19 08:10:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-19 08:10:00
@Title : Check Employee is
Present or Absent
- Use ((RANDOM)) for Attendance
Check and calculate the wage using switcher
'''
import random
from flask_restful import Resource, Api
from flask import Flask,request

app = Flask(__name__)
api = Api(app)
emp_data = []
class employee(Resource):
    '''
        Description:
            employee is a class which is use to get post and delete the data 
        Methods: 
            get , post , delete
    '''
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
                post function is use to add the data , if employee is present thr calculate the wage using switch case
            Parameter:
                self and name
            Return:
                temprary variable in which i can store the data
        '''
        EMP_RATE_PER_DAY = 20 
        TOTAL_SALARY = 0
        NUM_OF_WORKING_DAYS = 20
        randomCheck = random.randint(1,3)
        switcher = {
                1: 8,
                2: 4,
                3: 0,
            }
        empHrs = switcher.get(randomCheck,"employee wadge")
        salary=(empHrs*EMP_RATE_PER_DAY)
        TOTAL_SALARY = (salary * NUM_OF_WORKING_DAYS)
        Tem_emp_data = {'Data':name,'Attendence' : randomCheck,'Salary' : salary, 'Total Salary': TOTAL_SALARY}
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
 
api.add_resource(employee,'/Employee_switch/<string:name>')

if __name__ == '__main__':
    app.run(debug = True)