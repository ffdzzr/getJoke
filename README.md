get a random joke and you can combine it with other programs like cowsay.<br />
put line after into your ~/.bash_aliases, to get a joke every time you open up session 0 in your terminal<br />
<br /> 
if [ "$(tty)" == /dev/pts/0 ]; then timeout 1s cowsay -f moose "$(python3 /path/to/getJoke.py)"; fi<br /> 
<br />
⚠️ replace "/path/to/getJoke.py" with your own⚠️ <br />
<br />
<br />
using: https://v2.jokeapi.dev/ <br />
