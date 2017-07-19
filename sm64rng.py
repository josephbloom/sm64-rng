#!usr/bin/python

print """
**************************************************
**** Super Mario 64 - Random Number Generator ****
**************************************************

Thanks to Pannenkoek2012
https://youtu.be/MiuLeTE2MeQ

--------------------------------------------------

"""

def randomnumbergenerator(input):
    if input == 0x560a:
        input = 0 #prevent a two-number loop
    s0 = (input << 8) & 0xffff
    s0 ^= input
    input = ((s0 & 0xff) << 8) | ((s0 & 0xff00) >> 8)
    s0 = ((s0 & 0xff) << 1) ^ input
    s1 = (s0 >> 1) ^ 0xff80
    if ((s0 & 1) == 0):
        if s1 == 0xaa55:
            input = 0 #reset cycle at 65,114th number
        else:
            input = s1 ^ 0x1FF4
    else:
        input = s1 ^ 0x8180
    return input

input = 0
c = ''
while not c == 'q':
    c = raw_input("""Enter a positive integer for multiple numbers.
Enter no number for one new number.
'q' to quit: """)
    print
    if not c == 'q':
        try:
            for i in range(int(c)):
                input = randomnumbergenerator(input)
                print hex(input),input
        except:
            input = randomnumbergenerator(input)
            print hex(input),input
        print
