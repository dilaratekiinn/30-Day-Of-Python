
import re


website = "https://www.linkedin.com/feed/"
course = "Python Dersi : Baştan sona python"

 # 1- 'course' karakter dizisinde kaç karakter bulunmalıdır ?

result = len (course)

 # 2- ' website '  içinde www karakterlerini alın. 

result = website [7:10]

 # 3- 'website' içinde com karakterlerini alın. 

result = website[21:24]


 # 4- ' course ' içinde ilk 15 ve son 15 karakterlerini alın. 

result = course [0:15]
result = course [:15]
result = course [ -15: -1]

 #  5- 'course' ifadesindeki karakterlerini tersten yazdırınız.

result = course [::-1]


name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

 #  6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın. 
# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'

result = "Benim adım" + name + "" + surname +",Yaşım" + str(age) + "ve mesleğim" +job 

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

s= 'Hello world'
s= s[0:6] + 'W' + s[ -4:]

print (s)
# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

result ='abc' *3 

print(result)


