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
