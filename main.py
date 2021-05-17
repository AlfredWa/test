# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def ping(url):
    print(url)
    response = requests.get(url, timeout=3)
    print(response.text)

def trying():
    url1='http://www.baidu.com'
    url2='http://www.google.com'
    url3='http://www.baiduaaaaaa.com'
    array=[url1,url2,url3]

    for u in array:
        try:
            ping(u)
        except:
            print("fail to ping: "+u)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("test")
    trying()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
