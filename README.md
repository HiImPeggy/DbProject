# DbProject
1.	切至cmd
2.	Scripts\activate.bat
3.	進入至虛擬環境
4.	Python manage.py runserver
5.	查URLS
   
![image](https://github.com/HiImPeggy/DbProject/assets/171018168/b5f57500-a16e-4648-ad18-7f18e19750be)

Menu -> 進入網站
Admin-> 進入後端
Path 中的menu是在view.py中定義的class
 
![image](https://github.com/HiImPeggy/DbProject/assets/171018168/a3abdd7d-3dff-42e2-b0b2-31f80af0c43e)

Views.py中要連結至html

![image](https://github.com/HiImPeggy/DbProject/assets/171018168/2194852f-d61d-4790-9147-237fb25e4545)


Html在template的資料夾中

(1) 開發階段 (DEBUG=True)
首先，在開發階段時，因為static files經常性的修改，因此先讀取STATICFILES_DIRS的設定。

 ![image](https://github.com/HiImPeggy/DbProject/assets/171018168/b4e06b9b-e2b1-434c-b547-f174dae07399)

然後，這些html中要使用static資料夾內的資源，請記得加入tag。

 ![image](https://github.com/HiImPeggy/DbProject/assets/171018168/c2f119b8-526f-4bc2-9076-c52fcd378945)



(2) 佈建正式環境 (DEBUG=False)
在正式環境時，請加入STATIC_ROOT的設定，請注意STATIC_ROOT與STATICFILES_DIRS的名稱不能重複！只要Debug設為False，一定要加入這個設定，否則網頁無法正常開啟。

 ![image](https://github.com/HiImPeggy/DbProject/assets/171018168/61114510-ba23-4418-94e3-0efb7a18ec5c)

接著，請執行指令，將static裡面的資料輸出到新的資料夾staticfiles內。
python manage.py collectstatic

參考: 
https://chenuin.blogspot.com/2018/10/django-static-filescss-javascript-images.html

注意：
(1)	Setting.py中的更動
1. 使template運作

 ![image](https://github.com/HiImPeggy/DbProject/assets/171018168/b967846c-549e-4da9-a2cf-d33cfa7ce923)

2.使得static資料夾中的assets image可被使用

 ![image](https://github.com/HiImPeggy/DbProject/assets/171018168/380e32fe-0d50-49b7-8160-ca9f6c9686a3)

 ![image](https://github.com/HiImPeggy/DbProject/assets/171018168/f8a93fd6-fbbf-4cbf-b11b-f5a9bfcca378)


(2)	Html中要加入 load static

 ![image](https://github.com/HiImPeggy/DbProject/assets/171018168/50320baf-fb2d-4ad5-a688-eb26663606a9)

