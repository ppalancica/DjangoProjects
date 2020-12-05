from django.shortcuts import render
# from personal.models import Question

from account.models import Account

# Create your views here.

def home_screen_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    return render(request, 'personal/home.html', context)

# def home_screen_view(request):
#     questions = Question.objects.all()
#     context = {}
#     context['questions'] = questions
#     return render(request, 'personal/home.html', context)

# def home_screen_view(request):
#     print(request.headers)
#     return render(request, 'personal/home.html', {})

# def home_screen_view(request):
    # 1st way:
    #
    # context = {
    #     'some_string' = 'Some string value that we want to pass to the view',
    #     'some_number' = 123
    # }
    #
    # 2nd way:
    # context = {}
    # context['some_string'] = 'Some string value that we want to pass to the view'
    #
    #
    # 3rd way:
    # list_of_items = []
    # list_of_items.append('first item')
    # list_of_items.append('second item')
    # list_of_items.append('third item')
    #
    # context = {}
    # context['items'] = list_of_items
    #
    # return render(request, 'personal/home.html', context)
