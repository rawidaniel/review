import sys
from models import classes

def create(cls=sys.argv[1], params=sys.argv[2]):
        """Creates a new instance of a class"""
        
        if not cls:
            print("** class name missing **")
            return False
        if cls in classes:
            new_dict = eval(params)            
            instance = classes[cls](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()
        print(type(params))
create()