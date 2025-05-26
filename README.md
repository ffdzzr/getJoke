get a random joke and you can combine it with other programs like cowsay.  
put line after into your ~/.bash_aliases, to get a joke every time you open up session 0 in your terminal  
  
if [ "$(tty)" == /dev/pts/0 ]; then timeout 1s cowsay -f moose "$(python3 /path/to/getJoke.py)"; fi   
  
⚠️ replace "/path/to/getJoke.py" with your own⚠️  
  
  
using: https://v2.jokeapi.dev/
