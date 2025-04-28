import requests
from requests.exceptions import Timeout


# get a random joke and you can combine it with other programs like cowsay.
# put line after this into your .bashrc, to get a joke every time you open up terminal
# cowsay -f moose "$(python3 /path/to/getJoke.py)"
# !!!replace "/path/to/getJoke.py" with your own!!!


class API:
    def getJoke():
        try:
            url = "https://v2.jokeapi.dev/joke/Any?type=single"
            response = requests.get(url, timeout=0.5)
            return_code = response.status_code
            if return_code == 200:
                data = response.json()
                print(data["joke"])
        except:
            print("No jokes today, sorry")


def Main():
    API.getJoke()


if __name__ == "__main__":
    Main()




