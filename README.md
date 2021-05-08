mintmesh_test
=============

### Setup
In order to run the server on your local machine follow the given steps.
1. Create a virtualenv using any tool of your choice, this is tested on python3.7 but should work on higher versions as well.
2. Activate the virtualenv and install the dependencies in the requirements file `pip install --requirement requirements.txt`
3. **[OPTIONAL]** Create a .env file using .env.example as a template `cp .env.example .env`
4. Start the server using orchestration script in bin dir `bin/orchestrate.sh`

### API Documentation
1. `GET /api/case_details/<string:country>`
This route provides data for a single country and provides only 2 response codes.
200 - If the request is successfully processed
500 - If there was an error while processing the request

2. `GET /api/case_details`
This route provides data for all countries and provides only 2 response codes.
200 - If the request is successfully processed
500 - If there was an error while processing the request

3. `GET /health`
This route is for health check for the app process.
It provides only a 200 status code

### Code Quality
This repo uses following tools for code quality

1. `black`
`black --check --diff --target-version py37 .` Check for the code formaating using PEP8 as reference.
2. `flake8`
`flake8 --exclude __init__.py --max-line-length 88 .` Check for issues regarding static code analysis.
3. `isort`
`isort --atomic --check --force-single-line-imports --lines-after-imports 2 --lines-between-types 1 --line-length 88 --profile black .`
Check for import ordering using isort. This provides readability and removes clutter from import statements
