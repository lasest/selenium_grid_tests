# Website testing with selenium-grid

## Project structure

- `build`: contains files for building container images
- `deployment`: contains files for running containers
- `scripts`: contains files for running the project without containers
- `src`: contains utility functions necessary for test execution, tests for those functions and actual website tests. Website tests are in `./src/simbirsoft/tests/test_website.py`

## How to run

1. Clone the repository

`git clone git@github.com:lasest/selenium_grid_tests.git`

2. Cd into the repository

3. Build the images

`./build/docker_build.sh`

Two images will be built by the script:

- `simbirsoft_report` - the image for viewing test reports

- `simbirsoft_test` - the image for running tests

**Note:** the script uses `buildx` as the build backend, make sure that it is available

4. Run tests

`./deployment/docker_up_test.sh`

5. Shut down with `Ctrl + C` after tests have finished

6. Start the reports server

`./deployment/docker_up_report.sh`

7. View reports at `0.0.0.0:9000`

**Note:** all build and deployment scripts are provided for docker and podman. Each should work, but podman was tested more thoroughly.

To run with with `./scripts` create a `.env` file at `./src/simbirsoft/.env` with the following content:

```
HUB_HOST=0.0.0.0
REPORTS_PATH="<PATH_WHERE_REPORTS_WILL_BE_SAVED>"
EXPORT_PATH="<PATH_WHERE_EXPORTS_WILL_BE_SAVED>"
```

Running with `./scripts` requires [allure](https://github.com/allure-framework/allure2) to be installed on the system.

When run in any way, the application will require a location to store data. By default, that location will be `./app_data`. The directory should be created automatically when running the test container. `./app_data` should contain the following directories: `export`, `reports`.
