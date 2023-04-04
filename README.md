# 🔥 django-beginner-guide 🔥

## **tutorial - Project**
* __init__.py
* asgi.py
* settings.py
  * 프로젝트의 전체적인 환경설정 관련
  * 생성한 APP인 community가 구동할 수 있도록 INSTALLED_APPS에 추가함
* urls.py
  * user가 접근할 수 있는 링크 설정 관련
* wsgi.py

## **community - App**
* __init__.py
* admin.py
* apps.py
* forms.py
  * user가 입력한 form의 field명 설정
* models.py
  * 각 Model의 field(column) 옵션 설정
* tests.py
* views.py
  * APP의 각 기능들(write, list, view) 구현

### **templates**
* list.html
  * 게시물 list up
* view.html
  * 각 게시물의 세부 내용 보여줌
* write.html
  * user가 작성할 수 있는 form 보여줌

## **manage.py**
* bash 창에서 웹서버 실행 등과 같은 명령어 실행 시에 사용
