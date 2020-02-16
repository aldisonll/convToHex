# convert decimal to hexadecimal
encodeHex = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
hex = []
def convToHex(decimal):
 hexDecimal = ''
 a,b = decimal,16
 e = a - (int(a / b) * b)
 if e in encodeHex:
   hex.append(encodeHex[e])
 else:
   hex.append(e)
 if bool(int(a / b)):
  convToHex(int(a / b))
 else:
  for byte in range(len(hex)):
   hexDecimal += str(hex[byte])
  print("{}{}".format("0x",hexDecimal[::-1]))

# HOW TO USE:
#       convToHex(here)
# decimal number ~~^

