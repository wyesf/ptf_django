from django.db import models

# Create your models here.
# - 데이터 형 정하기 : 컬럼
# - DB 설계
#   1. 테이블
#   2. 컬럼
# - Data 작업 시작
# ex) str = integer 2022-01-01


class Opexseoul(models.Model) :
    regDate = models.DateField()
    restaurant = models.CharField(max_length=300)
    personnel = models.IntegerField()
    price = models.IntegerField()
    borough = models.CharField(max_length=500, default = '')

    # class 안에 있는 메서드
    def __str__(self) :
        return f"{self.restaurant}--{self.borough}"
    
    # class 내부 클래스 정의
    class Meta :
        verbose_name_plural = "Opex"