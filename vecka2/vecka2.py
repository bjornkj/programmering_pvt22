
# Exempel 1, öppna en fil, läs innehållet och gör lite beräkningar och stäng sedan filen
# fh = open('exempeltext')
# file_contents = fh.read()
# print(file_contents)
#
# num_letters = 0
# for l in file_contents:
#     if l.isalnum():
#         num_letters += 1
#
# num_words = len(file_contents.split())
#
# print(f"The file contains {num_letters} letters and {num_words} words")
# fh.close()




# Exempel 2, öppna en fil, läs innehål och stäng sedan automatiskt
# with open('exempeltext') as fh:
#     file_contents = fh.read()
#     num_words = len(file_contents.split())
#     print(num_words)


# Exempel 3, öppna en textfil och läs den rad för rad, skriv ut en rad om den innehåller ordet Media
# with open('system.log') as fh:
#     lines = fh.readlines()
#     num_lines = 0
#     for line in lines:
#         num_lines += 1
#         if "Media" in line:
#             print(line)
#
#     print(num_lines)


# Exempel 4, öppna en textfil och läs den rad för rad (på ett enklare sätt), skriv ut en rad om den innehåller ordet Media
with open('system.log') as fh:
    for line in fh:
        if 'Media' in line:
            print(line.strip())