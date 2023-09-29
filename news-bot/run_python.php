<?php
// Execute the Python script
$output = shell_exec('python main.py');

// Read the content of the summary.txt file
$summary = file_get_contents('summary.txt');

// Return the summary as a response
echo $summary;
?>
