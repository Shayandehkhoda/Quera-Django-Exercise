from django.http import HttpResponse

def sad(response, name):
    return HttpResponse(f'Nobody likes you, {name}!')

def happy(response, name, times):
    assert type(times) == int, 'num must be a number'
    assert times > 0, 'num must be positive'
    return HttpResponse(f'You are great, {name} :)<br>' * times)