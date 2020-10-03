from django.shortcuts import render
from django.http import HttpResponse


def interest(request):
    if 'amount' in request.GET:
        amount = float(request.GET['amount'])
        rate = float(request.GET['rate'])
        interest = amount * rate / 100
        return render(request, 'interest.html',
                      {'amount': amount, 'rate': rate, 'interest': interest})
    else:
        return render(request, 'interest.html')
