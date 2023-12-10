---
marp: true
footer: 'James Gress - https://jamesgress.com'
paginate: true
theme: custom-default
transition: glow
---

# GitHub Copilot Training
![bg fit right:40%](./img/ghcp.jpg)

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

- Generative AI
- What is GitHub Copilot
- Bennifits to using GitHub Copilot
- Frequently Asked Questions
- How to use GitHub Copilot
- Microsoft Training

<!-- Can have multiple on a slide -->

---

# Generative AI

Why now?  Generative AI and AI has been around for years and even decades!
<!-- It is at a point where it has sigificanly reduced the barrier to entry

It benifits beginners to experienced

At this point it can't be ignored, as it has the potential to radically change an orginizations landscape -->

---

# Why Generative AI

10% Initial Effort -> 80% Toil Reduction -> 10% Validating and Refining

---

# Generative AI Frequently Asked Questions

Potential to Generate IP Infringement

Ability to Copyright AI Generated Code

Legal and Government Regulations

Accuracy and Hallucinations 

<!-- Recently had a 1 year anniverisary on the launch of ChatGPT

Might bring up Scale -->

---

# Measuging ROI

---

# Reducing Mondain Tasks

Many professional developers only get to spend about 2 hours a day developing, the rest of the time is spent on mondain tasks.

---

# Data Security

GitHub Copilot for Business does not access the source code in your editor other than to generate a suggestion, and prompts used to generate a suggestion are transmitted to the model securely. Once a suggestion is generated, your prompts are not retained.

---

# Responsible AI

---


# Generative AI and AI Assisted Coding

Will change the way we do software

<!-- It is at a point where it has sigificanly reduced the barrier to entry

It benifits beginners to experienced

At this point it can't be ignored, as it has the potential to radically change an orginizations landscape -->


---

## GitHub Copilot Basics - Code Assist
<!-- Notes -->

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
# Microsoft Training
[Microsoft Copilot Training](https://learn.microsoft.com/en-us/training/paths/copilot/)

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
