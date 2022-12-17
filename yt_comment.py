import collections
import time
from pywinauto import mouse, keyboard
import random
import emoji

data_file = 'scraped_data/comments.txt'


def comment_on_yt():
    with open(data_file, 'r') as f:
        count = 0
        # random.shuffle(love_emoji)
        for i in f.readlines():
            mouse.click(button='left', coords=(300, 150))
            keyboard.send_keys(i, with_spaces=True)
            keyboard.send_keys('^{ENTER}')
            time.sleep(random.randint(6, 12))
            print(f'Commented {count}')
            count += 1


if __name__ == '__main__':
    count = 10
    while count:
        time.sleep(random.randint(20, 40))
        comment_on_yt()
        count -= 1
