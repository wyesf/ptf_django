from django.shortcuts import render
from .models import Opexseoul
from django.db.models import Count

# Create your views here.
def dashboard(request) :
        
    opex_datas = Opexseoul.objects.values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1).order_by('-name_count')[:6]
    # print(opex_datas)
    for data in opex_datas:
        print(data)

        return render(request, "dashboard/dashboard.html",{"opex_datas":opex_datas})





    # # DB : CountryData 클래스를 통해 DB 데이터 가져오기
    # # 쿼리(디비에서 데이터 가져오는 것) 데이터 변수에 대입
    # opex_datas = Opexseoul.objects.all()
    # print(opex_datas)

    # # form 객체 생성
    # # CountryDataForm() => 객체생성 그리고 앞에 form 달아 선언해줌
    # form = OpexseoulForm()
    # opex_datas = Opexseoul.objects.all()

    # # html 템플릿 작성
    # # 쿼리 데이터 식별자를 html 템플릿에 렌더링 (f5 눌러줘야 함)
    # # response 해주기
    # context = {
    #     "opex_datas" : opex_datas,
    #     "form" : form,
    # }




    #   # 중복처리
    #   cnt = []
    #   cnt.append(row[1])
    #   print(cnt)
    #   # cntnm = {}
    #   # for i in cnt :
    #   #   try : cntnm[i] += 1
    #   #   except : cntnm[i] = 1
    #   # print(cntnm)

    #   # resname = row[2]
    #   # print(row[2].count(resname))

