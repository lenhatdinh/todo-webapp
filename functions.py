DEFAULT_PATH = 'todo_list.txt'

def get_todo(filepath=DEFAULT_PATH):
    ''' Read a text file 
    and return a list of data in file.
    '''
    # Use with-context-manager (automatically close the file):
    with open(filepath,"r") as file:
        data_in_file = file.readlines()
        #file.close() # A good practice to close the file after finish the work
    return data_in_file

def update_file(newlist, filepath=DEFAULT_PATH):
    ''' Open a text file 
    and overwrite new data to file.
    '''
    with open(filepath,"w") as file:
        file.writelines(newlist)


if __name__ == '__main__':
    print("__name__: default value is \"__main__\".")
