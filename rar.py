from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

with SB(uc=True, test=True) as sb:
    if True:
        if True:
            url = "https://kick.com/asianandy"
            sb.uc_open_with_reconnect(url, 5)
            sb.uc_gui_click_captcha()
            sb.sleep(2)
            sb.uc_gui_handle_captcha()
            sb.sleep(5)
            if sb.is_element_present('button:contains("Accept")'):
                sb.uc_click('button:contains("Accept")', reconnect_time=4)
            if sb.is_element_present('button:contains("I am 18+")'):
                sb.uc_click('button:contains("I am 18+")', reconnect_time=4)
            if sb.is_element_visible('#injected-channel-player'):
                driver2 = sb.get_new_driver(undetectable=True)
                driver2.uc_open_with_reconnect(url, 5)
                driver2.uc_gui_click_captcha()
                sb.sleep(2)
                driver2.uc_gui_handle_captcha()
                sb.sleep(15)
                if driver2.is_element_present('button:contains("Accept")'):
                    driver2.uc_click('button:contains("Accept")', reconnect_time=4)
                if driver2.is_element_present('button:contains("I am 18+")'):
                    driver2.uc_click('button:contains("I am 18+")', reconnect_time=4)
                while sb.is_element_visible('#injected-channel-player'):
                    sb.sleep(120)
                sb.quit_extra_driver()
        sb.sleep(1)
