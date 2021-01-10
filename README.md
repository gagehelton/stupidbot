<h1>The Stupidest of all the Bots</h1>

# Commands
## .convert
* Converts passed ascii value to binary or hex
* Syntax - ```.convert CONVERSTION_TYPE VALUE```

## .wisdom
* Returns inspirobot.me image

## .jimmy
* Returns an image of Jimmy Rogers sleeping

## .468
* Returns display size options based on the 4/6/8 rule
* Syntax ```.468 VALUE```
* Value is distance to furthest viewer in feet

# Dropbox as CDN
## Mount as virtual file system
1. ```sudo apt install libfuse2```
2. ```pip3 install dbxfs```
3. ```mkdir ~/mydropbox```
4. ```dbxfs ~/mydropbox```
5. Generate access token in prompt
6. Navigate to the url given in the output to authorize
7. Copy the auth code back to your terminal

### References
* https://ostechnix.com/dbxfs-mount-dropbox-folder-locally-as-virtual-file-system-in-linux/
