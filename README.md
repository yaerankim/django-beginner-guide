# ๐ฅ django-beginner-guide ๐ฅ
Inflearn์ [Django ์ด๋ณด ๊ฐ์ด๋ - ์ค์ต์ ํตํด ์์๋ณด๋ ์ฅ๊ณ  ์๋ฌธ](https://www.inflearn.com/course/django-%EC%B4%88%EB%B3%B4-%EA%B0%80%EC%9D%B4%EB%93%9C-%EC%8B%A4%EC%8A%B5%EC%9D%84-%ED%86%B5%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-%EC%9E%A5%EA%B3%A0-%EC%9E%85%EB%AC%B8/dashboard)์ ๋ณด๊ณ  ๊ฐ๋จํ ๊ฒ์ํ ๋ง๋ค๊ธฐ ์ค์ต ์งํ

## **tutorial - Project**
* __init__.py
* asgi.py
* settings.py
  * ํ๋ก์ ํธ์ ์ ์ฒด์ ์ธ ํ๊ฒฝ์ค์  ๊ด๋ จ
  * ์์ฑํ APP์ธ community๊ฐ ๊ตฌ๋ํ  ์ ์๋๋ก INSTALLED_APPS์ ์ถ๊ฐํจ
* urls.py
  * user๊ฐ ์ ๊ทผํ  ์ ์๋ ๋งํฌ ์ค์  ๊ด๋ จ
* wsgi.py

## **community - App**
* __init__.py
* admin.py
* apps.py
* forms.py
  * user๊ฐ ์๋ ฅํ form์ field๋ช ์ค์ 
* models.py
  * ๊ฐ Model์ field(column) ์ต์ ์ค์ 
* tests.py
* views.py
  * APP์ ๊ฐ ๊ธฐ๋ฅ๋ค(write, list, view) ๊ตฌํ

### **templates**
* list.html
  * ๊ฒ์๋ฌผ list up
* view.html
  * ๊ฐ ๊ฒ์๋ฌผ์ ์ธ๋ถ ๋ด์ฉ ๋ณด์ฌ์ค
* write.html
  * user๊ฐ ์์ฑํ  ์ ์๋ form ๋ณด์ฌ์ค

## **manage.py**
* bash ์ฐฝ์์ ์น์๋ฒ ์คํ ๋ฑ๊ณผ ๊ฐ์ ๋ช๋ น์ด ์คํ ์์ ์ฌ์ฉ
