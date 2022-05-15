* Cowrie is a SSH/Telnet honeypot designed to log brute force attacks and shell commands. Two interaction modes:
	* Medium: Emulates UNIX in python, builds fake files/file content, saves any downloaded file
	* High: Acts as a proxy (Never explored)
* Cowrie honeypots are installed as docker images and all commands and executed via docker (start, stop, restart, inspect etc.)
* Docker containers created are started by default whenever system restarts
* Example docker commad to create a cowrie instances for particular ports:
	docker run --name cowrie --restart always -d -p 2218-2227:2218-2227 cowrie/cowrie:latest
* Once it's running, cowrie can be tested with the usual SSH, Telnet commands (remember listening ports), nmap scans.
* 2 cowrie docker instances running on the VM, with the following docker names:
	* cowrie: SSH and Telnet honeypots running against 10 different ports. 
		* SSH: 2218 - 2222
		* Telnet: 2223 - 2227
	* cowrie2: SSH honeypot running on port 2230 with SSH banner modified
* Cowrie instance can be configured using cowrie.cfg file, path can be obtained with the command *docker inspect cowrie*, and viewing the volume location for the given docker image.
* Interesting SSH characteristics in our control (Some of these are just for display purposes):
	* hostname
	* interactive timeout
	* authentication timeout
	* timezone
	* prompt format (Default something like root@svr03:~#, can be changed to "shell>")
	* fake address
	* enabling NAT/Public IP
	* username, password prompt
	* Architecture
	* Kernel version
	* Kernel build
	* Hardware platform
	* Operating system
	* SSH Version Banner
	* Cipher encryption algorithm used
	* MAC algorithm
	* Compression method used
* Cowrie logs are located in /var/lib/docker/volumes/<volume ID>/_data/log/cowrie
* Cowrie system diagrams
	* Commands: Based on the scripts in https://github.com/cowrie/cowrie/tree/master/src/cowrie/commands: https://docs.google.com/drawings/d/1FP0cOMoGinQh2t0wHKm1keu1jUVNipNJSmsbjDOL_rQ
	* Different modules in Cowrie Shell https://github.com/cowrie/cowrie/tree/master/src/cowrie/shell: https://docs.google.com/drawings/d/17Sp4MpXyPjMynRY8l2l-5rPZNAmIdes3wi_nOfa1FEA/edit
* Cowrie characteristics: https://docs.google.com/presentation/d/1rn_a1P-sCo8TbIoBkEQOQRsvxOikWfpth7kSukU6INY/edit#slide=id.p

