
# Single Page - HTML Only

Students will create a single webpage on ___.
---

<details>
<summary><strong>Project Overview</strong></summary>

Students will code an HTML page (`index.html`) and use markup to structure a page on ___.

The page should have a minimum of 3 sections each with a section header, paragraphs, and images. In one or more of the sections, the student needs to create at least two different lists each with at least 3 list items.

</details>

---
<details>
<summary><strong>VS Code Setup Instructions</strong></summary>

1. Make sure you have python poetry installed (open the Software Center and look for it in apps)
2. Open Command prompt by clicking in the search window and typing `cmd`
3. Type `poetry --version` - if it gave you a version, you are ready. If not, get the teacher to show you.
4. Make sure you add the Python Extension (the one with the Microsoft seal)
5. Open the terminal (View > New Terminal)
6. Run `poetry env activate` in the terminal
7. Note your virtual environment name
8. Open the Command Palette (`Ctrl + Shift + P`)
9. Select the Python interpreter (look for the Poetry environment)
10. Run `poetry update`
11. Run `pytest` to test your code - it will give you an error (that's to be expected)
12. Create a file named `index.html` into the `project` folder
13. Follow in class instructions on how to code your html file.
14. Review the [Project Requirements](project-requirements) for the assignment
15. Commit and push changes regularly
16. As you work, try typing `pytest` in the terminal to see what tests you are passing and which ones you are failing
17. If you don't know what a failed test means, talk to your teacher to help you work through it.
18. To get a 3/4 proficient in HTML, you need to pass all `test_html.py` tests.
19. To get a 4/4 exceeds, you need to pass all tests (`test_html.py` and `test_html_exceeds.py`).
20. Make sure you push all commits to receive a score.

</details>

---

<details>
<summary><strong>Project Requirements</strong></summary>

### Folder and File Structure
- Create a single web page named `index.html`
- Create a folder titled `images` (all lowercase)
- Include at least 3 images using meaningful names and no spaces.

### HTML Requirements
A single HTML file with:
- All standard HTML5 tags (`DOCTYPE`, `html`, `head`, `title`, `body`)
- An `h1` tag for your title (there can be only one `h1` tag per page)
- At least 3 `h2` tags for your section headers (subtitles)
- A minimum of 6 `p` tags (2 for each section)
- At least 2 lists (`ul` or `ol`) with at least 3 list items per list
- At least 3 links to external websites (you can do this in your credits for the images as well as citations for your content)
- At least 3 vocabulary terms in bold (`b` or `strong`)
    - NOTE: do not make any headings bold (they already are bold)
    - You will fail tests if you put a `b` or `strong` tag inside of a heading tag (`<h1>`, `<h2>`,...and so on>)
- At least 3 `figure` tags, each that includes:
    - A relatively small (no wider than 400px) image with an `alt` text
    - A `figcaption` with a `cite` tag for image credit (linked if not self-taken)

### Validity Requirements
- No HTML errors (validated via W3C tools)

</details>

---

<details>
<summary><strong>Submission Requirements</strong></summary>

- All changes must be committed and pushed to the repository
- Take one or more screen shots of your web page and upload them as files 
- I will be looking at your content as well.
</details>

---
