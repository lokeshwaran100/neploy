# Setting up Neploy Frontend

This readme contains the procedure to setup the frontend part of the Neploy application, a web-based code editor and compiler.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Folder Structure](#folder-structure)
- [Usage](#usage)



## Technologies Used
- HTML
- CSS
- JavaScript

## Setup
1. Go to directory frontend
```
cd frontend
```

2. Install the flask package
```
pip3 install flask
```

3. Run app.py file
```
python3 app.py
```



## Folder Structure
The folder structure for the Neploy frontend is as follows:
```

frontend/
├── app.py          # Main HTML file
├── static/             # Static assets
│   ├── styles.css      # CSS styles
│   ├── script.js       # JavaScript code
├── templates/          # Template
│   ├── index.html      # HTML code
├── README.md           # Project documentation (you are here)
```


## Usage
1. Write your code in the code editor area.
2. Click the "Compile" button to compile your code and view the output.
3. Click the "Review Code" button to get AI/ML code review result.
