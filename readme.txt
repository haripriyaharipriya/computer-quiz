COMPUTER QUIZ WEBSITE
======================

Website links
-------------
- Public website: https://mrna-screenshot-net-steady.trycloudflare.com/
- Public QR code: [Open QR code image](quiz-website-qr.png)

	![Quiz website QR code](quiz-website-qr.png)
- User login: [Open quiz website](user%20login.html)
- Admin dashboard: [Open admin dashboard](admin.html)
- Quiz questions: [Open quiz questions](question.html)

Admin login details
-------------------
- Username: admin
- Password: Admin@123

Participant login details
-------------------------
- TEAM1 / team01
- TEAM2 / team02
- TEAM3 / team03
- TEAM4 / team04
- TEAM5 / team05
- TEAM6 / team06
- TEAM7 / team07
- TEAM8 / team08
- TEAM9 / team09
- TEAM10 / team10
- TEAM11 / team11
- TEAM12 / team12
- TEAM13 / team13
- TEAM14 / team14
- TEAM15 / team15
- TEAM16 / team16
- TEAM17 / team17
- TEAM18 / team18
- TEAM19 / team19
- TEAM20 / team20
- TEAM21 / team21
- TEAM22 / team22
- TEAM23 / team23
- TEAM24 / team24
- TEAM25 / team25
- TEAM26 / team26
- TEAM27 / team27
- TEAM28 / team28
- TEAM29 / team29
- TEAM30 / team30

How to use
----------
1. Open user login.html in a web browser.
2. Enter a participant username and password to take the quiz.
3. Use the admin username and password with either Login button to view results.
4. The public link and QR code work across different networks while the local server and Cloudflare tunnel are running.
5. The public tunnel URL is temporary. Start the server, run `cloudflared tunnel --url http://localhost:8000`, then regenerate the QR code with `python generate_qr.py https://YOUR-CURRENT-TUNNEL.trycloudflare.com/`. Update the public link above when the URL changes. Use GitHub Pages, Netlify, or Vercel for permanent hosting.
6. Start the shared results server with `python server.py` before participants take the quiz.

Note: This is a browser-based demo. Login credentials are stored in the HTML file, so do not use real passwords.
Usernames are not case-sensitive; passwords must be entered exactly as shown.

