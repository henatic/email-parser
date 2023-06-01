from xlwt import Workbook

f = open("maillog (1).csv", "r")
lines = f.readlines()
f.close()
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

i = 0
lister = list()

for x in lines:
    if x.strip()[0] == '"':
        stripper = x.strip()[1:len(x.strip()) - 1]
        parseList = stripper.split(',')
        for y in parseList:
            if y not in lister:
                lister.append(y.strip())
                sheet1.write(i, 0, y.strip())
                i = i + 1
    elif x.strip() not in lister:
        lister.append(x.strip())
        sheet1.write(i, 0, x.strip())
        i = i + 1

wb.save('emailList.xls')