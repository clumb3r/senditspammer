import json
import threading
from past.builtins import raw_input
from colorama import Fore
from senditspamrandom import randomspam
from senditspamcustom import customspam

print(Fore.RED + """   _____ ______ _   _ _____ _____ _______    _____ _____        __  __ __  __ ______ _____  
  / ____|  ____| \ | |  __ \_   _|__   __|  / ____|  __ \ /\   |  \/  |  \/  |  ____|  __ \ 
 | (___ | |__  |  \| | |  | || |    | |    | (___ | |__) /  \  | \  / | \  / | |__  | |__) |
  \___ \|  __| | . ` | |  | || |    | |     \___ \|  ___/ /\ \ | |\/| | |\/| |  __| |  _  / 
  ____) | |____| |\  | |__| || |_   | |     ____) | |  / ____ \| |  | | |  | | |____| | \ \ 
 |_____/|______|_| \_|_____/_____|  |_|    |_____/|_| /_/    \_\_|  |_|_|  |_|______|_|  \_\

                                                                                           """)
print(
    Fore.GREEN + "WARNING: You must have the version of chrome driver that matches your chrome version. Find it here "
                 "> https://chromedriver.chromium.org/downloads")
print(Fore.RED + "READ ME! Using anymore then 1-3 threads can cause lag on low end computers. Selenium does NOT have "
                 "built in threading support. Due to this it may take a few seconds for multiple threads to register. "
                 "For more indepth documentation I highly encourage users to read the README.")
print(Fore.WHITE + "Created by clumber#7126 (:")
print(Fore.CYAN + "1: Random")
print(Fore.CYAN + "2: Custom")


class senditspamconfig:
    inp = int(input("Enter a number: "))
    if inp == 1:
        class senditspamrandom:
            def toJSON(self):
                return json.dumps(self, default=lambda o: o.__dict__,
                                  sort_keys=True, indent=4)

            def __init__(self, url, threads):
                self.url = url
                self.threads = threads
                with open('config.json', 'w') as outfile:
                    outfile.write(self.toJSON())

        url = raw_input("Enter URL: ")
        threads = int(raw_input("Enter Threads: "))
        random = senditspamrandom(url, threads)
        print(Fore.CYAN + "Spam started!")
        threads = [threading.Thread(target=randomspam) for i in range(threads)]
        for i in range(len(threads)):
            threads[i].start()
        for i in range(len(threads)):
            threads[i].join()

    elif inp == 2:
        class senditspamcustom:
            def toJSON(self):
                return json.dumps(self, default=lambda o: o.__dict__,
                                  sort_keys=True, indent=4)

            def __init__(self, url, msg):
                self.url = url
                self.msg = msg
                with open('config.json', 'w') as outfile:
                    outfile.write(self.toJSON())

        url = raw_input("Enter URL: ")
        msg = raw_input(Fore.CYAN + "Enter your message: ")
        custom = senditspamcustom(url, msg)
        print(Fore.CYAN + "Spam started!")
        threads = [threading.Thread(target=customspam) for i in range(1)]
        for i in range(len(threads)):
            threads[i].start()
        for i in range(len(threads)):
            threads[i].join()
