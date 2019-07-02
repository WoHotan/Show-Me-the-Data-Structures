import os

def find_files(suffix=None, path=None):
    if path == None:
        return "Please input a path"
    elif suffix == None:
        return "Please input suffix"
    result = []
    try:
        files = os.listdir(path)
    except Exception as e:
        return "path not found"
    files = [os.path.join(path, file) for file in files]
    for file in files:
       # print(file)
        if os.path.isfile(file) and file.endswith(suffix):
            result.append(file)
        if os.path.isdir(file):
            sub_result = find_files(suffix, file)
            result.extend(sub_result)
    return result

print(find_files('.py', '/home/esrz10/Desktop')) # should print all the py file from input dir
print(find_files('.py', "")) # should return "path not found"
print(find_files('.py'))     # should return "Please input a path"
print(find_files(path='/home/esrz10/Desktop')) # should return "Please input suffix"