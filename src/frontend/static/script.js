document.addEventListener("DOMContentLoaded", function() {
    const compileButton = document.getElementById("compile-button");
    const editorTextArea = document.getElementById("editor");

    compileButton.addEventListener("click", function() {
        const code = editorTextArea.value;

        // Create an object with the code and file name
        const data = { "code": code, "file": "code.py" };

        // Send code and file name to the specified endpoint URL
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

            // Update the output area with stdout and stderr values
            const outputArea = document.getElementById("output");
            outputArea.textContent = `\n${responseData.message}\n\n${responseData.stdout}\n\n${responseData.stderr}`;
        })
        .catch(error => {
            console.error('Error sending data to endpoint:', error);
        });
    });
});
