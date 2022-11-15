
# from models import *

# # rawi = User(first_name='rawi',last_name='daniel',email='rawidaniel@gmail.com',password='1122344')
# # rawi.save()
# li = {'first_name': 'ikram','last_name':'awol','email':'ikramawol@gmail.com','password':'1122344'}
# ikram = User(**li)
# ikram.save()
# abeni = User(first_name='abeni',last_name='eshite',email='abenieshite@gmail.com',password='1122344')



# abeni.save()
# print("OK")
# # # storage.save()
# # # ba = BaseModel()
# # # print(ba.id)


# # restaurants = storage.all('Restaurant')
# # foods = storage.all('Food')
# # #for obj in restaurants.values():
# # #   for food in foods.values():
# # #       obj.foods.append(food)
# # # storage.save()
# # # print("ok")
# #   # for fo in obj.foods:
# #   #   print(fo.name)

# # for obj in foods.values():
# #   for fo in obj.restaurants:
# #     print(fo.name)

# # user = storage.count()
# # print(user)
# from models import storage
# users = storage.all("User")
# for user in users.values():
#     storage.delete(user)
# storage.save()
# print("ok")