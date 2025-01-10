---
theme : "night"
transition: "slide"
highlightTheme: "monokai"
slideNumber: false
title: "P4L2 - REST APIs with Flask (Part 1)"
verticalSeparator: 'xxx'
presentation:
    width: 1500
    height: 1000

---

## Authentication with Flask

![flask-1](./flask-1.png)

---

## Learning Objectives
* Understnd the Importance of Authentication in Web Apps
* Be able to differentiate between Identity Management (Authentication) and Access Management (Authorization)
* Identify Cookies and Sessions, and their relationship in the context of Authentication
* See how to implement Token-Based Authentication (Identity Management) Using Cookies and Sessions

---

### Authentication vs Authorization

![office-auth-not-same](./office-auth-not-same.png)

---

### Identity and Access Management

![IM-AM-diff](./IM-AM-diff.png)

---

### The Club Analogy

![wristband](./wristband.jpg)

---

## The Stateless Protocol

![FB-login](./fb-login.webp)

[Singh M., Cookie+Session (Medium)](https://medium.com/@maheshlsingh8412/cookie-session-story-of-a-stateless-http-3cd09cc01541)

---

![no-state](./no-state-no-identity.webp)

Since HTTP is stateless, it does not know who you are. It does not know if you are the same person who logged in 5 minutes ago or if you are a new user. 

---

##### Enter Cookies

![cookies-user-data](./cookies-user-data.png)

---

![set-cookie](./set-cookie.webp)

##### Cookies allow us to make the HTTP request-response protocol stateful

![req-cookie](./req-cookie.webp)

---

### Contents of a Cookie

![Website-Cookies](./Website-cookies-imaging-with-description.jpg)

---

##### Uses of Cookies

![EL_Cookies](./EL_Cookies_infographic.png)

###### Let's code! 💻 {.fragment}

---

### Secure the Cookies 🔒 with Sessions

![diagram-Web-Sessions](./diagram-Web-Sessions.webp)



