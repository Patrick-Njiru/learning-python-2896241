# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#
import urllib.request

def main():
    # pass # this is a placeholder, do-nothing statement
    web_url = urllib.request.urlopen("https://www.google.com")
    print("result code:", web_url.getcode(), "\n")
    data = web_url.read()
    print(data)

if __name__ == "__main__":
    main()
