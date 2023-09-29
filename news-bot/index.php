<!DOCTYPE html>
<html>
<head>
    <title>Show News Summary</title>
</head>
<body>
    <h1>Show News Summary</h1>

    <button id="showButton">Show the News</button>

    <div id="summary"></div>

    <script>
        // JavaScript function to run the Python script
        function runPythonScript() {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', 'run_python.php', true);

            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    // Display the response (summary.txt content) in the 'summary' div
                    document.getElementById('summary').innerHTML = xhr.responseText;
                }
            };

            xhr.send();
        }

        // Attach the runPythonScript function to the button's click event
        document.getElementById('showButton').addEventListener('click', runPythonScript);
    </script>
</body>
</html>
