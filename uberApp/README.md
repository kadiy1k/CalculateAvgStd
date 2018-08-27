# UberApp

This application will continuously write data to a list and calculate average 
and standard deviation of elements in a list. The average, standard deviation a
nd the timestamp values are written to a MySql database. 

## Installation (python3 packages)

OS X & Linux:

```sh
pip3 install unittest
```

```sh
pip3 install PyMySQL
```

```sh
pip3 install statistics
```

```sh
pip3 install mysqlclient
```

## Usage example

- Download UberApp project 
- Install required packages from python library as mentioned in Installation instructions
- Export python path
  export PYTHONPATH="$PYTHONPATH:$HOME/.python"
- Update db_config in "main_uber_app.py" file with your database connection parameters
- Run the application as shown below from the command line interface
  $python main_uber_app.py


## Release History

* 0.0.1
    * Initial version