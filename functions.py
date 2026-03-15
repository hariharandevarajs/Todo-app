# def get_todos(filepath='files/todo.txt'): #default function
#     with open(filepath, 'r') as file_local:  # with method
#         todo_local = file_local.readlines()
#     return todo_local
#
# def write_todos(todo_arg,filepath='files/todo.txt'): # we should keep default parameter as lost one otherwise we get error.
#     with open(filepath, 'w') as file:
#         file.writelines(todo_arg)
#         '''
#         here we dont return anything bcz we need to write on the text
#         file. that's it ,  but get_todos function we need existing list based on that
#         we add new todos so that we were used return there
#
#         '''
# '''
# if i here print something like hello outside of the function , hello will execute print before  cli.py file excute ,
# How to Avoid this issue , use conditional statement here i will the condition
#
# '''
# # print(__name__)
# #
# # if __name__ == '__main__':
# #     print('hello')
# #     print(get_todos())

# -----------------------------------------------------

FILEBATH='files/todo.txt'

def get_todos(filepath=FILEBATH): #default function
    with open(filepath, 'r') as file_local:  # with method
        todo_local = file_local.readlines()
    return todo_local

def write_todos(todo_arg,filepath=FILEBATH): # we should keep default parameter as lost one otherwise we get error.
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)

# ----------------------


'''
i used this function to final one , like do to  create stand alone applaication 
other wise use above funtions is  enoguh 
'''
# FILEBATH=rf'C:\Users\devap\desktop\todoapp\Todo GUI\todo.txt'
#
# def get_todos(filepath=FILEBATH): #default function
#     with open(filepath, 'r') as file_local:  # with method
#         todo_local = file_local.readlines()
#     return todo_local
#
# def write_todos(todo_arg,filepath=FILEBATH): # we should keep default parameter as lost one otherwise we get error.
#     with open(filepath, 'w') as file:
#         file.writelines(todo_arg)

