This is a simple example application to demonstrate CI/CD.  The application presents the user with a very simple UI to sign into their Google account, and then uses the sign-in information to determine the user's name.
It's 
See https://developers.google.com/identity/sign-in/web for more information on adding Google sign-in to a web app (frontend) and https://realpython.com/flask-google-login/ for an example of a Flask application that uses Google login.

Developers can run the backend (which serves up the frontend content as well as an endpoint demonstrating the backend has access to the user's profile information).
Linux: `$ scripts/build.sh && scripts/run.sh`
Windows: `powershell -executionPolicy bypass '.\src\scripts\build.ps1' ; powershell -executionPolicy bypass '.\src\scripts\run.ps1'`

If you make changes and want to check them in, first run the tests and make sure they pass (and make sure to add tests for the changes you made).  If the tests fail, it's your responsibility to fix them before submitting a pull request.

On Linux systems:
src/scripts/test.sh

On Windows (couldn't get && to work in powershell):
powershell -executionPolicy bypass '.\src\scripts\test.ps1' 

For continuous integration we use GitHub Actions.  When you commit to the master branch of the repo, GitHub automatically runs the test pipeline and reports if there are any errors.  

For continuous deployment we use.... ???
