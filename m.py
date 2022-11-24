
from models import *

# rawi = User(first_name='rawi',last_name='daniel',email='rawi@gmail.com',password='rawi12345', is_admin=True)
# rawi.save()
# li = {'first_name': 'ikram','last_name':'awol','email':'ikram@gmail.com','password':'ikram12345'}
# ikram = User(**li)
# ikram.save()
# abeni = User(first_name='abeni',last_name='eshite',email='abeni@gmail.com',password='abeni123')

# abeni.save()


# kategna = Restaurant(name="kategna", contact="+251945678972",image="kategna.jpg", address= "Bole",description="""All of our foods are prepared with fresh spices 
# blended daily and our sauces are prepared as ordered. The friendly staff and warm decor makes KATEGNA the 
# perfect place to relax with family and friends. While we offer many traditional Ethiopian meat dishes, 
# we are sensitive to the needs of our vegan customers. Traditionally we prepare many authentic Ethiopian 
# dishes that are vegan, without the use of any animal products.""")
# kategna.save()

# natani = Restaurant(name="Natani", contact="+251967893890",image="natani.jpg", address= "Bole",description="""staff and warm decor makes KATEGNA the 
# perfect place to relax with family and friends. While we offer many traditional Ethiopian meat dishes, 
# we are sensitive to the needs of our vegan customers. Traditionally we prepare many authentic Ethiopian 
# dishes that are vegan, without the use of any animal products.""")
# natani.save()

firfir = Food(name="INJERA FIRFIR", image="firfir.jpg", price=234.67, recipe="injera, hot spice berbere, clarified butter" ,description="""Injera Firfir is an Ethiopian food typically 
served for breakfast. It is generally made with shredded flat injera, spiced clarified butter (called niter kibbeh 
in Amharic), and the hot spice berbere. The injera is torn into small bite size rolls or pieces, marinated in the 
prepared stew.""", restaurant_id="25e6212c-13b3-43aa-a77f-2e7a11725324")
firfir.save()

salad= Food(name="TOMATO SALAD", image="tomatosalad.jpg", price=334.90, recipe="tomatoes, onions, chilies" ,description="""The tomato salad always fresh and crisp, with so 
much flavor to them. The tomatoes were diced, mixed with some onions and chilies, and seasoned with salt, and lemon 
juice.""", restaurant_id="25e6212c-13b3-43aa-a77f-2e7a11725324")
salad.save()

shiro = Food(name="SHIRO WOT", image='shiro.jpg', price=190.78 ,recipe= "bean floir, garlic and onions",description="""Shiro wot is made from chickpea and broad bean 
flour, mixed with garlic and onions, and made into a thick, almost paste like substance. The chickpeas give the stew a
beautiful texture and nutty flavor. It’s very smooth and spreadable,almost the consistency of a thickened pureed soup""", 
restaurant_id="aea789b4-bf78-4e49-8717-e732dc18fdaf")
shiro.save()

fish = Food(name="SHIRO FASTING KATEGNA SPECIAL WITH FISH", image="fasting.jpg", price=400.00 ,recipe= "fish, vegan" ,description="""It’s essentially a mixed combination platter of 
injera topped with a variety of strictly vegan curries and vegetables available. The mixed Kategna vegetarian plate 
offers a little bit of everything so that you get some real variety in your meal.""", restaurant_id="aea789b4-bf78-4e49-8717-e732dc18fdaf")
fish.save()

