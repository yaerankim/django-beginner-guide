# 🔥 django-beginner-guide 🔥
Inflearn의 [Django 초보 가이드 - 실습을 통해 알아보는 장고 입문](https://www.inflearn.com/course/django-%EC%B4%88%EB%B3%B4-%EA%B0%80%EC%9D%B4%EB%93%9C-%EC%8B%A4%EC%8A%B5%EC%9D%84-%ED%86%B5%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-%EC%9E%A5%EA%B3%A0-%EC%9E%85%EB%AC%B8/dashboard)을 보고 간단한 게시판 만들기 실습 진행

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
