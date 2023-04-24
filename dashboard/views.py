from django.shortcuts import render
from .models import Opexseoul
from django.db.models import Count, Sum

# Create your views here.
def dashboard(request) :

    # 용산 / 중구 / 종로 / 영등포 / 서초
    seocho = Opexseoul.objects.filter(borough='서초구').values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1).order_by('-name_count')[:6]
    yongsan = Opexseoul.objects.filter(borough='용산구').values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1).order_by('-name_count')[:6]
    jung = Opexseoul.objects.filter(borough='중구').values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1).order_by('-name_count')[:6]
    jongno = Opexseoul.objects.filter(borough='종로구').values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1).order_by('-name_count')[:6]
    yeongdeungpo = Opexseoul.objects.filter(borough='영등포구').values("restaurant").annotate(name_count=Count('restaurant')).filter(name_count__gt=1).order_by('-name_count')[:6]


    test = {
        "seocho":seocho,
        "yongsan":yongsan,
        "jung":jung,
        "jongno":jongno,
        "yeongdeungpo":yeongdeungpo,
    }


# # value
#     yongsan1 = Opexseoul.objects.filter(borough='용산구').values(Sum('price')).order_by('-sum_price')
#     test2 = {
#         "yongsan1":yongsan1
#     }


    return render(request, "dashboard/dashboard.html",test)




    # a = {'borough': "서초구"}

    
    # if a in opex_datas :

    #     # print(opex_datas)
    #     for data in opex_datas:
    #         print(data)

            # return render(request, "dashboard/dashboard.html",{"opex_datas":opex_datas})





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

