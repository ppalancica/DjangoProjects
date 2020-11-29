from django.shortcuts import render

# Create your views here.

# def home_screen_view(request):
#     print(request.headers)
#     return render(request, 'personal/home.html', {})

def home_screen_view(request):
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

    list_of_items = []
    list_of_items.append('first item')
    list_of_items.append('second item')
    list_of_items.append('third item')

    context = {}
    context['items'] = list_of_items

    return render(request, 'personal/home.html', context)
