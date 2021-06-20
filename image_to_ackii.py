import cv2
import re
import keyboard


ACKII = ['@', '#', '%', '?', '*', '=', '+', '-', ':', ',', '.']
extentions = ".JPG|.jpg|.jpeg|.png|.heic|.gif|.ico|.tiff|.webp|.eps|.svg|.psd|.indd|.cdr|.ai|.raw"

def cropp(photo, wight):
    y,x = photo.shape[:2]
    ratio = x/y
    height = int(ratio*wight)
    return cv2.resize(photo, (height, wight)) 

def pixel_to_ACKII(photo):
    s=''
    for rows in photo:
        for pixel in rows:
            s+=ACKII[pixel//25]+' '
        s+='\n'
    print(s)
    return s


def main():
    path = input("enter path to image: ")
    name = re.sub(r'.jpg|.jpeg|.png', "", '\\'.join(path .split('\\')[-1:]))+'.txt'
    try:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        wight = int(input("enter the number of characters per line: "))
        img = cropp(img, wight)
        f = open('\\'.join(path .split('\\')[:-1])+'\\'+name, 'w')
        f.write(pixel_to_ACKII(img))
        f.close()
        a = keyboard.read_key()
    except:
        print("oops, file not found")
        a = keyboard.read_key()
        
main()