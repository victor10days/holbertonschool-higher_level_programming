# JavaScript DOM Manipulation - Complete Tutorial

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Project Setup](#project-setup)
4. [Core Concepts](#core-concepts)
5. [Task-by-Task Tutorial](#task-by-task-tutorial)
6. [Testing Your Code](#testing-your-code)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)
9. [Additional Resources](#additional-resources)

## Introduction

This tutorial will guide you through JavaScript DOM manipulation, teaching you how to interact with HTML elements dynamically. DOM (Document Object Model) manipulation is fundamental to creating interactive web pages.

### Learning Objectives
By the end of this tutorial, you'll understand:
- How to select HTML elements using JavaScript
- Differences between ID, class, and tag selectors
- How to modify element styles and content
- How to handle user events
- How to make API requests using the Fetch API
- How to dynamically create and modify DOM elements

## Prerequisites

### Required Knowledge
- Basic HTML structure
- CSS fundamentals
- JavaScript basics (variables, functions, conditional statements)
- Understanding of web browsers and developer tools

### Tools Needed
- A modern web browser (Chrome 57+, Firefox, Safari, Edge)
- A text editor or IDE (VS Code, Sublime Text, Atom, etc.)
- Git for version control
- Access to browser developer tools

## Project Setup

### Step 1: Directory Structure
```
javascript-dom_manipulation/
├── README.md
├── 0-script.js
├── 1-script.js
├── 2-script.js
├── 3-script.js
├── 4-script.js
├── 5-script.js
├── 6-script.js
├── 7-script.js
└── 8-script.js
```

### Step 2: Create Project Directory
```bash
mkdir javascript-dom_manipulation
cd javascript-dom_manipulation
```

### Step 3: Initialize Git Repository
```bash
git init
```

## Core Concepts

### DOM (Document Object Model)
The DOM is a programming interface for HTML documents. It represents the structure of a document as a tree of objects that can be modified with JavaScript.

### Key DOM Methods
- `document.querySelector()` - Selects the first element matching a CSS selector
- `document.querySelectorAll()` - Selects all elements matching a CSS selector
- `element.addEventListener()` - Attaches event listeners to elements
- `element.textContent` - Gets or sets the text content of an element
- `element.style` - Accesses CSS styling properties
- `element.classList` - Provides methods to work with CSS classes

### Selector Types
1. **Tag Selector**: `'header'` - Selects by HTML tag
2. **ID Selector**: `'#my-id'` - Selects by ID attribute
3. **Class Selector**: `'.my-class'` - Selects by class attribute

## Task-by-Task Tutorial

### Task 0: Color Me

**Objective**: Change the text color of a header element to red.

#### HTML Structure (0-main.html)
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
```

#### Step-by-Step Solution

1. **Understanding the Task**
   - We need to select the `<header>` element
   - Change its text color to red (#FF0000)
   - Use `document.querySelector()`

2. **Code Implementation (0-script.js)**
```javascript
document.querySelector('header').style.color = '#FF0000';
```

3. **Code Explanation**
   - `document.querySelector('header')` - Finds the first `<header>` element
   - `.style.color` - Accesses the CSS color property
   - `'#FF0000'` - Sets the color to red using hexadecimal notation

4. **Testing**
   - Open 0-main.html in your browser
   - The header text should appear in red

### Task 1: Click and Turn Red

**Objective**: Change header color to red when clicking a specific element.

#### HTML Structure (1-main.html)
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
```

#### Step-by-Step Solution

1. **Understanding the Task**
   - Click on element with ID "red_header"
   - This should change the header text color to red
   - We need event handling

2. **Code Implementation (1-script.js)**
```javascript
document.querySelector('#red_header').addEventListener('click', function() {
  document.querySelector('header').style.color = '#FF0000';
});
```

3. **Code Explanation**
   - `document.querySelector('#red_header')` - Selects element with ID "red_header"
   - `.addEventListener('click', function() {...})` - Attaches a click event listener
   - Inside the function, we change the header color just like in Task 0

4. **Testing**
   - Open 1-main.html in your browser
   - Click on "Red header" text
   - The header should turn red

### Task 2: Add `.red` Class

**Objective**: Add a CSS class instead of directly modifying styles.

#### HTML Structure (2-main.html)
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
```

#### Step-by-Step Solution

1. **Understanding the Task**
   - Instead of setting style directly, add a CSS class
   - The CSS class `.red` is already defined in the HTML
   - Use `classList.add()` method

2. **Code Implementation (2-script.js)**
```javascript
document.querySelector('#red_header').addEventListener('click', function() {
  document.querySelector('header').classList.add('red');
});
```

3. **Code Explanation**
   - Similar event handling as Task 1
   - `.classList.add('red')` - Adds the "red" class to the element
   - This is preferred over direct style manipulation for maintainability

4. **Benefits of Using Classes**
   - Easier to maintain
   - Allows for complex styling
   - Better separation of concerns (CSS for styling, JS for behavior)

### Task 3: Toggle Classes

**Objective**: Toggle between two classes (red and green).

#### HTML Structure (3-main.html)
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
```

#### Step-by-Step Solution

1. **Understanding the Task**
   - Header starts with "green" class
   - Clicking should toggle between "red" and "green"
   - Never both classes at the same time, never empty

2. **Code Implementation (3-script.js)**
```javascript
document.querySelector('#toggle_header').addEventListener('click', function() {
  const header = document.querySelector('header');
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
```

3. **Code Explanation**
   - Store the header element in a variable for efficiency
   - Check if header has "red" class using `classList.contains()`
   - Remove current class and add the opposite class
   - This ensures only one class is applied at a time

4. **Alternative Implementation**
```javascript
// More concise version (but less explicit)
document.querySelector('#toggle_header').addEventListener('click', function() {
  const header = document.querySelector('header');
  header.classList.toggle('red');
  header.classList.toggle('green');
});
```

### Task 4: List of Elements

**Objective**: Dynamically add list items to an unordered list.

#### HTML Structure (4-main.html)
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
```

#### Step-by-Step Solution

1. **Understanding the Task**
   - Click "Add item" to add new `<li>` elements
   - New items should contain the text "Item"
   - Add to the `<ul>` with class "my_list"

2. **Code Implementation (4-script.js)**
```javascript
document.querySelector('#add_item').addEventListener('click', function() {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newItem);
});
```

3. **Code Explanation**
   - `document.createElement('li')` - Creates a new `<li>` element
   - `newItem.textContent = 'Item'` - Sets the text content
   - `appendChild(newItem)` - Adds the new element to the list

4. **DOM Manipulation Steps**
   - Create element
   - Configure element (text, attributes, etc.)
   - Insert element into DOM

### Task 5: Change the Text

**Objective**: Update the text content of an element.

#### HTML Structure (5-main.html)
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
```

#### Step-by-Step Solution

1. **Understanding the Task**
   - Click "Update the header" to change header text
   - New text should be "New Header!!!"

2. **Code Implementation (5-script.js)**
```javascript
document.querySelector('#update_header').addEventListener('click', function() {
  document.querySelector('header').textContent = 'New Header!!!';
});
```

3. **Code Explanation**
   - `.textContent` property gets or sets the text content
   - This replaces all existing text content

4. **textContent vs innerHTML**
   - `textContent` - Sets plain text (safer, no HTML parsing)
   - `innerHTML` - Sets HTML content (can execute scripts, security risk)

### Task 6: Star Wars Character

**Objective**: Fetch data from an API and display it.

#### HTML Structure (6-main.html)
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
```

#### Step-by-Step Solution

1. **Understanding the Task**
   - Fetch character data from Star Wars API
   - Display the character name in element with ID "character"
   - Use the Fetch API

2. **Code Implementation (6-script.js)**
```javascript
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    document.querySelector('#character').textContent = data.name;
  });
```

3. **Code Explanation**
   - `fetch()` - Makes an HTTP request and returns a Promise
   - `.then(response => response.json())` - Converts response to JSON
   - `.then(data => {...})` - Handles the JSON data
   - Access the `name` property from the API response

4. **Understanding Promises**
   - Promises handle asynchronous operations
   - `.then()` chains handle successful responses
   - Can add `.catch()` for error handling

5. **Enhanced Version with Error Handling**
```javascript
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    document.querySelector('#character').textContent = data.name;
  })
  .catch(error => {
    console.error('Error:', error);
    document.querySelector('#character').textContent = 'Error loading character';
  });
```

### Task 7: Star Wars Movies

**Objective**: Fetch multiple items and display them as a list.

#### HTML Structure (7-main.html)
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
```

#### Step-by-Step Solution

1. **Understanding the Task**
   - Fetch list of Star Wars movies
   - Create `<li>` elements for each movie title
   - Add them to the `<ul>` with ID "list_movies"

2. **Code Implementation (7-script.js)**
```javascript
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const moviesList = document.querySelector('#list_movies');
    data.results.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      moviesList.appendChild(listItem);
    });
  });
```

3. **Code Explanation**
   - Fetch movies from the films endpoint
   - `data.results` contains an array of movie objects
   - `.forEach()` iterates through each movie
   - Create `<li>` element for each movie
   - Set text content to movie title
   - Append to the movies list

4. **Array Methods**
   - `forEach()` - Executes function for each array element
   - Alternative: `for...of` loop or traditional for loop

### Task 8: Say Hello!

**Objective**: Handle script loading in the `<head>` section.

#### HTML Structure (8-main.html)
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="8-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
  </body>
</html>
```

#### Step-by-Step Solution

1. **Understanding the Task**
   - Script is loaded in `<head>` before DOM is ready
   - Fetch greeting from translation API
   - Display in element with ID "hello"
   - Need to wait for DOM to load

2. **Code Implementation (8-script.js)**
```javascript
document.addEventListener('DOMContentLoaded', function() {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.querySelector('#hello').textContent = data.hello;
    });
});
```

3. **Code Explanation**
   - `DOMContentLoaded` event fires when DOM is fully loaded
   - This ensures elements exist before we try to select them
   - Fetch translation for French language (`?lang=fr`)
   - Display the `hello` property from the response

4. **DOM Loading Events**
   - `DOMContentLoaded` - DOM is ready (recommended)
   - `load` - All resources loaded (images, CSS, etc.)
   - `readystatechange` - Document ready state changes

## Testing Your Code

### Browser Developer Tools

1. **Open Developer Tools**
   - Chrome/Edge: F12 or Right-click → "Inspect"
   - Firefox: F12 or Right-click → "Inspect Element"
   - Safari: Enable Developer Menu, then F12

2. **Console Tab**
   - View JavaScript errors
   - Test code snippets
   - Use `console.log()` for debugging

3. **Network Tab**
   - Monitor API requests
   - Check response data
   - Debug network issues

4. **Elements Tab**
   - Inspect HTML structure
   - View applied CSS
   - Modify DOM in real-time

### Debugging Techniques

1. **Console Logging**
```javascript
console.log('Button clicked');
console.log('Data received:', data);
```

2. **Breakpoints**
   - Set breakpoints in Sources tab
   - Step through code execution
   - Inspect variable values

3. **Element Inspection**
```javascript
const element = document.querySelector('#my-element');
console.log('Element found:', element);
console.log('Element content:', element.textContent);
```

### Common Testing Steps

1. **Load HTML file in browser**
2. **Check console for errors**
3. **Test user interactions**
4. **Verify DOM changes**
5. **Test API requests in Network tab**

## Best Practices

### Code Organization

1. **Use Meaningful Variable Names**
```javascript
// Good
const headerElement = document.querySelector('header');
const addButton = document.querySelector('#add_item');

// Avoid
const h = document.querySelector('header');
const btn = document.querySelector('#add_item');
```

2. **Store DOM References**
```javascript
// Good - store reference
const moviesList = document.querySelector('#list_movies');
data.results.forEach(movie => {
  const listItem = document.createElement('li');
  listItem.textContent = movie.title;
  moviesList.appendChild(listItem);
});

// Avoid - repeated queries
data.results.forEach(movie => {
  const listItem = document.createElement('li');
  listItem.textContent = movie.title;
  document.querySelector('#list_movies').appendChild(listItem);
});
```

### Event Handling

1. **Use Arrow Functions or Named Functions**
```javascript
// Arrow function
document.querySelector('#button').addEventListener('click', () => {
  // Handle click
});

// Named function (reusable)
function handleClick() {
  // Handle click
}
document.querySelector('#button').addEventListener('click', handleClick);
```

2. **Remove Event Listeners When Necessary**
```javascript
const button = document.querySelector('#button');
const handleClick = () => console.log('Clicked');

button.addEventListener('click', handleClick);
// Later, if needed:
button.removeEventListener('click', handleClick);
```

### Error Handling

1. **Always Handle Promise Rejections**
```javascript
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => {
    // Handle success
  })
  .catch(error => {
    console.error('Error:', error);
    // Handle error
  });
```

2. **Check Element Existence**
```javascript
const element = document.querySelector('#my-element');
if (element) {
  element.textContent = 'Hello';
} else {
  console.error('Element not found');
}
```

### Performance Considerations

1. **Minimize DOM Queries**
```javascript
// Good - single query
const list = document.querySelector('#list');
for (let i = 0; i < items.length; i++) {
  const li = document.createElement('li');
  li.textContent = items[i];
  list.appendChild(li);
}
```

2. **Use Document Fragments for Multiple Elements**
```javascript
const fragment = document.createDocumentFragment();
items.forEach(item => {
  const li = document.createElement('li');
  li.textContent = item;
  fragment.appendChild(li);
});
document.querySelector('#list').appendChild(fragment);
```

## Troubleshooting

### Common Errors

1. **"Cannot read property of null"**
   - Element not found by selector
   - Check HTML structure and selectors
   - Ensure DOM is loaded before script runs

2. **"addEventListener is not a function"**
   - Selected element doesn't exist
   - Verify selector syntax
   - Check if element exists in HTML

3. **CORS Errors with Fetch**
   - API doesn't allow cross-origin requests
   - Use APIs that support CORS
   - For development, use browser flags or server

4. **Script Not Working**
   - Check script src path
   - Verify script placement in HTML
   - Look for JavaScript syntax errors

### Debugging Steps

1. **Check Browser Console**
   - Look for error messages
   - Check network requests
   - Verify API responses

2. **Verify Selectors**
```javascript
// Test selectors in console
console.log(document.querySelector('#my-id'));
console.log(document.querySelector('.my-class'));
```

3. **Test Event Listeners**
```javascript
// Add logging to verify events fire
document.querySelector('#button').addEventListener('click', () => {
  console.log('Button clicked!');
});
```

4. **Check API Responses**
```javascript
fetch('https://api.example.com/data')
  .then(response => {
    console.log('Response status:', response.status);
    return response.json();
  })
  .then(data => {
    console.log('Response data:', data);
  });
```

## Additional Resources

### MDN Documentation
- [DOM Introduction](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [Document.querySelector()](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
- [EventTarget.addEventListener()](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

### Practice Exercises

1. **Create a Simple Calculator**
   - Use DOM manipulation for input/output
   - Handle button clicks for operations
   - Display results dynamically

2. **Build a Todo List**
   - Add/remove items
   - Mark items as complete
   - Use local storage for persistence

3. **Weather App**
   - Fetch weather data from API
   - Display current conditions
   - Handle user input for location

### Code Standards

- Follow semistandard JavaScript style
- Use `const` and `let` instead of `var`
- Add semicolons after statements
- Use consistent indentation (2 or 4 spaces)
- Write descriptive comments when necessary

## Conclusion

This tutorial covered the fundamentals of JavaScript DOM manipulation:

- Selecting and modifying HTML elements
- Handling user events
- Making API requests with the Fetch API
- Creating and manipulating DOM elements dynamically

Practice these concepts by building small projects and experimenting with different APIs. The key to mastering DOM manipulation is understanding the relationship between HTML, CSS, and JavaScript, and how they work together to create interactive web experiences.

Remember to always test your code in the browser, use developer tools for debugging, and follow best practices for maintainable code.