# Basketball-Stats 

## Description:
<p>This project is a personal project, using concepts of web scraping, database management 
and machine learning that can be broken down into three phases</p>

<strong>Phase 1:</strong> Web scraping 
<strong>Phase 2:</strong> Creating the database 
<strong>Phase 3:</strong> Predicting the MVP based on player stats 

<p>Phase 1: By using the python libraries beautifulsoup, we can scrap data from 
basketball-reference.com. There are going to be multiple scrapers that scrap information
like season stats, team stats, and finally player stats. The scrapers will all output to a 
csv file</p>

<p>Phase 2: By using the mysql workbench and hosting the database on AWS(Amazon Web Services),
it allows for AWS to handle server provisioning, patching and configuration. Taking the csv files 
from the first phase, we can add it into a database and write queries for certain stats. For example,
we can write a query to see who has the total most field goals in a certain year</p>

<p>Phase 3: Using the database, we can retrieve player stats for a given year. With these stats, we can 
highlight import features, and thus put it into a random forest function. This function should predict who 
won MVP for a given year</p>

## Setting up the virtual environment using Conda
<p>This is a guide to create a new virtual environment using conda from<br>
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/</p>

<p>1) Check if conda is installed and in your path <br>
If conda is installed, this should be your output</p>

```
$ conda -V
conda 3.7.0
```
<p>2) Check if conda is up to date </p>

```
$ conda update conda
```
<p>3) Create a virtual environment for your project <br> 
Where yourenvname is the name of the environment and x.x is the version of python</p>

```
$ conda create -n yourenvname python=x.x anaconda
```
<p>4) Activating your virtual environment</p> 

```
$ source activate yourenvname 
```
<p>5) Install additonal Python packages to a virtual environment</p>

```
$ conda install -n yourenvname [package]
```
<p>6) Deactivate and delete your virtual environment</p> 

```
$ source deactivate                # Deactivate your virtual environment
$ conda remove -n yourenvname -all # Deletes your virtual environment  
```

## Installing
### Installing Python Libraries with conda
<p>With the code below run it to get the required libraries to run the scraper</p>

```
$ conda install --file requirements.txt
```

### Installing the custom modules 
<p>The custom module has not been built yet</p>

### Via Github 
<p>You can clone this repo and import the libraries at your own discretion</p>

