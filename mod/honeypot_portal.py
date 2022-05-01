from sshpot2 import PotSSHFactory
from twisted.internet import reactor

def start_ssh(lport, logpath):
    t = PotSSHFactory(logpath + "/ssh.log")
    reactor.listenTCP(lport, t)
    reactor.run()

if __name__ == "__main__":
    print("----HoneyPot Builder----")
    print("Available services")
    print("1. SSH")
    print("2. FTP (Under construction)")
    print("3. Telnet (Under construction)")
    
    try:
        serv_op = int(input("Select service:")[0])
    except ValueError:
        print("ERROR: Non integer option")
    else:
        if (serv_op < 1) and (serv_op > 3):
            print("ERROR: Incorrect option")
            exit(1)

    try:
        listen_port = int(input("Enter listening port:"))
    except ValueError:
        print("ERROR: Non integer value")

    logging_path = input("Enter path for logging:")

    if serv_op == 1:
        start_ssh(listen_port, logging_path)
