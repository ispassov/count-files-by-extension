import os

arr_list = []
arr_del = []
menu_input = ''

def count_files_by_ext():
    for root, dirs, files in os.walk('.'):          #GET ALL FILE IN DIR AND SUBDIR
        for file_ in files:
            ext = os.path.splitext(file_)[1]        #GET FILE EXTENSION FOR EVERY FILE
            arr_list.append(ext)                    #PUT EXTENSION VALUE IN ARRAY
    type_of_ext = list(dict.fromkeys(arr_list))     #REMOVE DUPLICATES FROM ARRAY
    list.sort(type_of_ext)                          #SORT RESULT (type_of_ext) LIST
    for type_ in type_of_ext:                       #PRINT EXTENSION TYPE AND HOW MANY FILES ARE WITH THIS EXTESNSION
        print(str(type_) + ' - ' + str(arr_list.count(type_)))
    arr_list.clear()

def delete_files_by_ext():
    arr_del = input('Add extension: ').split(' ')
    if input('Delete files with this extension: ' + str(arr_del) + '\ny/n ?') == 'y':
        for root, dirs, files in os.walk('.'):
            for file_ in files:
                for ext in arr_del:
                    if os.path.splitext(file_)[1] == ext:
                        try:
                            os.remove(str(root)[0:] + '\\' + file_)
                            print(str(root)[0:] + file_ + '\\' + ' has been deleted.')
                        except:
                            print(str(root)[0:] + file_ + '\\' + ' COULD NOT DELETE !!!!!!!!!!')
    arr_del.clear()

def remove_empty_dirs():
    for root, dirs, files in os.walk('.'):
        for dir_ in dirs:
            if len(os.listdir(root + '\\' + dir_)) == 0:    #CHEKC IF FOLDER IS EMPTY
                os.rmdir(root + '\\' + dir_)
                print(root + '\\' + dir_ + ' has been removed.')

while menu_input != 'end':
    menu_input = input('1. Count files by extension.\n2. Delete files by extension.\n3. Remove empty dirs.\n(for exit type end)\n')
    if menu_input == '1':
        count_files_by_ext()
    elif menu_input == '2':
        delete_files_by_ext()
    elif menu_input == '3':
        remove_empty_dirs()