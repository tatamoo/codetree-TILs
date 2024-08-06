while True:
    width,height,char = input().split()
    width,height = int(width),int(height)
    print(width*height)
    if char == 'C':
      break;