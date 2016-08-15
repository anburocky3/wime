#!/usr/bin/python

os = __import__('os')
from subprocess import check_output
import subprocess
import sys, traceback
import platform

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
        try:

                linux = "1"

                windows = "2"

                mac = "3"

                info = "4"

                print "\033c"
                # print "                                            "
                # print "                                            "                                            
                print bcolors.WARNING + "  /$$      /$$ /$$$$$$ /$$      /$$ /$$$$$$$$                    /$$$$$$ " + bcolors.ENDC
                print bcolors.WARNING + "  | $$  /$ | $$|_  $$_/| $$$    /$$$| $$_____/                  /$$__  $$" + bcolors.ENDC
                print bcolors.WARNING +"  | $$ /$$$| $$  | $$  | $$$$  /$$$$| $$                        |__/  \ $$"  + bcolors.ENDC
                print "  | $$/$$ $$ $$  | $$  | $$ $$/$$ $$| $$$$$       /$$$$$$         /$$$$$/"                             
                print "  | $$$$_  $$$$  | $$  | $$  $$$| $$| $$__/       |______/        |___  $$"
                print bcolors.OKGREEN +"  | $$$/ \  $$$  | $$  | $$\  $ | $$| $$                        /$$  \ $$"  + bcolors.ENDC
                print bcolors.OKGREEN +"  | $$/   \  $$ /$$$$$$| $$ \/  | $$| $$$$$$$$                  |  $$$$$$/"  + bcolors.ENDC
                print bcolors.OKGREEN +"  |__/     \__/|______/|__/     |__/|________/                   \______/ "  + bcolors.ENDC
                print "|=======================================================================>>"
                print bcolors.OKBLUE +"|          Programmer: Anbuselvan Rocky   | fb.me/anburocky3             --==|"+ bcolors.ENDC
                print "|=======================================================================>>"                                            
                                    
                print" "
                print "Please choose your operating system."
                print " "
                print " 1) linux"
                print " 2) Windows"
                print " 3) Mac OS"
                print " 4) Info"

                print" "

                enter = raw_input("> ")

                while enter == linux and platform.system() == "Linux":
                        print " "
                        print "All wireless networks :"
                        print " "
                        command = "ls -1 /etc/NetworkManager/system-connections/"
                        proc = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
                        (out, err) = proc.communicate()
                        outwithoutreturn = out.rstrip('\n')
                        print outwithoutreturn
                        proc

                        print " "
                        
                        print "Insert the network name , or press (a) to see information about all networks."
                        print " "
                        nombre = raw_input("> ")
                        if nombre == "a":
                                print "\033[1;36m###################### - Information about all networks - ######################\033[1;m"                        	
                                wifi0 = os.system("egrep -h -s -A 9 --color -T 'ssid=' /etc/NetworkManager/system-connections/*")
                                print wifi0
                                print "\033[1;36m################################################################################\033[1;m"                                
                        else:
                                print "\033[1;36m################################ - " + nombre + " - ################################\033[1;m"
                                print " "

                                wifi0 = str(os.system("egrep -h -s -A 0 --color -T 'security=|key-mgmt=|psk=' /etc/NetworkManager/system-connections/" + nombre))
                                print " "
                                print "\033[1;36m################################################################################\033[1;m"
                                print " "
                

                        
                       

                while enter == windows and platform.system() == "Windows":

                        
                        print check_output("netsh wlan show profile key=clear", shell=True)
                        print "Insert the network name , or press (a) to see information about all networks."
                        print " "
                        nombre = raw_input("> ")
                        if nombre == "a":
                                print "############################ - Information about all networks - ############################"                          
                                print " "                            
                                wifi2 = check_output("netsh wlan show profile name=* key=clear", shell=True)
                                print wifi2
                                print " " 
                                print "#############################################################################################"
                        else:
                                print "###################################### - " + nombre + " - ######################################"
                                print " "                            
                                wifi2 = check_output("netsh wlan show profile name=" + nombre +" key=clear", shell=True)
                                print " "                            

                                print wifi2
                                print "#############################################################################################"
                                print " "  
                        guardar = raw_input("Do you want to save the result ? [y/n] > ")
                        if guardar == "y":
                                f = open(nombre+'.txt','w')
                                f.write(wifi2 + '\n')
                                f.close()
                                                   

                                        
                if enter == mac:
                        print "Wow! thanks for your response, we are launching it soon..."
                if enter == info:
                        print "\033c"
                        print "\033[1;36m================================================================================\033[0m"
                        print "|                    \033[93mPROGRAMMER :\033[0m \033[92mAnbuselvan Rocky\033[0m                             |"
                        print "|                                                                              |"
                        print "|                                                                              |"
                        print "!          facebook             : https://fb.me/anburocky3                     !" 
                        print "!          twitter              : https://twitter.com/anbuselvanrocky          !"
                        print "!          email                : anbuceo@gmail.com                            !"
                        print "!          website              : http://anbuselvanrocky.net                   !"
                        print "\033[1;36m================================================================================\033[0m"
                        print ""
                        print ""
                        print ""
                        print ""


                else:
                        print "Please select an option . (1) for linux , (2) for windows , and (3) for Mac OS ."


        except KeyboardInterrupt:
                print "Shutdown requested...exiting"
        except Exception:
                traceback.print_exc(file=sys.stdout)
        sys.exit(0)

if __name__ == "__main__":
            main()
