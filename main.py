import pandas
import os

dir = 'C:/Users/ryuje/OneDrive/양진이/바탕 화면/blog5'
files = os.listdir(dir)
global dataframeFile  # 데이터프레임의 전역화

# 데이터프레임초기화
dataframeFile = pandas.DataFrame(index=range(0, 0), columns=['파일명', '이름', '확장자', '위치정보'])

# [파일검색 함수] : 재귀호출을 디렉토리에 있는 모든 파일을 데이터프레임형식으로 전달하는 함수
def file_search(dir, dataframeFile):
    files = os.listdir(dir)
    for file in files:
        fullname_file = os.path.join(dir, file)
        #파일의 구분자를 정재 실시
        fullname_file = fullname_file.replace("\\", "/")
        if os.path.isdir(fullname_file):
            dataframeFile = file_search(fullname_file, dataframeFile)  # 재귀함수 호출
        else:
            name, ext = os.path.splitext(file)
            dic_file = {'파일명': file, '이름': name, '확장자': ext, '위치정보': fullname_file}
            dataframeFile = dataframeFile.append(dic_file, ignore_index=True)
    # 데이터프레임 리턴
    return dataframeFile

# 재귀함수 호출
dataframeFile = file_search(dir, dataframeFile)
# 데이터프레임 결과출력
print(dataframeFile)

xldataframe = dataframeFile.where(dataframeFile['확장자']=='.xlsx')
#drop을 통해 정재를 추진
xldataframe = xldataframe.dropna()
print(xldataframe)

for i in range(0, len(xldataframe.index)):
    if i==0:
        XlsxData_dataframe = pandas.read_excel(xldataframe.iloc[i].loc['위치정보'], sheet_name="Sheet1")
        total_dataframe = XlsxData_dataframe
    else:
        XlsxData_dataframe = pandas.read_excel(xldataframe.iloc[i].loc['위치정보'], sheet_name="Sheet1")
        total_dataframe = total_dataframe.append(XlsxData_dataframe, ignore_index = True)

print(total_dataframe)

writer = pandas.ExcelWriter('C:/Users/ryuje/OneDrive/양진이/바탕 화면/blog5/result.xlsx', engine = 'xlsxwriter')

total_dataframe.to_excel(writer, sheet_name = 'Sheet1')
writer.save()

print("완료")







