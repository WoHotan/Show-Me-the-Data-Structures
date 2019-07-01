import os

def find_files(suffix, path):
    result = []
    files = os.listdir(path)
    files = [os.path.join(path, file) for file in files]
    for file in files:
       # print(file)
        if os.path.isfile(file) and file.endswith(suffix):
            result.append(file)
        if os.path.isdir(file):
            sub_result = find_files(suffix, file)
            result.extend(sub_result)
    return result

print(find_files('.py', '/home/esrz10/Desktop')) #should print all the py file from input dir
print(find_files('.py', "")) #should return FileNotFoundError: [Errno 2] No such file or directory: