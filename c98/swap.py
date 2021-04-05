def swappingDafile():
    file1 = input("enter first file name")
    file2 = input("enter second file name")
    with open(file1,"r") as abc:
        data_abc = abc.read()
    with open(file2,"r") as ghi:
        data_ghi = ghi.read()
    with open(file1,"w") as abc:
        abc.write(data_ghi)
    with open(file2,"w") as ghi:
        ghi.write(data_abc)
swappingDafile()