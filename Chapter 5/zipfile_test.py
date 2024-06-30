import zipfile

# #파일 합치기
with zipfile.ZipFile('mytest.zip','w') as myzip:
    myzip.write('../example_txt_file/a.txt')
    myzip.write('../example_txt_file/b.txt')
    myzip.write('../example_txt_file/c.txt')

# 해제하기
with zipfile.ZipFile('mytest.zip') as myzip:
    myzip.extractall()