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


# import functions
# import FreeSimpleGUI as sg
#
# label=sg.Text("Type in a todo")
# input_box=sg.InputText(tooltip="enter todo",key="todo")
# add_button=sg.Button("Add")
#
# list_box=sg.Listbox(values=functions.get_todos(),key='todos',
#                     enable_events=True,size=[45,10])
# Edit_button=sg.Button("Edit")
#
# window1=sg.Window('My todo App',
#                   layout=[[label], [input_box, add_button],[list_box,Edit_button]],
#                   font=('Helvetica', 22))
# # Test =window1.read()
# # print(Test) #it return as tuple when you give input area plus add
#
# while True:
#     event, values = window1.read()
#     print(1,event)
#     print(2,values)
#     print(3,values['todos'])
#     print('hello')
#     match event:
#         case "Add":
#             todos = functions.get_todos()
#             print(todos)
#             new_todo= values['todo'] + '\n'
#             todos.append(new_todo)
#             functions.write_todos(todos)
#             window1['todos'].update(values=todos)
#         case "Edit":
#             todo_to_edit=values['todos'][0]
#             new_todo= values['todo']
#
#             todos= functions.get_todos()
#             index=todos.index(todo_to_edit)
#             todos[index]=new_todo
#             functions.write_todos(todos)
#             window1['todos'].update(values=todos)
#         case "todos":
#             window1['todo'].update(value=values['todos'][0])
#         case sg.WINDOW_CLOSED:
#             break  # you can use exit() as well , break is best our case
#
#
# window1.close()


# ---------------------------------------------

'''
Add complete and exit Button
without selecting todo if i press edit or complete g, we getting Index error , we use try and catch to fix this
Add Current date and time
apply them
apply size
in pluging apply rainbow theme , for getting highlight the code like bracket and text...

'''

import functions
import FreeSimpleGUI as sg
import time

sg.theme(("Black"))
clock = sg.Text("",key='clock')
label=sg.Text("Type in a todo")
input_box=sg.InputText(tooltip="enter todo",key="todo")
add_button=sg.Button("Add")

list_box=sg.Listbox(values=functions.get_todos(),
                    key='todos',
                    enable_events=True,size=[45,10])
Edit_button=sg.Button("Edit")
Complete_button=sg.Button("Complete")
Exit_button=sg.Button("Exit")

window1=sg.Window('My todo App',
                  layout=[[clock],
                          [label],
                          [input_box, add_button],
                          [list_box,Edit_button,Complete_button],
                          [Exit_button]],
                  font=('Helvetica', 22))
# Test =window1.read()
# print(Test) #it return as tuple when you give input area plus add

while True:
    event, values = window1.read(timeout=200)
    window1["clock"].update(value=time.strftime("DATE:%b-%d-%y Time:%H:%M:%S"))
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
            window1['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit=values['todos'][0]
                new_todo= values['todo']
                todos= functions.get_todos()
                index=todos.index(todo_to_edit)
                todos[index]=new_todo
                functions.write_todos(todos)
                window1['todos'].update(values=todos)
            except IndexError:
                # print('Choose one of them if you want to Edit')
                sg.popup("Choose one of them if you want to Edit")
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                print(todo_to_complete)
                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                print(index)
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window1['todos'].update(values=todos)
                window1['todo'].update(value='')
            except IndexError:
                sg.popup("Choose one of the todo before click Complete")
        case "Exit":
            break


        case "todos":
                window1['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break  # you can use exit() as well , break is best our case


window1.close()


