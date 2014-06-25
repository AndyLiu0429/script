tr = [[5,4],
      [3,4],
      [0,1],
      [4,3]]

def h(x1, y1):
    m=0.0
    for t in tr:
        m += ((x1 + y1*t[0])-t[1]) ** 2
    print m / 8.0

if __name__ == '__main__':
    h(0,1)
