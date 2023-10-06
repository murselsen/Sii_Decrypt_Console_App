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
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
myDocumentsPath = buf.value
print("*************************************************")
print("*        【 Company: The King'S Works 】        *")
print("*        【 Product Name : Scs SII Decrypt 】   *")
print("*        【 Author: MQuel 】                    *")
print("*        【 Github: github@murselsen 】         *")
print("*        【 Discord: 35mursel 】                *")
print("*        【 Version: v2.1 】                    *")
print("*        【 License: 2023 - 2030 】             *")
print("*************************************************")

profileTable = {'ID': [], 'Profile': [], 'Path': []}
gameList = {"ets": "Euro Truck Simulator 2", "ats": "American Truck Simulator"}
SII_exe = os.path.join(os.getcwd(), "SII.exe")


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

    for index, game in enumerate(gameList):
        print("🎮|App :", gameList.get(game))

    _selectGame = input("Select the SCS game you want to Decrypt => (ets/ats) : ")
    if _selectGame == '' or _selectGame == ' ':
        print(
            " Error Input : ", _selectGame
        )
        os.system('cls')
        os.execl(sys.executable, "start " + os.path.abspath(__file__))
    else:
        # print("Input : ", _selectGame)

        _selectGameResult = gameList.get(_selectGame)
        # print("\nSelect Game: ", _selectGameResult)
        _selectGamePath = os.path.join(myDocumentsPath, _selectGameResult)
        # print("Select Game Path :", _selectGamePath)

        _selectGamePathExists = os.path.exists(_selectGamePath)
        # print("Select Game Path Exists Result :", _selectGamePathExists)

        if _selectGamePathExists:
            os.chdir(_selectGamePath)
            # cwd()
            # Profiles Path
            _selectGameProfilesPath = os.path.join(_selectGamePath, "Profiles")
            # print("Select Game Profiles Path :", _selectGameProfilesPath)

            _selectGameProfilePathExists = os.path.exists(_selectGameProfilesPath)
            # print("Select Game Profiles Path Exists Result :", _selectGameProfilePathExists)

            if _selectGameProfilePathExists:
                os.chdir(_selectGameProfilesPath)
                # cwd()
                print("Profile List")
                print("------------------")
                for profileDir_index, profileDir in enumerate(os.listdir(os.getcwd())):
                    print(
                        "---------------------------------------------------------------------------------------------")
                    print("[", profileDir_index, "] | Active Profile\n"
                                                 "[", profileDir_index, "] | -> Name :", profileDir)
                    _activeProfilePath = os.path.join(os.getcwd(), profileDir)
                    _activeProfilePathExists = os.path.exists(_activeProfilePath)
                    os.chdir(_activeProfilePath)
                    shutil.copyfile(SII_exe, os.getcwd() + "/SII.exe")

                    _activeProfileInfoFilePath = os.path.join(_activeProfilePath, "profile.sii")

                    _activeProfileInfoFilePathExists = os.path.exists(_activeProfileInfoFilePath)
                    cmd = "SII.exe profile.sii"
                    os.system(cmd)
                    # time.sleep(1.0)
                    # cwd()
                    print("Profile SII Reading....")
                    newLines = []
                    with open("profile.sii", "r") as profileDetailReading:

                        lines = profileDetailReading.readlines()
                        for line_index, line in enumerate(lines):

                            if line.startswith(" cached_discovery["):
                                del lines[line_index]
                            elif  line.startswith(" cached_stats["):
                                del lines[line_index]
                            else:
                                if line.startswith(" cached_discovery:"):
                                    line = " cached_discovery: 0\n"
                                elif line.startswith(" cached_stats:"):
                                    line = " cached_stats: 0\n"
                                else:
                                    pass
                                newLines.append(line)
                    # print(newLines)
                    print("Profile SII Writing...")
                    with open("profile.sii","w") as profileDetailWriting:
                        profileDetailWriting.writelines(newLines)


                    print(
                        "Cached Stats AND Discovery truncated !"
                    )

                    breakpoint()
                    _activeProfileSavePath = os.path.join(_activeProfilePath, "save")
                    _activeProfileSavePathExists = os.path.exists(_activeProfileSavePath)
                    if _activeProfileSavePathExists:
                        os.chdir(_activeProfileSavePath)
                        print("[", profileDir_index, "] Active Profile Save Dir")
                        for saves_index, saves in enumerate(os.listdir(os.getcwd())):

                            print("[", profileDir_index, "] | [", saves_index, "] -> Name :", saves)
                            _activeProfileSaveDirItemPath = os.path.join(os.getcwd(), saves)
                            _activeProfileSaveDirItemPathExists = os.path.exists(_activeProfileSaveDirItemPath)
                            os.chdir(_activeProfileSaveDirItemPath)
                            for saveFile_index, saveFile in enumerate(os.listdir(os.getcwd())):
                                shutil.copyfile(SII_exe, os.getcwd() + "/SII.exe")
                                if saveFile == "game.sii":
                                    print("\n🔔 | Status: Game.sii files will be decrypted. Please Wait!")
                                    os.system("SII.exe game.sii")
                                    time.sleep(3.0)
                                elif saveFile == "info.sii":
                                    print("\n🔔 | Status: Info.sii files will be decrypted. Please Wait!")
                                    os.system("SII.exe info.sii")
                                    time.sleep(1.0)
                                else:
                                    continue

                            os.chdir(_activeProfileSavePath)

                    else:
                        continue

                    os.chdir(_selectGameProfilesPath)  # Select Game Profiles Dir Path
                    logging.info("\n Status : Completed")
            else:
                os.system("exit")
        else:
            os.system("exit")


try:
    main()
except Exception as e:
    logging.error("Error: %s", e)
