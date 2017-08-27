# s = 'a'
s = '\u33C1'
print("simbol %s has unicode: %d" % (s, ord(s)))


# z = 0x03A3
z = 0x2E9D
print("code %d has symbol: %s" % (z, chr(z)))

time = "18:44:42"
hours = int(time[0:2])
minutes = int(time[3:5])
seconds = int(time[6:])

num_of_seconds = hours*3600 + minutes*60 + seconds

print("Nuber of seconds: %d" % (num_of_seconds))
\

