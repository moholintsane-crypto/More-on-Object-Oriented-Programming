# Create Class
class Employee:

    # Initializing
    def __init__(self):
        print('Employee created')

    # Calling destructor
    def __del__(self):
        print('Destructor called')

def Create_object():
    print('Making object...')
    object = Employee()
    print('function end...')
    return object

print('Calling Create_object() function...')
object = Create_object()
print('Program End...')