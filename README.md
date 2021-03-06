# Basketball-Stats 

## Description:
<p>This project is a personal project, using concepts of web scraping, database management 
and machine learning, we can use data from the that can be broken down into three phases
and a possible fourth phase.</p>

<strong>Current Phase: 3</strong><br>
<strong>Phase 1:</strong> Web scraping<br>
<strong>Phase 2:</strong> Creating the database<br> 
<strong>Phase 3:</strong> Predicting the MVP based on player stats<br> 

<strong>Additional Features:</strong><br>
<p>1) Creating a docker file, and create a docker container for the local database</p>

<p>Phase 1: By using the python libraries beautifulsoup, we can scrap data from 
basketball-reference.com. There are going to be multiple scrapers that scrap information
like season stats, team stats, and finally player stats from 1980 to current date. 
The scrapers will all output to mutiple csv files in a directory called <em>Output</em>.</p>

<p>Phase 2: By using the mysql workbench and hosting the locally. Taking the csv files 
from the first phase, we can add it into a database and write queries for certain stats. For example,
we can write a query to see who has the total most field goals in a certain year.</p>

<p>Phase 3: Using the database, we can retrieve player stats for a given year. With these stats, we can 
highlight import features, and thus put it into a random forest function. This function should the import stats, 
then we can use Linear Regression to predict who won MVP for a given year.</p>

<p>Phase 4: Using flask, creating a web application to for the scrapers, database, and for the mvp prediction.
This is an optional phase that may or may not be created.</p>

## Setting up the virtual environment using Conda
<p>This is a guide to create a new virtual environment using conda from<br>
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/.</p>

<p>1) Check if conda is installed and in your path <br>
If conda is installed, this should be your output.</p>

```
$ conda -V
conda 3.7.0
```
<p>2) Check if conda is up to date.</p>

```
$ conda update conda
```
<p>3) Create a virtual environment for your project, <br> 
Where yourenvname is the name of the environment and x.x is the version of python.</p>

```
$ conda create -n yourenvname python=x.x anaconda
```
<p>4) Activating your virtual environment.</p> 

```
$ source activate yourenvname 
```
<p>5) Install additonal Python packages to a virtual environment.</p>

```
$ conda install -n yourenvname [package]
```
<p>6) Deactivate and delete your virtual environment.</p> 

```
$ source deactivate                # Deactivate your virtual environment
$ conda remove -n yourenvname -all # Deletes your virtual environment  
```

## Installing
### Installing Python Libraries with conda
<p>With the code below run it to get the required libraries to run the scraper.</p>

```
$ conda install --file requirements.txt
```

### Downloading custom modules Via Github 
<p>You can clone this repo and import the libraries at your own discretion.</p>

## Running the program 
### Running the web scrapers 
<p>To run each of the scrapers, the code below will show how.</p>

```
$ python /your/path/BasketBall-Stats/Python_Scrapers/Create_Player_Name # Gets dataframe of player names from 1980 - current 
$ python /your/path/Basketball-Stats/Run_Scraper/get_season_stats.py    # Gets season stats from 1980 - current
$ python /your/path/Basketball-Stats/Run_Scraper/get_team_stats.py      # Gets team stats from 1980 - current
$ python /your/path/Basketball-Stats/Run_Scraper/get_player_stats.py    # Gets player stats from 1980 - current
``` 
<p><strong>NOTE: You must run Create_Player_Name first before any other scraper</strong></p>
<p>Where your path is where you decide to store the source directory, <em>Basketball-Stats</em>. <strong>NOTE:</strong> The file should be ran from
the root directory, aka <em>Basketball-Stats</em>.</p>

### Web Scrapers Expected Output
<p>Inside of the source directory,<em>Basketball-Stats</em>, there will be a directory called <em>Output</em>.<br>
Inside of <em>Output</em>, should be three directories, corresponding to the name of the scrapers. More information 
be in a Web_Scraper_User_Manual</p>

### Running the Database 
<p><strong>IMPORTANT:</strong>For any queries, the names of people with accent has been normalized<br>
Example: Nikola Jokić will be Nikola Jokic</p>
<p>TBD</p>

### Running the Prediction of MVP
<p>TBD</p>

### Running the Django Website

