# import sys
# print(type(sys.argv[1]))
# print(sys.argv[1])

# r ='{"he": "hello"}'
# for i in eval(r).values():
#   print(i)

class Home:
    def __init__(self) :
      self.id =1

ho = Home()
print(ho.id)
ho.id = 2
print(ho.id)

HBNB_MYSQL_USER=hbnb_addis_review HBNB_MYSQL_PWD=addisreview HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_addis_review_db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python -m api.v1.app
  