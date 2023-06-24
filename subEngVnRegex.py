import re, os, xlsxwriter

def main():
    for file in os.listdir("./srtFiles"):
        if file.endswith(".vi.srt"):
            print(os.path.join("./srtFiles", file))

            fileName = os.path.splitext(file)[0]

            pattern = r'(.*).vi'
            fileMatch = re.findall(pattern, fileName)

            # read file line by line (srt Eng)
            fileEng = open("./srtFiles/" + str(fileMatch[0]) + ".srt", "r")
            linesEng = fileEng.readlines()
            fileEng.close()

            # read file line by line (srt Vn)
            fileVn = open("./srtFiles/" + str(fileMatch[0]) + ".vi.srt", "r")
            linesVn = fileVn.readlines()
            fileVn.close()

            textVn = []
            for line in linesVn:
                if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
                    textVn.append(line.rstrip('\n'))
            # print(textVn)

            textEng = []
            for line in linesEng:
                if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
                    textEng.append(line.rstrip('\n'))
            # print(textEng)

            # Workbook() takes one, non-optional, argument
            # which is the filename that we want to create.
            workbook = xlsxwriter.Workbook("./srtFiles/" + str(fileMatch[0]) + ".sub.xlsx")

            # The workbook object is then used to add new
            # worksheet via the add_worksheet() method.
            worksheet = workbook.add_worksheet()
            
            # Use the worksheet object to write
            # data via the write() method.
            for i in range(len(textEng)):
                worksheet.write('A' + str(i), textEng[i])
                worksheet.write('B' + str(i), textVn[i])
            
            # Finally, close the Excel file
            # via the close() method.
            workbook.close()
    
main()