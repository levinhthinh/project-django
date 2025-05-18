from django.shortcuts import render

# Create your views here.
def homepage(request):
    context= {
        'Name': 'Lê Vĩnh Thịnh',
        'Age': '15',
        'Birth': '10/01',
        'Hobby': [
            'ngủ',
            'ăn'
            'chơi game',
            'thể dục',
            'học tập'
        ],
        'Email':'123@gmail.com',
        'Sdt':'1234056'
    }
    return render(request,"myapp/home.html",context)