# Week 2

## Notes



## Quiz

### Question 1

Semantics is

**Answer:**

- [x] the practice of giving content on the page meaning and structure by using proper element
- [ ] the set of rules that defines the combinations of symbols that are considered to be a correctly structured document or fragment in that language
- [ ] circular

### Question 2

Semantic code describes the \_\_\_ of content on a page, regardless of the style or appearance of that content.

**Answer:**

- [ ] number
- [x] value
- [ ] language

### Question 3

Using the header and footer tags can improve the search engine optimization for your page.

**Answer:**

- [x] True
- [ ] False

### Question 4

Every well-formed HTML document should include:

**Answer:**

- [x] doctype, head, body
- [ ] doctype, header, body
- [ ] header, nav, footer
- [ ] alt text

### Question 5

What is wrong with the following code?

```html
<a href = "http://www.umich.edu"></a>
```

**Answer:**

- [ ] The alt text attribute is missing from the tag.
- [ ] The anchor link is self-closing.  Remove the `</a>` and the code will work.
- [ ] This code is semantically and syntactically correct.
- [x] This link doesn't provide any way to click on the link.

### Question 6

Block-level elements begin on a new line

**Answer:**

- [x] True
- [ ] False

### Question 7

Inline-level elements begin on a new line

**Answer:**

- [ ] True
- [x] False

### Question 8

A `<div>` block is an inline-level element

**Answer:**

- [ ] True
- [x] False

### Question 9

A `<span>` block is an inline-level element

**Answer:**

- [x] True
- [ ] False

### Question 10

Which tag represents a line break (new line)?

**Answer:**

- [ ] `<line>`
- [ ] `<lb>`
- [ ] `<break>`
- [x] `<br>`

### Question 11

Which of the following is the correct way to comment on HTML5?

**Answer:**

- [ ] `<?-- HTML -->`
- [ ] `<#-- HTML -->`
- [x] `<!-- HTML -->`
- [ ] `<$-- HTML -->`

### Question 12

Which of the following are valid tags for  HTML5 headings?

**Answer:**

- [x] `<h5>..</h5>`
- [ ] `<h7>..</h7>`
- [ ] `<h9>..</h9>`
- [ ] `<heading>..</heading>`

### Question 13

All of the content you wish to appear on the screen should be in which tag?

**Answer:**

- [ ] `<html>`
- [x] `<body>`
- [ ] `<content>`
- [ ] `<main>`

### Question 14

Which tag is used to create a link?

**Answer:**

- [ ] `<hyper>`
- [ ] `<anchor>`
- [x] `<a>`
- [ ] `<link>`

### Question 15

Which of the following code is the correct way to link to an email address?

**Answer:**

- [ ] `<a href= "shayhowe@awesome.com?subject=Hi&body=How are you">Email</a>`
- [x] `<a href= "shayhowe@awesome.com?subject=Hi&body=How%20are%20you">Email</a>`
- [ ] `<a href= "shayhowe@awesome.com?subject=Hi&body=How%are%you">Email</a>`
- [ ] `<a href= "shayhowe@awesome.com?subject=Hi&body=How%20are%20you">Email<a>`

### Question 16

Which HTML element is used to define list items?

**Answer:**

- [x] `<li>`
- [ ] `<dl>`
- [ ] `<item>`
- [ ] `<ul>`

### Question 17

The start attribute defines the number from which an unordered list should start.

**Answer:**

- [ ] True
- [x] False

### Question 18

The reverse attribute allows a list to appear in a reverse order in an unordered list.

**Answer:**

- [ ] True
- [x] False

### Question 19

Which attribute can be used to change its number within an ordered list?

**Answer:**

- [ ] num
- [ ] skip
- [ ] change
- [x] value

### Question 20

Which code properly creates the nested list structure shown here?

```
1. Vegetables
2. Fruit
  ·Blueberries
  ·Bananas
```

Notice that the blueberries and bananas are part of the fruit component.

**Answer:**

```html
<ol>		
    <li>Vegetables</li>	
    <li>Fruit
       <ul>				
          <li>Blueberries</li>
	  <li>Bananas</li>
       </ul>
    </li>
</ol>
```

### Question 21

The `<ul>` and `<o>` elements may contain only `<li>` elements.

**Answer:**

- [x] True
- [ ] False

### Question 22

The tags to create definitions are:

**Answer:**

- [ ] `<def>`, `<dt>`, `<dd>`
- [ ] `<def>`, `<dt>`, `<li>`
- [ ] `<dl>`, `<term>`, `<def>`
- [x] `<dl>`, `<dt>`, `<dd>`

### Question 23

What should `target = "_blank"` do when included in a link tag?

**Answer:**

- [x] Opens the link in a new tab or window
- [ ] Opens the link in a in a tab called `"_blank"`
- [ ] This is not a valid expression.

### Question 24

In order for the `<img>` element to work, a src attribute and value must be included to specify the source of the image.

**Answer:**

- [x] True
- [ ] False

### Question 25

The alt text of an image should describe the appearance of an image

**Answer:**

- [ ] True
- [x] False

### Question 26

When should an image have null (empty) alt text (alt - "") 

**Answer:**

- [ ] When the image is black and white
- [ ] When the image is complex
- [x] When the image is decorative
- [ ] When the image already displays descriptive text

### Question 27

Which of the following is the best way to use a Font Awesome icon to link to Twitter?

**Answer:**

- [x] `<a href="https://twitter.com/" aria-label="Twitter">  <i class="fa fa-twitter"></i></a>`
- [ ] `<a> <i class="fa fa-twitter"></i></a>`
- [ ] `<a href="https://twitter.com/" >  <i class="fa fa-twitter" aria-label="Twitter"></i></a>`
- [ ] `<a href="https://twitter.com/">  <i class="fa fa-twitter"></i></a>`

### Question 28

What are the elements to help organize the data and structure of a table?

**Answer:**

- [ ] `<caption>`, `<head>`, `<body>`, `<foot>`
- [ ] `<caption>`, `<thead>`, `<tbody>`, `<foot>`
- [x] `<caption>`, `<thead>`, `<tbody>`, `<tfoot>`
- [ ] `<caption>`, `<thead>`, `<body>`, `<foot>`

### Question 29

What does `<thead>` stand for?

**Answer:**

- [ ] The head
- [x] Table head
- [ ] Table header
- [ ] None of the above

### Question 30

Which code will properly insert headings along each row?

**Answer:**

```html
<table>
  <tr><th>Name</th><td>Colleen</td></tr>
  <tr><th>Age</th><td>26</td></tr>
  <tr><th>Team</th><td>Browns</td></tr>
</table>
```