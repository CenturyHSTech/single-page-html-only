# Single Page - HTML Only

Students will create a single webpage on a topic of your choice with headers, paragraphs, text formatting, links, and text formatting.
---

<details>
<summary><strong>Project Overview</strong></summary>

Students will code an HTML page (`index.html`) and use markup to structure a page on a topic of your choice.

The page should have a minimum of 3 sections each with a section header, paragraphs, links, and lists. In one or more of the sections, the student needs to create at least two different lists each with at least 3 list items.

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

### HTML Requirements
A single HTML file with:
- All standard HTML5 tags (`DOCTYPE`, `html`, `head`, `title`, `body`)
- An `h1` tag for your title (there can be only one `h1` tag per page)
- At least 3 `h2` tags for your section headers (subtitles)
- A minimum of 6 `p` tags (2 for each section)
- At least 2 lists (`ul` or `ol`) with at least 3 list items per list
- At least 3 links to external websites
- A variety of text formatting tags such as `strong`, `em`, `code`, `cite`
    * for bold and italic text, be sure to pick good keywords to emphasize.
    * a proficient score will include at least 4 examples of these tags beign properly used.

### Validity Requirements
- No HTML errors (validated via W3C tools)

### CSS Requirements
- No style attributes are allowed
- Either use a `style` tag in the head or link to an external stylesheet
- Apply colors (text and background color) to the entire page (use the `body` selector)
- Choose colors from a consistent color palette (I recommend getting one from [Coolors.co Trending Palettes](https://coolors.co/palettes/trending))
- Make sure any hyperlink is readable
- Make sure your colors pass the [webAIM Color Contrast Checker](https://webaim.org/resources/contrastchecker/) at a AAA level for Normal text
    * **NOTE**: your `h1` tag could fail for normal as long as it passes for Large text

</details>

---

<details>
<summary><strong>Submission Requirements</strong></summary>

- All changes must be committed and pushed to the repository
- Take one or more screen shots of your web page and upload them as files 
- I will be looking at your content as well.
</details>

---
