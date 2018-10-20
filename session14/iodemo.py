# fout = open('session14/output.txt', 'a')
# #first parameter is the file name
# #second parameter is the mode we open it in
#     #a = append: the file is created if does not exist, subsequently writes data into it.
#     #r = read only
#     #w = start writing at the beginning of the file

import os
# print(os.getcwd())
# #get current working directory

# line1 = "How many roads must a man walk down\n"
# fout.write(line1)
# line2 = "Before you call him a man?\n"
# fout.write(line2)
# fout.close()

# print(os.path.abspath('session14/output.txt'))
# print(os.path.exists('session14/output.txt'))
# print(os.path.exists('session14/input.txt'))

# #Exercise 1
# '''Modify the function sed that takes as arguments a pattern string, a replacement string, and two filenames; it should read the first file and write the contents into the second file (creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced with the replacement string.'''

# # checking file in directory
# #  os.path.isdir('output.txt')
# #  os.path.isfile('namehere')
#  #list all folders and files on current folder
# #   os.listdir(os.getcwd())

def walk(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

# try:
#     fin = open('notexisting.txt')
# except:
#     print('Something is wrong.')

# a = [1,2,3]
# try:
#     print(a[1.5])
# except:
#     print('Something is wrong')

# folder = os.getcwd()
# walk(folder)

# import pickle

# t1 = [1, 2, 3]
# f = open('save.p', 'wb')
# s = pickle.dump(t1, f)
# f.close()

# t2 = pickle.load(open('save.p', 'rb'))
# print(t2)



# Writing modules
