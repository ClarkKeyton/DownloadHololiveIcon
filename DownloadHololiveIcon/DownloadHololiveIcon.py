import requests

def Download():
    url = 'https://hololivepro.com/wp-content/themes/hololive_production/images/favicon.ico'
    fr = requests.get(url, allow_redirects=True)
    open('hololive.ico', 'wb').write(fr.content)
if __name__ == "__main__":
    Download()