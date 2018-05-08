from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    msg = 'hello world'
    ret = HttpResponse(msg)
    return ret

def hello_tpl(request):

    tpl = 'todos/hello_tpl.html'
    arr = [
        {'id': 1, 'name': 'asdf'},
        {'id': 2, 'name': 'ghjk'},
        {'id': 3, 'name': 'zxcv'},
        {'id': 4, 'name': 'qwer'}
    ]
    info = {'arr': arr}
    ret = render(request, tpl, info)
    return ret