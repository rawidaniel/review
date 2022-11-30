```


   ,---,           ,---,        ,---,       ,---,  .--.--.                             ,-.----.       ,---,.               ,---,    ,---,.           .---. 
  '  .' \        .'  .' `\    .'  .' `\  ,`--.' | /  /    '.                           \    /  \    ,'  .' |       ,---.,`--.' |  ,'  .' |          /. ./| 
 /  ;    '.    ,---.'     \ ,---.'     \ |   :  :|  :  /`. /             ,---,.        ;   :    \ ,---.'   |      /__./||   :  :,---.'   |      .--'.  ' ; 
:  :       \   |   |  .`\  ||   |  .`\  |:   |  ';  |  |--`            ,'  .' |        |   | .\ : |   |   .' ,---.;  ; |:   |  '|   |   .'     /__./ \ : | 
:  |   /\   \  :   : |  '  |:   : |  '  ||   :  ||  :  ;_            ,---.'   ,        .   : |: | :   :  |-,/___/ \  | ||   :  |:   :  |-, .--'.  '   \' . 
|  :  ' ;.   : |   ' '  ;  :|   ' '  ;  :'   '  ; \  \    `.         |   |    |        |   |  \ : :   |  ;/|\   ;  \ ' |'   '  ;:   |  ;/|/___/ \ |    ' ' 
|  |  ;/  \   \'   | ;  .  |'   | ;  .  ||   |  |  `----.   \        :   :  .'         |   : .  / |   :   .' \   \  \: ||   |  ||   :   .';   \  \;      : 
'  :  | \  \ ,'|   | :  |  '|   | :  |  ''   :  ;  __ \  \  |        :   |.'           ;   | |  \ |   |  |-,  ;   \  ' .'   :  ;|   |  |-, \   ;  `      | 
|  |  '  '--'  '   : | /  ; '   : | /  ; |   |  ' /  /`--'  /        `---'             |   | ;\  \'   :  ;/|   \   \   '|   |  ''   :  ;/|  .   \    .\  ; 
|  :  :        |   | '` ,/  |   | '` ,/  '   :  |'--'.     /                           :   ' | \.'|   |    \    \   `  ;'   :  ||   |    \   \   \   ' \ | 
|  | ,'        ;   :  .'    ;   :  .'    ;   |.'   `--'---'                            :   : :-'  |   :   .'     :   \ |;   |.' |   :   .'    :   '  |--"  
`--''          |   ,.'      |   ,.'      '---'                                         |   |.'    |   | ,'        '---" '---'   |   | ,'       \   \ ;     
               '---'        '---'                                                      `---'      `----'                        `----'          '---"      
                                                                                                                                                           



```
                                                                                                                                                           
# ADDIS-REVIEW     
__a website where you can review foods in addis__
#

## Description
`Addis-RevieW` is a food rating and commenting website made for those who live in Ethiopia, near Addis Ababa

### How does it work?
The website lists top restaurant in the capital city of Ethiopia and makes it easy for visitors, food travlers and tourists to chose where to dine before going there.
The user can read reviews and see the average rate of the food which makes it easy for choosing restaurant that is best in town ! The user can also create an account and
 write review and rate the foods he chose.

### For whom?
This is made for everyone who enjoys trying out new restaurants but also curious on the money they spend. i.e. Food Travlers, Mukbang lovers, Tourists, Grooms, Visitors ...

### Inspiration
We always see other similar websites on the internet, but lets be honest, they don't have Ethiopian food and you can't use them. That is when we thought there should be a website like that where
 our people enjoy both traditional and junk foods. :)

## How to run the project
The website is made using docker. There are three containers to run on your machine if you like to run it on your PC. 

### Running the DataBase container
>The website uses `MySQL`.
>To run it using docker
```bash
docker pull Addis-review-FD
```
```bash
docker exec -it Addis-review-FD bash
```
to run it interactively or 
```bash
docker exec Addis-review-FD
```
to run it on the background

### Running the APIs container
>The website uses `RESTful`.
>To run it using docker
```bash
docker pull Addis-review-API
```
```bash
docker exec -it Addis-review-API bash
```
to run it interactively or 
```bash
docker exec Addis-review-API
```
to run it on the background
#
Or to run it using flask
- first you need to install required dependencies by running the following command, assuming you have python3 installed on your machine
```python
pip3 -r install requirements.txt
```
- Now you can run the app safely
```python
flask run
```
but as you know, this is depricated to use it in production environment



### Running the Forntend container
>The website uses `MySQL`.
>To run it using docker
```bash
docker pull Addis-review-FntEnd
```
```bash
docker exec -it Addis-review-FntEnd bash
```
to run it interactively or 
```bash
docker exec Addis-review-FntEnd
```
to run it on the background
...
if you have NGINX on your server and you know how to use it, you should use gunicorn for the application server.

## How to use the project
It is pretty simple as using any website on the internet. But here are the steps:
- [Create a new account](http://18.205.104.232:5000/signup).
- This will direct you to login page. You need to login for extra security [Login](http://18.205.104.232:5000/login).
- Now you will be redirected to the `RESTAURANT` page, where you get to see lists of the restaurants in the database. You need to choose one to look there food.
- Now you see the food, there rate and price. click on which ever you want to see reviews and rate as well as to put your own review and rate.
- There you go ! You did it.

## Credits and Remarks
* Thank you all

## How to contribute to the project 
You should contact us:
> See the developer sections below.

## Developers
* [ABENEZER ESHETIE - GitHub](https://github.com/EbenGitHub)
* [RAWI DANIEL - GitHub](https://github.com/rawidaniel)
* [IKRAM AWOL - GitHub](https://github.com/rawidaniel)
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
```



   __    __    _  _           ___  ____     ___  _____  _   _  _____  ____  ____    ___ 
  /__\  (  )  ( \/ )   ___   / __)( ___)   / __)(  _  )( )_( )(  _  )(  _ \(_  _)  | __)
 /(__)\  )(__  )  (   (___)  \__ \ )__)   ( (__  )(_)(  ) _ (  )(_)(  )   /  )(    |__ \
(__)(__)(____)(_/\_)         (___/(____)   \___)(_____)(_) (_)(_____)(_)\_) (__)   (___/




```
