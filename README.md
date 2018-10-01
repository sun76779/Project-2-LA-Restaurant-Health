# Project 2 | LA Restaurant Health Inspection | Rula, Shang, Danny


## Datasets

Los Angeles County Health Inspection Data (from Kaggle)

## Questions We Try to Answer
* Is there a correlation between average restaurant score with location? 
* Do we see higher frequency of certain violations depending on letter score? 
* Do we see improvement in scores year to year? 

## Toolbox
* MySQL 
* Python Flask
* Javascript/HTML/CSS
* D3
* Carto for Mapping


## Installation

* Create a MySQL database i.e. `'Project 2'` and import the `restaurant_data.csv` into the database
* Edit the `app.py` and put your database credentials in there.
* Launching Flask application by running: `python app.py`


## How to Use the Website

* Summary Page containing:
  * An explanation of the Health Inspection Score/Grade.
  * Navigation Menu provides links on the right: "Restaurant Search" which links to the restaurt data, and "Map" which links to the detail restaurt mapping

* Restaurant Search:
  * A List of All Restaurant in this study.
  * User can set multiple filters and search for Restaurant Health Score Historical Data from 2015-2018

* Map:
  * This Interactive map allows you to pan and zoom to get restaurant health inspection score details in your local neighbourhood or any neighborhood in Los Angeles City
  * The map contains different layers: you can multi-select "All Year", "2015", "2016", "2017", and "2018".
  * Use `Search Location`: Type an place/address or restaurant name and Enter. You'll see search results as red mini-pins, where mini-pins show the results, then find a score point nearby.

- - -


**Thank You!**

## Copyright

USC Data Boot Camp © 2018 Group Project - Rula Othman, Shang Wang, and Hyung Bo Sim. All Rights Reserved.
