from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def sintactico(request):
    #print('CORRECTO')
   # return HttpResponse("Sintáctico Estructural...<3")
    template_name="sintactico/sintactico.html"
    return render(request,template_name,{})