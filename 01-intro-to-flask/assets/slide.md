---
theme : "night"
transition: "slide"
highlightTheme: "monokai"
slideNumber: false
title: "P4L1 - Intro to Flask"
verticalSeparator: 'xxx'
presentation:
    width: 1500
    height: 1000

---

## Introduction to Flask

![flask-1](./flask-1.png)

---

#### The backend we built in Phase 3

![learn-backend-javascript](./learn-backend-java-script-9-638.webp)

With our custom-made ORM, we built the above, except instead of a Web Server, we scripted a CLI application to interact with our ORM.

---

##### Our goal: Full-Stack Applications!

![full-stack](./full-stack.jpg)

We still need something like `json-server` which can bridge the gap between front and back end and complete the **Request-Response Cycle**

---

#### We need some WSGI in our Flask 🍹

![communication-2](./communication-2.jpg)

The **Web Server Gateway Interface** provided by **Werkzeug** will be able to handle the HTTP traffic to our web server.

---

<section data-background-color="mistyrose">
    <img src="./static-dynamic-resources.png"/>
    <p>Although our server app will focus on requests for dynamic resources--database records--our app could also route requests for static resources, such as images, to an entirely different server.</p>
</section>

---

![flask-slide](./flask-slide-ppt.png)

#### Let's code! {.fragment}