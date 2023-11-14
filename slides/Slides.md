---
marp: true
footer: 'James Gress - https://jamesgress.com'
paginate: true
theme: custom-default
transition: glow
---

# GitHub Copilot Training
![bg right:40%](./img/jamesgress.png)

---

![bg left:40%](./img/jamesgress.png)

# James Gress
## Director Emerging Technologies<br>Generative AI<br>Accenture

<i class="fa-brands fa-x-twitter"></i> [@jmgress](https://twitter.com/jmgress)
<i class="fa-brands fa-linkedin"></i> [James Gress](https://linkedin.com/in/jamesgress/)
<i class="fa fa-window-maximize"></i> [https://jamesgress\.com/](https://jamesgress.com/)
<i class="fa-brands fa-github"></i> [jmgress](https://github.com/jmgress)
<i class="fa-brands fa-meetup"></i> [Generative AI](https://www.meetup.com/tampa-bay-generative-ai-meetup/)

---

<!-- Speaker Notes -->
## Content

- What is GitHub Copilot
- Bennifits to using GitHub Copilot
- How to use GitHub Copilot
- Microsoft Training
<!-- Can have multiple on a slide -->

---

## GitHub Copilot Code Assist
<!-- Can also do a multiline
comment that will show in notes -->

---

![bg color](black)
<div class="video-wrapper">
  <video controls autoplay loop muted style="width:95%;">
    <source src="./img/copilot_create_code.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

---

## GitHub Copilot Commit Message - Example 1
<!-- Can also do a multiline
comment that will show in notes -->

---
![bg color](black)
<div class="video-wrapper">
  <video controls autoplay loop muted style="width:95%;">
    <source src="./img/copilot_commit_message.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

---

## GitHub Copilot Commit Message - Example 2
<!-- Can also do a multiline
comment that will show in notes -->

---
![bg color](black)
<div class="video-wrapper">
  <video controls autoplay loop muted style="width:70%;">
    <source src="./img/copilot_commit_message2.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

---

## Slide 3

> This is a quote.

---

![bg fit](./img/git.drawio.svg)

---

![bg opacity](https://picsum.photos/800/600?image=53)
## Slide 5

<div class="columns">
<div>

## Left

- 1
- 2

</div>
<div>

## Right

- 3
- 4

</div>
</div>


---

# <!--fit--> In Progress

---

<!-- Needed for mermaid, can be anywhere in file except frontmatter -->
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

# Mermaid

<div class="mermaid">
gitGraph
    commit
    commit
    branch develop
    checkout develop
    commit
    commit
    checkout main
    merge develop
    commit
    commit
</div>
