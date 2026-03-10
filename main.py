# print("Enter todo things:")
# user_text=input("enter todo things today:")
# print(user_text)

# firstname = "John"
# middlename = "Jack"
# lastname = "Smith"
#
# person = [firstname, middlename, lastname,"New York"]
# print(person)

# words = ["Good Morning", "Good Afternoon", "Good Evening"]
# print(words)
# print(type(words))

# Title=input("enter your seo title:  ")
# print(f"your title charcter is: {len(Title)}")


# user_promt="enter name :"
# Best_Friends=[]
# i=0;
# while i<3:
#     todo=input(user_promt)
#     Best_Friends.append(todo)
#     print(todo)
#     print("next")
#     i+=1
#
# print(f"my best frds are: {Best_Friends}")

# user_password=input("Enter Your Password:")
# password = "hari"
# while user_password != password:
#     print("wrong pin")
#     print(f"Reenter")
#     user_password = input("Enter Your Password:")
#
# print(f"password correct:{user_password}")


# i = 1
# while i < 7:
#
#     print(i)
#     i += 1

# todo=[]
# while True:
#     user_input = input("Enter Your Todo addd , show , exit: ").strip()
#     #strip() method - used to remove white space after string
#     match user_input:
#         case 'add':
#             todoo = input("enter todo: ")
#             todo.append(todoo)
#         case 'show' | 'display': #case 'show' | display - use or operator
#             # print(todo)
#             for item in todo:
                  #item=item.title()
#                 print(item)
#         case 'exit':
#             break
#         case whatever:
#             print("enter exact option which show in the optioin section")
# print("bye")

# In the coding area, we have created a members list. Below that line, write a for-loop block that:
#
# (1) iterates over the items of the members list, and
#
# (2) prints out each item of the list with the first letter capitalized.

# members=['hello',"hi"]
# for item in members:
#     print(item.capitalize())

# todo=[]
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit: ").strip()
#     #strip() method - used to remove white space after string
#     match user_input:
#         case 'add':
#             todoo = input("enter todo: ")
#             todo.append(todoo)
#         case 'show' | 'display': #case 'show' | display - use or operator
#             # print(todo)
#             for item in todo:
#                   item=item.title()
#                   print(item)
#         case 'edit':
#             number=int(input("what you want to edit :"))
#             number = number - 1
#             new_todo = input("Enter new Todo: ")
#             todo[number] = new_todo
#             print(todo[number])
#
#
#         case 'exit':
#             break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
# print("bye")
# -----------------------------------------
# filenames=["1.raw.txt","2.media.txt"]

# for filename in filenames:
#     filename=filename.replace('.','-',1) #here 1 means 1st occurance
#     print(filename)
# print(filenames) # here you can see the no changes bczs strings are immutable , list mutable, in this scenario , you store in the new variable

# filenames=["1.raw.txt","2.media.txt"]
# new_filename=[]
# for filename in filenames:
#     filename=filename.replace('.','-',1)
#     new_filename.append(filename)
#     print(new_filename)
# print(filenames)
# print(new_filename)

#tuple immutable - append method - doest have in tuple.

# filenames=("1.raw.txt","2.media.txt")
# filenames[2]="hello.txt"

# --------------------------------------------

# name = 'harz'
# print(name)
# name=name.replace('z','i')
# print(name)

# ----------------------
# name = ['naveen kumar','hari haran']
# updated_username=[]
# for item in name:
#     item=item.replace(' ','-')
#     updated_username.append(item)
# print(updated_username)
# ------------------------------
# seconds = [1.23, 1.45, 1.02]
# current = 1.11
# seconds.append(current)
# print(seconds)

# ------------------------
# Your task for this exercise is to:
#
# (1) create a color_codes variable and assign a tuple to it,
#
# (2) the tuple should contain three tuples as items.
#
# (3) each of the three tuples should contain three items. The items can be any type (e.g,, string, number, etc).

# color_codes = ((1,2,3), (4,5,6), (7,8,9))

# -------------------------------------------
#   #enumerateFuntions
# todo=[]
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit: ").strip()
#     #strip() method - used to remove white space after string
#     match user_input:
#         case 'add':
#             todoo = input("enter todo: ")
#             todo.append(todoo)
#         case 'show' | 'display': #case 'show' | display - use or operator
#             # print(todo)
#             for index,item in enumerate(todo): #enumerate function uses for get item with index
#                   print(f"{index+1}.{item}") #f- striings uses to access variable inside the string.
#         case 'edit':
#             number=int(input("what you want to edit :"))
#             number = number - 1
#             new_todo = input("Enter new Todo: ")
#             todo[number] = new_todo
#             print(todo[number])
#
#
#         case 'exit':
#             break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
# print("bye")

# -----------------------
# In the coding area, we have a list of strings. Add some code that:
#
# (1) iterates over the list items,
#
# (2) prints out the index of each item, a colon ":", and the item.
#
# Here is how the output should look like:
#
# 0 : table
#
# 1 : chair
#
# 2 : door

# products = ['table', 'chair', 'door']
#
# for index, item in enumerate(products):
#     print(index, ":", item)

# --------------------------------------------------

# Here is another similar problem that needs some more careful consideration. Add some code that iterates over the products list items and produces the following output:
#
# Product: table
#
# Product: chair
#
# Product: door

# products = ['table', 'chair', 'door']
#
# for index, item in enumerate(products):
#     print('Product:', item)


# --------------------------------------------------------
# In the code area we have a list of strings. Your task is to write some code that:
#
# (1) iterates over the filenames list,
#
# (2) adds a number and a dash in front of each string, and .txt at the end using f-strings, and
#
# (3) prints each modified string as shown below.
#
# 0-document.txt
#
# 1-report.txt
#
# 2-presentation.txt

# filenames = ['document', 'report', 'presentation']
#
# for index,item in enumerate(filenames):
#     print(f"{index}-{item}.txt")

# -----------------------------
# Similar to the previous exercise, we have a list of three strings defined in the code area. Your task is to:
#
# (1) iterate over the filenames list,
#
# (2) capitalize the first letter of each string,
#
# (3) add a number and a dash in front of each string, and .txt at the end, and
#
# (4) print each modified string as shown below.
#
# 0-Document.txt
#
# 1-Report.txt
#
# 2-Presentation.txt

# filenames = ['document', 'report', 'presentation']
#
# for index,item in enumerate(filenames): #instead of index use i like item - j
#     print(f"{index}-{item.capitalize()}.txt")

# --------------------------------------------
# add complete feature in the todo_app :
# remove del values
# pop - del index value - default last index

# todo=[]
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     #strip() method - used to remove white space after string
#     match user_input:
#         case 'add':
#             todoo = input("enter todo: ")
#             todo.append(todoo)
#         case 'show' | 'display': #case 'show' | display - use or operator
#             # print(todo)
#             for index,item in enumerate(todo): #enumerate function uses for get item with index
#                   row=f"{index+1}.{item}" #f- striings uses to access variable inside the string.
#                   print(row)
#         case 'edit':
#             number=int(input("what you want to edit :"))
#             number = number - 1
#             new_todo = input("Enter new Todo: ")
#             todo[number] = new_todo
#             print(todo[number])
#         case 'complete':
#             completed=int(input('what you completed:'))
#             if completed==0:
#                 print('valuse shoule be start with 1')
#             if completed>0:
#                 completed = completed - 1
#                 del_item = todo.pop(completed)
#                 print(f"{del_item} has been deleted ")
#
#
#         case 'exit':
#             break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
# print("bye")

# ----------------
#remove delete values
# seconds = [1.23, 1.45, 1.02, 1.11]
# seconds.remove(1.45)
# print(seconds)
# -------------------

# len()- find leanth
# todo=["hello","hi"]
# for index,item in enumerate(todo):
#     row = f"{index + 1}.{item}"
#     print(row)
# print(f"list length is : {len(todo)}")

# -------------------------
#enumerate works method
# for index,item in enumerate(["hello","hi"]): #use list inside enumerate function
#     row = f"{index + 1}.{item}"
#     print(row)

# for index,item in enumerate("hello"):
#     row = f"{index + 1}.{item}"
#     print(row)

# a = enumerate(["hello","hi"])
# print(a)
# a=list(a)
# print(a)


# ----------------
# mystring = "hello"
# mylist = [1, 2, 3]
#
# print(len(mystring))
# print(len(mylist))

# ------------------------------
# We have defined a list in the coding area. Add some code that:
#
# (1) iterates over the items of mylist,
#
# (2) prints out the current length of the list in each iteration

# mylist=[1,2,3,4]
# for item in mylist:
#     print(len(mylist))


# ---------------------------------------------
#
# my_list=['e','f','c']
#
# # my_list=my_list.sort() #here return nothing why this method with list return none
# my_list.sort()
# for index, item in enumerate(my_list):
#     print(f"{index+1}.{item}")

#string return new string with method
#
# name = "hari"
# name=name.replace('i','y')
# print(name)

# -------------------------

# float_num=[1.2,0.5,50,2.0,100]
# float_num.sort()
# for j in float_num:
#     print(j)

# -----------------------
# its works , but work in python console ,
# run the code again exiting thisngs gone , so we save in separate file so we use todo.txt file
# #todo = [] - no need here
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     #strip() method - used to remove white space after string
#     match user_input:
#         case 'add':
#             todoo = input("enter todo: ") +"\n" #print the coede next line
#             file = open("todo.txt",'r')
#             todo=file.readlines()
#             file.close()
#
#             todo.append(todoo)
#
#             file=open('todo.txt', 'w')
#             file.writelines(todo)#w - write r- read
#             file.close()
#         case 'show' | 'display':
#             # print(todo)
#             for index,item in enumerate(todo):
#                   row=f"{index+1}.{item}"
#                   print(row)
#         case 'edit':
#             number=int(input("what you want to edit :"))
#             number = number - 1
#             new_todo = input("Enter new Todo: ")
#             todo[number] = new_todo
#             print(todo[number])
#         case 'complete':
#             completed=int(input('what you completed:'))
#             if completed==0:
#                 print('valuse shoule be start with 1')
#             if completed>0:
#                 completed = completed - 1
#                 del_item = todo.pop(completed)
#                 print(f"{del_item} has been deleted ")
#
#
#         case 'exit':
#             break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
# print("bye")
# --------------------------------------------------
# >>> file=open('whatever.txt','r')
# >>> file.read()
# 'line\nline2\n'
# >>> file.read()
# ''
# >>> file.close()
# >>> file.read()
# Traceback (most recent call last):
#   File "<python-input-14>", line 1, in <module>
#     file.read()
#     ~~~~~~~~~^^
# ValueError: I/O operation on closed file.

#if you didnt close the file , the existing values will be overwritten ,
# so every time you make read or write close the file.
# use close once you read or write in the files
# ------------------------------------------------------

# here we show the list of items , intially we have list in the program ,after we start store txt file no need list so we removed that
# todo things store in list but here we store instead of that in txt file, so we open and read the file and pass the variable into for loop to show

# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     #strip() method - used to remove white space after string
#     match user_input:
#         case 'add':
#             todoo = input("enter todo: ") +"\n" #print the coede next line
#             file = open("todo.txt",'r')
#             todo=file.readlines()
#             file.close()
#
#             todo.append(todoo)
#
#             file=open('todo.txt', 'w')
#             file.writelines(todo)#w - write r- read
#             file.close()
#         case 'show' | 'display':
#             file=open('todo.txt','r')
#             todo=file.readlines()
#             file.close()
#             for index,item in enumerate(todo):
#                   row=f"{index+1}.{item}"
#                   print(row)
#         case 'edit':
#             number=int(input("what you want to edit :"))
#             number = number - 1
#             new_todo = input("Enter new Todo: ")
#             todo[number] = new_todo
#             print(todo[number])
#         case 'complete':
#             completed=int(input('what you completed:'))
#             if completed==0:
#                 print('valuse shoule be start with 1')
#             if completed>0:
#                 completed = completed - 1
#                 del_item = todo.pop(completed)
#                 print(f"{del_item} has been deleted ")
#
#
#         case 'exit':
#             break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
# print("bye")
# ----------------------------------------------------------------------------
# if i create a new folder in the project and i drag and drop
# the todo.txt file in it , the existing files name in coding change automatically
# path file also work
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     #strip() method - used to remove white space after string
#     match user_input:
#         case 'add':
#             todoo = input("enter todo: ") +"\n" #print the coede next line
#             file = open("files/todo.txt", 'r')
#             todo=file.readlines()
#             file.close()
#
#             todo.append(todoo)
#
#             file=open('files/todo.txt', 'w')
#             file.writelines(todo)#w - write r- read
#             file.close()
#         case 'show' | 'display':
#             file=open('files/todo.txt', 'r')
#             todo=file.readlines()
#             file.close()
#             for index,item in enumerate(todo):
#                   row=f"{index+1}.{item}"
#                   print(row)
#         case 'edit':
#             number=int(input("what you want to edit :"))
#             number = number - 1
#             new_todo = input("Enter new Todo: ")
#             todo[number] = new_todo
#             print(todo[number])
#         case 'complete':
#             completed=int(input('what you completed:'))
#             if completed==0:
#                 print('valuse shoule be start with 1')
#             if completed>0:
#                 completed = completed - 1
#                 del_item = todo.pop(completed)
#                 print(f"{del_item} has been deleted ")
#
#
#         case 'exit':
#             break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
# print("bye")

# ----------------------------------

# here we zip function and how to store difference file and different txt
# mycontent= ['hello','how are you','i am fine']
#
# filenames=['doc.txt','doc2.txt','doc3.txt']
#
# for content,filename in zip(mycontent,filenames):
#     file=open(rf"C:\Users\devap\desktop\todoapp\bouns\{filename}",'w') #copy path and paste fString and add before r like thi
#     file.writelines(content)
#     file.close()
# ------------------------------------------------

# content_1="The American black bear (Ursus americanus) is a medium-sized bear native to North America. It is the continent's smallest and most widely distributed bear species. American black bears are omnivores, with their diets varying greatly depending on season and location. They typically live in largely forested areas, but do leave forests in search of food. Sometimes they become attracted to human communities because of the immediate availability of food. The American black bear is the world's most common bear species."
# file = open("bear.txt", "w")
# file.writelines(content_1)
# file.close()
#
# file = open("bear.txt", "r")
# content = file.read()
# file.close()
#
# print(content)

# --------------------------------
# In the coding area, there's an essay.txt file uploaded. Your task is to write a program that:
#
# (1) opens the essay.txt file in read mode,
#
# (2) reads its content,
#
# (3) converts the first letter of each word into uppercase,
#
# (4) prints out the updated content.

# content='hello how are you ?'
# file=open('essay.txt','w')
# file.writelines(content.title())
# #title -change every word first letter caps and
# # #captalize change sentence first letter onlly caps
# file.close()
#
# file=open('essay.txt','r')
# Titlecontent=file.read()
# file.close()
# print(Titlecontent)

# ---------------------------------
# In the coding area, there is an essay.txt file uploaded. Your task is to write a program that:
#
# (1) opens the essay.txt file in read mode,
#
# (2) reads its content,
#
# (3) finds out the number of characters in the content,
#
# (4) prints out the number of characters.

# file=open('essay.txt','r')
# content=file.read()
# file.close()
#
# print(len(content))

# -----------------------------------------
#
# Instructions
# In the coding area, we have defined two lists.
# Each country in the first list should be written in a new file corresponding
# to the name in the filenames list. So, "Albania" should be
# written in a new a.txt file, "Belgium" in a new "b.txt" file and so on.

# country=['india','srilanka','newzeland']
# filename=['new a.txt','a.txt','b.txt']
#
# for i,j in zip(country,filename):
#     file=open(rf"C:\Users\devap\desktop\todoapp\bouns\{j}","w")
#     file.writelines(i)
#     file.close()

# ------------------------------------
# Instructions
# In the coding area, we have defined a list of countries.
# Add some code that uses a for loop to generate a text file for each country
# (e.g., "Albania.txt", "Belgium.txt", and so on).
#
# Each file should have its country name as content
# (e.g., Albania.txt has Albania as content).
country=['india','srilanka','newzeland']
# for item in country:
#     file=open(rf"C:\Users\devap\desktop\todoapp\bouns\{item}.txt",'w')
#     file.close() # if you doesn't close () it will be overwritten
# -----------------------------------------------
# Please code this exercise in your computer IDE, so you gain experience with working with text files in a local IDE. For this exercise, download the members.txt file attached to the resources. Then, create a program that:
#
# 1. prompts the user to enter a new member.
#
# 2. adds that member to members.txt at the end of the existing members. For example, the user here has entered the member Solomon Right.
#
#
# In the above example, Solomon Right will be added to members.txt updating the content of the file to:
#
# John Smith
#
# Sen Lakmi
#
# Sono Octonot
#
# Solomon Right

#
# file= open(rf"C:\Users\devap\desktop\todoapp\bouns\members.txt",'r')
# existing_mem=file.readlines()
# file.close()
# i=0;
# while i<3:
#     user = input("enter your name: ");
#     existing_mem.append(user + "\n")
#     file = open(rf"C:\Users\devap\desktop\todoapp\bouns\members.txt", 'w')
#     file.writelines(existing_mem)
#     i+=1
# ----------------------------------

# Open your computer IDE and place the following in a Python file:
#
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# Then, create a program that:
#
# 1. generates multiple text files by iterating over the filenames list,
#
# 2. and writes the text Hello  inside each generated text file.


# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for file in filenames:
#     file = open(rf"C:\Users\devap\desktop\todoapp\bouns\{file}", 'w')
#     stored = file.writelines('hello')
#     file.close()


# -----------------------------------------

# Please download the three text files a.txt, b.txt, and c.txt from the resources and place them in your computer IDE.
#
# Then, create a program that:
#
# 1. reads each text file and
#
# 2. prints out the content of each file in the command line.
#
# The expected output would be like the following:
#

# files=['a.txt','b1.txt','c1.txt']
# for file in files:
#     print(file)
#     file = open(rf"C:\Users\devap\desktop\todoapp\bouns\{file}", 'r')
#     stored = file.read()
#     file.close()
#
#     print(stored)


# ------------------------------
# use reddit and quora and discord for gaining express
# ---------------------------
# remove /n from list - usiing string method  and strip method
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     #strip() method - used to remove white space after string
#     match user_input:
#         case 'add':
#             todoo = input("enter todo: ") +"\n" #print the coede next line
#             file = open("files/todo.txt", 'r')
#             todo=file.readlines()
#             file.close()
#
#             todo.append(todoo)
#
#             file=open('files/todo.txt', 'w')
#             file.writelines(todo)#w - write r- read
#             file.close()
#         case 'show' | 'display':
#             file=open('files/todo.txt', 'r')
#             todo=file.readlines()
#             file.close()
#             print(todo) #/n comes after every iteration - we use replace method to solve this gap issue
#             for index,item in enumerate(todo):
#                 n_removed=item.replace('\n',"") # string method
#                 # print(item)
#                 row=f"{index+1}.{n_removed}"
#                 print(row)
#         case 'edit':
#             number=int(input("what you want to edit :"))
#             number = number - 1
#             new_todo = input("Enter new Todo: ")
#             todo[number] = new_todo
#             print(todo[number])
#         case 'complete':
#             completed=int(input('what you completed:'))
#             if completed==0:
#                 print('valuse shoule be start with 1')
#             if completed>0:
#                 completed = completed - 1
#                 del_item = todo.pop(completed)
#                 print(f"{del_item} has been deleted ")
#
#
#         case 'exit':
#             break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
# print("bye")

# -------------- Strip() method used to remove /n
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     #strip() method - used to remove white space after string
#     match user_input:
#         case 'add':
#             todoo = input("enter todo: ") +"\n" #print the coede next line
#             file = open("files/todo.txt", 'r')
#             todo=file.readlines()
#             file.close()
#
#             todo.append(todoo)
#
#             file=open('files/todo.txt', 'w')
#             file.writelines(todo)#w - write r- read
#             file.close()
#         case 'show' | 'display':
#             file=open('files/todo.txt', 'r')
#             todo=file.readlines()
#             file.close()
#             # print(todo) #/n comes after every iteration - we use replace method to solve this gap issue
#             new_todo=[] #strip
#             for index,item in enumerate(todo):
#                 new_item=item.strip('\n') #strip
#                 new_todo.append(new_item) #strip
#                 row=f"{index+1}.{new_item}" #strip
#                 print(row)
#             # print(new_todo)
#         case 'edit':
#             number=int(input("what you want to edit :"))
#             number = number - 1
#             new_todo = input("Enter new Todo: ")
#             todo[number] = new_todo
#             print(todo[number])
#         case 'complete':
#             completed=int(input('what you completed:'))
#             if completed==0:
#                 print('valuse shoule be start with 1')
#             if completed>0:
#                 completed = completed - 1
#                 del_item = todo.pop(completed)
#                 print(f"{del_item} has been deleted ")
#
#
#         case 'exit':
#             break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
# print("bye")


# --------------------------


# -------------- list comprehensation used to remove /n
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     #strip() method - used to remove white space after string
#     match user_input:
#         case 'add':
#             todoo = input("enter todo: ") +"\n" #print the coede next line
#             file = open("files/todo.txt", 'r')
#             todo=file.readlines()
#             file.close()
#
#             todo.append(todoo)
#
#             file=open('files/todo.txt', 'w')
#             file.writelines(todo)#w - write r- read
#             file.close()
#         case 'show' | 'display':
#             file=open('files/todo.txt', 'r')
#             todo=file.readlines()
#             file.close()
#             # print(todo) #/n comes after every iteration - we use replace method to solve this gap issue
#             new_todo=[item.strip('\n') for item in todo] #list comprehension method
#             for index,item in enumerate(new_todo):#list comprehension method
#                 row=f"{index+1}.{item}"
#             # print(new_todo)
#         case 'edit':
#             number=int(input("what you want to edit :"))
#             number = number - 1
#             new_todo = input("Enter new Todo: ")
#             todo[number] = new_todo
#             print(todo[number])
#         case 'complete':
#             completed=int(input('what you completed:'))
#             if completed==0:
#                 print('valuse shoule be start with 1')
#             if completed>0:
#                 completed = completed - 1
#                 del_item = todo.pop(completed)
#                 print(f"{del_item} has been deleted ")
#
#
#         case 'exit':
#             break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
# print("bye")


# -------------------------------------------

'''
Use command  - like this for multiple lines
hello i want to tell somethings here
'''

# --------------------
# '''
# # print this output
# # ['1-doc.txt', '1-report.txt', '1-presentation.txt']
# '''
# filenames=["1.doc","1.report","1.presentation"]
# filenames=[filename.replace('.','-') +'.txt' for filename in filenames  ]
# print(filenames)
# ----------------------------
'''
We have defined a list of strings in the coding area. Your task is to add some code that:

(1) uses list comprehension to capitalize all the names and surnames of the list, and

(2) prints the updated list.

The output of your code should be as below:

['John Smith', 'Jay Santi', 'Eva Kuki']
'''

# names = ["john smith", "jay santi", "eva kuki"]
#
# names=[name.title() for name in names]
#
# print(names)
# -------------------------------------------------------
'''
Extend the given code so the code prints out a list containing the number of characters for each username.

The output of your code should be as below:

[9, 11, 11]
'''

# usernames = ["john 1990", "alberta1970", "magnola2000"]
#
# usernames=[len(username) for username in usernames]
#
# print(usernames)

# --------------------------------
'''
The coding area contains a list of numbers, each stored as a string. Your task is to add some code that:

(1) converts the numbers from strings to floats, and

(2) prints out the updated list.

The output of your code should be as below. Notice the numbers are floats without quotes.

[10.0, 19.1, 20.0]
'''

# user_entries = ['10', '19.1', '20']
# user_entries=[float(user_entrie) for user_entrie in user_entries]
#
# print(user_entries)

# ----------------------

'''
We have defined a numbers variable in the coding area. Add some code that:

(1) multiplies each number of the list by 2, and

(2) prints out the updated list.

Here is the expected output:

[20, 40, 60]

'''

# muli_by_2=[10,20,30]
# muli_by_2=[item*2 for item in muli_by_2]
# print(muli_by_2)

# -----------------------------------------
'''
Extend the given code so it prints out the sum of the numbers. Note that the numbers are currently string types.

The output of your code should be as below:

49.1
'''
#
# user_entries = ['10', '19.1', '20']

# first convert into str to float
# then do sum the list
# user_entries=[float(user_entrie) for user_entrie in user_entries]
# print(user_entries)
# print(sum(user_entries))
# Normal For loop
# sum=0
# for item in user_entries:
#     sum+=item
# print(sum)
# ----------------------------------------------------


'''
temperatures = [10, 12, 14]

file = open("file.txt", 'w')

file.writelines(temperatures)
'''
# #convert into string from given num then added
# temperatures = [10, 12, 14]
# temperatures=[str(i)+ '\n' for i in temperatures]
# file = open(rf"C:\Users\devap\desktop\todoapp\bouns\temperature.txt", 'w')
#
# file.writelines(temperatures)
# print('complete')

# -------------------------

'''
using with in file handleing , no need to mention file.close here  - allways recommanded method 
edit and compplete solved
'''
#
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     #strip() method - used to remove white space after string
#     match user_input:
#         case 'add':
#             todoo = input("enter todo: ") +"\n" #print the coede next line
#             with open("files/todo.txt", 'r') as file: #with method
#                 todo = file.readlines()
#                 #no need to mention close method here
#             todo.append(todoo)
#
#             with open('files/todo.txt', 'w') as file:
#                 file.writelines(todo)#w - write r- read
#
#         case 'show' | 'display':
#             file=open('files/todo.txt', 'r')
#             todo=file.readlines()
#             file.close()
#             # print(todo) #/n comes after every iteration - we use replace method to solve this gap issue
#             new_todo=[] #strip
#             for index,item in enumerate(todo):
#                 new_item=item.strip('\n') #strip
#                 new_todo.append(new_item) #strip
#                 row=f"{index+1}.{new_item}" #strip
#                 print(row)
#             # print(new_todo)
#         case 'edit':
#             number=int(input("what you want to edit :"))
#             number = number - 1
#             new_todo = input("Enter new Todo: ")
#             with open('files/todo.txt', 'r') as file:
#                 afterread=file.readlines()
#             print(afterread)
#             afterread[number] = new_todo
#             print(afterread[number])
#             with open('files/todo.txt', 'w') as file:
#                 file.writelines(afterread)
#                 #changes after just write the list thats all dont do  file.writelines(afterread[number])
#
#         case 'complete':
#             completed=int(input('what you completed:'))
#             with open('files/todo.txt', 'r') as file:
#                 afterread=file.readlines()
#             print(afterread)
#             print('read')
#             # new_todo = []  # strip
#             # for index, item in enumerate(afterread):
#             #     new_item = item.strip('\n')  # strip
#             #     new_todo.append(new_item)  # strip
#             #     row = f"{index + 1}.{new_item}"  # strip
#             #     print(row)
#             # print(new_todo)
#
#             completed = completed - 1
#             todo_to_remove=afterread[completed].strip('\n')
#             del_item = afterread.pop(completed)
#             print(f"{todo_to_remove} has been deleted ")
#             with open('files/todo.txt', 'w') as file:
#                 file.writelines(afterread)
#             print('write successfully')
#
#         case 'exit':
#             break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
# print("bye")

# --------------------------
'''
The code in the coding area successfully reads and prints out the content of 
the bear.txt file. Your task is to rewrite the code by using a "with" context manager to achieve the same thing.
'''
# with open(rf'C:\Users\devap\desktop\todoapp\bouns\srilanka.txt','r') as file:
#     read=file.readlines()
# print(read)

# -------------------------------------------
'''
The code in the coding area successfully reads and prints out the number of characters in the bear.txt file. Similar to the previous task, your task is to rewrite 
the code by using a "with" context manager to achieve the same thing.
'''
# with open(rf'C:\Users\devap\desktop\todoapp\bouns\srilanka.txt','r') as file:
#     read=file.readlines()
#
# new_cha= len(read[0])
# print(new_cha)

# ------------------------------------------
'''
Usedouble .. double dot to set up file path
'''
# with open("../todoapp/bouns/srilanka.txt",'r') as file:
#     read=file.readlines()
#
# new_cha= len(read[0])
# print(new_cha)

# --------------------------------

# date=input("enter date :")
# mood=input("enter you mood 1 to 10 : ")
# thoughts_of_the_day=input(" enter your thoughts : \n")
# with open(rf"../todoapp/bouns/{date}.txt",'w') as file:
#     file.write(mood + 2*'\n')
#     file.write(thoughts_of_the_day)
#
# with open(rf"../todoapp/bouns/{date}.txt",'r') as file:
#     read=file.readlines()
#
# print(read)

# ------------------------------------
#
# In the coding area, we have defined a list of languages. Add some code that:
#
# (1) iterates over the list using a for-loop,
#
# (2) creates a new text file in each iteration using a with-context manager,
#
# (3) each file should be named according to the current item (i.e., English.txt, German.txt, and Spanish.txt).
#
# (4) the content of each file should be the item of the list (e.g., the content of the file English.txt should be English).


# languages = ['English', 'German', 'Spanish']
#
# for item in languages:
#     with open(f"../todoapp/bouns/{item}.txt",'w') as file:
#         file.write(f"{item}")

# ------------------------------------------------
'''
In the coding area there is a story.txt file tab that contains some text. Your task is to make a copy of the story.txt file. Here are the exact steps:

(1) Read the story.txt file using a with-context manager and store its text in a string variable.

(2) Create a new story_copy.txt file using a second with-context and write the string variable in the file.
'''

# with open('../todoapp/bouns/story.txt', 'r') as file:
#     content = file.read()
#
# with open('../todoapp/bouns/story_copy.txt', 'w') as file:
#     file.write(content)

# ------------------------------------------


# with open('../todoapp/bouns/story_copy.txt', 'r') as file:
#     # print(file.read())
#     content=file.read()
#     # print(len(file.readlines()))
#     print(len(content))

# If the read() method is called two times, it returns an empty string the second time.To avoid that, we call the read() method once and store its output in a variable:
#
#     content = file.read()

# -----------------------------------
'''
adding additional features like add todo on the line instead of do next line
using in operator and if else , remove match bcz match support only string not expression

'''


# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     if 'add' in user_input:
#
#         todoo = user_input[4:] + "\n"
#         with open("files/todo.txt", 'r') as file: #with method
#             todo = file.readlines()
#             #no need to mention close method here
#         todo.append(todoo)
#
#         with open('files/todo.txt', 'w') as file:
#             file.writelines(todo)#w - write r- read
#
#     if 'show' in user_input:
#         file=open('files/todo.txt', 'r')
#         todo=file.readlines()
#         file.close()
#         # print(todo) #/n comes after every iteration - we use replace method to solve this gap issue
#         new_todo=[] #strip
#         for index,item in enumerate(todo):
#             new_item=item.strip('\n') #strip
#             new_todo.append(new_item) #strip
#             row=f"{index+1}.{new_item}" #strip
#             print(row)
#         # print(new_todo)
#     if 'edit' in user_input:
#         print(user_input[5:])
#         number=int(user_input[5:])
#         number = number - 1
#         new_todo = input("Enter new Todo: ") +'\n'
#         with open('files/todo.txt', 'r') as file:
#             afterread=file.readlines()
#         print(afterread)
#         afterread[number] = new_todo
#         print(afterread[number])
#         with open('files/todo.txt', 'w') as file:
#             file.writelines(afterread)
#             #changes after just write the list thats all dont do  file.writelines(afterread[number])
#
#     if 'complete' in user_input:
#
#         completed=int(user_input[9:])
#         with open('files/todo.txt', 'r') as file:
#             afterread=file.readlines()
#         print(afterread)
#         print('read')
#         # new_todo = []  # strip
#         # for index, item in enumerate(afterread):
#         #     new_item = item.strip('\n')  # strip
#         #     new_todo.append(new_item)  # strip
#         #     row = f"{index + 1}.{new_item}"  # strip
#         #     print(row)
#         # print(new_todo)
#
#         completed = completed - 1
#         todo_to_remove=afterread[completed].strip('\n')
#         del_item = afterread.pop(completed)
#         print(f"{todo_to_remove} has been deleted ")
#         with open('files/todo.txt', 'w') as file:
#             file.writelines(afterread)
#         print('write successfully')
#
#     if 'exit' in user_input:
#         break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
# print("bye")

# -----------------------------------

'''
code experiments - or , and , not
'''
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     if 'add' in user_input : #or 'new' in user_input , not in user_input
#
#         todoo = user_input[4:] + "\n"
#         with open("files/todo.txt", 'r') as file: #with method
#             todo = file.readlines()
#             #no need to mention close method here
#         todo.append(todoo)
#
#         with open('files/todo.txt', 'w') as file:
#             file.writelines(todo)#w - write r- read
#
#     elif 'show' in user_input:
#         file=open('files/todo.txt', 'r')
#         todo=file.readlines()
#         file.close()
#         # print(todo) #/n comes after every iteration - we use replace method to solve this gap issue
#         new_todo=[] #strip
#         for index,item in enumerate(todo):
#             new_item=item.strip('\n') #strip
#             new_todo.append(new_item) #strip
#             row=f"{index+1}.{new_item}" #strip
#             print(row)
#         # print(new_todo)
#     elif 'edit' in user_input:
#         print(user_input[5:])
#         number=int(user_input[5:])
#         number = number - 1
#         new_todo = input("Enter new Todo: ") +'\n'
#         with open('files/todo.txt', 'r') as file:
#             afterread=file.readlines()
#         print(afterread)
#         afterread[number] = new_todo
#         print(afterread[number])
#         with open('files/todo.txt', 'w') as file:
#             file.writelines(afterread)
#             #changes after just write the list thats all dont do  file.writelines(afterread[number])
#
#     elif 'complete' in user_input:
#
#         completed=int(user_input[9:])
#         with open('files/todo.txt', 'r') as file:
#             afterread=file.readlines()
#         print(afterread)
#         print('read')
#         # new_todo = []  # strip
#         # for index, item in enumerate(afterread):
#         #     new_item = item.strip('\n')  # strip
#         #     new_todo.append(new_item)  # strip
#         #     row = f"{index + 1}.{new_item}"  # strip
#         #     print(row)
#         # print(new_todo)
#
#         completed = completed - 1
#         todo_to_remove=afterread[completed].strip('\n')
#         del_item = afterread.pop(completed)
#         print(f"{todo_to_remove} has been deleted ")
#         with open('files/todo.txt', 'w') as file:
#             file.writelines(afterread)
#         print('write successfully')
#
#     elif 'exit' in user_input:
#         break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
#     else:
#         print('cmd not valid')
# print("bye")


# -----------------------------
# user = input("Enter your pass: ")
# password = 8
# if len(user) >= password and any(char.isdigit() for char in user) and any(char.isupper() for char in user) :
#     print(len(user))
#     print('strong password')
# else:
#     print(len(user))
#     print('weak password')

# --------------------------------
# user = input("Enter your pass: ")
#
# result=[]
#
# if len(user) >=8:
#     result.append(True)
#
# else:
#     result.append(False)
#
#
# digit = False
#
# for item in user:
#     if item.isdigit():
#         digit = True
# result.append(digit)
# Upper = False
#
# for item in user:
#     if item.isdigit():
#         Upper = True
# result.append(Upper)
#
# if all(result):
#     print("Yes, strong Password")
# else:
#     print("No, strong Password")
# ------------------------------

'''
list has appenad method,
dic doesnt have append method
list=[15,16,25]
dic={'height':45,'weight':25
} 

you want to store the data with label use dict
'''
# user = input("Enter your pass: ")
#
# result={} #use dic for claer data with lable
#
# if len(user) >=8:
#     result["Charcter"]=True #use this method to add in dic
#
# else:
#     result["Charcter"]=False
#
#
# digit = False
#
# for item in user:
#     if item.isdigit():
#         digit = True
# result['digit']=digit
# Upper = False
#
# for item in user:
#     if item.isdigit():
#         Upper = True
# result["Uppercase"]=Upper
#
# print(result)
# print(result.values())
# if all(result.values()):
#     print("Yes, strong Password")
# else:
#     print("No, strong Password")

# -------------------------------------

# Write a program that:
#
# (1) asks users to enter a password using an input() function,
#
# (2) returns "Great password there!" if the password has more than 7 characters. For example:
#
# (3) returns "Your password is weak." if the password has 7 or fewer characters. For example:

# user =input("Enter your Password: ")
#
# if len(user) >7:
#     print('great password')
# else:
#     print('not great password')

# -----------------------

'''
Write a program that: 

(1) asks users to enter a password,

(2) returns "Great password there" if the password has more than 7 characters,

(3) returns "Password is OK, but not too strong" if the password has exactly 7 characters,

(4) returns "Your password is weak" if the password has 7 or fewer characters. 
'''

# user =input("Enter your Password: ")
#
# if len(user) >7:
#     print('great password')
# elif len(user) == 7 :
#     print('Password is okay Only')
# else:
#     print('not great password')

# ------------------------

'''
Your task for this exercise is to:

(1) assign a dictionary to variable day_temperatures,

(2) the dictionary should contain three keys: 'morning', 'noon', and 'evening'

(3) each key should have a float as value.
'''

# day_temperatures = {'morning': 5.1, 'noon': 6.1, 'evening': 10.2}
#

# -------------------------

# List can change tuples cant change , we can assign again
'''
Your task for this exercise is to:

(1) assign a dictionary to variable day_temperatures,

(2) the dictionary should contain three keys: 'morning', 'noon', and 'evening'

(3) each key should contain a tuple as a value,

(4) each tuple should contain three floats.
'''
# day_temperatures = {'morning': (1.1 , 2.2, 3.4), 'noon': (2.3, 4.5, 3.1), 'evening': (2.4, 3.5, 6.5)}

# ---------------------
'''
Print out the slice ['a', 'b', 'c'] of the letters list using slicing.
'''
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[0:3])

# ----------------------
'''
Print out the slice ['e', 'f', 'g'] of the letters list using slicing.
'''

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[-3:])

# -----------------------
'''
Bug-Fixing Exercise

'''
# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for id in ids:
#     if '_' in id:
#         x = x + 1
# print(x)

# -----------------------------------------------
'''
Here we learnt about 
Error Handling , try ,expect , continue 

'''
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     if user_input.startswith("add") : #or 'new' in user_input , not in user_input
#
#         todoo = user_input[4:] + "\n"
#         with open("files/todo.txt", 'r') as file: #with method
#             todo = file.readlines()
#             #no need to mention close method here
#         todo.append(todoo)
#
#         with open('files/todo.txt', 'w') as file:
#             file.writelines(todo)#w - write r- read
#
#     elif user_input.startswith("show"):
#         file=open('files/todo.txt', 'r')
#         todo=file.readlines()
#         file.close()
#         # print(todo) #/n comes after every iteration - we use replace method to solve this gap issue
#         new_todo=[] #strip
#         for index,item in enumerate(todo):
#             new_item=item.strip('\n') #strip
#             new_todo.append(new_item) #strip
#             row=f"{index+1}.{new_item}" #strip
#             print(row)
#         # print(new_todo)
#     elif user_input.startswith("edit"):
#         try:
#             number = user_input[5:]
#             print(user_input[5:])
#             number=int(user_input[5:])
#             number = number - 1
#             new_todo = input("Enter new Todo: ") +'\n'
#             with open('files/todo.txt', 'r') as file:
#                 afterread=file.readlines()
#             print(afterread)
#             afterread[number] = new_todo
#             print(afterread[number])
#             with open('files/todo.txt', 'w') as file:
#                 file.writelines(afterread)
#                 #changes after just write the list thats all dont do  file.writelines(afterread[number])
#         except ValueError:
#             print("Your cmd is not valid , enter number")
#             continue # if i give continue exit from rest of elif conditions and return to strating program
#
#     elif user_input.startswith("complete"):
#         try:
#
#             completed=int(user_input[9:])
#             with open('files/todo.txt', 'r') as file:
#                 afterread=file.readlines()
#             print(afterread)
#             print('read')
#             # new_todo = []  # strip
#             # for index, item in enumerate(afterread):
#             #     new_item = item.strip('\n')  # strip
#             #     new_todo.append(new_item)  # strip
#             #     row = f"{index + 1}.{new_item}"  # strip
#             #     print(row)
#             # print(new_todo)
#
#             completed = completed - 1
#             todo_to_remove=afterread[completed].strip('\n')
#             del_item = afterread.pop(completed)
#             print(f"{todo_to_remove} has been deleted ")
#             with open('files/todo.txt', 'w') as file:
#                 file.writelines(afterread)
#             print('write successfully')
#         except IndexError:
#             print('the value you enter not present  in todo list')
#             continue
#         except ValueError:
#             print("Your cmd is not valid , enter number")
#             continue # if i give continue exit from rest of elif conditions and return to strating program(continue the while loop from beginning)
#
#
#     elif user_input.startswith("exit"):
#         break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
#     else:
#         print('cmd not valid')
# print("bye")

# ---------------------------------------------------------
'''
Syntax Error and Exception Error 

the difference between of the two , program check syntax first and then check logic of the program like index Error or more ..

'''
# -----------------------

'''
if condition doesn't check the error , it is handle the logic only.
exception handle error not logic
'''
# try:
#     width =float(input('enter your width: ')) #if user enter four instead of 4 throwing value error catch with exception
#     length=float(input("enter your length: "))
#     if width==length:
#         exit("The looks like squre")
#     area = length * width
#     print(area)
#
# except ValueError:
#     print('Type Number')

# -------------------------------------------------

'''
Take a look at the code in the coding area. You should expand that code. Your task is to:

(1) calculate the percentage using the  value/total * 100 formula

(2) print out the message "That is 40.0%" (or whatever the calculated percentage value is)

(3) If the user doesn't enter a number but a string (e.g., hi) for the total value or the value, the program should print out the message shown in the screenshot below:

'''
# try:
#     total =float(input('enter your total: ')) #if user enter four instead of 4 throwing value error catch with exception
#     Value=float(input("enter your Value: "))
#
#     per = (Value/total)*100
#     print(per)
#
#     #Calculate my 10th percentage
#     # per = (total / Value) * 100
#     # print(per)
#
#     # Calculate my 12th percentage
#     # value=value/2
#     # per = (Value/total) * 100
#     # print(round(per))
#
# except ValueError:
#     print('need  Number , run again')

# ------------------------------------------------
'''
Solution

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = value / total_value * 100
    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
    
'''
'''
As you might know, it is not mathematically possible to divide a number by zero. Consequently, this is also not possible in Python either -you will get a ZeroDivisionError if you try:

>>> 20 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
With that in mind, your task for this exercise is to extend the program you created in Exercise 1 by displaying a message to the user when they enter 0 for the "total value".
'''

# try:
#     total =float(input('enter your total: ')) #if user enter four instead of 4 throwing value error catch with exception
#     Value=float(input("enter your Value: "))
#
#     per = (Value/total)*100
#     print(per)
#
#     #Calculate my 10th percentage
#     # per = (total / Value) * 100
#     # print(per)
#
#     # Calculate my 12th percentage
#     # value=value/2
#     # per = (Value/total) * 100
#     # print(round(per))
#
# except ValueError:
#     print('need  Number , run again')
# except ZeroDivisionError:
#     print(f"Your total value cannot be zero.")

# ----------------------------------------------------------------

'''
solution

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = value / total_value * 100
    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero.")
    
'''

# ---------------------------------------------

'''
Your task for this exercise is to:

(1) loop over the colors items

(2) print out the item in every loop if the item is greater than 50.

In other words, the output of your program would be:

98
54
54
'''

# colors = [11, 34, 98, 43, 45, 54, 54]
#
# for item in colors:
#     if item >50:
#         print(item)

# ------------------------------------

'''
Your task for this exercise is to:

(1) loop over the passwords list and

(2) print out only those passwords that are less than 8 characters.
'''

# passwords = ["acasd9983k", "34aiufaac99", "98jjanf", "afjj879"]
#
# for password in passwords:
#     if len(password) < 8:
#         print(password)

# ----------------------------------

'''
In the coding area we have defined a list of filenames. Your task is to:

(1) loop over the list

(2) print out the filename of each item without the extension using slicing.

The output of your program would look like this:

report
downloads
success
folders
'''

# filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
#
# # Print filenames without their extensions
# for filename in filenames:
#     print(filename[:-4])


# -----------------------------------------

'''
This exercise is similar to the previous one but with an added feature. In the coding area we have defined a list of filenames. Your task is to:

(1) loop over the list

(2) print out the filename of each item without the extension using slicing and with the first letter capitalized.

The output of your program would look like this:

Report
Downloads
Success
Folders
'''

# filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
#
# # Print filenames without their extensions
# for filename in filenames:
#     filename=filename.capitalize()
#     print(filename[:-4])

# --------------------------------------------
'''
use function method for repetative codes
we can't access  inside function variable outside , we can use global variable inside function

'''
# def get_todos():
#     with open("files/todo.txt", 'r') as file_local:  # with method
#         todo_local = file_local.readlines()
#     return todo_local
#
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     if user_input.startswith("add") : #or 'new' in user_input , not in user_input
#
#         todoo = user_input[4:] + "\n"
#         todo=get_todos()
#         todo.append(todoo)
#
#         with open('files/todo.txt', 'w') as file:
#             file.writelines(todo)#w - write r- read
#
#     elif user_input.startswith("show"):
#         todo=get_todos()
#         # print(todo) #/n comes after every iteration - we use replace method to solve this gap issue
#         new_todo=[] #strip
#         for index,item in enumerate(todo):
#             new_item=item.strip('\n') #strip
#             new_todo.append(new_item) #strip
#             row=f"{index+1}.{new_item}" #strip
#             print(row)
#         # print(new_todo)
#     elif user_input.startswith("edit"):
#         try:
#             number = user_input[5:]
#             print(user_input[5:])
#             number=int(user_input[5:])
#             number = number - 1
#             new_todo = input("Enter new Todo: ") +'\n'
#             todo=get_todos()
#             todo[number] = new_todo
#             print(todo[number])
#             with open('files/todo.txt', 'w') as file:
#                 file.writelines(todo)
#                 #changes after just write the list thats all dont do  file.writelines(afterread[number])
#         except ValueError:
#             print("Your cmd is not valid , enter number")
#             continue # if i give continue exit from rest of elif conditions and return to strating program
#
#     elif user_input.startswith("complete"):
#         try:
#
#             completed=int(user_input[9:])
#             todo=get_todos()
#             print(todo)
#             print('read')
#             # new_todo = []  # strip
#             # for index, item in enumerate(afterread):
#             #     new_item = item.strip('\n')  # strip
#             #     new_todo.append(new_item)  # strip
#             #     row = f"{index + 1}.{new_item}"  # strip
#             #     print(row)
#             # print(new_todo)
#
#             completed = completed - 1
#             todo_to_remove=todo[completed].strip('\n')
#             del_item = todo.pop(completed)
#             print(f"{todo_to_remove} has been deleted ")
#             with open('files/todo.txt', 'w') as file:
#                 file.writelines(todo)
#             print('write successfully')
#         except IndexError:
#             print('the value you enter not present  in todo list')
#             continue
#         except ValueError:
#             print("Your cmd is not valid , enter number")
#             continue # if i give continue exit from rest of elif conditions and return to strating program(continue the while loop from beginning)
#
#
#     elif user_input.startswith("exit"):
#         break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
#     else:
#         print('cmd not valid')
# print("bye")

'''
Function example 
we can't access funtion inside variable outside , we can use global variable inside function
'''

# def greet():
#     message = "Hello World"
#     new_msg=message.capitalize()
#     return new_msg
#
# print(greet())


# Same way we mentioned in our todo app
# ------------------------------------------------
'''
print() and return both are different

'''
# def greet():
#     message = "Hello World"
#     new_msg=message.capitalize()
#     # return new_msg #if i dont give return what we get as a output none
#     # print(new_msg)
#     return new_msg
#
# print(greet())
# print(len(greet()))

# if you try to print the len og message get error , bcz it doesnt return nothing , if use return show the length of the message

# -----------------------------------------
'''
bonus example
'''
# def getAverage():
#     with open(rf"C:\Users\devap\desktop\todoapp\bouns\file\data.txt",'r') as file:
#         data = file.readlines()[1:] #here we remove 1st item from list we use thiss
#     items=[]
#     for item in data:
#         item=int(item.strip('\n'))
#         items.append(item)
#     print(items)
#     return sum(items)/len(items)
#
# Average=getAverage()
# print(f"the average is: {Average}")

# -------------------------------

'''
Another method
'''


# def getAverage():
#     with open(rf"C:\Users\devap\desktop\todoapp\bouns\file\data.txt",'r') as file:
#         data = file.readlines() #here we remove 1st item from list we use thiss
#     values=data[1:]
#     values=[float(i) for i in values]
#     Avg_local=sum(values) / len(values)
#     return Avg_local
#
# Average=getAverage()
# print(f"the average is: {Average}")


# --------------------

'''
Complete the function given in the coding area. The function should:

(1) calculate the maximum value of the grades list,

(2) return the calculated value.

After completing the function definition you should call the function and print out its output.

The output of your code would be:

9.7
'''

# def get_grades():
#     grades = [9.6, 9.2, 9.7]
#     maximum =max(grades)
#     return maximum
#
# values = get_grades()
# print(values)

# -------------------------------
'''
The get_max function you created in the previous exercise returned 9.7. 

In this exercise, you should:

(1) change the function so this time it returns the following string:

"Max: 9.7, Min: 9.2"

where 9.7 is the maximum, and 9.2 is the minimum.

'''
# def get_grades():
#     grades = [9.6, 9.2, 9.7]
#     maximum =max(grades)
#     minimum=min(grades)
#     return f"Max:{maximum},Min:{minimum}"
#
# values = get_grades()
# print(values)

# ----------------------------
'''
Your task for this exercise is to:

(1) define a function named format_filename

(2) define a variable named filename inside the function

(3) assign the string "report.txt" to filename

(4) remove the last four characters (.txt) from the filename string and capitalize its first letter.

(5) return the altered string.

(6) call the function and print out its output.

'''

# def format_filename():
#     filename = "report.txt"
#     filename = filename.replace('.txt', "")
#     filename_local = filename.capitalize()
#     return filename_local
#
# Values=format_filename()
# print(Values)

'''
Another method
'''

# def format_filename():
#     filename = "report.txt"  # Hardcoded filename
#     formatted_name = filename[:-4].capitalize()
#     return formatted_name
#
# print(format_filename())

# ------------------------------------
'''

Your task for this exercise is to:

(1) define a function named square_number

(2) define a variable named number inside the function

(3) assign the integer 5 to number

(4) raise number to the power of 2 and store the result in a result variable.

(5) return the result variable.

(6) call the function and print its output

'''
# def square_number():
#     number=5
#     result=number**2
#     return result
# Values=square_number()
# print(Values)

# ---------------------------------------
'''
Bug Fixing Exercise
'''
# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     print(maximum)
#
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
#
# print(fahrenheit)

# if i print get error because there is no return on fiunction

# solution

# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     return maximum
#
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
#
# print(fahrenheit)

# -----------------------------------------

'''
using arguments and parameters

'''
# def greet(message): #parameter
#     new_msg=message.capitalize()
#     # return new_msg #if i dont give return what we get as a output none
#     # print(new_msg)
#     return new_msg
#
# Value = greet("hello world") #argument
# print(Value)


# -------------------------------------------------------
'''
Using functions and Arguments in  the todo app, see get todo() and 
write todo function how we pass the arugement


for example if you return as filepath in get todo function (), 
show atripute error bcz filepath string not happend method. error accour this line todo.append(todoo)

if you reassign filepath like fileptah = todo1.txt, 
showing error bcz that file doesnt exist 

'''
# def get_todos(filepath):
#     with open(filepath, 'r') as file_local:  # with method
#         todo_local = file_local.readlines()
#     return todo_local

# def write_todos(filepath,todo_arg):
#     with open(filepath, 'w') as file:
#         file.writelines(todo_arg)
#         '''
#         here we dont return anything bcz we need to write on the text
#         file. that's it ,  but get_todos function we need existing list based on that
#         we add new todos so that we were used return there
#
#         '''
#
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     if user_input.startswith("add") : #or 'new' in user_input , not in user_input
#
#         todoo = user_input[4:] + "\n"
#         todo=get_todos("files/todo.txt")
#         todo.append(todoo)
#
#         write_todos('files/todo.txt',todo)
#
#     elif user_input.startswith("show"):
#         todo=get_todos("files/todo.txt")
#         # print(todo) #/n comes after every iteration - we use replace method to solve this gap issue
#         new_todo=[] #strip
#         for index,item in enumerate(todo):
#             new_item=item.strip('\n') #strip
#             new_todo.append(new_item) #strip
#             row=f"{index+1}.{new_item}" #strip
#             print(row)
#         # print(new_todo)
#     elif user_input.startswith("edit"):
#         try:
#             number = user_input[5:]
#             print(user_input[5:])
#             number=int(user_input[5:])
#             number = number - 1
#             new_todo = input("Enter new Todo: ") +'\n'
#             todo=get_todos("files/todo.txt")
#             todo[number] = new_todo
#             print(todo[number])
#             write_todos('files/todo.txt',todo)
#         except ValueError:
#             print("Your cmd is not valid , enter number")
#             continue # if i give continue exit from rest of elif conditions and return to strating program
#
#     elif user_input.startswith("complete"):
#         try:
#
#             completed=int(user_input[9:])
#             todo=get_todos("files/todo.txt")
#             print(todo)
#             print('read')
#             # new_todo = []  # strip
#             # for index, item in enumerate(afterread):
#             #     new_item = item.strip('\n')  # strip
#             #     new_todo.append(new_item)  # strip
#             #     row = f"{index + 1}.{new_item}"  # strip
#             #     print(row)
#             # print(new_todo)
#
#             completed = completed - 1
#             todo_to_remove=todo[completed].strip('\n')
#             del_item = todo.pop(completed)
#             print(f"{todo_to_remove} has been deleted ")
#             write_todos('files/todo.txt',todo)
#             print('write successfully')
#         except IndexError:
#             print('the value you enter not present  in todo list')
#             continue
#         except ValueError:
#             print("Your cmd is not valid , enter number")
#             continue # if i give continue exit from rest of elif conditions and return to strating program(continue the while loop from beginning)
#
#
#     elif user_input.startswith("exit"):
#         break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
#     else:
#         print('cmd not valid')
# print("bye")

# -------------------------------------------------

'''
Decoupling in Python means making parts of a program independent 
from each other so that one part can change without affecting the other parts.

he said he cover these concept later on this course.
'''
# test="hello world".split(" ")
# print(test)

# -----------
# feet_inches=input("Enter the feet and inches: ")

# def convert(feet_inches_local):
#     parts=feet_inches_local.split(" ") # assign variable to store List of values
#     feet = float(parts[0])
#     inches = float(parts[1])
#     meters = feet * 0.3048 + inches * 0.0254
#
#     # return f"user feet and inche in meters is {meters}"
#     # #here okay but you want to use this function result somewhere in your code you should return value instead of string , then only we can validate this like we use if condition based on this , that condition dependent on this return
#     return meters
# Value=convert(feet_inches)
# print(Value)
#
# if Value < 1:
#     print('your height not eligible to play this game ')
# else:
#     print('Elgible to play this game')

# ------------------------------------------------------
'''
Your task for this exercise is to:

(1) define a function named liters_to_m3

(2) the function should take a liters parameter

(3) in the function you should converts liters to cubic meters (1000 liters = 1 cubic meters)

(4) then, return the cubic meters.
'''
# def liters_to_m3(liters_local):
#     liters_local=int(liters_local)
#     cubic=liters_local/1000
#     return f"your cubic is {cubic}"
#
# Value = liters_to_m3(2500)
# print(Value)

# ----------------------

'''

Complete the strength function. The function will check the strength of a given password. Specifically, the function should:

(1) get a password argument

(2) return the string "Strong Password" if all of the following conditions are true:

Password is 8 or more characters

Password has at least one uppercase letter

Password has at least one digit.

(3) if one or more of the above conditions are not met, the function should return "Weak Password".

'''

# user_password = input("Enter your pass: ")
#
# def get_strong_password(user_password):
#
#     result={} #use dic for claer data with lable
#
#     if len(user_password) >=8:
#         result["Charcter"]=True #use this method to add in dic
#
#     else:
#         result["Charcter"]=False
#
#
#     digit = False
#
#     for item in user_password:
#         if item.isdigit():
#             digit = True
#     result['digit']=digit
#
#     Upper = False
#
#     for item in user_password:
#         if item.isupper():
#             Upper = True
#     result["Uppercase"]=Upper
#
#     print(result)
#     print(result.values())
#     return result.values()
# Results=get_strong_password(user_password)
# if all(Results):
#     print("Yes, strong Password")
# else:
#     print("No, strong Password")

# --------------------------------------------------

'''
Define a function that:

(1) takes a list as an argument

(2) returns the average value of the list items.

For example, if I called your function with foo([10, 20, 30, 40]) it should return 25 which is the average of the numbers of the list.

Note: You can name the function anyway you want. It's enough to define the function. There is no need to call it.

'''
# marks=[10, 20, 30, 40]
#
# def average(Marks_arg):
#     average=sum(Marks_arg)/len(Marks_arg)
#     return average
# Value= average(marks)
# print(Value)

# ---------------------------------------

'''
Define a function that:

(1) takes a person's name as a parameter

(2) greets the person with Hi Person.

For example, if I call your function using foo("lisa") the function should return Hi lisa .
'''

# def person_name(name):
#     return f"Hello {name}"
#
# Value=person_name("Hari")
# print(Value)

# ---------------------------------

'''
Implement a function that:

(1) takes two strings as parameters,

(2) concatenates the strings

(3) returns the concatenated string.

For example, if I called your function with foo('hello', 'hi') it would return hellohi.

'''
# def concatenates_str(greeting,name):
#     result=greeting+" "+name
#     return result
# Value=concatenates_str("Good Morning","Hari")
# print(Value)

# -----------------------------------------

'''
Implement a function that:

(1) takes a person's name (e.g. 'john') as a parameter

(2) returns a greeting (e.g. Hi John)

Note that the first letter of the person's name should be capitalized by the function.

'''
# def person_name(name):
#     result = name.capitalize()
#     return f"Hi {result}"
#
# Value=person_name('john')
# print(Value)

# -------------------------------------------------
'''
default function arguments 

'''

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
#
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     if user_input.startswith("add") : #or 'new' in user_input , not in user_input
#
#         todoo = user_input[4:] + "\n"
#         todo=get_todos() #default function
#         todo.append(todoo)
#
#         write_todos(todo)#default function , No need to mention default arugument you should mention remaing one only
#
#     elif user_input.startswith("show"):
#         todo=get_todos()
#         # print(todo) #/n comes after every iteration - we use replace method to solve this gap issue
#         new_todo=[] #strip
#         for index,item in enumerate(todo):
#             new_item=item.strip('\n') #strip
#             new_todo.append(new_item) #strip
#             row=f"{index+1}.{new_item}" #strip
#             print(row)
#         # print(new_todo)
#     elif user_input.startswith("edit"):
#         try:
#             number = user_input[5:]
#             print(user_input[5:])
#             number=int(user_input[5:])
#             number = number - 1
#             new_todo = input("Enter new Todo: ") +'\n'
#             todo=get_todos()
#             todo[number] = new_todo
#             print(todo[number])
#             write_todos(todo)
#         except ValueError:
#             print("Your cmd is not valid , enter number")
#             continue # if i give continue exit from rest of elif conditions and return to strating program
#
#     elif user_input.startswith("complete"):
#         try:
#
#             completed=int(user_input[9:])
#             todo=get_todos()
#             print(todo)
#             print('read')
#             # new_todo = []  # strip
#             # for index, item in enumerate(afterread):
#             #     new_item = item.strip('\n')  # strip
#             #     new_todo.append(new_item)  # strip
#             #     row = f"{index + 1}.{new_item}"  # strip
#             #     print(row)
#             # print(new_todo)
#
#             completed = completed - 1
#             todo_to_remove=todo[completed].strip('\n')
#             del_item = todo.pop(completed)
#             print(f"{todo_to_remove} has been deleted ")
#             write_todos(todo)
#             print('write successfully')
#         except IndexError:
#             print('the value you enter not present  in todo list')
#             continue
#         except ValueError:
#             print("Your cmd is not valid , enter number")
#             continue # if i give continue exit from rest of elif conditions and return to strating program(continue the while loop from beginning)
#
#
#     elif user_input.startswith("exit"):
#         break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
#     else:
#         print('cmd not valid')
# print("bye")


# ----------------------------------------
'''
FOr future reference use this doc string function
Help function
'''
# def person_name(name):
#     """Just name print function"""
#     result = name.capitalize()
#     return f"Hi {result}"
#
# Value=help(person_name)
# print(Value)

# --------------------------------
'''
MultilineString

'''
# test="""
# MultilineString
# """
#
# print(test)

# ------------------------------
'''
Earlier Function 

here we couldn't access the feet and inches like as i mentioned before

'''

# feet_inches=input("Enter the feet and inches: ")

# def convert(feet_inches_local):
#     parts=feet_inches_local.split(" ") # assign variable to store List of values
#     feet = float(parts[0])
#     inches = float(parts[1])
#     meters = feet * 0.3048 + inches * 0.0254
#
#     # return f"user feet and inche in meters is {meters}"
#     # #here okay but you want to use this function result somewhere in your code you should return value instead of string , then only we can validate this like we use if condition based on this , that condition dependent on this return
#     return meters
# Value=convert(feet_inches)
# print(Value)
#
# if Value < 1:
#     print('your height not eligible to play this game ')
# else:
#     print('Elgible to play this game')

'''
After Done decoupling 
Here seperate the fucntions like parsing and covert , here we can access the things
'''



# feet_inches=input("Enter the feet and inches: ")
#
# def parse(feet_inches_local):
#     parts = feet_inches_local.split(" ")  # assign variable to store List of values
#     feet = float(parts[0])
#     inches = float(parts[1])
#     return feet, inches
#
# def convert(feet,inches):
#     meters = feet * 0.3048 + inches * 0.0254
#     return meters

# f,i=parse(feet_inches)
# print(parse(feet_inches)) #here it return as tuples
# print(f,i)
#
# Value=convert(f,i)
# print(Value)
# -------------
# feet_inches_tuples=parse(feet_inches)
# print(feet_inches_tuples) #here it return as tuples
#
# Value=convert(feet_inches_tuples[0],feet_inches_tuples[1])
# print(Value)

# if Value < 1:
#     print('your height not eligible to play this game ')
# else:
#     print('Elgible to play this game')

# -------------------------------------------
'''
Here is the exact solution as you expect result like 
return f"user feet and inche in meters is {meters}"
'''
# feet_inches = input("Enter feet and inches: ")
#
# def parse(feet_inches_local):
#     parts = feet_inches_local.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#     return feet, inches
#
#
# def convert(feet, inches):
#     meters = feet * 0.3048 + inches * 0.0254
#     return meters
#
#
# def format_output(feet, inches, meters):
#     return f"user feet {feet} and inch {inches} in meters is {meters}"
#
#
# # ---- Main Flow ----
# feet, inches = parse(feet_inches)
# meters = convert(feet, inches)
#
# result = format_output(feet, inches, meters)
# print(result)
#
# if meters < 1:
#     print("your height not eligible to play this game")
# else:
#     print("Eligible to play this game")

# ---------------------------------

'''
Define a function named get_age  which:

(1) has two parameters, year_of_birth and current_year

(2) the current_year  parameter should be a default parameter

(3) the default value of current_year should be the current year (e.g., the integer 2025)

(4) the function should calculate and return the age of the user given the year_of_birth and the current_year.

'''

# def get_age(year_of_birth,current_year=int(2026)):
#     Calculate_age=int(current_year)-(year_of_birth)
#     return Calculate_age
# result= get_age(1998)
# print(result)

# -----------------------------------------------------
'''
Write a get_nr_items function that:

(1) gets as a parameter one string with commas (e.g., "john,lisa, teresa")

(2) the function calculates the number of words (i.e., three words in the above example)

(3) returns the number of words.

For example, if I called your function with get_nr_items("john,lisa, teresa") it would return 3.
'''

# def get_nr_items(names):
#     find_words=names.split(",")
#     print(find_words)
#     count = 0
#     for item in find_words:
#         count+=1
#     return count
#
# Result= get_nr_items("john,lisa, teresa, john , mahesh,sanjay,hari")
#
# print(Result)

'''
Another Methods
'''
# user_input = input("Enter your Friends name seperate by , example: john,hari...: ")

# def get_nr_items(user_input_arg):
#     items = user_input.split(',')
#     return len(items)
# result = get_nr_items(user_input)
# print(result)

# ----------------------------------------

'''
Define a function that:

(1) takes the side length of a square as a parameter

(2) calculates and returns the area of a square.

For example, if I was to call your function with foo(7)it would return 49.  You can name the function anyway you want.

'''

# def find_square(side_length_local):
#     side_length_local=int(side_length_local)
#     area=side_length_local**2
#     return area
#
# result = find_square(4)
# print(result)


'''
Define a function that:

(1) takes a temperature as a parameter

(2) returns "Warm" if the temperature is greater than 7

(3) returns "Cold" if the temperature is equal to or less than 7.

If I called your function with foo(10) it would return Warm. If I called it with foo(7) or foo(5) it would return Cold and so on.

'''
# user_Temperature=input("Enter Temperature : ")
#
# def get_temperature(Current_temperature):
#     Current_temperature=int(Current_temperature)
#     if Current_temperature == 0 :
#         return "Very Cold"
#     elif Current_temperature >7:
#         return "Warm"
#     elif Current_temperature <= 7:
#         return "Cold"
#
# result = get_temperature(user_Temperature)
# print(result)

'''
Define a function that:

(1) takes a string as a parameter

(2) returns False if the string contains less than 8 characters

(3) returns True if the string contains 8 or more characters

In other words, if I called your function with foo("mypass") it would return False. If I called it with foo("mylongpassword") it would return True, and so on.

'''
# user_password=input("Enter your password: ")
#
# def check_pass_len(user_password_local):
#     if len(user_password_local) < 8:
#         return False
#     elif len(user_password_local) >= 8:
#         return True
# # result = check_pass_len(user_password)
# # print(result)
#
# if check_pass_len(user_password)==True:
#     print("Password is valid")
# elif check_pass_len(user_password)==False:
#     print("Password is not valid")
#     user_password = input("Enter your password: ")
#     print(check_pass_len(user_password))


# -------------------------------

'''
here i create the function user get 
asked enter password more than 8 charcter untill charcter length more than 8
I used while loop to acheive this ...

'''
# user_password = input("Enter your password: ")
#
# def check_pass_len(user_password_local):
#     if len(user_password_local) < 8:
#         return False
#     else:
#         return True
#
#
# while check_pass_len(user_password) == False:
#     print("Password is not valid. Must be at least 8 characters.")
#     user_password = input("Enter your password again: ")
#
# print("Password is valid")

# ----------------------

'''
seperate the fuctions from main file to reduce long coding 
create function.py file same dirtory where the main.py located and paste the function code there

use starting line in main.py file import functions and inside the program call like functions.get_todos like that

'''
# import functions
# while True:
#     user_input = input("Enter Your Todo add , show , edit, exit ,complete: ").strip()
#     if user_input.startswith("add") : #or 'new' in user_input , not in user_input
#
#         todoo = user_input[4:] + "\n"
#         todo=functions.get_todos() #default function
#         todo.append(todoo)
#
#         functions.write_todos(todo)#default function , No need to mention default arugument you should mention remaing one only
#
#     elif user_input.startswith("show"):
#         todo=functions.get_todos()
#         # print(todo) #/n comes after every iteration - we use replace method to solve this gap issue
#         new_todo=[] #strip
#         for index,item in enumerate(todo):
#             new_item=item.strip('\n') #strip
#             new_todo.append(new_item) #strip
#             row=f"{index+1}.{new_item}" #strip
#             print(row)
#         # print(new_todo)
#     elif user_input.startswith("edit"):
#         try:
#             number = int(user_input[5:])
#             print(user_input[5:])
#             # number=int(user_input[5:])
#             number = number - 1
#             new_todo = input("Enter new Todo: ") +'\n'
#             todo=functions.get_todos()
#             todo[number] = new_todo
#             print(todo[number])
#             functions.write_todos(todo)
#         except ValueError:
#             print("Your cmd is not valid , enter number")
#             continue # if i give continue exit from rest of elif conditions and return to strating program
#
#     elif user_input.startswith("complete"):
#         try:
#
#             completed=int(user_input[9:])
#             todo=functions.get_todos()
#             print(todo)
#             print('read')
#             # new_todo = []  # strip
#             # for index, item in enumerate(afterread):
#             #     new_item = item.strip('\n')  # strip
#             #     new_todo.append(new_item)  # strip
#             #     row = f"{index + 1}.{new_item}"  # strip
#             #     print(row)
#             # print(new_todo)
#
#             completed = completed - 1
#             todo_to_remove=todo[completed].strip('\n')
#             del_item = todo.pop(completed)
#             print(f"{todo_to_remove} has been deleted ")
#             functions.write_todos(todo)
#             print('write successfully')
#         except IndexError:
#             print('the value you enter not present  in todo list')
#             continue
#         except ValueError:
#             print("Your cmd is not valid , enter number")
#             continue # if i give continue exit from rest of elif conditions and return to strating program(continue the while loop from beginning)
#
#
#     elif user_input.startswith("exit"):
#         break
#         # case whatever:
#         #     print("enter exact option which show in the optioin section")
#     else:
#         print('cmd not valid')
# print("bye")
# -----------------------------------


'''
feet and inches solution by author
'''

# feet_inches = input("Enter feet and inches: ")
#
#
# def parse(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#     return {"feet": feet, "inches": inches}
#
#
# def convert(feet, inches):
#     meters = feet * 0.3048 + inches * 0.0254
#     return meters
#
#
# parsed = parse(feet_inches)
#
# result = convert(parsed['feet'], parsed['inches'])
#
# print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")
#
# if result < 1:
#     print("Kid is too small.")
# else:
#     print("Kid can use the slide.")

'''
you can add seperate file parse and add seperate file convert function in another file
'''
# from bouns.feet_inches_phars import parse
# from bouns.feet_inches_convert import convert
#
# feet_inches = input("Enter feet and inches: ")
# parsed = parse(feet_inches)
#
# result = convert(parsed['feet'], parsed['inches'])
#
# print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")
#
# if result < 1:
#     print("Kid is too small.")
# else:
#     print("Kid can use the slide.")

# ----------------------------------
'''
Define a  water_state function that:

(1) gets a temperature parameter

(2) returns the string "Solid" if the temperature is less than or equal to 0

(3) returns "Liquid" if the temperature is greater than 0, but less than 100.

(4) returns "Gas" if the temperature is greater than or equal to 100.

'''


# user=input("Enter Temperature : ")
#
# def water_state(temperature):
#     temperature = float(temperature)
#     if temperature < 0 or temperature == 0:
#         return "Solid"
#     elif temperature > 0 and temperature < 100:
#         return "Liquid"
#     elif temperature > 100:
#         return "Gas"
#
#
# result=water_state(user)
# print(result)


# -------------Try while method---------------------
# user=input("Enter Temperature : ")
#
# def water_state(temperature):
#     temperature = float(temperature)
#     if temperature < 0 or temperature == 0:
#         return "Solid"
#     elif temperature > 0 and temperature < 100:
#         return "Liquid"
#     elif temperature > 100:
#         return "Gas"
#
#
# result=water_state(user)
# # while result != 'Solid':
# #     user = input("Enter Temperature again: ")
# #     result = water_state(user)
# # print('thankyou')
# # print(result)

# --------------------------------
'''

In the previous exercise, we hardcoded the values 0 and 100. However, it is better to place those values in constants. Therefore, your task is to:

(1) create a FREEZING_POINT and a BOILING_POINT variable outside of the water_state function and store the values 0 and 100 in them respectively.

(2) modify the function of the previous exercise by using the variables given above instead of the hardcoded 0 and 100 values. The previous function is provided in the coding area.

'''

# FREEZING_POINT=0
# BOILING_POINT=100
#
# user=input("Enter Temperature : ")
#
# def water_state(temperature):
#     temperature = float(temperature)
#     if temperature < FREEZING_POINT or temperature == FREEZING_POINT:
#         return "Solid"
#     elif temperature > FREEZING_POINT and temperature < BOILING_POINT:
#         return "Liquid"
#     elif temperature > BOILING_POINT:
#         return "Gas"
#
#
# result=water_state(user)
# print(result)

# ----------------------------
'''
Define a function that:

(1) takes temperature as a parameter

(2) returns "Hot" if the temperature is greater than 25

(3) returns "Warm" if the temperature is between 15 and 25, including 15 and 25.

(4) returns "Cold" if the temperature is less than 15.

If I called your function with foo(10) it would return "Cold". 

Calling it with foo(15), foo(16), or foo(25) would all return "Warm". Calling it with foo(26) would return "Hot".

'''
# user=input("Enter Temp: ")
# def get_temperature(temperature):
#     temperature=float(temperature)
#     if temperature < 15:
#         return "Cold"
#     elif temperature >= 15 and temperature < 25:
#         return "Warm"
#     elif temperature >= 25 :
#         return "Hot"
#
# result=get_temperature(user)
# while result != "Warm":
#     user = input("Enter Temp Again: ")
#     result = get_temperature(user)
#     print(result)
# print("hello")
# print(f"correct:{result}")
'''
when i enter 25 we get enter again because we dont print after result they directly go while loop and ask enter input from user , then print happen bczs while loop inside print there.
'''
# -------------------------

'''
Github and git both are version control softwere , 
git can be used in local computer , github cloud based , you can be get more control of code via version control system , 
lets take an example , you made changes in your code four days before right now you forgot what changes you made , 
that time git or github helps you to get that version code , this is the use case of the git and github
'''

# ---------------------------------------
'''
some modules are not globalspace like eg. print in globalspcace , 
but time and date are not like this , it is module one we should be implemented from import
'''
#
# import time
#
# now = time.strftime("DATE:%b-%d-%y Time:%H:%M:%S")
# print(f"it is {now}")

# ----------------------

'''

you can be used varibale in fuctions module , 
bczs you want change one stretch eveything, give filebath as variable
Eg. FILEBATH ='todo.txt'

you can check it like python console

import functions
>>> dir(functions)
['FILEBATH', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'get_todos', 'write_todos']

'''

import glob

# myfiles = glob.glob("*.txt") #glob module and 2nd one is glob function
# print(myfiles)

# myfiles = glob.glob("function module/*.txt")
# print(myfiles)

# for filepaths in myfiles:
#     with open(filepaths,'r') as file:
#         readmode=file.readline().upper()
#     print(readmode)
#     print(filepaths)
#
#     with open(filepaths,'w') as file:
#         file.writelines(readmode + '\n')
#         file.writelines("Hari")

# --------------

# user = input("Enter your to do: ")
#
# with open(rf"C:\Users\devap\desktop\todoapp\function module\test1.txt",'r') as file:
#     readed= file.readlines()
#
#
# readed.append('\n'+user)
#
# with open(rf"C:\Users\devap\desktop\todoapp\function module\test1.txt",'w') as file:
#     file.writelines(readed)
# print('complete adding')

# --------------------

# import glob
#
# myfiles = glob.glob("function module/*.txt")
#
#
# for filepaths in myfiles:
#     with open(filepaths,'r') as file:
#         readmode=file.readlines()
#         readmode.append('\n' + 'Hari')
#
#     with open(filepaths,'w') as file:
#         file.writelines(readmode)
#
#readlines -list
#realine -str

# -------------------------------------------

# import glob
# myfiles = glob.glob("function module/*.txt")
#
# for item in myfiles:
#     with open(item,'r') as file:
#         print(item)
#         print(file.readline().upper())

# --------------------------------------------
# experiment 3
'''
csv file handling methods i used here.
'''
# import csv
#
# user = input("Enter city: ")
# with open("wheather.csv","r") as file:
#     data = list(csv.reader(file))
# # print(data)
#
# for item in data[1:]:
#     if item[0]==user:
#         print(item[1])

# --------------------------------------------

'''
making the files as zip here

'''

# import shutil
# shutil.make_archive("output","zip","function module")

# ---------------------------------
# import webbrowser
#
# user_term= input("Enter a search term : ")
#
# webbrowser.open(f"https://www.google.com/search?q={user_term}")

# -------------------------------------------------------

'''

work with json - my method

'''



# import json
#
# with open('questions.json','r') as file:
#     content=file.read()
# print(content)
# # print(type(content)) # give here as a string
#
# data =json.loads(content)
# print(data)
# # print(type(data))#give here as list
#
# for item in data:
#     print(item["question"])
#     for index, alternative in enumerate(item["options"]):
#         print(index+1, "-" ,alternative)
#     user=int(input("Enter your answer : "))
#     user=user-1
#     user1=item["options"][user]
#     print(user1)
#     user_index_number=item["options"].index(user1)
#     user_index_number=user_index_number+1
#     print(user_index_number)
#     if user_index_number==item["crtanswer"]:
#         print(f"crtanswer is {item["crtanswer"]}")
#     else:
#         print(f'wrong answer , correct answer is {item["crtanswer"]}')

'''
work with json - Actual method

'''

# import json
#
# with open('questions.json','r') as file:
#     content=file.read()
# print(content)
# # print(type(content)) # give here as a string
#
# data =json.loads(content)
# print(data)
# # print(type(data))#give here as list
# Score = 0;
# result=""
# for item in data:
#     print(item["question"])
#     for index, alternative in enumerate(item["options"]):
#         print(index+1, "-" ,alternative)
#     user=int(input("Enter your answer : "))
#     item["user_Answer"]=user
#
#
# for index,item in enumerate(data):
#     if item["user_Answer"] == item["crtanswer"]:
#         Score += 1
#         result = "Crt Ans"
#     else:
#         result = "wrong Ans"
#
#     message= (f"{result} :{index+1}- your answer :{item["user_Answer"]} \n"
#                   f"crtanswer: {item["crtanswer"]}")
#     print(message)
#
# print(Score ,"/" , len(data))

# -----------------------------------

# import random
#
# # Get two numbers from the user and covert them to integers
# lower_bound = int(input("Enter the lower bound: "))
# upper_bound = int(input("Enter the upper bound: "))
#
# # Pick a random int using randrange()
# rand = random.randrange(lower_bound, upper_bound + 1) # We add 1 to upper_bound because randrange does not include the upper_bound number.
#
# print(rand)
# ------------------bug exercise----------------
# parsers.py
#
#
# def parse(user_input):
#     """Extract the values split by a comma in a string
#     and return the two values via a dictionary.
#     """
#     # Get the two values in a list
#     parts = user_input.split(",")
#
#     # Store the two values in variables
#     lower_bound = int(parts[0])
#     upper_bound = int(parts[1])
#
#     # Inject the values in a dictionary
#     return {"lower_bound": lower_bound, "upper_bound": upper_bound}
#
# main.py
#
# from parsers import parse
# import random
#
# # Ask the user to enter a lower and an upper bound divided by a comma
# user_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10)")
#
# # Parse the user string by calling the parse function
# parsed = parse(user_input)
#
# # Pick a random int between the two numbers
# rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])
#
# print(rand)
#print(parsed)
'''

check git working

'''


