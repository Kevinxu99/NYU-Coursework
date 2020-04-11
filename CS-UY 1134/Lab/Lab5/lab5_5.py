import os
def disk_usage(path):
    if(os.path.isdir(path)==False):
        return os.path.getsize(path)
    du=os.path.getsize(path)
    for filename in os.listdir(path):
        du+=disk_usage(os.path.join(path,filename))
    return du