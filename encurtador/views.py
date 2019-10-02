from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
# view baseada em função (FBV)
def function_based_view(request, *args, **kwargs):
    return HttpResponse("Olá mundo!")


# view baseada em classe (CBV)
class UrlCBView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("olá novamente!")


class HomeView(View):
    def get(self, request, *args, **kwargs):
        retorno = """
        <html>
            <head>
                <title>Home View</title>
            </head>
            <body>
                <h1>Página Principal</h1>
            </body>
        </html>
        """
        return HttpResponse(retorno)


def ano_view(request, ano, *args, **kwargs):
    pagina = f"""
    <html>
        <head><title>Exibir Ano</title></head>
        <body>
            <h1>{ano}</h1>
        </body>
    </html>"""
    return HttpResponse(pagina)