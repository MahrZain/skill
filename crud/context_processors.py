from .models import crudUser
def alldata(request):
    c = crudUser.objects.all()
    return ({'data': c})