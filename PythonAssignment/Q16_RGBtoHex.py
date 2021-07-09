"""RGB to Hex conversion and vice versa, e.g. (255,0,255) into 0XFF00FF"""

RGB_input=list(map(int,input().strip("()").split(",")))
HEXvalue="0x"
for i in RGB_input:
    HEXvalue+=hex(i)[2:]
print(HEXvalue)