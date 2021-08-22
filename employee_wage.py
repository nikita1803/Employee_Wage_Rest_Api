'''
@Author: Nikita Rai
@Date: 2021-08-21 08:10:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-21 08:10:00
@Title : Check Employee is
Present or Absent
- Use ((RANDOM)) for Attendance
and calculate the wage 
'''
from employee_wage_uc4 import employee
import random
from flask_restful import Resource, Api, abort , reqparse
from flask import Flask, json,request,jsonify

app = Flask(__name__)
api = Api(app)

Emp_details = {
    1: {"employee_name": "Nikita","Attendence":"2","Work_hours":"20","Total_Salary": "800"},
}
task_post_args = reqparse.RequestParser()
task_post_args.add_argument("employee_name" , type=str, help = "employee_name." , required=True)
task_post_args.add_argument("Attendence" , type=str, help = "Attendence." )
task_post_args.add_argument("Work_hours" , type=str, help = "Work_hours." )
task_post_args.add_argument("Total_Salary" , type=str, help = "employee_salary." )

task_put_args = reqparse.RequestParser()
task_put_args.add_argument("employee_name" , type=str, help = "employee_name.")
task_put_args.add_argument("Attendence" , type=str, help = "Attendence.")
task_put_args.add_argument("Work_hours" , type=str, help = "Work_hours.")
task_put_args.add_argument("Total_Salary" , type=str, help = "employee_salary.")

class ToDoList(Resource):
    '''
        Description:
            Todo list is a class which is use to show all the data related to employees.
        Methods: 
            get method is used
    '''
    def get(self):
        return Emp_details

class ToDo(Resource):
    '''
        Description:
            Todo is a class which is use to get , post , put patch and delete the data 
        Methods: 
            get , post , delete , put
    '''
    def get(self,employee_id):
        '''
            Description:
                get function is use to only read the data 
            Parameter:
                self and employee_id
            Return:
                employee details
        '''
        return Emp_details

    def post(self,employee_id):
        '''
            Description:
                post function is use to store the value 
            Parameter:
                self and employee_id
            Return:
                employee details of employee id
        '''
        args = task_post_args.parse_args()
        if employee_id in Emp_details:
            error = "Employee already exsists"
            return jsonify(error)
        EMP_RATE_PER_DAY = 20 
        TOTAL_SALARY = 0
        NUM_OF_WORKING_DAYS = 20
        MAX_HRS_IN_MONTH = 100
        TOTAL_EMP_HR = 0
        TOTAL_WORKING_DAYS = 0
        EMP_RATE_PER_HR = 20
        randomCheck = random.randint(1,3)
        switcher = {
                1: 8,
                2: 4,
                3: 0,
            }
        while ( TOTAL_EMP_HR<100 and TOTAL_WORKING_DAYS < NUM_OF_WORKING_DAYS ) :
          TOTAL_WORKING_DAYS+=1
          empHrs = switcher.get(randomCheck,"employee wadge")
          TOTAL_EMP_HR = empHrs + TOTAL_EMP_HR
        salary = ( TOTAL_EMP_HR * EMP_RATE_PER_HR)
        Emp_details[employee_id] = {"employee_name": args["employee_name"],"Attendence" : randomCheck,"Work_hours" : TOTAL_EMP_HR, "Total_Salary": salary}
        return Emp_details[employee_id]

    def put(self, employee_id):
        '''
            Description:
                put function is use to update the data of employee 
            Parameter:
                self and employee_id
            Return:
                employee details of employee id
        '''
        args = task_put_args.parse_args()
        if employee_id not in Emp_details:
            abort(404, message="Employee doesn't exist, cannot update")
        if args['employee_name']:
            Emp_details[employee_id]["employee_name"] = args["employee_name"]
        if args['Attendence']:
            Emp_details[employee_id]['Attendence'] = args['Attendence']
        if args['Work_hours']:
            Emp_details[employee_id]['Work_hours'] = args['Work_hours']
        if args["Total_Salary"]:
            Emp_details[employee_id]['Total_Salary'] = args['Total_Salary']
        return Emp_details[employee_id]

    def delete(self, employee_id):
        '''
            Description:
                delete function is use to delete the data 
            Parameter:
                self and employee_id
            Return:
                employee details of employee id
        '''
        del Emp_details[employee_id]
        return Emp_details
api.add_resource(ToDo, '/emp/<int:employee_id>')
api.add_resource(ToDoList , '/Emp_details')

if __name__ == '__main__':
    app.run(port = 5000,debug = True)