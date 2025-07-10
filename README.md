# Wap Testing

## Setup
- Create python virtual environment `python -m venv .venv`.
- Initialize virtual environment `source .venv/bin/activate`.
- Install dependencies `pip install -r requirements.txt`.
- Download [chromedriver](https://googlechromelabs.github.io/chrome-for-testing/) from google.
- Replace the `executable_path` in `chrome_driver.yaml`.

## Tests
The project current consists of two test which are the following:
- Test search for a game title and open streamer profile
  
  ![test_search_and_open_streamer_profile](resources/gif/test_search_and_open_streamer_profile.gif)
- Test search for a game title and watch stream
  
  ![test_search_and_watch_stream](resources/gif/test_search_and_watch_stream.gif)

To run the tests in the current project just simply execute `pytest` in the terminal.

## Structure
```
.
├── configs
│   └── chrome_driver.yaml
├── drivers
│   ├── driver.py
│   └── impl
│       └── chrome_driver.py
├── errors
│   ├── driver_error.py
│   └── not_found_error.py
├── features
│   └── search.feature
├── locators
│   └── locators.py
├── logs
├── pages
│   ├── base_page.py
│   ├── __init__.py
│   └── search
│       ├── locators.py
│       └── page.py
├── README.md
├── requirements.txt
├── resources
│   ├── gif
│   │   ├── test_search_and_open_streamer_profile.gif
│   │   └── test_search_and_watch_stream.gif
│   └── screenshots
├── tests
│   ├── conftest.py 
│   └── search
│       ├── conftest.py
│       ├── test_search_and_open_streamer_profile.py
│       └── test_search_and_watch_stream.py
└── utils
    └── logger.py
```
- `configs` contains the configurations to be used in the project.
- `drivers` contains the custom implementation for different drivers.
- `errors` contains the errors used in the framework.
- `features` contains the feature definition to be tested.
- `locators` contains the common locators used in the framework.
- `logs` contains auto generated log file with contents related to the test execution.
- `pages` contains the pages to be tested.
- `requirements.txt` contains a list of required module for the project.
- `resources` contains the files that are used and also generated from the project.
- `tests` contains the test details.
- `utils` contains the utilities that can be used across the project.