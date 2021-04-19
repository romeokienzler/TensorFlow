Fork and Pull
Objective for Exercise

To fork a repository in GitHub
To make changes to the forked repository and commit the changes
To create pull requests
Note: These instructions works on BASH terminal on Windows & Mac terminals.

How to fork a repository and commit the fork repository and create a pull request.
Open the link: https://github.com/romeokienzler/TensorFlow/

Click ‘Fork’ and copy the repository in your account.

Copy the SSH Repository Link and clone it locally using:

git clone yoursshrepolink

image

Open and edit any file in the editor.

After saving the file,

git add .

And commit the changes with the message:

git commit -m “message”

image

git push to make the changes in remote repository

image

Check the repository, it is added

image

Click ‘Compare’ to compare the changes.

image

NOTE: This request will go to AUTHOR of the repository and if the changes looks good, only then the original repository can get the changes.

image

Create a Pull request to make the changes in the original file.

Note: The pull request will now send to the author of the repository and if accepted the changes will be made to the original repository.

Author(s)
Malika Singla
Other Contributor(s)
Lavanya

Changelog
Date	Version	Changed by	Change Description
2020-08-25	2.0	Lavanya	Migrated Lab to Markdown and added to course repo in GitLab
© IBM Corporation 2020. All rights reserved.
