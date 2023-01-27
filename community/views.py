from django.shortcuts import render
from community.forms import *

# Create your views here.
def write(request):
	if request.method == 'POST':
		form = Form(request.POST) # request.POST에 있는 내용을 그대로 변수 form에 넣음
		if form.is_valid(): # form에 있는 데이터가 유효하다면
			form.save() # Database에 form의 field가 저장됨
            
	# method가 POST가 아니라면
	else:
		form = Form() # 그냥 form을 출력해줌
	return render(request, 'write.html', {'form':form})

def list(request):
    articleList = Article.objects.all()
    return render(request, 'list.html', {'articleList':articleList})

def view(request, num="1"):
	# Article Model의 object들 중에 id가 num인 아이템 하나를 갖고 온다(get)는 뜻
	article = Article.objects.get(id=num)
	return render(request, 'view.html', {'article':article})