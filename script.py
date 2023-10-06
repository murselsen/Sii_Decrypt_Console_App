import ctypes.wintypes
import os
import asyncio
import shutil
import time
from tabulate import tabulate
import logging

logging.basicConfig(filename="logs.log.log", level=logging.INFO)
logging.basicConfig(filename="logs.crash.log", level=logging.ERROR)

CSIDL_PERSONAL = 5  # My Documents
SHGFP_TYPE_CURRENT = 0  # Get current, not default value

global result, appMainPath, buf, myDocuments, ets, SII_exe, active_profile, active_save, profileTable, saveTable
buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
myDocumentsPath = buf.value
print("*************************************************")
print("*        【 Company: The King'S Works 】        *")
print("*        【 Product Name : Scs SII Decrypt 】   *")
print("*        【 Author: MQuel 】                    *")
print("*        【 Github: github@murselsen 】         *")
print("*        【 Version: v1.0 】                    *")
print("*        【 License: 2023 - 2030 】             *")
print("*************************************************")

profileTable = {'ID': [], 'Profile': [], 'Path': []}


def main():
    def exit(status):
        if status:
            input("🚪 | Press any key to exit :")
        else:
            return True

    def cwd():
        label = "📂 | Where I am:  |"
        labelLength = len(label)
        cwd = os.getcwd() + " |"
        cwdLength = len(cwd)
        print("\n+", "-".center(labelLength - 1, "-"), "+", "-".center(cwdLength - 2, "-"), "+")
        print("|", label, cwd)
        print("+", "-".center(labelLength - 1, "-"), "+", "-".center(cwdLength - 2, "-"), "+\n")

    for i, dir in enumerate(os.listdir(myDocumentsPath)):
        print("📜 | [", i, "] | App Document Name => ", dir)
        etsPathExists = os.path.exists(os.path.join(myDocumentsPath, "Euro Truck Simulator 2"))
        if etsPathExists:
            if (dir == "Euro Truck Simulator 2"):
                etsPath = os.path.join(myDocumentsPath, dir)
            result = True
        else:
            result = False

    if result == True:
        print("✅ | Euro Truck Simulator 2 His file has been found ")
        print("🔔 | Result: ", result)
        # input("🔑 | Press a key to continue : ")
        appMainPath = os.getcwd()
        SII_exe = os.path.join(os.getcwd(), "SII.exe")

        profilesPath = os.path.join(etsPath, "profiles")
        os.chdir(profilesPath)
        cwd()
        print("-".center(53, "-"))
        print("| 👥 | Profile List")
        print("-".center(53, "-"))
        profilesList = os.listdir(os.getcwd())
        for index, profile in enumerate(profilesList):
            profileLine = "| [" + str(index) + "] | 👤 | Profile: " + str(profile)
            print(profileLine)
            print("-".center(len(profileLine) + 4, "-"))

        _inputSelectProfile = int(
            input("| 👥 | => Select the profile you want to decrypt: (0/" + str(len(profilesList) - 1) + ") "))
        print("-".center(53, "-"))
        print("| SELECT | 👤 | Profile: ", profilesList[_inputSelectProfile])
        selectProfile = profilesList[_inputSelectProfile]
        active_profile = selectProfile
        selectProfilePath = os.path.join(profilesPath, selectProfile)
        os.chdir(selectProfilePath)

        cwd()

        selectProfileFileList = os.listdir(os.getcwd())

        SII_copyfile = shutil.copyfile(SII_exe, os.getcwd() + "/SII.exe")
        os.path.exists(SII_copyfile)
        print("🔔 | Copying SII.exe -> ", os.path.exists(SII_copyfile), "\n")

        for i, profileFile in enumerate(selectProfileFileList):
            if (len(profileFile.split(".")) == 2):
                # print("| [",_inputSelectProfile,"] | 👤 | 📁 | File: ", profileFile)

                if (profileFile == "profile.sii"):
                    print("🔔 | ", profilesList[_inputSelectProfile], " | ", profileFile, " decrypting, Please wait...")
                    profileSII_Decrypt = os.system("SII.exe " + profileFile)
                    time.sleep(3.3)
                    if (profileSII_Decrypt == 0 or profileSII_Decrypt == 1):

                        print("🔔 | Decrypt: ", True, "\n")
                    else:
                        print("🔔 | ", profilesList[_inputSelectProfile], " | ", profileFile,
                              " decrypting,\n Please wait...")
                        print("🔔 | Decrypt: ", False, "\n\n")

                    time.sleep(2.5)
                else:
                    pass



            else:
                # print("| 👤 | 📂 | Dir: ", profileFile.split(".")[0])
                if (profileFile.split(".")[0] == "save"):
                    # print("| [", _inputSelectProfile, "] | 👤 | 📂 | Dir: ", profileFile.split(".")[0])
                    # print("| ✅ | Found the SAVE file belonging to the 👤 ", profile, "! ")

                    savePath = os.path.join(etsPath, "profiles", active_profile, "save")
                    os.chdir(savePath)

                    cwd()

                    saveList = os.listdir(os.getcwd())
                    for index, saveDir in enumerate(saveList):
                        print("| [", index, "] | 👤 | ", active_profile, " | Save Dir Name: ", saveDir)

                    _inputSelectSave = int(
                        input("| 👥 | => Select the save you want to decrypt: (0/" + str(len(saveList) - 1) + ") "))
                    print("-".center(53, "-"))
                    selectSave = saveList[_inputSelectSave]
                    active_save = selectSave
                    selectSavePath = os.path.join(savePath, selectSave)
                    os.chdir(selectSavePath)

                    cwd()

                    selectSaveFileList = os.listdir(os.getcwd())

                    SII_Save_Copyfile = shutil.copyfile(SII_exe, os.getcwd() + "/SII.exe")
                    os.path.exists(SII_Save_Copyfile)
                    print("🔔 | Profile :",active_profile," => Save :",active_save," | Copying SII.exe -> ", os.path.exists(SII_copyfile), "\n")

                    for index, saveFile in enumerate(selectSaveFileList):
                        print("| [", index, "] | 👤 | Name :", active_profile, "\n | Save : ",active_save,"\n | File : ",saveFile,"\n")
                        if saveFile == "game.sii":
                            print("🔔 | Status: Game.sii files will be decrypted. Please Wait!")
                            os.system("SII.exe game.sii")
                            time.sleep(3.0)
                        elif saveFile == "info.sii":
                            print("🔔 | Status: Info.sii files will be decrypted. Please Wait!")
                            os.system("SII.exe info.sii")
                            time.sleep(1.0)
                        else:
                            continue

        exit(True)

    else:
        print("⁉️ | Euro Truck Simulator 2 Folder Not Found")
        exit(True)


try:
    main()
except Exception as e:
    logging.error("main crashed. Error: %s", e)
