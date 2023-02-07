#### Exercise

1. Javascript Injection.

---

From the testing in class, I come up with this idea.

```const loginForm = document.getElementById("loginForm");
loginForm.addEventListener("submit", function(e) {
    e.preventDefault();
    const username = document.getElementById("username");
    const password = document.getElementsByName("password")[0];
    alert("username:"+username?.value+"\npassword:"+password?.value);
});
```

2. ncat

---

After using code in documentation, I come with this result
![table](./image/hack.jpg)

3. essay

---

a) From what I have learned in the class, the worst scenario that I cam imagine from the activity is someone get my password as well as username in a website that I log in. By using Javascript Injection, anyone who has knowledge even little can use javascript and get what he wants. From the code that I use, I set the 'submit' event so that I can push or send the action to my server or website.

b) If I want to use netcat to make a trojan horse, I will create a link or something that scam users to get sth. When user click on it, it will run a command that will give permission in cmd along with item that you want. In the end, this will become trojan horse scenario. In a user perspective, I suggest you should now download or click on any links that doesn't get authorization or protection from sth or else you fuck up.
