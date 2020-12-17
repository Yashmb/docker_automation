import os

width = os.get_terminal_size().columns

welcome = (" Docker Automation ").center(width)

def tab():
    print("\n"*2)

def head():
    os.system("clear")
    tab()
    print((" ----------------- ").center(width))
    print(welcome)
    print((" ----------------- ").center(width))
    tab()

def cls():
    os.system("clear")
    head()

head()

def index():
    print("""
    1. local system
    2. remote system
    q. quit
    \n
    """)
    global sys
    try:
        sys = (input("select : "))
    except ValueError:
        print("Select an option")
    head()

def main():
    print("""
    1. Docker Configuration
    2. Docker Service
    3. Docker Management
    4. Docker Container Configuration
    0. back
    \n
    """)
    
while True:
    index()
 
    if sys == "1":
        while True:
            head()
            main()

            global inp

            try:
                inp = int(input("select : "))
            except ValueError:
                os.system("clear")
                head()
                print("Select an option")
                continue

            if inp == 1:
                head()

                confirm = input("""Type "yes" to continue : """)
                cls()

                if confirm == "yes":
                    ex = os.system("rpm -q docker-ce > /dev/null 2>&1")
                    if ex != 0:
                        print(("Installing Docker ...").center(width))
                        tab()
                        print(("please don't exit").center(width))
                        os.system("wget https://raw.githubusercontent.com/Yashmb/repos/main/docker.repo -O /etc/yum.repos.d/docker.repo > /dev/null 2>&1")
                        os.system("yum install docker-ce --nobest -y > /dev/null 2>&1")
                        cls()
                        print(("Docker Successfully Installed !").center(width))
                        tab()
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    else:
                        print(("Docker already configured .").center(width))
                        tab()
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                else:
                    cls()
            
            elif inp == 2:
                while True:
                    head()
                
                    print("""
                    1. Start Docker
                    2. Stop Docker
                    3. Docker Status
                    0. back
                    \n
                    """)

                    try:
                        svc = int(input("select : "))
                    except ValueError:
                        cls()
                        print("Select an option")
                        continue

                    if svc == 1:
                        tab()
                        os.system("systemctl start docker")
                        cls()
                        print(("Docker service started").center(width))
                        tab()
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif svc == 2:
                        tab()
                        os.system("systemctl stop docker")
                        cls()
                        print(("Docker service stopped").center(width))
                        tab()
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif svc == 3:
                        tab()
                        os.system("systemctl status docker")
                        tab()
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif svc == 0:
                        break
                
                cls()

            elif inp == 3:
                while True:
                    head()

                    print("""
                    1. Docker Images
                    2. Docker Containers
                    3. 
                    0. back
                    \n
                    """)

                    try:
                        mng = int(input("select : "))
                    except ValueError:
                        cls()
                        print("Select an option")
                        continue

                    if mng == 1:
                        while True:
                            head()

                            print("""
                            1. Images List
                            2. Download Image
                            3. Search Image
                            0. back
                            \n
                            """)

                            try:
                                img = int(input("select : "))
                            except ValueError:
                                cls()
                                print("Select an option")
                                continue

                            if img == 1:
                                tab()
                                os.system("docker images")
                                tab()
                                cl = input("Press any key to continue")
                                if cl == "":
                                    os.system("clear")
                                    continue
                            elif img == 2:
                                tab()
                                img_name = input("Enter Image Name : ")
                                tab()
                                vtag = input("""Enter Version (for latest version type "latest")""")
                                tab()
                                
                                cmd = ("docker pull {0}:{1}".format(img_name, vtag))
                                os.system(cmd)
                                tab()
                                cl = input("Press any key to continue")
                                if cl == "":
                                    os.system("clear")
                                    continue
                            elif img == 3:
                                tab()
                                img_name = input("Enter Image Name :")
                                tab()
                                vtag = input("""Enter Version (for latest version type "latest")""")
                                tab()

                                cmd = ("docker search {0}:{1}".format(img_name, vtag))
                                os.system(cmd)
                                tab()
                                cl = input("Press any key to continue")
                                if cl == "":
                                    os.system("clear")
                                    continue
                            elif img == 0:
                                break

                        cls()        
                    
                    elif mng == 2:
                        while True:
                            head()

                            print("""
                            1. Launch Docker Container
                            2. Start/Stop/Attach Container
                            3. Expose Container
                            4. Delete Containers
                            0. back
                            \n
                            """)

                            try:
                                cont = int(input("select : "))
                            except ValueError:
                                cls()
                                print("Select an option")
                                continue

                            if cont == 1:
                                while True:
                                    head()

                                    print("""
                                    1. Interactive
                                    2. Non-Interactive
                                    0. back
                                    \n
                                    """)

                                    try:
                                        iact = int(input("select : "))
                                    except ValueError:
                                        cls()
                                        print("Select an option")
                                        continue

                                    if iact == 1:
                                        tab()
                                        os.system("docker images")
                                        tab()
                                        cont_name = input("Enter Container Name : ")                                    
                                        tab()
                                        img_name = input("Enter Image Name : ")                                        
                                        tab()

                                        cmd = ("docker run -it --name {0} {1}".format(cont_name, img_name))
                                        os.system(cmd)
                                        tab()
                                        cl = input("Press any key to continue")
                                        if cl == "":
                                            os.system("clear")
                                            continue
                                    elif iact == 2:
                                        tab()
                                        os.system("docker images")
                                        tab()
                                        cont_name = input("Enter Container Name : ")    
                                        tab()
                                        img_name = input("Enter Image Name : ")                                    
                                        tab()

                                        cmd = ("docker run -dit --name {0} {1}".format(cont_name, img_name))
                                        os.system(cmd)
                                        tab()
                                        cl = input("Press any key to continue")
                                        if cl == "":
                                            os.system("clear")
                                            continue
                                    elif iact == 0:
                                        break

                                cls()        






            else:
                exit()

                
                    