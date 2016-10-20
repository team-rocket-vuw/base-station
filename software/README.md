#Team Rocket Basestation

<br/>

##Description

Web app to control and monitor Teamrocket's rocket on site.


##Build Instructions

###Required dependencies:

- __Python3__ - (https://www.python.org)
- __NodeJS & npm__ - (https://nodejs.org/en/)

Then in the `software/` directory, enter the following into your terminal:

`pip install -r requirements.txt`<br/>
`npm install`</br>

This installs all of the required dependencies to build and run the project.

`TODO this step should be combined into one`

In one terminal, run `npm run dev`: This will start the webpack service, which compiles the jsx and scss files, and continually runs a watcher in the background, that will recompile any changes in realtime.

Alternately you can run `npm run build` to just build the jsx and scss files once.

Then `sh run.sh` or `./run.sh` and open a browser at `http://127.0.0.1:5000/`

