import re
m = re.search(r"([A-Z]{2})(\d{3})", 'AF304')
print (m.group(1))
print (m.group(2))