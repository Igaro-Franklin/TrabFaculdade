from django.shortcuts import HttpResponse

def minha_view(request):
    return HttpResponse("Realizado com sucesso a atividade")