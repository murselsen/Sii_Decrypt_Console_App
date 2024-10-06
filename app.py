import ctypes.wintypes
import logging
import os
import shutil
import sys
import time
from script import main

logging.basicConfig(filename="info.log", level=logging.INFO)
logging.basicConfig(filename="crash.log", level=logging.ERROR)

CSIDL_PERSONAL = 5  # My Documents
SHGFP_TYPE_CURRENT = 0  # Get current, not default value

global result, appMainPath, buf, myDocuments, gameList, SII_exe, active_profile, active_save, profileTable, saveTable

buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
myDocumentsPath = buf.value
print("*************************************************")
print("*        【 Company: The King'S Works 】        *")
print("*        【 Product Name : Scs SII Decrypt 】   *")
print("*        【 Author: MQuel 】                    *")
print("*        【 Github: github@murselsen 】         *")
print("*        【 Discord: 35mursel 】                *")
print("*        【 Version: v3 】                      *")
print("*        【 License: 2023 - 2030 】             *")
print("*************************************************")
print("*                                               *")
print("*        【 Mod: Ets - All Profile Descrypt 】  *")
print("*                                               *")
print("*************************************************")


profileTable = {'ID': [], 'Profile': [], 'Path': []}
gameList = {"ets": "Euro Truck Simulator 2", "ats": "American Truck Simulator"}
SII_exe = os.path.join(os.getcwd(), "SII.exe")


def main():
    print("Program Starting...")
    
    
    
try:
    main()
except Exception as e:
    logging.error("Error: %s", e)