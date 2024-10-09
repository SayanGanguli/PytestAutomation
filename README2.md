<<<<<<< HEAD

# Papertrail
This project is used to login to the Papertrail Product of SolarWinds and edit the username



## Environment Variables

To run this project, you will need to add the following environment variables 

`1. Username / EmailID` 

`2. Password`


## Installation

It is best practice to create a virtual environemnt for a Python Project.
Activate the virtual environment.
Install all the required libraries by following this:

```bash
  pip install -r lib.txt
```
    
## Running Tests

To run tests, run the following command

```bash
  pytest
```


## Documentation

There are six sections in Project Folder:

    1. Configuration - This directory conatins the environemnt variable in Json format.
    2. Utitlity - This directory conatins UtilPage to read the environemnt file.
    3. pageObjects - This package conatins loginPage functionalities / operations in the application
    4. testCase - This package conatins two different files:
        a. conftest - Used for  
            -> Browser Configuration 
            -> Setup, Tear Down with pytest fixture
            -> Taking Screenshot only for failed test cases
        b. testLogin - Used for test cases related to login page

    5. Screenshot - This directory contains the screenshot for failed test cases. If all test cases are passed this will be an empty directory
    6. Reports - This directory conatins the HTML reports after the completion of execution

** There is a pytest.ini file placed at root folder to capture all the additional commands to run the pytest with HTML report






## Features

- Cross platform
- Cross browser

=======
# Pytest Automation
Welcome To This Project

## Prerequisites

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install

### Installation

Below is an example of how to start <B><I>Pytest Automation</I></B>.

```bash
pip install pytest
```
```bash
pip install selenium
```
```bash
pip install pytest-html
```
```bash
pip install pytest-xdist
```
```bash
pip install pytest-bdd
```
```bash
pip install webdriver-manager
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
>>>>>>> bb4909868f867ee0ac79deebd6050d047ea36886
