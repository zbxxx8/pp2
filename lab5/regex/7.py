example='hello_i_am_zhansulu'
import re
def snake_to_camel(example):
    example1=example.split('_') 
    return ''.join(i.capitalize() for i in example1)
print(snake_to_camel(example))