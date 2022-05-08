from sshpot import PotSSHFactory
from telnetpot import PotTelnetFactory
from ftppot import PotFTPFactory
from twisted.internet import reactor
import os

def start_ssh(lport, logpath):
    t = PotSSHFactory(logpath + "/logins.log", "ssh")
    reactor.listenTCP(lport, t)
    reactor.run()

def start_telnet(lport, logpath):
    t = PotTelnetFactory(logpath + "/logins.log", "telnet")
    reactor.listenTCP(lport, t)
    reactor.run()

def start_ftp(lport, logpath):
    t = PotFTPFactory(logpath + "/logins.log", "ftp")
    reactor.listenTCP(lport, t)
    reactor.run()

if __name__ == "__main__":
    print("----HoneyPot Builder----")

    while 1:
        print("\nAvailable services")
        print("1. SSH")
        print("2. FTP")
        print("3. Telnet")
        
        try:
            serv_op = int(input("Select service:")[0])
        except ValueError:
            print("ERROR: Non integer option")
        else:
            if (serv_op < 1) or (serv_op > 3):
                print("Incorrect option. Exiting...")
                exit(1)
            
        try:
            listen_port = int(input("Enter listening port:"))
        except ValueError:
            print("ERROR: Non integer value")

        logging_path = input("Enter path for logging:")

        pid = os.fork()

        if (pid == 0):
            if serv_op == 1:
                start_ssh(listen_port, logging_path)
            if serv_op == 2:
                start_ftp(listen_port, logging_path)
            if serv_op == 3:
                start_telnet(listen_port, logging_path)
            exit(0)
        else:
            print(f"Honeypot listening on port {listen_port}. PID: {pid}")
