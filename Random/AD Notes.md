#security 

# Terminology: 
- Domain Controller: Server that runs the Active Directory Service 
- Active Directory Domain Service: Contains all objects (all information basically)
	- Users: One of many security principles, can be assigned privileges over resources 
		- Has two type of entities: 
			- People 
			- Services 
	- Machines: Also considered security principle 
		- Usually local administers on the computer itself 
		-  The machine account name is the computer's name followed by a dollar sign, ex: DC01$
	- Security Groups: user groups to assign access rights to files or other resources to entire groups instead of single users
		- ![[Screenshot 2024-10-31 at 9.36.46 PM.png]]
- Organizational Units: container objects that allow you to classify users and machines.
- Group Policy Objects: a collection of settings that can be applied to OUs
- Trees: integrating multiple domains so that you can partition your network into units that can be managed independently
- Forest: The union of several trees with different namespaces into the same network
- Trust Relationship: having a trust relationship between domains allows you to authorize a user from domain `THM UK` to access resources from domain `MHT EU`

---
# OU's vs Security groups: 

- **OUs** are handy for **applying policies** to users and computers, which include specific configurations that pertain to sets of users depending on their particular role in the enterprise. Remember, a user can only be a member of a single OU at a time, as it wouldn't make sense to try to apply two different sets of policies to a single user.
- **Security Groups**, on the other hand, are used to **grant permissions over resources**. For example, you will use groups if you want to allow some users to access a shared folder or network printer. A user can be a part of many groups, which is needed to grant access to multiple resources.
  
---
# Network protocols: 

Two protocols can be used for network authentication in windows domains:
- **Kerberos:** Used by any recent version of Windows. This is the default protocol in any recent domain.
	- Users who log into a service using Kerberos will be assigned tickets. Think of tickets as proof of a previous authentication
	- read more about how this works on [task 7](https://tryhackme.com/r/room/winadbasics)
	- 
- **NetNTLM:** Legacy authentication protocol kept for compatibility purposes.
