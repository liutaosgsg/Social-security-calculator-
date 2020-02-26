"""

"""
from django.shortcuts import render
from django.http import HttpResponse
def shebao_view(request):
    if request.method=='GET':
        return render(request,'shebao.html')
    elif request.method=='POST':
        base_money=int(request.POST.get('base_money','0'))
        print(base_money)
        if base_money<=3082 or base_money>=23118:
            tips='输入数字超范围'
            return render(request,'shebao.html',locals())
        op=request.POST.get('op','0')
        if op=='1':
            area='城镇户口'
            person_endowment=base_money*0.08
            person_unemployment=base_money*0.002
            person_injury=0
            person_maternity=0
            person_medical=base_money*0.02+3
            person_housing=base_money*0.12
            person_moeny=person_endowment+person_unemployment+person_medical+person_housing
            co_endowment=base_money*0.19
            co_unemployment=base_money*0.008
            co_injury=base_money*0.005
            co_maternity=base_money*0.008
            co_medical=base_money*0.01
            co_housing=base_money*0.12
            co_moeny=co_endowment+co_unemployment+co_injury+co_maternity+co_medical+co_housing
            total_money=person_moeny+co_moeny
            return render(request, 'shebao_result.html', locals())
        elif op=='2':
            area='农村户口'
            person_endowment=base_money*0.08
            person_unemployment=base_money*0
            person_injury=0
            person_maternity=0
            person_medical=base_money*0.02+3
            person_housing=base_money*0.12
            person_moeny=person_endowment+person_unemployment+person_medical+person_housing
            co_endowment=base_money*0.19
            co_unemployment=base_money*0.008
            co_injury=base_money*0.005
            co_maternity=base_money*0.008
            co_medical=base_money*0.01
            co_housing=base_money*0.12
            co_moeny=co_endowment+co_unemployment+co_injury+co_maternity+co_medical+co_housing
            total_money=person_moeny+co_moeny
            return render(request, 'shebao_result.html', locals())