from django.db import models

# Create your models here.
# 각 Model(DB) table의 field(column) 설정
class Article(models.Model):
	name = models.CharField(max_length=50) # 저자 이름
	title = models.CharField(max_length=50) # 책 이름
	contents = models.TextField() # 책 내용
	url = models.URLField() # 책 url
	email = models.EmailField() # 저장 이메일
	# auto_now_add=True -> 게시물이 생성되면 자동으로 cdate 입력되도록 설정
	cdate = models.DateTimeField(auto_now_add=True) # 게시물이 생성된 날짜 및 시간