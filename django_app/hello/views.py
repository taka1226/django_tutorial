from django.shortcuts import render
from .models import Friend
from .models import Test
from .forms import HelloForm

def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': 'all friends.',
        'form': HelloForm(),
        'data': [],
    }


    query = Test.objects.filter(fields__contains=[{'name': 'sample2', 'value': "True"}])
    print(query.get())


    if (request.method == 'POST'):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = HelloForm(request.POST)
    else:
        params['data'] = Friend.objects.all().values('id', 'name')
    return render(request, 'hello/index.html.django', params)
