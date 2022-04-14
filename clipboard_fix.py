import clipboard as cb
from pynput.keyboard import GlobalHotKeys
import time

with open("a.txt", "r", encoding="utf-8") as a:
    prefix = a.read()

with open("b.txt", "r", encoding="utf-8") as b:
    suffix = b.read()

with open("delay.txt", "r", encoding="utf-8") as d:
    delay = d.read()

print(
    f"""
-----------------
프로그램 시작
prefix: {prefix}
suffix: {suffix}
delay: {delay}
-----------------
"""
)


def change_clipboard():
    time.sleep(float(delay))
    temp = prefix + cb.paste() + suffix
    print("-----------------")
    print(f"입력받은 문자: {cb.paste()}")
    print(f"출력할 문자: {temp}")
    print("-----------------")
    cb.copy(temp)


with GlobalHotKeys({"<ctrl>+c": change_clipboard}) as listener:
    listener.join()
