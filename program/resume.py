import sys

fh = open(sys.argv[1], "r")
lines = "\n".join(fh.readlines())

codes = [ord(c) for c in lines]
num = sum(codes[i] * 256 ** i for i in xrange(len(codes)))
print num

def convert(num):
    if num:
        return chr(num % 256) + convert(num // 256)
    else:
        return ""

print convert(num)