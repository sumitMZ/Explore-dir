import os

def opm(path,bull) :
    drs = os.listdir(path)
    bull+="---"
    if not drs :
        return
    else:
        for i in drs:
            if os.path.isfile(path+'/'+i) :
                print(bull,'> File: ',(i))
            elif os.path.isdir(path+'/'+i) :
                print(bull,'> Dir: ',(i))
                opm(path+'/'+i,bull)
        print()
dirs =('/'+"home")
opm(dirs,"=>")

