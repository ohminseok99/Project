from django.shortcuts import render,redirect
import requests
import os
def kakaoPay(request):
    return render(request,'kakaopay/kakao.html')

def kakaoPayLogic(request):
    _admin_key = os.environ.get('ADMIN_KEY')
    _url = f'https://kapi.kakao.com/v1/payment/ready'
    _headers = {
        'Authorization': f'KakaoAK {_admin_key}',
    }
    _data = {
        'cid': 'TC0ONETIME',
        'partner_order_id':'partner_order_id',
        'partner_user_id':'partner_user_id',
        'item_name': request.GET.get("name"),
        'quantity':'1',
        'total_amount': request.GET.get('price'),
        'vat_amount':'200',
        'tax_free_amount':'0',
        # 내 애플리케이션 -> 앱설정 / 플랫폼 - WEB 사이트 도메인에 등록된 정보만 가능합니다
        # * 등록 : http://IP:8000
        'approval_url':'http://127.0.0.1:8000/kakaoPay/paySuccess',
        'fail_url':'http://127.0.0.1:8000/kakaoPay/payFail',
        'cancel_url':'http://127.0.0.1:8000/kakaoPay/payCancle'
    }
    _res = requests.post(_url, data=_data, headers=_headers)
    _result = _res.json()
    request.session['tid'] = _res.json()['tid']
    request.session['product_name'] = request.GET.get("name")
    request.session['product_price'] = request.GET.get('price')
    return redirect(_result['next_redirect_pc_url'])

def paySuccess(request):
    _url = 'https://kapi.kakao.com/v1/payment/approve'
    _admin_key = 'be2190ad4b18f87304163c08961dfb5a'
    _headers = {
        'Authorization': f'KakaoAK {_admin_key}'
    }
    _data = {
        'cid': 'TC0ONETIME',
        'tid': request.session['tid'],
        'partner_order_id': 'partner_order_id',
        'partner_user_id': 'partner_user_id',
        'pg_token': request.GET['pg_token']
    }
    _res = requests.post(_url, data=_data, headers=_headers)
    _result = _res.json()
    if _result.get('msg'):
        return redirect('kakaoPay/payFail')
    else:
        return render(request, 'kakaopay/paySuccess.html', {'name':request.session['product_name'], 'price' : request.session['product_price']})

def payFail(request):
    return render(request, 'index.html', {'name': request.session['product_name'], 'price' : request.session['product_price']})
def payCancle(request):
    return render(request,'kakaopay/payFail.html', {'name':request.session['product_name'], 'price' : request.session['product_price']})