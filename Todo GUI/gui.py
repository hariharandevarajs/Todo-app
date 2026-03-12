# import functions
# import FreeSimpleGUI as sg
#
#
# '''
# enter terminal to use third parth librabry in our projects like - pip install FreeSimpleGUI
# '''
# label=sg.Text("Type in a todo")
# input_box=sg.InputText(tooltip="enter todo")
# add_button=sg.Button("Add")
#
#
# window1=sg.Window('My todo App',layout=[[label],[input_box,add_button]]) #each row represent the list likelable on first row, inputbox and add button second row
#
# window1.read()
# print('hello')
# window1.close()


# -------------------------------
#
# import functions
# import FreeSimpleGUI as sg


'''
add font and size and add button to activate method
'''
# label=sg.Text("Type in a todo")
# input_box=sg.InputText(tooltip="enter todo",key="todo")
# add_button=sg.Button("Add")
#
#
# window1=sg.Window('My todo App',
#                   layout=[[label], [input_box, add_button]],
#                   font=('Helvetica', 22))
# # Test =window1.read()
# # print(Test) #it return as tuple when you give input area plus add
#
# while True:
#     event, values = window1.read()
#     print(event)
#     print(values)
#     print('hello')
#     match event:
#         case "Add":
#             todos = functions.get_todos()
#             print(todos)
#             new_todo= values['todo'] + '\n'
#             todos.append(new_todo)
#             functions.write_todos(todos)
#         case sg.WINDOW_CLOSED:
#             break
#
#
# window1.close()

# -------------------------

'''
Add edit button and display todo things one by one here
'''


import functions
import FreeSimpleGUI as sg

label=sg.Text("Type in a todo")
input_box=sg.InputText(tooltip="enter todo",key="todo")
add_button=sg.Button("Add")

list_box=sg.Listbox(values=functions.get_todos(),key='todos',
                    enable_events=True,size=[45,10])
Edit_button=sg.Button("Edit")

window1=sg.Window('My todo App',
                  layout=[[label], [input_box, add_button],[list_box,Edit_button]],
                  font=('Helvetica', 22))
# Test =window1.read()
# print(Test) #it return as tuple when you give input area plus add

while True:
    event, values = window1.read()
    print(1,event)
    print(2,values)
    print(3,values['todos'])
    print('hello')
    match event:
        case "Add":
            todos = functions.get_todos()
            print(todos)
            new_todo= values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Edit":
            todo_to_edit=values['todos'][0]
            new_todo= values['todo']

            todos= functions.get_todos()
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break


window1.close()