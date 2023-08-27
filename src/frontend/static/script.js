document.addEventListener("DOMContentLoaded", function() {
    const compileButton = document.getElementById("compile-button");
    const editorTextArea = document.getElementById("editor");
    const optimizerButton = document.getElementById("optimizer-button");
    compileButton.addEventListener("click", function() {
        const code = editorTextArea.value;


        const data = { "code": code, "file": "code.py" };


        fetch('http://127.0.0.1:30410/build', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(responseData => {
            console.log("Server response:", responseData);


            const outputArea = document.getElementById("output");
            outputArea.textContent = `\n${responseData.message}\n\n${responseData.stdout}\n\n${responseData.stderr}`;
        })
        .catch(error => {
            console.error('Error sending data to endpoint:', error);
        });
    });
    optimizerButton.addEventListener("click", function() {
        const code = editorTextArea.value;

        const data = { "code": code, "file": "code.py" };

        fetch('http://127.0.0.1:30410/optimise', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(responseData => {
          console.log("Optimizer response:", responseData);


          const outputArea = document.getElementById("output");
          outputArea.textContent = `\n${responseData.message}\n\n${responseData.stdout}\n\n${responseData.stderr}`;
        })
        .catch(error => {
          console.error('Error fetching optimizer data:', error);
        });
      });
    });




