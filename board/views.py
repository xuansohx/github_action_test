from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import requests

from .models import GithubLottery

def fetch_lotto(request):
    # url 접근(요청)이 와야만 실행되는 함수
    g = GithubLottery.objects.last()
    if g:
        no = g.no # + 1
    else:
        no = 888

    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=888'
    res = requests.get(url)
    data = res.json() # 데이터파싱
    g = GithubLottery.objects.create(
        no=data['drwNo'],
        win_amount=data['firstWinamnt'],
    )
    return_json = serializers.serialize(g)
    return JsonResponse({'status':200}) # 내보내기