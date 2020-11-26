from django.shortcuts import render
from analise_de_imoveis.core.forms import CoreForm
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
    form = CoreForm()
    if request.method == 'POST':
        return webscraping(request)
    return render(request, 'analise_de_imoveis/index.html', {'form': form})


def pegarlinks(estado, tipo_busca, tipo, headers):
    links = []
    for i in range(100):
        page = requests.get(f"https://{estado}.olx.com.br/imoveis/{tipo_busca}/{tipo}?o={i}", headers=headers,
                            timeout=5)
        soup = BeautifulSoup(page.content, 'html.parser')
        tags_a = soup.select('a[class="fnmrjs-0 fyjObc"]')

        for tag_a in tags_a:
            dict = tag_a.attrs
            links.append(dict['href'])
        print(i, page.status_code)

    return links


def verificarlinksunicos(links):
    links_unicos = []
    for link in links:
        if link not in links_unicos:
            links_unicos.append(link)
    return links_unicos

def webscraping(request):
    form = CoreForm(request.POST)
    if form.is_valid():
        estado = form.cleaned_data['estado']
        tipo_busca = form.cleaned_data['tipo_busca']
        tipo = form.cleaned_data['tipo']
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
        links = pegarlinks(estado, tipo_busca, tipo, headers)
        links_unicos = verificarlinksunicos(links)
        return render(request, 'analise_de_imoveis/index.html', {'form': form, 'links': links_unicos})
    else:
        return render(request, 'analise_de_imoveis/index.html', {'form': form})
