#Code 

# Crowd

Crowd is the final event hosting app you will ever need, making event creation , registration, and event payment easier then ever before. 

---
## Installation

Make sure you have [xcode](https://developer.apple.com/xcode/) setup, [watcman](https://facebook.github.io/watchman/), and [npm](https://nodejs.org/en/learn/getting-started/an-introduction-to-the-npm-package-manager#packages)

Navigate to  `backend` and setup your `.env` as such: 
```bash
PORT=3000
MONGODB_URI=""
STRIPE_SK=""
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
SENDGRID_KEY=""
```

next make sure to run `npm i` in the backend and frontend to install any dependencies. 

the in the `backend` run `npm run start` and in the frontend (With the simulator of your choice running in Xcode) run `npx expo prebuild` then `npx expo run:ios`

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)