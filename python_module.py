import glob

filelist = glob.glob("C:/Users/ryuje/Desktop/**/*.txt", recursive=True)
for item in filelist:
    print(item)
