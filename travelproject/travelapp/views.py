from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Teams


def demo(request):
    obj=Place.objects.all()
    obj1=Teams.objects.all()
    return render(request, "index.html",{'result':obj,'result1':obj1})

#
# def calculate(request):
#     if request.method == 'POST':
#         num1 = float(request.POST['num1'])
#         num2 = float(request.POST['num2'])
#
#         addition_result = num1 + num2
#         subtraction_result = num1 - num2
#         multiplication_result = num1 * num2
#
#         if num2 != 0:
#             division_result = num1 / num2
#         else:
#             division_result = 'Cannot divide by zero'
#
#         return render(request, "result.html", {
#             'addition_result': addition_result,
#             'subtraction_result': subtraction_result,
#             'multiplication_result': multiplication_result,
#             'division_result': division_result
#         })
#
#     return HttpResponse("Method not allowed")
