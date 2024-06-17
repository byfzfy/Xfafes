import pwinput, ctypes, os, time, traceback
from colorama import Fore
from pystyle import Center
import colorama
from colorama import Fore, Style
import getpass
import uuid
import sys
import guardshield
from pypresence import Presence

import json

from textual.app import App, ComposeResult
from textual.containers import Container, VerticalScroll, Horizontal, Vertical
from textual.widgets import Header, Footer, Switch, Static, Button, LoadingIndicator, Checkbox, Tabs, Markdown, Input, Log

import threading, requests



def debugger_detected():
    print("Debugger detected!")
    os._exit(1)  # Immediate termination of the application

# Create a Security instance with desired settings
module = guardshield.Security(
    anti_debugger=True,
    kill_on_debug=False,
    detect_vm=False,
    detect_sandbox=False,
    on_detection=debugger_detected
)

def monitor_debugging():
    while True:
        if module.check_debug():
            debugger_detected()
        time.sleep(1)

# Start the security check loop in a separate thread
threading.Thread(target=monitor_debugging, daemon=True).start()

# Additional security checks
module.check_security()
module.check_sandbox()
module.check_vm()

version = "1.1"
firefox_version = "firefox-1391"
download_url = "https://cdn.discordapp.com/attachments/1113512911583858728/1123367800304570409/firefox-1391.zip"
browser_args=[
    "--no-sandbox", 
    "--disable-setuid-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--disable-background-timer-throttling",
    "--disable-backgrounding-occluded-windows",
    "--disable-extensions",
    "--disable-plugins",
    "--disable-software-rasterizer",
    "--disable-sync",
    "--no-zygote",
    "--single-process",
    "--disable-notifications",
    "--disable-background-networking",
    "--disable-breakpad",
    "--disable-infobars",
    "--disable-site-isolation-trials",
    "--disable-accelerated-video-decode",
    "--disable-background-video-track",
    "--disable-canvas-aa",
    "--disable-client-side-phishing-detection",
    "--disable-component-extensions-with-background-pages",
    "--disable-default-apps",
    "--disable-dev-shm-usage",
    "--disable-extensions-except",
    "--disable-hang-monitor",
    "--disable-ipc-flooding-protection",
    "--disable-popup-blocking",
    "--disable-prompt-on-repost",
    "--disable-renderer-backgrounding",
]



import random, time, httpx, traceback, threading, uuid, json, asyncio, string, base64, ctypes, requests, subprocess
from datetime import datetime, timezone
from playwright.async_api import async_playwright
from colorama import Fore



class Generatorr:

    gened = 0
    error = 0
    solved = 0 

    solved_captcha = []

    def __init__(self, data: dict):


        ctypes.windll.kernel32.SetConsoleTitleW(f"Xylo Integrity")

        self.browser_args = browser_args
        self.auth = data['auth']
        self.proxies = data['proxies']
        self.usernames = data['usernames']
        self.config = json.load(open('config.json', 'r'))

        try:
            self.hl = data['hl_debug']
        except:
            self.hl = True
        self.fp_list = []
        self.lt = 'en-US,en;q=0.5'
        self.useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0'
        
        self.generator_run()

    def get_fp(self):
        while True:
            try:

                proxie = random.choice(self.proxies)

                headers = {
                    'User-Agent': self.useragent,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': self.lt,
                    'Connection': 'keep-alive',
                    'Referer': 'https://www.twitch.tv/',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'iframe',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-site',
                }
                                        
                response = requests.get(
                    'https://gql.twitch.tv/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/fp?x-kpsdk-v=j-0.0.0',
                    headers=headers,
                    proxies = {"http":"http://" + proxie,"https":"http://" + proxie},
                    timeout=20,
                )
                self.fp_list.append([
                                        response.text,
                                        proxie
                                    ]) 
                return
            except Exception as e:
                print()
                pass

    async def start_browser(self):

        self.playwright = await async_playwright().start()

        self.main_browser = await self.playwright.firefox.launch(
            headless=True,
            args=self.browser_args
        )
        

        avail = [
            '1920x1080|1280x720', 
            '2560x1440|1440x900',  
            '3840x2160|2560x1440',
            '2880x1800|1280x800',  
            '2560x1600|1280x800', 
            '2160x1440|1920x1080',  
            '2736x1824|1920x1080',  
            '2048x1536|1024x768',  
            '2388x1668|1194x834',  
            '2732x2048|1366x1024', 
            '1080x2340|720x1520', 
            '1080x2400|1080x2400',  
            '1125x2436|1125x2436',  
            '1284x2778|1284x2778',  
        ]

        selected_avail = random.choice(avail)
        avail, view = selected_avail.split("|")

        availwidth, availheight = avail.split("x")
        width, height = view.split("x")


        context = await self.main_browser.new_context(

        locale=self.lt,
            permissions=['geolocation'],
            screen={"width": int(availwidth),"height": int(availheight)},
            viewport={"width": int(width),"height":int(height)},
            user_agent=self.useragent,
        )
        self.context = context
        
        return await self.context.new_page()

    async def solv_captcha(self, page):
        
        class CapDat():
            fp = None; proxy = None

        async def route_men(route):

            
            ctypes.windll.kernel32.SetConsoleTitleW(f"Xylo AIO -> Integrity")

            if "https://www.twitch.tv/signup" == route.request.url:
                
                if len(self.fp_list) == 0:
                    threading.Thread(target=self.get_fp).start()
                while True:
                    try:
                        fp_data = self.fp_list[0]
                        CapDat.fp = fp_data[0]
                        CapDat.proxy = fp_data[1]
                        self.fp_list.pop(0)
                        break
                    except: pass
                        

                html = '<iframe src="https://passport.twitch.tv/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/fp?x-kpsdk-v=j-0.0.0" style="width: 0px; height: 0px; border: 0px none; display: none;">'+CapDat.fp+'</iframe>'
                await route.fulfill(status=200, body=html,headers={'Content-Type': 'text/html'})

            elif "https://www.twitch.tv/favicon.ico" == route.request.url:


                data = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(32))
                http_headers = {
                    "Connection": "keep-alive",
                    "Content-Type": "application/octet-stream",
                    "ETag": '"'+str(uuid.uuid1())+'"',
                    "Vary": "Accept-Encoding"
                }

                await route.fulfill(status=200, body=data,headers=http_headers)

            elif "https://passport.twitch.tv/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/tl" == route.request.url:

                headers = route.request.headers
                post_data = route.request.post_data
                def return_captcha():
                    for i in range(3):
                        try:
                            response = httpx.post(
                                'https://passport.twitch.tv/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/tl',
                                headers=headers,
                                data=post_data,
                                proxies="http://"+CapDat.proxy,
                                timeout=100
                                )

                            captcha_data = {
                                'x_kpsdk_ct': response.headers['x-kpsdk-ct'],
                                'x_kpsdk_st': response.headers['x-kpsdk-st'],
                                'lt': self.lt,
                                'proxy': CapDat.proxy,
                                'useragent': self.useragent
                            }
                            
                            self.solved_captcha.append(captcha_data)
                            break
                        except:
                            pass #traceback.print_exc()


                threading.Thread(target=return_captcha).start()
                threading.Thread(target=self.get_fp).start()

                try:
                    await page.goto("about:blank")
                except: pass
            
            elif "https://reporting.cdndex.io/error" == route.request.url:

                try:
                    await page.goto("about:blank")
                except: pass

            else: await route.continue_()
        
        await page.route("**/*", route_men)

        while True:


            
            try:
                await self.context.clear_cookies()
                await page.goto("https://www.twitch.tv/signup", timeout=5000000)
            except: pass

    async def run_solver(self):
        page = await self.start_browser()
        await self.solv_captcha(page)
        


    def chat_access(self,token_nick,id, x_device_id, proxie):
        try:
            data = data.replace("1693252575",str(round(time.time()))).replace("949377547",str(id)).replace("wrsj97h3p",token_nick).replace("SVCfn8CKf42Lr08DaRu08v1M81xbFBoK",x_device_id)
            encodedStr = str(base64.b64encode(data.encode("utf-8")), "utf-8")

            headers = {
                'accept': '*/*',
                'accept-language': 'pl,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
                'origin': 'https://www.twitch.tv',
                'referer': 'https://www.twitch.tv/',
                'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': self.useragent,
            }

            data = {
                'data': encodedStr
            }
            res = httpx.post(
                settings_url,
                headers=headers,
                data=data,
            )
        except:
            pass



    def create_integrity(self, captcha):
        

        loop_count = 15
        for i in range(loop_count):
            def thread():
                try:

                    ts = int(captcha['x_kpsdk_st'])
                        
 
                    x_kpsdk_cd = json.dumps(self.auth.x_kpsdk_cd(ts))


                    tokendata = random.choice(open('data/tokens.txt', 'r').read().splitlines()) 


                    x_device_id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(32))

                    ayrilan_veri = tokendata.split(":")


                    idd = ayrilan_veri[0]
                    token = ayrilan_veri[1]
                    username = ayrilan_veri[3]
                    password = ayrilan_veri[4]




                    headers = {
                        'User-Agent': self.useragent,
                        'Accept': '*/*',
                        'Accept-Language': captcha['lt'],
                        'Referer': 'https://www.twitch.tv/',
                        'x-kpsdk-ct': captcha['x_kpsdk_ct'],
                        'x-kpsdk-cd': x_kpsdk_cd,
                        'x-kpsdk-v': 'j-0.0.0',
                        'Origin': 'https://www.twitch.tv',
                        'Connection': 'keep-alive',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-site',
                        'Authorization': 'OAuth '+ token,
                        'X-Device-ID': x_device_id,
                        'Client-ID': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                    }




                    response = httpx.post(
                            'https://gql.twitch.tv/integrity',
                            headers=headers,
                            proxies="http://"+captcha['proxy'],
                            timeout=100
                                        )

                    captcha_token = response.json()['token']





                    is_flagged = b'"is_bad_bot":"true"' in base64.urlsafe_b64decode(captcha_token + '===')


                    if is_flagged == True:
                        print()
                    else:
                        with open("integrity.txt", "r") as txt_file:
                            lines = txt_file.readlines()
                            for line in lines:
                                if token in line:
                                    old_captcha_token = line.split(":")[1].strip()
                                    new_captcha_token = captcha_token  # Yeni bir captcha tokenı üretmek için gereken işlevi çağırın.
                                    line = line.replace(old_captcha_token, new_captcha_token)
                                    with open("integrity.txt", "w") as updated_txt_file:
                                        updated_txt_file.writelines(lines)
                                    print(f"{Fore.LIGHTWHITE_EX}{Fore.LIGHTGREEN_EX}Integrity Refreshed -> {Fore.LIGHTGREEN_EX}{token}{Fore.RESET}")
                                    return new_captcha_token
                        # Dosyada belirli bir tokena sahip bir satır bulunamadıysa, yeni bir satır ekleyin
                        with open("integrity.txt", "a") as txt_file:
                            datatok = {
                                "access": token,
                                "id": idd,
                                "username": username,
                                "integrity": {
                                    "token": captcha_token,
                                    "proxy": captcha['proxy'],
                                    "data": {
                                        "X-Device-ID": x_device_id,
                                        "User-Agent": self.useragent,
                                        "Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko"  # assuming this is constant; replace with a variable if needed
                                    }
                                },
                                "info": {
                                    "bio_changed": True,  # replace with actual logic if necessary
                                    "avatar_changed": True,  # replace with actual logic if necessary
                                    "social_added": True,  # replace with actual logic if necessary
                                    "color_changed": True,  # replace with actual logic if necessary
                                    "email_verified": True  
                                }
                            }
                            
                            txt_file.write(json.dumps(datatok) + "\n")





                        print(f"  {Fore.LIGHTWHITE_EX} {Fore.LIGHTGREEN_EX} Integrity Refreshed {Fore.LIGHTGREEN_EX} {token}{Fore.RESET}")

                        if self.config['integrity']['change_avatar']['status'] == True:

                            iddsuser = idd
                            Integrity = captcha_token
                            proxy = "http://" + captcha['proxy']
                            X_Device_Id = x_device_id
                            User_Agent = self.useragent
                            Client_Id = "kimne78kx3ncx6brgo4mv6wki5h1ko"




                        if self.config['integrity']['change_bio']['status'] == True:
                            time.sleep(0.5)
                            if self.config['integrity']['change_bio']['status'] == True:
                                url = "https://raw.githubusercontent.com/fishzint/token-onliner/main/data/custom%20status.txt"
                                response = requests.get(url)

                                lines = response.text.split('\n')
                                selected_line = random.choice(lines)
                                bio = selected_line
                            else:

                                bio = self.config['integrity']['change_bio']['bio']



                            headers = {
                                "Authorization": "Bearer " + token
                            }
                            r = requests.get("https://id.twitch.tv/oauth2/validate", headers=headers)
                            user_id = r.json()['user_id']
                            username = r.json()['login']
                            requests.post("https://id.twitch.tv/oauth2/validate", headers=headers)

                            headers = {
                                "Accept": "*/*",
                                "Accept-Encoding": "gzip, deflate, br",
                                "Accept-Language": captcha['lt'],
                                "Authorization": f"OAuth {token}",
                                "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
                                "Client-Integrity": captcha_token,
                                "Connection": "keep-alive",
                                "Content-Length": "273",
                                "Content-Type": "text/plain;charset=UTF-8",
                                "Host": "gql.twitch.tv",
                                "Origin": "https://www.twitch.tv",
                                "Referer": "https://www.twitch.tv/",
                                "Sec-Ch-Ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
                                "Sec-Ch-Ua-Mobile": "?0",
                                "Sec-Ch-Ua-Platform": '"Windows"',
                                "Sec-Fetch-Dest": "empty",
                                "Sec-Fetch-Mode": "cors",
                                "Sec-Fetch-Site": "same-site",
                                "User-Agent": self.useragent,
                                "X-Device-Id": x_device_id
                            }
                            jso00n = [{"operationName": "UpdateUserProfile","variables": {"input": {"displayName": username,"description": bio,"userID": user_id,}},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "991718a69ef28e681c33f7e1b26cf4a33a2a100d0c7cf26fbff4e2c0a26d15f2",}},}]
                            r = requests.post("https://gql.twitch.tv/gql",headers=headers, json=jso00n)

                            if 'failed integrity check' in r.text:
                                print("")
                            else:
                                print(f"Bio Changed -> {username}")

                except Exception as e:
                    print("")
                    pass

            threading.Thread(target=thread).start()
            

    def generator_run(self):


        def browser_thread():
            asyncio.run(self.run_solver())


        tokens = open("data/tokens.txt","r").read().splitlines()

        def run_creator(captcha):
            res = self.create_integrity(captcha)

        token_count = len(tokens)
        try:
            if token_count == 0:
                print("Add Tokens to data/tokens.txt!")
            else:
                print(f"\n\n    {Fore.LIGHTWHITE_EX}( {Fore.LIGHTYELLOW_EX}/{Fore.LIGHTWHITE_EX} ) {Fore.LIGHTWHITE_EX}Starting...{Fore.RESET}")
                print("\n\n")
                for i in range(2):
                    threading.Thread(target=browser_thread).start()
                while True:


                    try:
                        if self.solved_captcha != []:
                            for captcha in self.solved_captcha:
                                threading.Thread(target=run_creator, args=[captcha,]).start()
                                self.solved_captcha.remove(captcha)
                                
                    except:
                        traceback.print_exc()

        except Exception as e:
            print(str(traceback.format_exc()))









import random, time, httpx, traceback, threading, uuid, json, asyncio, string, base64, ctypes, requests,subprocess
from playwright.async_api import async_playwright
from colorama import Fore
from pystyle import Center, Colors, Colorate
from faker import Faker


class Generator:

    gened = 0
    error = 0
    solved = 0 

    solved_captcha = []

    def __init__(self, data: dict):


        ctypes.windll.kernel32.SetConsoleTitleW(f"Xylo Gen")

        self.browser_args = browser_args
        self.auth = data['auth']
        self.proxies = data['proxies']
        self.usernames = data['usernames']
        self.config = json.load(open('config.json', 'r'))
        try:
            self.hl = data['hl_debug']
        except:
            self.hl = True
        self.fp_list = []
        self.lt = 'en-US,en;q=0.5'
        self.useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'
        
        self.generator_run()

    def get_fp(self):
        while True:
            try:

                proxie = random.choice(self.proxies)

                headers = {
                    'User-Agent': self.useragent,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': self.lt,
                    'Connection': 'keep-alive',
                    'Referer': 'https://www.twitch.tv/',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'iframe',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-site',
                }
                                        
                response = requests.get(
                    'https://passport.twitch.tv/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/fp?x-kpsdk-v=j-0.0.0',
                    headers=headers,
                    proxies = {"http":"http://" + proxie,"https":"http://" + proxie},
                    timeout=20,
                )
                self.fp_list.append([
                                        response.text,
                                        proxie
                                    ]) 
                return
            except Exception as e:
                print("")
                pass

    async def start_browser(self):

        self.playwright = await async_playwright().start()
        self.main_browser = await self.playwright.firefox.launch(
            headless=True,
            args=self.browser_args
        )


        avail = [
            '1920x1080|1280x720', 
            '2560x1440|1440x900',  
            '3840x2160|2560x1440',
            '2880x1800|1280x800',  
            '2560x1600|1280x800', 
            '2160x1440|1920x1080',  
            '2736x1824|1920x1080',  
            '2048x1536|1024x768',  
            '2388x1668|1194x834',  
            '2732x2048|1366x1024', 
            '1080x2340|720x1520', 
            '1080x2400|1080x2400',  
            '1125x2436|1125x2436',  
            '1284x2778|1284x2778',  
        ]

        selected_avail = random.choice(avail)
        avail, view = selected_avail.split("|")

        availwidth, availheight = avail.split("x")
        width, height = view.split("x")


        context = await self.main_browser.new_context(

        locale=self.lt,
            permissions=['geolocation'],
            screen={"width": int(availwidth),"height": int(availheight)},
            viewport={"width": int(width),"height":int(height)},
            user_agent=self.useragent,
        )
        self.context = context
        
        return await self.context.new_page()

    async def solv_captcha(self, page):
        
        class CapDat():
            fp = None; proxy = None

        async def route_men(route):

            
            ctypes.windll.kernel32.SetConsoleTitleW(f"Generated -> {self.gened}")

            if "https://www.twitch.tv/signup" == route.request.url:
                
                if len(self.fp_list) == 0:
                    threading.Thread(target=self.get_fp).start()
                while True:
                    try:
                        fp_data = self.fp_list[0]
                        CapDat.fp = fp_data[0]
                        CapDat.proxy = fp_data[1]
                        self.fp_list.pop(0)
                        break
                    except: pass
                        

                html = '<iframe src="https://passport.twitch.tv/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/fp?x-kpsdk-v=j-0.0.0" style="width: 0px; height: 0px; border: 0px none; display: none;">'+CapDat.fp+'</iframe>'
                await route.fulfill(status=200, body=html,headers={'Content-Type': 'text/html'})

            elif "https://www.twitch.tv/favicon.ico" == route.request.url:


                data = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(32))
                http_headers = {
                    "Connection": "keep-alive",
                    "Content-Type": "application/octet-stream",
                    "ETag": '"'+str(uuid.uuid1())+'"',
                    "Vary": "Accept-Encoding"
                }

                await route.fulfill(status=200, body=data,headers=http_headers)

            elif "https://passport.twitch.tv/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/tl" == route.request.url:

                headers = route.request.headers
                post_data = route.request.post_data
                def return_captcha():
                    for i in range(20):
                        try:
                            response = httpx.post(
                                'https://passport.twitch.tv/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/tl',
                                headers=headers,
                                data=post_data,
                                proxies="http://"+CapDat.proxy,
                                timeout=100
                                )

                            captcha_data = {
                                'x_kpsdk_ct': response.headers['x-kpsdk-ct'],
                                'x_kpsdk_st': response.headers['x-kpsdk-st'],
                                'lt': self.lt,
                                'proxy': CapDat.proxy,
                                'useragent': self.useragent
                            }
                            
                            self.solved_captcha.append(captcha_data)
                            break
                        except:
                            pass #traceback.print_exc()


                threading.Thread(target=return_captcha).start()
                threading.Thread(target=self.get_fp).start()

                try:
                    await page.goto("about:blank")
                except: pass
            
            elif "https://reporting.cdndex.io/error" == route.request.url:
                pass
                try:
                    await page.goto("about:blank")
                except: pass

            else: await route.continue_()
        
        await page.route("**/*", route_men)

        while True:


            
            try:
                await self.context.clear_cookies()
                await page.goto("https://www.twitch.tv/signup", timeout=5000000)
            except: pass

    async def run_solver(self):
        page = await self.start_browser()
        await self.solv_captcha(page)
        


    def chat_access(self,token_nick,id, x_device_id, proxie):
        try:
            data = data.replace("1693252575",str(round(time.time()))).replace("949377547",str(id)).replace("wrsj97h3p",token_nick).replace("SVCfn8CKf42Lr08DaRu08v1M81xbFBoK",x_device_id)
            encodedStr = str(base64.b64encode(data.encode("utf-8")), "utf-8")

            headers = {
                'accept': '*/*',
                'accept-language': 'pl,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
                'origin': 'https://www.twitch.tv',
                'referer': 'https://www.twitch.tv/',
                'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': self.useragent,
            }

            data = {
                'data': encodedStr
            }
            res = httpx.post(
                settings_url,
                headers=headers,
                data=data,
            )
        except:
            pass



    def create_account(self, captcha):
        






        loop_count = 20
        for i in range(loop_count):
            def thread():
                try:

                    ts = int(captcha['x_kpsdk_st'])
                        
 
                    x_kpsdk_cd = json.dumps(self.auth.x_kpsdk_cd(ts))



                    x_device_id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(32))
                    password = ''.join(random.choice(string.ascii_letters + string.digits ) for i in range(13)) + random.choice(['!','?'])
                    

                    try:
                        if self.config['gen']['realistic_usernames'] == True:

                            headers = {"Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7", "Content-Type": "application/json; charset=UTF-8", "Origin": "https://www.spinxo.com", "Referer": "https://www.spinxo.com/gamertags", "Sec-Ch-Ua-Mobile": "?0", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0", "X-Requested-With": "XMLHttpRequest"}

                            payload = {"snr": {"category": 0, "UserName": "", "Hobbies": "", "ThingsILike": "", "Numbers": "", "WhatAreYouLike": "", "Words": "", "Stub": "gamertags", "LanguageCode": "en", "NamesLanguageID": "45", "Rhyming": False, "OneWord": False, "UseExactWords": False, "ScreenNameStyleString": "Any", "GenderAny": False, "GenderMale": False, "GenderFemale": False}}



                            name = httpx.post("https://www.spinxo.com/services/NameService.asmx/GetNames", headers=headers, json=payload)
                            response_json = name.json()
                            namecuq = random.randint(0, 25)
                            username1 = response_json.get("d", {}).get("Names", [])[namecuq]


                            extra_numbers = ''.join(random.choices(string.digits, k=5))
                                
                            username = username1 + extra_numbers

                        elif self.config['gen']['number_usernames'] == True:
                            org_username = ''.join(random.choice(string.digits) for _ in range(10))
                            username = org_username
                        elif self.config['gen']['custom_username']['status'] == True:


                            start = self.config['gen']['custom_username']['name_']
                            


                            org_username = ''.join(random.choice(string.digits) for _ in range(5))

                            username = start + org_username         
                        else:
                                org_username = ''.join(random.choice(string.ascii_letters + string.digits ) for i in range(random.randint(8,12)))
                                username = org_username
                    except Exception as e:

                        org_username = ''.join(random.choice(string.ascii_letters + string.digits ) for i in range(random.randint(8,12)))
                        username = org_username                 



                    headers = {
                        'User-Agent': self.useragent,
                        'Accept': '*/*',
                        'Accept-Language': captcha['lt'],
                        'Referer': 'https://www.twitch.tv/',
                        'x-kpsdk-ct': captcha['x_kpsdk_ct'],
                        'x-kpsdk-cd': x_kpsdk_cd,
                        'x-kpsdk-v': 'j-0.0.0',
                        'Origin': 'https://www.twitch.tv',
                        'Connection': 'keep-alive',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-site',
                        'X-Auth-Action': 'register',
                        'X-Device-ID': x_device_id,
                        'Client-ID': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                    }
                    try:
                        response = httpx.post(
                            'https://passport.twitch.tv/integrity', 
                            headers=headers,
                            proxies="http://"+captcha['proxy'],
                            timeout=100
                                            )

                        captcha['x_kpsdk_ct'] = response.headers['x-kpsdk-ct']
                        captcha_token = response.json()['token']
                    except:
                        return

                    self.solved = self.solved + 1
                    cookies = {
                        'unique_id': x_device_id,
                        'unique_id_durable': x_device_id,
                        'experiment_overrides': '{%22experiments%22:{}%2C%22disabled%22:[]}',
                        'ga__12_abel-ssn': captcha['x_kpsdk_ct'],
                        'ga__12_abel': captcha['x_kpsdk_ct'],
                    }
                    
                    headers = {
                        'User-Agent': self.useragent,
                        'Accept': '*/*',
                        'Accept-Language': self.lt,
                        'Referer': 'https://www.twitch.tv/',
                        'Content-Type': 'text/plain;charset=UTF-8',
                        'Origin': 'https://www.twitch.tv',
                        'Connection': 'keep-alive',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-site',
                        }


                    email = ''.join(random.choice(string.ascii_letters) for i in range(14)) + random.choice(["@gmail.com","@outlook.com"])


                    data = '{"username":"'+username+'","password":"'+password+'","email":"'+email+'","birthday":{"day":'+str(random.randint(1,28))+',"month":2,"year":'+str(random.randint(1981,1998))+'},"client_id":"kimne78kx3ncx6brgo4mv6wki5h1ko","integrity_token":"'+captcha_token+'"}'
                    try:
                        response = httpx.post('https://passport.twitch.tv/protected_register', 
                                                headers=headers, 
                                                data=data, 
                                                cookies=cookies,
                                                proxies="http://"+captcha['proxy'],
                                                timeout=100
                                                )

                    except:
                        None

                    if "access_token" in response.text:
                        res =  {"access":response.json(),"login":{"username":username,"password":password,"email":email}}
                    
                        access_token = res['access']['access_token']
                        user_id = res['access']['userID']
                        username = res['login']['username']
                        password = res['login']['password']
                        email = res['login']['email']
                        
                        self.gened = self.gened + 1

                        
                        print(f"[✅] Token -> {access_token} ")
                            
                        open("data/account.txt","a").write(username + ":" + password + ":" + email + f"\n")



                        open("data/tokens.txt","a").write(user_id + ":" + access_token + ":" + email + ":" + username + ":" + password + f"\n")
                        open("data/tokenonly.txt","a").write(access_token + f"\n")                


                        self.chat_access(username, user_id, x_device_id, captcha['proxy'])


                    elif "error_description" in response.text:
                        ercont = response.json()['error_description']
                        
                        pass
                    else:
                        pass
                except Exception as e:
                    pass

            threading.Thread(target=thread).start()
            



    def generator_run(self):


        def browser_thread():
            asyncio.run(self.run_solver())


        

        def run_creator(captcha):
            res = self.create_account(captcha)
        
        try:
            print()
            print()
            for start_browser in range(2):
                threading.Thread(target=browser_thread).start()
            while True:


                try:
                    time.sleep(0.01)
                    if self.solved_captcha != []:
                        for captcha in self.solved_captcha:
                            threading.Thread(target=run_creator, args=[captcha,]).start()
                            self.solved_captcha.remove(captcha)
                            
                except:
                    traceback.print_exc()

        except Exception as e:
            print(str(traceback.format_exc()))



import os, time, httpx


class Installer:
    def __init__(self):
        self.local_appdata_path = os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local')
        self.install_playwright()

    def install_playwright(self):
        playwright_path = self.local_appdata_path + "\\" + "ms-playwright"
    
        try:
            os.mkdir(playwright_path) 
        except:
            pass

        if not os.path.exists(playwright_path + "\\" + firefox_version):
            with httpx.stream('GET', download_url) as response:
                total_length = int(response.headers['Content-Length'])
                downloaded_length = 0

                with open(playwright_path + "\\playwright.zip", 'wb') as file:
                    for chunk in response.iter_raw():
                        file.write(chunk)
                        downloaded_length += len(chunk)
                        printProgressBar(downloaded_length, total_length, prefix='Downloading data [1]:', suffix='Complete', length=50)

            unzip_file(playwright_path + "\\playwright.zip", playwright_path)
            os.remove(playwright_path + "\\playwright.zip")
            

import subprocess, platform, hashlib, zipfile, json, httpx
import base64
from Crypto.Cipher import AES
from Crypto import Random
import hashlib



def get_fingerprint():

    list_to_hash = [
        platform.machine(),
        platform.processor(),
        platform.win32_edition(),
        platform.win32_is_iot(),
        str(subprocess.check_output('wmic csproduct get uuid')).split(f'\\r\\n')[1].strip(f'\\r').strip()
    ]

    return hashlib.sha256(str(list_to_hash).encode()).hexdigest()


def user_id(user):
    headers = {'Connection': 'keep-alive','Pragma': 'no-cache','Cache-Control': 'no-cache','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"','Accept-Language': 'en-US','sec-ch-ua-mobile': '?0','Client-Version': '7b9843d8-1916-4c86-aeb3-7850e2896464','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36','Content-Type': 'text/plain;charset=UTF-8','Client-Session-Id': '51789c1a5bf92c65','Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko','X-Device-Id': 'xH9DusxeZ5JEV7wvmL8ODHLkDcg08Hgr','sec-ch-ua-platform': '"Windows"','Accept': '*/*','Origin': 'https://www.twitch.tv','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.twitch.tv/',}
    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+user+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'
    try:
        response = httpx.post('https://gql.twitch.tv/gql', headers=headers, data=data)
        return response.json()[0]['data']['user']['id']
    except:
        return False
    

class AESCipher(object):
    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

class Aes:
    def __init__(self):
        self.key = "SecKey2115"

    def decrypt(self, text, key=None):
        if key is not None:
            self.key = key
        return AESCipher(self.key).decrypt(text)

    def encrypt(self, text, key=None):
        if key is not None:
            self.key = key
        return AESCipher(self.key).encrypt(text).decode()
    


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()



def unzip_file(file_path, extract_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print(f"File '{file_path}' successfully extracted to '{extract_path}'.")


import subprocess, platform, hashlib, zipfile, json, httpx, re, random
import base64
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import psutil

import re
import random
import string
from websocket import create_connection

def get_stream_data(target):

    socket_mess_list = ['CAP REQ :twitch.tv/tags twitch.tv/commands','PASS SCHMOOPIIE','NICK justinfan23340','USER justinfan23340 8 * :justinfan23340']
    ws = create_connection("wss://irc-ws.chat.twitch.tv/")
    for i in socket_mess_list:
        ws.send(i)

    room_data = {
        "followers_only": None,
        "emote_only": None,
        "sub_only": None,
        "slow": None
    }

    ws.send('JOIN #' + target)
    for i in range(13):
        mess = ws.recv()
        if "ROOMSTATE" in mess:


            followers_only_key = int(mess.split("followers-only=")[1].split(";")[0])
            emote_only_key = int(mess.split("emote-only=")[1].split(";")[0])

            slow_key = int(mess.split("slow=")[1].split(";")[0])
            sub_only_key = int(mess.split("subs-only=")[1].split(" ")[0])


            if followers_only_key == -1:
                room_data['followers_only'] = False
            else:
                room_data['followers_only'] = True

            if emote_only_key == 0:
                room_data['emote_only'] = False
            else:
                room_data['emote_only'] = True

            if slow_key == 0:
                room_data['slow'] = False
            else:
                room_data['slow'] = True

            if sub_only_key == 0:
                room_data['sub_only'] = False
            else:
                room_data['sub_only'] = True


            break

    return room_data

def replace_int(match):
    return str(random.randint(0, 9))

def replace_str(match):
    characters = string.ascii_lowercase + string.ascii_uppercase 
    random_string = ''.join(random.choice(characters) for _ in range(1))
    return random_string

def replace_invite(match):
    invite = random.choice(["Jo1n D1$c0rd", "Th3 b3st b0ting Discord", "Fr33 b0ts", "J0in our dc", "D1$c0rd", "dc", "discord", "Join", "Join dc", "dc server"])
    return invite

def replace_arrow(match):
    invite = random.choice(["->", "-", ">", " ", "=>", "== >", "-+", ">>", ">>>", "_>", "lll>", "[]>", "=+", "- >", "= >", "-=->", "-=>", "--}", "-}", "==}"])
    return invite

def replace_dprefix(match):
    invite = random.choice(["dc . gg /", "discord . gg /", ".gg/", "gg/", "discord gg /", "discord . gg/", "d1$c0rd.gg/", "discord_gg/"])
    return invite

def replace_lorem(match):
    lorem_ipsum = """Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
    words = lorem_ipsum.split()
    random_index = random.randint(0, len(words) - 1)
    random_word = words[random_index]
    return random_word


def get_nodejs_pids():
    nodejs_pids = []
    
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == 'node.exe':
            nodejs_pids.append(process.info['pid'])
    
    return nodejs_pids



def gen_bio(text):

    replace_dict = {
        r'<R_INT>': replace_int,
        r'<R_STR>': replace_str,
        r'<D_INV>': replace_invite,
        r'<R_ARROW>': replace_arrow,
        r'<D_PREFX>': replace_dprefix,
        r'<R_LI>': replace_lorem
    }

    for i in replace_dict:
        pattern = re.compile(i)
        text = re.sub(pattern, replace_dict[i], text)

    return text





def get_fingerprint():

    list_to_hash = [
        platform.machine(),
        platform.processor(),
        platform.win32_edition(),
        platform.win32_is_iot(),
        str(subprocess.check_output('wmic csproduct get uuid')).split(f'\\r\\n')[1].strip(f'\\r').strip()
    ]

    return hashlib.sha256(str(list_to_hash).encode()).hexdigest()



def bordcast_id(user):

    headers = {'Connection': 'keep-alive','Pragma': 'no-cache','Cache-Control': 'no-cache','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"','Accept-Language': 'en-US','sec-ch-ua-mobile': '?0','Client-Version': '7b9843d8-1916-4c86-aeb3-7850e2896464','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36','Content-Type': 'text/plain;charset=UTF-8','Client-Session-Id': '51789c1a5bf92c65','Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko','X-Device-Id': 'xH9DusxeZ5JEV7wvmL8ODHLkDcg08Hgr','sec-ch-ua-platform': '"Windows"','Accept': '*/*','Origin': 'https://www.twitch.tv','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.twitch.tv/',}
    data = '''{
      "operationName":"WatchTrackQuery",
      "variables":{
         "channelLogin":"'''+user+'''",
         "videoID":null,
         "hasVideoID":false
      },
      "extensions":{
         "persistedQuery":{
            "version":1,
            "sha256Hash":"d8e507b720dd231780d57d325fb3a9bb8ee1ee60d424ae106e6dab328ea9b4c6"
         }
      }
   }'''

    try:
        response = httpx.post('https://gql.twitch.tv/gql', headers=headers, data=data)
        return response.json()['data']['user']['lastBroadcast']['id']
    except:
        return False

#print(bordcast_id("anthonyz"))




def user_id(user):
    headers = {'Connection': 'keep-alive','Pragma': 'no-cache','Cache-Control': 'no-cache','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"','Accept-Language': 'en-US','sec-ch-ua-mobile': '?0','Client-Version': '7b9843d8-1916-4c86-aeb3-7850e2896464','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36','Content-Type': 'text/plain;charset=UTF-8','Client-Session-Id': '51789c1a5bf92c65','Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko','X-Device-Id': 'xH9DusxeZ5JEV7wvmL8ODHLkDcg08Hgr','sec-ch-ua-platform': '"Windows"','Accept': '*/*','Origin': 'https://www.twitch.tv','Sec-Fetch-Site': 'same-site','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://www.twitch.tv/',}
    data = '[{"operationName": "WatchTrackQuery","variables": {"channelLogin": "'+user+'","videoID": null,"hasVideoID": false},"extensions": {"persistedQuery": {"version": 1,"sha256Hash": "38bbbbd9ae2e0150f335e208b05cf09978e542b464a78c2d4952673cd02ea42b"}}}]'
    try:
        response = httpx.post('https://gql.twitch.tv/gql', headers=headers, data=data)
        return response.json()[0]['data']['user']['id']
    except:
        return False
    

class AESCipher(object):
    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]

class Aes:
    def __init__(self):
        self.key = "SecKey2115"

    def decrypt(self, text, key=None):
        if key is not None:
            self.key = key
        return AESCipher(self.key).decrypt(text)

    def encrypt(self, text, key=None):
        if key is not None:
            self.key = key
        return AESCipher(self.key).encrypt(text).decode()
    


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()



def unzip_file(file_path, extract_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    #print(f"File '{file_path}' successfully extracted to '{extract_path}'.")


class SettingsTool:

    def __init__(self):
        self.settings_id = self.load_twitch()
        self.settings = self.get_settings()


    def load_twitch(self):

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'pl,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'Connection': 'keep-alive',
            'Referer': 'https://www.twitch.tv/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'no-reload': 'true',
        }

        response = httpx.get('https://www.twitch.tv/', params=params, headers=headers)
    def get_settings(self):
        try:
            return json.loads(httpx.get('https://static.twitchcdn.net/config/settings.'+self.settings_id+'.js').text.split('window.__twilightSettings = ')[1])
        except:
            return False
        

settings_url = SettingsTool()


# def get_username(self):
#     while True:

#         username = random.choice(self.usernames)

#         headers = {
#             'Accept': '*/*',
#             'Accept-Language': self.lt,
#             'Cache-Control': 'no-cache',
#             'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
#             'Client-Version': '31c1d55c-9db6-494e-b7bf-e5dfb0bb8cda',
#             'Connection': 'keep-alive',
#             'Content-Type': 'text/plain;charset=UTF-8',
#             'Origin': 'https://www.twitch.tv',
#             'Pragma': 'no-cache',
#             'Referer': 'https://www.twitch.tv/',
#             'Sec-Fetch-Dest': 'empty',
#             'Sec-Fetch-Mode': 'cors',
#             'Sec-Fetch-Site': 'same-site',
#             'User-Agent': self.useragent,
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#         }
#         data = '[{"operationName":"UsernameValidator_User","variables":{"username":"'+username+'"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660"}}}]'
#         try:
#             response = httpx.post('https://gql.twitch.tv/gql', headers=headers, data=data)
#             if response.json()[0]['data']['isUsernameAvailable'] == True:
#                 return username
#         except:
#             pass


data = '''[{"event":"mobile_latency_event","properties":{"app_session_id":"9054052c-4366-466e-837c-df4d979ba37f","app_version":"14.5.2","device_model":"SM-G955N","turbo":false,"debug_startTime":1683045767536,"device_type":"android","language":"pl-pl","login":"asdfsf3efw4ef34f","app_window_height":960,"app_window_width":540,"platform":"android","device_manufacturer":"samsung","load_time":33891,"communication_mode":"unknown","page_session_id":"a9fc4e85-9c10-411e-9677-a88f2e5ee48d","branch_id":"1181986510468424428","client_app":"android","adv_id":"48822b9c-6b81-4027-ab03-47a7f8d994c7","device_software":"android-28","orientation":"portrait","device_id":"9d93b84ba93546c4927f83341e81bdff","deeplink":0,"cold_start":1,"device_diagonal":4.6,"debug_endTime":1683045801427,"app_build":"1405020","user_id":905598689,"mobile_connection_type":"unknown","latency_event":"app_init","device_os_version":"9","time":1683045801}},{"event":"experiment_branch","properties":{"app_session_id":"9054052c-4366-466e-837c-df4d979ba37f","app_version":"14.5.2","device_model":"SM-G955N","turbo":false,"device_type":"android","language":"pl-pl","login":"asdfsf3efw4ef34f","app_window_height":960,"app_window_width":540,"experiment_type":"user_id","platform":"android","device_manufacturer":"samsung","experiment_version":9191,"page_session_id":"a9fc4e85-9c10-411e-9677-a88f2e5ee48d","branch_id":"1181986510468424428","client_app":"android","feature_flag":false,"adv_id":"48822b9c-6b81-4027-ab03-47a7f8d994c7","device_software":"android-28","experiment_name":"mobile_native_user_id_experiment","experiment_group":"b4","orientation":"portrait","device_id":"9d93b84ba93546c4927f83341e81bdff","experiment_id":"6a1cba54-d5d3-4117-ab42-06bd5514a134","device_diagonal":4.6,"app_build":"1405020","user_id":905598689,"mobile_connection_type":"unknown","device_os_version":"9","time":1683045801,"experiment_source":"miniexperiment"}},{"event":"mobile_latency_event","properties":{"app_session_id":"9054052c-4366-466e-837c-df4d979ba37f","app_version":"14.5.2","device_model":"SM-G955N","sub_screen":null,"turbo":false,"device_type":"android","language":"pl-pl","login":"asdfsf3efw4ef34f","app_window_height":960,"app_window_width":540,"platform":"android","device_manufacturer":"samsung","screen_name":"account_verification","load_time":347,"communication_mode":"unknown","page_session_id":"a9fc4e85-9c10-411e-9677-a88f2e5ee48d","branch_id":"1181986510468424428","client_app":"android","adv_id":"48822b9c-6b81-4027-ab03-47a7f8d994c7","device_software":"android-28","orientation":"portrait","device_id":"9d93b84ba93546c4927f83341e81bdff","deeplink":0,"cold_start":0,"device_diagonal":4.6,"app_build":"1405020","user_id":905598689,"mobile_connection_type":"unknown","latency_event":"page_loaded","device_os_version":"9","time":1683045801}},{"event":"pageview","properties":{"game":null,"app_session_id":"9054052c-4366-466e-837c-df4d979ba37f","app_version":"14.5.2","device_model":"SM-G955N","turbo":false,"device_type":"android","language":"pl-pl","medium":null,"login":"asdfsf3efw4ef34f","app_window_height":960,"app_window_width":540,"content":null,"platform":"android","device_manufacturer":"samsung","viewport_height":960,"content_filter":null,"content_type":null,"page_session_id":"45085f9c-4d4b-4822-8b80-cdcb02962113","branch_id":"1181986510468424428","client_app":"android","adv_id":"48822b9c-6b81-4027-ab03-47a7f8d994c7","device_software":"android-28","channel_name":null,"orientation":"portrait","device_id":"9d93b84ba93546c4927f83341e81bdff","content_id":null,"device_diagonal":4.6,"active_status":null,"viewport_width":540,"app_build":"1405020","user_id":905598689,"mobile_connection_type":"unknown","location":"email_verification#signup","device_os_version":"9","time":1683045801,"channel_id":null,"is_following":null,"section_header":null}},{"event":"experiment_branch","properties":{"app_session_id":"9054052c-4366-466e-837c-df4d979ba37f","app_version":"14.5.2","device_model":"SM-G955N","turbo":false,"device_type":"android","language":"pl-pl","login":"asdfsf3efw4ef34f","app_window_height":960,"app_window_width":540,"experiment_type":"device_id","platform":"android","device_manufacturer":"samsung","experiment_version":27407,"page_session_id":"45085f9c-4d4b-4822-8b80-cdcb02962113","branch_id":"1181986510468424428","client_app":"android","feature_flag":false,"adv_id":"48822b9c-6b81-4027-ab03-47a7f8d994c7","device_software":"android-28","experiment_name":"android_pending_transactions_fix","experiment_group":"active_14.3","orientation":"portrait","device_id":"9d93b84ba93546c4927f83341e81bdff","experiment_id":"c6838631-e0f8-4fcd-8d07-2df62f3d60e8","device_diagonal":4.6,"app_build":"1405020","user_id":905598689,"mobile_connection_type":"unknown","device_os_version":"9","time":1683045801,"experiment_source":"miniexperiment"}},{"event":"email_verify_load","properties":{"app_session_id":"9054052c-4366-466e-837c-df4d979ba37f","app_version":"14.5.2","device_model":"SM-G955N","turbo":false,"device_type":"android","language":"pl-pl","login":"asdfsf3efw4ef34f","app_window_height":960,"app_window_width":540,"platform":"android","device_manufacturer":"samsung","page_session_id":"45085f9c-4d4b-4822-8b80-cdcb02962113","branch_id":"1181986510468424428","client_app":"android","context":"signup","adv_id":"48822b9c-6b81-4027-ab03-47a7f8d994c7","device_software":"android-28","orientation":"portrait","device_id":"9d93b84ba93546c4927f83341e81bdff","device_diagonal":4.6,"app_build":"1405020","user_id":905598689,"mobile_connection_type":"unknown","location":"email_verification_signup","device_os_version":"9","time":1683045801}},{"event":"performance_monitoring","properties":{"running_services":"","native_heap_allocated":40179400,"app_session_id":"9054052c-4366-466e-837c-df4d979ba37f","app_version":"14.5.2","device_model":"SM-G955N","elapsed_seconds_in_location":0,"turbo":false,"device_type":"android","language":"pl-pl","login":"asdfsf3efw4ef34f","app_window_height":960,"app_window_width":540,"device_available_memory":3316985856,"dalvik_heap_allocated":16101904,"platform":"android","device_manufacturer":"samsung","page_session_id":"45085f9c-4d4b-4822-8b80-cdcb02962113","branch_id":"1181986510468424428","dalvik_heap_limit":192000000,"client_app":"android","adv_id":"48822b9c-6b81-4027-ab03-47a7f8d994c7","device_software":"android-28","app_state":"foreground","orientation":"portrait","device_total_memory":4133113856,"device_id":"9d93b84ba93546c4927f83341e81bdff","logged_in":true,"app_memory_allocated_with_deviation":184688000,"linux_kernel_version":"4.19.110","is_64_bit_architecture":true,"device_diagonal":4.6,"app_build":"1405020","proc_stat_data":"9449 (tch.android.app) S 1500 1500 0 0 -1 1077936448 129974 0 1 0 514 276 0 0 10 -10 98 0 138594 20723728384 67845 18446744073709551615 97390846685184 97390846702624 140727105705856 0 0 0 4612 1 1073775868 0 0 0 17 1 0 0 0 0 0 97390846708344 97390846709760 97390848487424 140727105706807 140727105706906 140727105706906 140727105707998 0","user_id":905598689,"heap_allocated":56281304,"mobile_connection_type":"unknown","up_time":34,"location":"email_verification#signup","device_os_version":"9","time":1683045801}},{"event":"update_prompt","properties":{"app_session_id":"9054052c-4366-466e-837c-df4d979ba37f","target_app_version_code":1500000,"app_version":"14.5.2","device_model":"SM-G955N","turbo":false,"device_type":"android","language":"pl-pl","login":"asdfsf3efw4ef34f","app_window_height":960,"app_window_width":540,"platform":"android","device_manufacturer":"samsung","install_status_code":0,"page_session_id":"45085f9c-4d4b-4822-8b80-cdcb02962113","branch_id":"1181986510468424428","client_app":"android","adv_id":"48822b9c-6b81-4027-ab03-47a7f8d994c7","device_software":"android-28","orientation":"portrait","device_id":"9d93b84ba93546c4927f83341e81bdff","is_initial_install_status_code":true,"device_diagonal":4.6,"target_app_version":null,"update_prompt_action":"install_status_updated","app_build":"1405020","user_id":905598689,"mobile_connection_type":"unknown","device_os_version":"9","time":1683045801}},{"event":"update_prompt","properties":{"app_session_id":"9054052c-4366-466e-837c-df4d979ba37f","target_app_version_code":1500000,"app_version":"14.5.2","device_model":"SM-G955N","turbo":false,"device_type":"android","language":"pl-pl","login":"asdfsf3efw4ef34f","app_window_height":960,"app_window_width":540,"platform":"android","device_manufacturer":"samsung","page_session_id":"45085f9c-4d4b-4822-8b80-cdcb02962113","branch_id":"1181986510468424428","client_app":"android","adv_id":"48822b9c-6b81-4027-ab03-47a7f8d994c7","device_software":"android-28","orientation":"portrait","device_id":"9d93b84ba93546c4927f83341e81bdff","dismiss_count":0,"device_diagonal":4.6,"target_app_version":null,"update_prompt_action":"download_impression","app_build":"1405020","user_id":905598689,"mobile_connection_type":"unknown","device_os_version":"9","time":1683045801}},{"event":"mobile_latency_event","properties":{"app_session_id":"9054052c-4366-466e-837c-df4d979ba37f","app_version":"14.5.2","device_model":"SM-G955N","turbo":false,"debug_startTime":1683045801162,"device_type":"android","language":"pl-pl","login":"asdfsf3efw4ef34f","app_window_height":960,"app_window_width":540,"platform":"android","device_manufacturer":"samsung","result":"0","load_time":11623,"communication_mode":"unknown","page_session_id":"45085f9c-4d4b-4822-8b80-cdcb02962113","branch_id":"1181986510468424428","client_app":"android","adv_id":"48822b9c-6b81-4027-ab03-47a7f8d994c7","device_software":"android-28","orientation":"portrait","device_id":"9d93b84ba93546c4927f83341e81bdff","deeplink":0,"cold_start":0,"device_diagonal":4.6,"debug_endTime":1683045812785,"app_build":"1405020","user_id":905598689,"mobile_connection_type":"unknown","latency_event":"followed_first_page_query","device_os_version":"9","time":1683045812}}]'''










































































import httpx, json, threading, time, random, math, hashlib, functools
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class X_kpsdk_cd:
    def __init__(self) -> None:
        self._0x18e9d3 = []
        self._0x567464 = 0x0
        self._0xb27c80 = 0x0
        self._0x297e3e = 0x0


    def hashdif(self,hashx):
        return 0x10000000000000 / (int((str('0x' + hashx[slice(0x0, 0xd)])),0) + 1)

    def GetID(self):
        global _0x186a64
        global _0x314ceb
        _0x186a64 = ''
        _0x314ceb = 0x0
        while _0x314ceb < 0x20:
            _0x186a64 = _0x186a64 + '0123456789abcdef'[math.floor((0x10 * random.uniform(1,0)))]
            _0x314ceb = _0x314ceb + 1
        return _0x186a64

    #CALC ANWSERS FROM HASH
    def _0x3352e2(self,_0xe551fb, timex1,requestid):
        difficulty = _0xe551fb['difficulty']
        subchallengeCount = _0xe551fb['subchallengeCount']
        platformInputs = _0xe551fb['platformInputs']
        _0x365fdc = []
        global _0x185ced
        global _0x2f208c
        _0x2f208c = hashlib.sha256((platformInputs+f",\x20{timex1},\x20{requestid}").encode('utf-8')).hexdigest()
        _0x185ced = 0x0
        _0x449621 = difficulty / subchallengeCount
        while _0x185ced < subchallengeCount:
            global _0x12f42c
            _0x12f42c = 0x1
            while True:
                _0x48c683 = hashlib.sha256((str(_0x12f42c)+",\x20" + _0x2f208c).encode('utf-8')).hexdigest()
                if self.hashdif(_0x48c683) >= _0x449621:
                    _0x365fdc.append(_0x12f42c)
                    _0x2f208c = _0x48c683
                    break
                _0x12f42c = _0x12f42c + 0x1
            _0x185ced = _0x185ced + 0x1

        return {"answers":_0x365fdc, "finalHash": _0x2f208c}

    def Calc(self, _0xe551fb,_0x530c71, _0x17ebdf = None, _0x4165cf = None):

        _0xe551fb = _0xe551fb # Game settings
        _0x7222e7 = round(time.time() * 1000) # Start time 
        _0x4cfd74 = random.uniform(10000.00000000056,100000.90000000056) # Browser Start Page time
        if _0x4165cf != None:
            _0x4165cf = _0x4165cf
        else:
            _0x4165cf = _0x7222e7 - _0x530c71
        if _0x17ebdf != None:
            _0x17ebdf = _0x17ebdf
        else:
            _0x17ebdf = self.GetID() # Request id
        _0x598bb9 = self._0x3352e2(_0xe551fb, _0x4165cf, _0x17ebdf) # Calc Answers
        time.sleep(0.00001)
        _0x4583bf = _0x4cfd74 + (round(time.time()*1000) - _0x7222e7)
        _0x121145 = round(0x3e8 * (_0x4583bf - _0x4cfd74)) / 0x3e8 # Calc Answers Time

        _0xe79016 = {}
        _0xe79016['workTime'] = _0x4165cf
        _0xe79016['id'] = _0x17ebdf
        _0xe79016['answers'] = _0x598bb9['answers']
        _0xe79016['duration'] = _0x121145
        _0xe79016['d'] = _0x530c71
        _0xe79016['st'] = 0x0
        _0xe79016['rst'] = 0x0

        return _0xe79016

    def CalcTime(self, _0x55f935,_0x58b0fe):

        _0x2a0645 = _0x55f935 - _0x58b0fe
        self._0x18e9d3.append(_0x2a0645)

        if 0x1 == len(self._0x18e9d3):
            self._0x567464 = 0
            self._0xb27c80 = _0x55f935
            self._0x297e3e = _0x58b0fe
            return None
        else:
            def _0xdf8cc0(xl1 , xl2):
                return functools.reduce(lambda a, b: a+b, [xl1 + 0x1 / xl2,0])
            for i in self._0x18e9d3:
                self._0x567464 = _0xdf8cc0(self._0x567464,i)
        return round(len(self._0x18e9d3) / self._0x567464)

    def x_kpsdk_cd(self,ServerTime):

        _0x32aee9 = ServerTime
        _0x14697c = round(time.time()*1000)
        self.CalcTime(_0x14697c,_0x32aee9)
        _0x14697c = round(time.time()*1000)
        var = self.CalcTime(_0x14697c,_0x32aee9)

        _0xb271ef = {'difficulty': 10,'platformInputs': "tp-v2-input", 'subchallengeCount':2} # Game Data
        _0x28caae = self.Calc(_0xb271ef ,var)
        _0x28caae['st'] = ServerTime
        _0x28caae['rst'] = self._0xb27c80

        return _0x28caae


class Authentication:
    def __init__(self, key: str, fingerprint: str, kill):
        self.kill = kill
        self.key = key
        self.fingerprint = fingerprint
        self.api_url = ""
        self.offline_counter = 0

    def encrypt(self, auth_data, key):
        cipher = AES.new(key, AES.MODE_CBC)
        cipher_text = cipher.encrypt(pad(auth_data.encode('utf-8'), AES.block_size))
        return cipher.iv + cipher_text

    def auth(self):
        try:
            auth_data = json.dumps({"key": self.key, "uuid": self.fingerprint})
            key = b'K4S4D4S1K1M1Y3AA'
            auth_dataencrypt = self.encrypt(auth_data, key)

            res = httpx.post(
                self.api_url + "/authv1.3",
                json={
                    "data": auth_dataencrypt.hex()
                }
            )

            status = res.json()['success']

            if status is True:
                return 200
            elif status is False:
                return 400
            else:
                return 404

        except Exception as e:
            return 500
    

    def checkgenlimit(self):
        try:
            auth_data = json.dumps({"key": self.key, "uuid": self.fingerprint})
            key = b''
            auth_dataencrypt = self.encrypt(auth_data, key)

            res = httpx.post(
                self.api_url + "/checklimitx",
                json={
                    "data": auth_dataencrypt.hex()
                }
            )

            return res.text

        except Exception as e:
            return 500




    def check_loop(self):
        while True:
            time.sleep(300)
            res = self.auth()
            if res == 200:

                self.offline_counter = 0 # ok
                pass
            elif res == 400:
                self.kill() # time expired / invalid
            elif res == 404:
                self.kill() # error
            elif res == 500:
                # offline
                if self.offline_counter <= 5:
                    self.offline_counter += 1
                else:
                    self.kill() # connection error



    def start_check(self):
        threading.Thread(target=self.check_loop).start()



    def x_kpsdk_cd(self, ts):
        # try:
        #     kpsdk = json.dumps({
        #         "key": self.key,
        #         "uuid": self.fingerprint,
        #         "timex":ts
        #     })

        #     res = httpx.post(
        #         self.api_url + "/hash", 
        #         json={ "data" : 
        #               untils.AESCipher(self.encrypt_key).encrypt(kpsdk).decode()
        #               },
        #         timeout=1000
        #         )
        #     return json.loads(untils.AESCipher(self.encrypt_key).decrypt(res.text))
        
        # except:
        #     return False

        return X_kpsdk_cd().x_kpsdk_cd(int(ts))














api = "https://cb27-2a12-bec0-20c-4d81-00-1.ngrok-free.app"
AUTH_KEY = "XyLoAiO$$^%$%$!@^&*%$#768352764278eg43fjhgfkjdhHGXC^D&F"



def get_hwid():
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 2)][::-1])
    return mac_address

def start_key_timer(key, hwid):
    API_ENDPOINT = f"{api}/startkey"
    headers = {'Authorization': AUTH_KEY}
    response = requests.post(API_ENDPOINT, json={"key": key, "hwid": hwid}, headers=headers)

    if response.status_code == 200:
        print("Success!")
    else:
        print("Failed!")

def check_key_validity(key):
    API_ENDPOINT = f"{api}/keyinfo"
    headers = {'Authorization': AUTH_KEY}
    response = requests.get(API_ENDPOINT, params={"key": key}, headers=headers)

    if response.status_code == 200:
        key_info = response.json()
        if key_info["valid"]:
            return True, key_info["remaining_time"], key_info["hwid"]
        else:
            return False, None, None
    else:
        return False, None, None

def success():
    App().run()

with open('config.json', 'r') as config_file:
    config_verisi = json.load(config_file)

class Selection:

    data = None

    def __init__(self) -> None:
        self.selection_data = {
            0: 'Account Gen',
            1: 'Integrity Gen/Refresh',
            2: 'Viewbot (Soon)',
            3: 'Followbot (Soon)',
            4: 'Chat Spam (Soon)',
            5: 'Unfollow (Soon)'
        }

    def menu(self):
        os.system("cls")
        menu_items = [Fore.LIGHTCYAN_EX + "Ξ───────────────────────────────Ξ"]
        for key, value in self.selection_data.items():
            menu_items.append(f"{Fore.LIGHTBLUE_EX}{key}: {value}")
        menu_items.append(Fore.LIGHTCYAN_EX + "Ξ───────────────────────────────Ξ")

        terminal_height = os.get_terminal_size().lines

        menu_height = len(menu_items)
        padding_lines = (terminal_height - menu_height) // 2 - 2 

        print("\n" * padding_lines)
        for item in menu_items:
            print(Center.XCenter(item))

    def run(self, data):
        self.data = data
        while True:
            self.menu()
            res = input(Center.XCenter(Fore.LIGHTCYAN_EX + "Select an option: " + Fore.RESET))
            try:
                res = int(res)
                if res in self.selection_data:
                    self.start_selected(res)
                else:
                    print(Center.XCenter(Fore.RED + "Invalid Input"))
            except ValueError:
                print(Center.XCenter(Fore.RED + "Invalid Input"))
            time.sleep(2)
            os.system("cls")

    def start_selected(self, selected):
        os.system("cls")
        run_list = [Generator, Generatorr]
        if selected == 0:
            run_list[0](self.data)
        elif selected == 1:
            run_list[1](self.data)
        else:
            print(Center.XCenter(Fore.RED + "Option not implemented yet."))
        time.sleep(5)

class App:
    def __init__(self) -> None:
        self.force_kill = ()
        os.system("cls")
        ctypes.windll.kernel32.SetConsoleTitleW(f"Xylo Twitch AIO")
        self.key = None
        self.config = json.load(open('config.json', 'r'))
        self.login()
        
    def login(self):
        config_dosyasi_adi = 'config.json'

        if 'key' in config_verisi and config_verisi['key']:
            self.key = config_verisi['key']
        else:
            self.key = pwinput.pwinput(prompt=f"\n                                     {Fore.CYAN}( {Fore.GREEN}/{Fore.CYAN} ){Fore.LIGHTWHITE_EX} KEY -> ", mask='•')

        self.auth = Authentication(
            key=self.key,
            fingerprint=self.key,
            kill=self.force_kill
        )
        #self.auth.auth()
        res = 200

        if res == 200:
            config_verisi['key'] = self.key
            with open(config_dosyasi_adi, 'w') as config_dosyasi:
                json.dump(config_verisi, config_dosyasi, indent=2)
            self.auth.start_check()
            return True
        elif res == 400:
            os.system("cls")
            print("\n" + Fore.RED + " ERR > INVALID KEY")
            time.sleep(5)
            self.force_kill()
        elif res == 404:
            self.force_kill()
        elif res == 500:
            self.force_kill()

    def run_installer(self):
        Installer()

    def run(self):
        data = {
            "proxies": open("data/proxies.txt", "r").read().splitlines(),
            "usernames": open("data/tokens.txt", "r").read().splitlines(),
            "token": open("data/tokens.txt", "r").read().splitlines(),
            "integrity": open("integrity.txt", "r").read().splitlines(),
            "auth": self.auth
        }

        Selection().run(data)

colorama.init()

def get_input(prompt):
    print(prompt, end='', flush=True)
    return input()


def main():
    key = pwinput.pwinput(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                                                      KEY -> ", mask='•')
    valid, remaining_time, stored_hwid = check_key_validity(key)
    if valid:
        print("Valid!")
        time.sleep(2)
        hwid = get_hwid()
        if stored_hwid is None:
            print("Success!")
            start_key_timer(key, hwid)
            success()
        elif stored_hwid == hwid:
            print("Success!")
            success()
        else:
            print("[ X ] -> HWID Error")
    else:
        print("[ X ] -> Invalid key")



if __name__ == "__main__":
    main()