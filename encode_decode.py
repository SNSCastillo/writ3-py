import codecs

def encode_utf8(obj):
    return codecs.encode(obj, encoding='utf-8', errors='strict')  # De texto a bytes

def decode_utf8(obj):
    return codecs.decode(obj, encoding='utf-8', errors='strict') # De bytes a texto

obje1 = '77,777,777'
print(encode_utf8(obje1))

obje2 = b'hello world'
print(decode_utf8(obje2))