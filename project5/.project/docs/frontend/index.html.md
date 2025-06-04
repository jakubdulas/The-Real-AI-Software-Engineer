# frontend/index.html

This file provides the HTML structure for the TODO list web application frontend.

## Structure and Usage

- **HTML5 DOCTYPE** and language set to English.
- **Meta charset UTF-8** for character encoding.
- **Title:** "TODO List App"
- **Link to CSS:** External stylesheet (styles.css) for minimal styling.

### Main Body
- **Main container div** with class `container` wrapping all content.
    - **H1 Heading:** Shows the app title ('TODO List').
    - **Add Task Form:**
        - Text input for entering a new task title with placeholder and required attribute.
        - 'Add' button to submit new tasks.
    - **Task List:**
        - Unordered list (`<ul id="task-list">`) where tasks are rendered dynamically by JavaScript.
- **Script Tag:** Loads frontend logic from `main.js`.

## Integration
- The form and task list interact with the backend API through JavaScript (see `main.js`).

## Comments and Key Sections
- Code is straightforward and semantic; add further comments in `main.js` for dynamic behavior description.
