from django.views.generic import ListView
import requests
import json
# Create your views here.

class ListResults(ListView):

    template_name = 'base.html'

    def get_queryset(self):
        data = requests.get(
        'https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')

        json_data = json.loads(data.content)
        queryset = list()

        for info in json_data['cand']:
            if info['seq'] in ['1', '2']:
                queryset.append(
                    {'candidato':info['nm'],
                    'votos':info['vap'],
                    'porcentagem':info['pvap']
                    })
        return queryset

