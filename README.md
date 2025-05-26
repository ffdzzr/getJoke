get a random joke and you can combine it with other programs like cowsay.  
put line after into your .bashrc, to get a joke first time you open up terminal  
cowsay -f moose "$(python3 /path/to/getJoke.py)"
if [ "$(tty)" == /dev/pts/0 ]; then cowsay -f moose "$(python3 /path/to/getJoke.py)"; fi   
  
!!!replace "/path/to/getJoke.py" with your own!!!  
  
  
using: https://v2.jokeapi.dev/
