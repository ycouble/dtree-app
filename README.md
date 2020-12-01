# Decision tree web app generator

Tool to generate a decision tree application (where user can traverse a decision tree and gather actions to perform at each node, enter results of analysis to find the next step to do...)

# Current XMIND Convention

- Name of a node : Title of the questionnaire page
- Labels : Previous question option item (text to be put on the radio/checkbox/etc. text). If several labels, then it corresponds to the combination of several options
- Notes : Text of the current question. Items listed in the text are meant to be added to the todo list and displayed as tasks
- Parent-child : Indicates that the children are the different valid answer options of the parent question.

# Features (in no particular order)

- [x] Import from json
- [x] First data model (json)
- [ ] Implementation of the different types of questions (radio, select, numerical, etc.)
- [ ] Question type parsing
- [ ] Tree traversing etc.
- [ ] Import from xmind
- [ ] Web App generation
- [ ] Questionnaire regeneration (from updated json/xmind)
- [ ] State saving / resuming with hashcode
- [ ] Sum-up and task list email report

# How to use an xmind file

Unzip the xmind file !

# Start React-App

Please install yarn (v. 1.22.10).

Then do the following to start the web-app:

- `yarn` -> to install dependecies of the web app locally
- `yarn start` -> to start the development server
- Go to http://localhost:3000/

# Start Python Server

- Create virtual env (ex: `mkvirtualenv dtree-app`)
- Then `pip install -r requirements.txt`
