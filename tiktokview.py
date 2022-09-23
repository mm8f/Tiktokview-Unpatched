import datetime
import random
import time
from colorama import init, Fore
from src import process


def main():
    init(autoreset=True)
    inject = process.ZefoyViews()
    print(
        Fore.GREEN + """                     .                          
                     M                          
                    dM                          
                    MMr                         
                   4MMML                  .     
                   MMMMM.                xf     
   .              "MMMMM               .MM-     
    Mh..          +MMMMMM            .MMMM      
    .MMM.         .MMMMML.          MMMMMh      
     )MMMh.        MMMMMM         MMMMMMM       
      3MMMMx.     'MMMMMMf      xnMMMMMM"       
      '*MMMMM      MMMMMM.     nMMMMMMP"        
        *MMMMMx    "MMMMM\    .MMMMMMM=         
         *MMMMMh   "MMMMM"   JMMMMMMP           
           MMMMMM   3MMMM.  dMMMMMM            .
            MMMMMM  "MMMM  .MMMMM(        .nnMP"
=..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*  
  "MMn...     'MMMMr 'MM   MMM"   .nMMMMMMM*"   
   "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""     
     ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"        
        *PMMMMMMhn. *x > M  .MMMM**""           
           ""**MMMMhx/.h/ .=*"                  
                    .3P"%....                   
                  nP"     "*MMnx
"""
    )
    print(Fore.LIGHTRED_EX + "Made by 420#0001")
    url_video = input("Enter URL Video: ")

    inject.get_session_captcha()
    time.sleep(1)

    if inject.post_solve_captcha(captcha_result=inject.captcha_solver()):

        print("\n[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + "Success Solve Captcha" + "\n")

        while True:

            inject_views = inject.send_views(
                url_video=url_video
            )
            if inject_views:

                if "Please try again later" in inject_views:
                    print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_views)
                    exit()

                elif "Successfully views sent." in inject_views:
                    print("[ " + str(
                        datetime.datetime.now()) + " ] " + Fore.LIGHTGREEN_EX + inject_views + " to " + Fore.LIGHTYELLOW_EX + "" + url_video,
                          end="\n\n")

                elif "Session Expired. Please Re Login!" in inject_views:
                    print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_views)
                    exit()

                elif "Please try again later. Server too busy." in inject_views:
                    print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTRED_EX + inject_views)
                    time.sleep(random.randint(300, 600))
                    exit()

                else:
                    for i in range(int(inject_views), 0, -1):
                        print("[ " + str(datetime.datetime.now()) + " ] " + Fore.LIGHTYELLOW_EX + "Please wait " + str(
                            i) + " seconds to send views again.", end="\r")
                        time.sleep(1)

                time.sleep(random.randint(1, 5))

            else:
                pass

    else:
        print(Fore.RED + "Failed to solve captcha.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "Exit")
        exit()
