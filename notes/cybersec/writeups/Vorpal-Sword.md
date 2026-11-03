# CTF Write-Up

### Platform: DiceCTF
### Challenge:  Vorpal sword 

Description: Choose your own adventure!

---

### Initial Steps: 

This is a crypto challenge and we are handed the code that a server runs on, the challenge was to get the flag by finding the vulnerability in the program (duh). I did not manage to get this on my own time, but I believe I understand how oblivious transfer and the solution enough to make a write up about it. The server is written in python, here is the code uncommented and handed as is: 

```python 
#!/usr/local/bin/python

import secrets
from Crypto.PublicKey import RSA

DEATH_CAUSES = [
	'a fever',
	'dysentery',
	'measles',
	'cholera',
	'typhoid',
	'exhaustion',
	'a snakebite',
	'a broken leg',
	'a broken arm',
	'drowning',
]

def run_ot(key, msg0, msg1):
	'''
	https://en.wikipedia.org/wiki/Oblivious_transfer#1–2_oblivious_transfer
	'''
	x0 = secrets.randbelow(key.n)
	x1 = secrets.randbelow(key.n)
	print(f'n: {key.n}')
	print(f'e: {key.e}')
	print(f'x0: {x0}')
	print(f'x1: {x1}')
	v = int(input('v: '))
	assert 0 <= v < key.n, 'invalid value'
	k0 = pow(v - x0, key.d, key.n)
	k1 = pow(v - x1, key.d, key.n)
	m0 = int.from_bytes(msg0.encode(), 'big')
	m1 = int.from_bytes(msg1.encode(), 'big')
	c0 = (m0 + k0) % key.n
	c1 = (m1 + k1) % key.n
	print(f'c0: {c0}')
	print(f'c1: {c1}')

if __name__ == '__main__':
	with open('flag.txt') as f:
		flag = f.read().strip()

	print('=== CHOOSE YOUR OWN ADVENTURE: Vorpal Sword Edition ===')
	print('you enter a cave.')

	for _ in range(64):
		print('the tunnel forks ahead. do you take the left or right path?')
		key = RSA.generate(1024)
		msgs = [None, None]
		page = secrets.randbits(32)
		live = f'you continue walking. turn to page {page}.'
		die = f'you die of {secrets.choice(DEATH_CAUSES)}.'
		msgs = (live, die) if secrets.randbits(1) else (die, live)
		run_ot(key, *msgs)
		page_guess = int(input('turn to page: '))
		if page_guess != page:
			exit()

	print(f'you find a chest containing {flag}')
```

So looks very confusing let's break it down using the provided wikipedia link in the file [https://en.wikipedia.org/wiki/Oblivious_transfer#1–2_oblivious_transfer](https://en.wikipedia.org/wiki/Oblivious_transfer#1–2_oblivious_transfer). 

--- 
### Understanding the crypto algorithm: 

So looking at the wikipedia article it looks like this program implements oblivious transfer, specifically $\frac{1}{2}$ oblivious transfer. What is oblivious transfer (OT) anyways? I will be borrowing a lot from the wikipedia article as I believe it explains it fairly well, Let's dive in!

So let's start off with what is OT and it's purpose? 
> [!quote] Wikipedia Definition
> *" OT is a type of protocol in which a sender transfers one of potentially many pieces of information to a receiver, but remains [oblivious](https://en.wiktionary.org/wiki/oblivious "wikt:oblivious") as to what piece (if any) has been transferred."*

Okay neat definition but very vague definition, basically what OT is
- is a way for two people two send information with the sender only wanting the **receiver to receive one message**. 
-  **receiver should only be able to learn 1 of n messages sent** (which in this case is $1$ of $2$ messages).
-  want the **sender to not know which option the receiver chose**, hence the term Oblivious Transfer, as both parties are Oblivious to the information the other user has/selected. 

Let's see how this transaction works, we will be using RSA as it is also used in the server code. Here is a figure illustrating the transaction. 



 