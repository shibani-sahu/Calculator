from django.shortcuts import render
import math


layout= [
    ['√' , 'pi ' , '^', '!',],
    ['AC', '(' , ')' , '%'],
    ['7' , '8' , '9', '÷' ],
    ['4' , '5' , '6' ,'×' ],
    ['1' , '2' , '3' ,'-' ],
    ['0' , '.' , ' ' ,'+'],
    ['=']
]

def calculate_expression(expression):
    try:
        expression= expression.replace('×', '*').replace('÷', '/')
        expression=expression.replace('pi', str(math.pi)).replace('^', '**')
        expression= expression.replace('%', '/100')

        if '√' in expression:
            expression= expression.replace('√' , 'math.sqrt(')+')'
        
        if '!' in expression:
            expression= expression.replace('!', '')
            expression= str(math.factorial(int(expression)))

        return str(eval(expression))

    except:
        return "Error"

def calculator_view(request):
    expression= ""
    if request.method == 'POST':
        btn = request.POST.get('btn')
        expression = request.POST.get("expression", "")


        if btn== 'AC':
            expression='' 
        elif btn== ' ':
            expression= expression[:-1]
        elif btn == '=':
            expression= calculate_expression(expression)
        else:
            expression += btn      

    return render(request, 'index.html', {"layout": layout, "expression": expression})

# Create your views here.
