import ctypes.wintypes
import logging
import os
import shutil
import sys
import time

logging.basicConfig(filename="info.log", level=logging.INFO)
logging.basicConfig(filename="crash.log", level=logging.ERROR)

CSIDL_PERSONAL = 5  # My Documents
SHGFP_TYPE_CURRENT = 0  # Get current, not default value

global result, appMainPath, buf, myDocuments, gameList, SII_exe, active_profile, active_save, profileTable, saveTable

buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(
    None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf
)
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


profileTable = {"ID": [], "Profile": [], "Path": []}
gameList = {"ets": "Euro Truck Simulator 2", "ats": "American Truck Simulator"}
SII_exe = os.path.join(os.getcwd(), "SII.exe")


def main():
    def cwd():
        label = "📂 | Where I am:  |"
        labelLength = len(label)
        cwd = os.getcwd() + " |"
        cwdLength = len(cwd)
        print(
            "\n+",
            "-".center(labelLength - 1, "-"),
            "+",
            "-".center(cwdLength - 2, "-"),
            "+",
        )
        print("|", label, cwd)
        print(
            "+",
            "-".center(labelLength - 1, "-"),
            "+",
            "-".center(cwdLength - 2, "-"),
            "+\n",
        )

    # print("Program Starting...")
    _selectGamePath = os.path.join(myDocumentsPath, gameList.get("ets"))
    # print("Select Game Path:", _selectGamePath)
    _selectGamePathExists = os.path.exists(_selectGamePath)
    if _selectGamePathExists:

        logging.info("%s", gameList.get("ets") + " folder found.")
        os.chdir(_selectGamePath)

        _selectGameProfilesPath = os.path.join(_selectGamePath, "profiles")
        os.chdir(_selectGameProfilesPath)
        if os.path.exists(_selectGameProfilesPath):
            logging.info("\n%s", gameList.get("ets") + " profiles folder found.")

            for profileFolderIndex, profileFolder in enumerate(os.listdir(os.getcwd())):
                profilePath = os.path.join(os.getcwd(), profileFolder)
                os.chdir(profilePath)

                profileSiiPath = os.path.join(profilePath, "profile.sii")
                profile_decrypt_exe_path = os.getcwd() + "/profile_decrypt.exe"
                shutil.copyfile(SII_exe, profile_decrypt_exe_path)
                if os.path.exists(profile_decrypt_exe_path):
                    os.system("profile_decrypt.exe profile.sii")
                    logging.info("Profile_Decrypt.exe file deleted.")
                else:
                    logging.error("Profile_Decrypt.exe file not deleted.")

                # print(profileSiiPath, "Sii Reading...")
                logging.info("\n" + profileSiiPath + "\nSii Reading...")

                if os.path.exists(profile_decrypt_exe_path):
                    os.remove(profile_decrypt_exe_path)
                    logging.info("Profile_Decrypt.exe file deleted.")
                else:
                    logging.error("Profile_Decrypt.exe file not deleted.")
                os.chdir(_selectGameProfilesPath)

        else:
            logging.error("%s", gameList.get("ets") + " profiles folder not found.")

    else:
        logging.error("Error: %s", gameList.get("ets") + " folder not found !")


try:
    main()
    os.system("exit");
except Exception as e:
    logging.error("Error: %s", e)
logging.info("**********************************************")
