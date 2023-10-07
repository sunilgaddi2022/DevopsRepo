from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    print(request.args.get('num1'))
    return 'Hello, World'

@app.route('/pricing')
def pricing():
    return "1000"

@app.route('/', methods=['POST', 'PUT']) #GET, POST, PUT, Delete
def helloWorld():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    num3 = int(request.args.get('num3'))
    return str(num1+num2+num3)

@app.route('/identify',methods=['POST'])
def palli():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if username=='prashant' and password=='admin123':
        return "Welcome"
    else:
        return "Wrong Credentials"
    
@app.route('/student',methods=['GET','POST'])
def name():
    name = request.args.get('name')
    age = 0
    for i in student:
        if name == i['name']:
            age = i['age']
    return str(age)    

"""
@app.route('/checkpallindrome',methods=['GET','POST'])
def name():
    number = int(request.args.get('num1'))
    temp = number
    rev = 0
    while (number > 0):
        dig = number % 10
        rev = rev * 10 + dig
        number = number // 10
    if (temp == rev):
        return "The number is a palindrome!"
    else:
        return "The number isn't a palindrome!"	

"""   


if __name__ == '__main__':
    app.run(debug=True)
