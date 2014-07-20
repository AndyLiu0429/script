from Crypto.Hash import SHA256
import sys

if __name__=="__main__":
    h=''
    blocks=[]
    with open(sys.argv[1],'rb') as f:
        data = f.read(1024)
        while data:
            blocks.insert(0,data)
            data = f.read(1024)

    for singleblock in blocks:
        h=SHA256.new(singleblock+h).digest()
    print h.encode('hex')