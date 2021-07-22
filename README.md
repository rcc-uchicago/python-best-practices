# python-best-practices
 RCC workshop: Best coding practices for Python projects


# Exercise 2: Pizza Histogram Generator
The pizza histogram generator will aggregate counts of pizza types (sausage, cheese, etc.) from a CSV file and will generate a histogram displaying the aggregate counts.

## Getting Started
Fork this repository if you haven't already and then clone your version of the repository to your local device, replacing `<YOUR_GITHUB_HANDLE>` with your GitHub username:
```
$ git clone https://github.com/<YOUR_GITHUB_HANDLE>/python-best-practices.git
$ cd python-best-practices
```
If you do not have Python3 installed on your device, install it [here](https://www.python.org/downloads/). There are no additional packages required to run this script. 

## Usage 
To generate the pizza histogram with the only required input:
```
$ python pizza_histogram.py -i /path/to/input/data.csv
```
An example input.csv file is located at `python-best-practices/pizza_orders.csv`. Other optional arguments:
```
$ python pizza_histogram.py -i /path/to/input/data.csv -d False -s True -o histogram.png
```
See below table for description of arguments:
| Argument | Flag | Description |
| --- | --- | --- |
| input_data ***(required)*** | -i | The path to the CSV with pizza types and counts |
| display ***(optional)*** | -d | Whether or not to display the output histogram. Options are `True` or `False`. Default value is `True`. |
| save ***(optional)*** | -s | Whether or not to save the output histogram as a .png file. Options are `True` or `False`. Default value is `True`. |
| out_filename ***(optional)*** | -o | The filename you would like to save your output histogram as. Default value is `orders.png`. |

## Dependencies (optional)
There are no additional dependencies needed to run this script.


