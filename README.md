# File/Photo selector
A quick way to duplicate a set of specific files

A client sent a list of photo ids from a photoshoot day (I like photo number 2 56 89 700 12 36 48 ...) and you have a big folder containing all of them. Searching for each file seperately can be a waste of time. A shortcut is using command prompt to duplicate all at once, using the commands generated by this code.

user manual:
1. Open command prompt and select original file folder by typing 'cd' and the path to the folder
2. Create a folder that will be the destination for the selected files in the original folder
3. Enter the desination folder name and the file IDs ending with a 0 in this program
4. Finally copy the output of this program to paste in the command prompt, enter and just wait for the files to be copied to the destination folder.
note : this program alse removes duplicate IDs and sorts the IDs in ascending order.

Ex: selecting wedding photo number 2 89 40 and 600 for editing
(in CMD prompt) cd C:\documents\photos\wedding_photos
(in wedding_photos folder) create new folder -  for_editing
(run this code and enter) canonR6___, .jpg, for_editing, 2 89 40 600 0
(in CMD prompt) paste the text generated from this code and done