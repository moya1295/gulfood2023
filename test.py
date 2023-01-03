import re

add = ['\r\n\t\t\t\t\t\t\t\t\t\t',
 '\r\n\r\n\t\t\t\t\t\t\t\t\t\tP.O. Box 20772 ',
 '\r\n\t\t\t\t\t\t\t\t\t\t\t\tJeddah ',
 '\r\n\t\t\t\t\t\t\t\t\t\t\t\tMekkah ',
 '\r\n\t\t\t\t\t\t\t\t\t\t\t\tSaudi Arabia \r\n\t\t\t\t\t\t\t\t\t']

final = []

for x in add:
    x = re.sub(r'[\r\n\t]','',x)
    if x != "":
        final.append(x)

print (final)