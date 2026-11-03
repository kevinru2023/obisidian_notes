# CTF Write-Up

### Platform: DICEctf 
### Challenge: cookie-recipes-v3

Description: Mmmmmmm...

---

### Initial Steps 

First lets go ahead and take a look at the website to understand what we are working with, here is a picture of the website: ![[CleanShot 2025-03-28 at 20.54.43@2x.png]]
Pressing the buttons does exactly as it says, and when we click deliver we get this message: ![[CleanShot 2025-03-28 at 20.55.10@2x.png]]

Okay now we have a goal in mind so lets go ahead and take a look at the code now since they were nice enough to give us the source! 

--- 
### Code 
```javascript
const express = require('express')

const app = express()

const cookies = new Map()

app.use((req, res, next) => {
    const cookies = req.headers.cookie
    const user = cookies?.split('=')?.[1]

    if (user) { req.user = user }
    else {
        const id = Math.random().toString(36).slice(2)
        res.setHeader('set-cookie', `user=${id}`)
        req.user = id
    }

    next()
})

app.get('/', (req, res) => {
    const count = cookies.get(req.user) ?? 0
    res.type('html').send(`
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@exampledev/new.css@1/new.min.css">
        <link rel="stylesheet" href="https://fonts.xz.style/serve/inter.css">
        <div>You have <span>${count}</span> cookies</div>
        <button id="basic">Basic cookie recipe (makes one)</button>
        <br>
        <button id="advanced">Advanced cookie recipe (makes a dozen)</button>
        <br>
        <button disabled>Super cookie recipe (makes a million)</button>
        <br>
        <button id="deliver">Deliver cookies</button>
        <script src="/script.js"></script>
    `)
})

app.get('/script.js', (_req, res) => {
    res.type('js').send(`
        const basic = document.querySelector('#basic')
        const advanced = document.querySelector('#advanced')
        const deliver = document.querySelector('#deliver')

        const showCookies = (number) => {
            const span = document.querySelector('span')
            span.textContent = number
        }

        basic.addEventListener('click', async () => {
            const res = await fetch('/bake?number=1', { method: 'POST' })
            const number = await res.text()
            showCookies(+number)
        })

        advanced.addEventListener('click', async () => {
            const res = await fetch('/bake?number=12', { method: 'POST' })
            const number = await res.text()
            showCookies(+number)
        })


        deliver.addEventListener('click', async () => {
            const res = await fetch('/deliver', { method: 'POST' })
            const text = await res.text()
            alert(text)
        })
    `)
})

app.post('/bake', (req, res) => {
    const number = req.query.number
    if (!number) {
        res.end('missing number')
    } else if (number.length <= 2) {
        cookies.set(req.user, (cookies.get(req.user) ?? 0) + Number(number))
        res.end(cookies.get(req.user).toString())
    } else {
        res.end('that is too many cookies')
    }
})

app.post('/deliver', (req, res) => {
    const current = cookies.get(req.user) ?? 0
    const target = 1_000_000_000
    if (current < target) {
        res.end(`not enough (need ${target - current}) more`)
    } else {
        res.end(process.env.FLAG)
    }
})

app.listen(3000)
```

some things that pop out immediately are the fact that the number length is limited to 2! At first I tried to underflow but apparently javascript doesn't work that way so then I realized something else, there is no type validation! 

---
### Exploit 

Knowing what we know let's go ahead and open up the developer console and change the request to be some letters instead and see what happens!  ![[CleanShot 2025-03-28 at 20.59.41@2x.png]]

And then after clicking the Deliver cookies button looks like we are given the flag, we were right, the type validation broke the program and gave us the flag! nice little easy web challenge! ![[CleanShot 2025-03-28 at 21.00.27@2x.png]]
