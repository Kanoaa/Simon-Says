import board
import digitalio as dio
import time
import random

green = dio.DigitalInOut(board.D6)
green.direction = dio.Direction.OUTPUT

green_btn = dio.DigitalInOut(board.D1)
green.direction = dio.Direction.OUTPUT

red = dio.DigitalInOut(board.D7)
red.direction = dio.Direction.OUTPUT

red_btn = dio.DigitalInOut(board.D2)
red.direction = dio.Direction.OUTPUT

white = dio.DigitalInOut(board.D8)
white.direction = dio.Direction.OUTPUT

white_btn = dio.DigitalInOut(board.D3)
white.direction = dio.Direction.OUTPUT

yellow = dio.DigitalInOut(board.D9)
yellow.direction = dio.Direction.OUTPUT

yellow_btn = dio.DigitalInOut(board.D4)
yellow.direction = dio.Direction.OUTPUT

strt_btn = dio.DigitalInOut(board.D5)

seq = []
user_seq = []

seq_sleep = 0.5
start_sleep = 0.1

def start():
    for i in range(4):
        green.value = True
        time.sleep(start_sleep)
        red.value = True
        green.value = False
        time.sleep(start_sleep)
        white.value = True
        red.value = False
        time.sleep(start_sleep)
        yellow.value = True
        white.value = False
        time.sleep(start_sleep)
        yellow.value = False

def inp():
    while start and not green_btn.value and not red_btn.value and not white_btn.value and not yellow_btn.value:
        pass
    if green_btn.value:
        green.value = True
        time.sleep(seq_sleep)
        green.value = False
        user_seq.append(1)
        print(user_seq)
    if red_btn.value:
         red.value = True
         time.sleep(seq_sleep)
         red.value = False
         user_seq.append(2)
         print(user_seq)
    if white_btn.value:
         white.value = True
         time.sleep(seq_sleep)
         white.value = False
         user_seq.append(3)
         print(user_seq)
    if yellow_btn.value:
         yellow.value = True
         time.sleep(seq_sleep)
         yellow.value = False
         user_seq.append(4)
         print(user_seq)
    
    
    
def play():
    count = 1
    for i in range(count):
        col = random.randint(1, 4)
        seq.append(col)
        count += 1
        print(seq)
        for i in range(col):
            if col == 1:
                green.value = True
                time.sleep(seq_sleep)
                green.value = False
            elif col == 2:
                red.value = True
                time.sleep(seq_sleep)
                red.value = False
            elif col == 3:
                white.value = True
                time.sleep(seq_sleep)
                white.value = False
            else: 
                yellow.value = True
                time.sleep(seq_sleep)
                yellow.value = False
       
    
        
while True:
    if strt_btn.value == True:
        start()
        #Need a comparison and a way to continue to play the sequence. I tried using a if statement to compare the two sequences to see if they are alike (if user_seq == seq:) and if they were equal then I added the next repeating sequence but I couldn't figure out how to work it.

        for i in range(2):
            play()
            time.sleep(seq_sleep)
            inp()
    
                
        
       
                
        

        
