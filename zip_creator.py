import zipfile
import pathlib

#we uses shutil earlier , now we are going to use zip file, shutil was limited one

def make_archive(filepaths,destination_directory):
    destination_path=pathlib.Path(destination_directory,"compressed.zip") #here pathlip  help to create compresses.zip file under the destination_directory_folder
    with zipfile.ZipFile(destination_path,'w') as archive:
        for filepath in filepaths:
            print(filepath)
            filepath=pathlib.Path(filepath)

            ##compress.zip created but full filepath came like this compressed\Users\devap\Downloads
            ##so here we used pathlip to store exact file name under destination directory folder

            print(filepath.name)
            archive.write(filepath, arcname=filepath.name)





if __name__=="__main__":
    make_archive(filepaths=["bear.txt","essay.txt"],destination_directory="destination_directory_folder")

'''

above __name__=='__main__' - helps to check the current file wheateher working or not, like testing purpose 

'''
