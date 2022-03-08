import requests

def main():
    word = "cloudfare"
    url = requests.get("https://www.cloudfare.com/es-es/")
    headers = dict(url.headers)
    verify = False
    for header in headers:
        print(header)
        if word in headers[header].lower():
            verify = True
            break
    if verify :
       print("cloudfare presente")
    else:
        print("cloudfare no esta presente")
        if __name__ == "__main__":
            try:
                main()
            except KeyboardInterrupt:
                exit()

main()

