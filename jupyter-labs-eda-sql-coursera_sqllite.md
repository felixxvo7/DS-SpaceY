<p style="text-align:center">
    <a href="https://skills.network" target="_blank">
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo">
    </a>
</p>

<h1 align=center><font size = 5>Assignment: SQL Notebook for Peer Assignment</font></h1>

Estimated time needed: **60** minutes.

## Introduction
Using this Python notebook you will:

1.  Understand the Spacex DataSet
2.  Load the dataset  into the corresponding table in a Db2 database
3.  Execute SQL queries to answer assignment questions 


## Overview of the DataSet

SpaceX has gained worldwide attention for a series of historic milestones. 

It is the only private company ever to return a spacecraft from low-earth orbit, which it first accomplished in December 2010.
SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars wheras other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage. 


Therefore if we can determine if the first stage will land, we can determine the cost of a launch. 

This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.

This dataset includes a record for each payload carried during a SpaceX mission into outer space.


### Download the datasets

This assignment requires you to load the spacex dataset.

In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. Click on the link below to download and save the dataset (.CSV file):

 <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv" target="_blank">Spacex DataSet</a>




```python
!pip install sqlalchemy==1.3.9

```

    Collecting sqlalchemy==1.3.9
      Downloading SQLAlchemy-1.3.9.tar.gz (6.0 MB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m6.0/6.0 MB[0m [31m85.0 MB/s[0m eta [36m0:00:00[0m:00:01[0m00:01[0m
    [?25h  Preparing metadata (setup.py) ... [?25ldone
    [?25hBuilding wheels for collected packages: sqlalchemy
      Building wheel for sqlalchemy (setup.py) ... [?25ldone
    [?25h  Created wheel for sqlalchemy: filename=SQLAlchemy-1.3.9-cp311-cp311-linux_x86_64.whl size=1159882 sha256=0c677aa9120771cd070bbf62163ab204379d2bf918b67959cccfbd3f2303acde
      Stored in directory: /home/jupyterlab/.cache/pip/wheels/3a/7c/1e/12404784a68083eb969f877a1808a1847bab897684b56ddc55
    Successfully built sqlalchemy
    Installing collected packages: sqlalchemy
      Attempting uninstall: sqlalchemy
        Found existing installation: SQLAlchemy 2.0.30
        Uninstalling SQLAlchemy-2.0.30:
          Successfully uninstalled SQLAlchemy-2.0.30
    [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    ipython-sql 0.5.0 requires sqlalchemy>=2.0, but you have sqlalchemy 1.3.9 which is incompatible.
    jupyterhub 5.2.1 requires SQLAlchemy>=1.4.1, but you have sqlalchemy 1.3.9 which is incompatible.[0m[31m
    [0mSuccessfully installed sqlalchemy-1.3.9


### Connect to the database

Let us first load the SQL extension and establish a connection with the database



```python
!pip install ipython-sql
!pip install ipython-sql prettytable
```

    Requirement already satisfied: ipython-sql in /opt/conda/lib/python3.11/site-packages (0.5.0)
    Requirement already satisfied: prettytable in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (3.12.0)
    Requirement already satisfied: ipython in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (8.22.2)
    Collecting sqlalchemy>=2.0 (from ipython-sql)
      Downloading SQLAlchemy-2.0.37-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.6 kB)
    Requirement already satisfied: sqlparse in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (0.5.3)
    Requirement already satisfied: six in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (1.16.0)
    Requirement already satisfied: ipython-genutils in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (0.2.0)
    Requirement already satisfied: greenlet!=0.4.17 in /opt/conda/lib/python3.11/site-packages (from sqlalchemy>=2.0->ipython-sql) (3.0.3)
    Requirement already satisfied: typing-extensions>=4.6.0 in /opt/conda/lib/python3.11/site-packages (from sqlalchemy>=2.0->ipython-sql) (4.12.2)
    Requirement already satisfied: decorator in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (5.1.1)
    Requirement already satisfied: jedi>=0.16 in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (0.19.1)
    Requirement already satisfied: matplotlib-inline in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (0.1.7)
    Requirement already satisfied: prompt-toolkit<3.1.0,>=3.0.41 in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (3.0.42)
    Requirement already satisfied: pygments>=2.4.0 in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (2.18.0)
    Requirement already satisfied: stack-data in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (0.6.2)
    Requirement already satisfied: traitlets>=5.13.0 in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (5.14.3)
    Requirement already satisfied: pexpect>4.3 in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (4.9.0)
    Requirement already satisfied: wcwidth in /opt/conda/lib/python3.11/site-packages (from prettytable->ipython-sql) (0.2.13)
    Requirement already satisfied: parso<0.9.0,>=0.8.3 in /opt/conda/lib/python3.11/site-packages (from jedi>=0.16->ipython->ipython-sql) (0.8.4)
    Requirement already satisfied: ptyprocess>=0.5 in /opt/conda/lib/python3.11/site-packages (from pexpect>4.3->ipython->ipython-sql) (0.7.0)
    Requirement already satisfied: executing>=1.2.0 in /opt/conda/lib/python3.11/site-packages (from stack-data->ipython->ipython-sql) (2.0.1)
    Requirement already satisfied: asttokens>=2.1.0 in /opt/conda/lib/python3.11/site-packages (from stack-data->ipython->ipython-sql) (2.4.1)
    Requirement already satisfied: pure-eval in /opt/conda/lib/python3.11/site-packages (from stack-data->ipython->ipython-sql) (0.2.2)
    Downloading SQLAlchemy-2.0.37-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.2 MB)
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m3.2/3.2 MB[0m [31m82.3 MB/s[0m eta [36m0:00:00[0m:00:01[0m
    [?25hInstalling collected packages: sqlalchemy
      Attempting uninstall: sqlalchemy
        Found existing installation: SQLAlchemy 1.3.9
        Uninstalling SQLAlchemy-1.3.9:
          Successfully uninstalled SQLAlchemy-1.3.9
    Successfully installed sqlalchemy-2.0.37
    Requirement already satisfied: ipython-sql in /opt/conda/lib/python3.11/site-packages (0.5.0)
    Requirement already satisfied: prettytable in /opt/conda/lib/python3.11/site-packages (3.12.0)
    Requirement already satisfied: ipython in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (8.22.2)
    Requirement already satisfied: sqlalchemy>=2.0 in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (2.0.37)
    Requirement already satisfied: sqlparse in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (0.5.3)
    Requirement already satisfied: six in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (1.16.0)
    Requirement already satisfied: ipython-genutils in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (0.2.0)
    Requirement already satisfied: wcwidth in /opt/conda/lib/python3.11/site-packages (from prettytable) (0.2.13)
    Requirement already satisfied: greenlet!=0.4.17 in /opt/conda/lib/python3.11/site-packages (from sqlalchemy>=2.0->ipython-sql) (3.0.3)
    Requirement already satisfied: typing-extensions>=4.6.0 in /opt/conda/lib/python3.11/site-packages (from sqlalchemy>=2.0->ipython-sql) (4.12.2)
    Requirement already satisfied: decorator in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (5.1.1)
    Requirement already satisfied: jedi>=0.16 in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (0.19.1)
    Requirement already satisfied: matplotlib-inline in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (0.1.7)
    Requirement already satisfied: prompt-toolkit<3.1.0,>=3.0.41 in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (3.0.42)
    Requirement already satisfied: pygments>=2.4.0 in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (2.18.0)
    Requirement already satisfied: stack-data in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (0.6.2)
    Requirement already satisfied: traitlets>=5.13.0 in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (5.14.3)
    Requirement already satisfied: pexpect>4.3 in /opt/conda/lib/python3.11/site-packages (from ipython->ipython-sql) (4.9.0)
    Requirement already satisfied: parso<0.9.0,>=0.8.3 in /opt/conda/lib/python3.11/site-packages (from jedi>=0.16->ipython->ipython-sql) (0.8.4)
    Requirement already satisfied: ptyprocess>=0.5 in /opt/conda/lib/python3.11/site-packages (from pexpect>4.3->ipython->ipython-sql) (0.7.0)
    Requirement already satisfied: executing>=1.2.0 in /opt/conda/lib/python3.11/site-packages (from stack-data->ipython->ipython-sql) (2.0.1)
    Requirement already satisfied: asttokens>=2.1.0 in /opt/conda/lib/python3.11/site-packages (from stack-data->ipython->ipython-sql) (2.4.1)
    Requirement already satisfied: pure-eval in /opt/conda/lib/python3.11/site-packages (from stack-data->ipython->ipython-sql) (0.2.2)



```python
%load_ext sql
```


```python
import csv, sqlite3
import prettytable
prettytable.DEFAULT = 'DEFAULT'

con = sqlite3.connect("my_data1.db")
cur = con.cursor()
```


```python
!pip install -q pandas
```


```python
%sql sqlite:///my_data1.db
```


```python
import pandas as pd
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv")
df.to_sql("SPACEXTBL", con, if_exists='replace', index=False,method="multi")
```




    101



**Note:This below code is added to remove blank rows from table**



```python
#DROP THE TABLE IF EXISTS

%sql DROP TABLE IF EXISTS SPACEXTABLE;
```

     * sqlite:///my_data1.db
    Done.





    []




```python
%sql create table SPACEXTABLE as select * from SPACEXTBL where Date is not null
```

     * sqlite:///my_data1.db
    Done.





    []



## Tasks

Now write and execute SQL queries to solve the assignment tasks.

**Note: If the column names are in mixed case enclose it in double quotes
   For Example "Landing_Outcome"**

### Task 1




##### Display the names of the unique launch sites  in the space mission



```python
%sql SELECT DISTINCT "Launch_Site" FROM missions;

```

     * sqlite:///my_data1.db
    (sqlite3.OperationalError) no such table: missions
    [SQL: SELECT DISTINCT "Launch_Site" FROM missions;]
    (Background on this error at: https://sqlalche.me/e/20/e3q8)



### Task 2


#####  Display 5 records where launch sites begin with the string 'CCA' 



```python
%sql SELECT "Launch_Site" FROM missions WHERE "Launch_Site" LIKE 'CCA%' LIMIT 5;

```

     * sqlite:///my_data1.db
    (sqlite3.OperationalError) no such table: missions
    [SQL: SELECT "Launch_Site" FROM missions WHERE "Launch_Site" LIKE 'CCA%' LIMIT 5;]
    (Background on this error at: https://sqlalche.me/e/20/e3q8)


### Task 3




##### Display the total payload mass carried by boosters launched by NASA (CRS)



```python
%sql SELECT SUM("Payload_Mass") AS "Total_Payload_Mass" FROM missions WHERE "Agency" = 'NASA (CRS)';

```

     * sqlite:///my_data1.db
    (sqlite3.OperationalError) no such table: missions
    [SQL: SELECT SUM("Payload_Mass") AS "Total_Payload_Mass" FROM missions WHERE "Agency" = 'NASA (CRS)' ;]
    (Background on this error at: https://sqlalche.me/e/20/e3q8)


### Task 4




##### Display average payload mass carried by booster version F9 v1.1



```python
%sql SELECT AVG("Payload_Mass") AS "Average_Payload_Mass" FROM missions WHERE "Booster_Version" = 'F9 v1.1';

```

     * sqlite:///my_data1.db
    (sqlite3.OperationalError) no such table: missions
    [SQL: SELECT AVG("Payload_Mass") AS "Average_Payload_Mass" FROM missions WHERE "Booster_Version" = 'F9 v1.1' ;]
    (Background on this error at: https://sqlalche.me/e/20/e3q8)


### Task 5

##### List the date when the first succesful landing outcome in ground pad was acheived.


_Hint:Use min function_ 



```python
%sql SELECT MIN("Date") AS "First_Successful_Landing" FROM missions WHERE "Landing_Outcome" = 'Success (ground pad)';

```

     * sqlite:///my_data1.db
    (sqlite3.OperationalError) no such table: missions
    [SQL: SELECT MIN("Date") AS "First_Successful_Landing" FROM missions WHERE "Landing_Outcome" = 'Success (ground pad)' ;]
    (Background on this error at: https://sqlalche.me/e/20/e3q8)


### Task 6

##### List the names of the boosters which have success in drone ship and have payload mass greater than 4000 but less than 6000



```python
%sql SELECT "Booster_Version" FROM missions WHERE "Landing_Outcome" = 'Success (drone ship)' AND "Payload_Mass" > 4000 AND "Payload_Mass" < 6000;

```

     * sqlite:///my_data1.db
    (sqlite3.OperationalError) no such table: missions
    [SQL: SELECT "Booster_Version" FROM missions WHERE "Landing_Outcome" = 'Success (drone ship)' AND "Payload_Mass" > 4000 AND "Payload_Mass" < 6000;]
    (Background on this error at: https://sqlalche.me/e/20/e3q8)


### Task 7




##### List the total number of successful and failure mission outcomes



```python
%sql SELECT "Landing_Outcome", COUNT(*) AS "Count" FROM missions GROUP BY "Landing_Outcome";

```

     * sqlite:///my_data1.db
    (sqlite3.OperationalError) no such table: missions
    [SQL: SELECT "Landing_Outcome" , COUNT(*) AS "Count" FROM missions GROUP BY "Landing_Outcome" ;]
    (Background on this error at: https://sqlalche.me/e/20/e3q8)


### Task 8



##### List the   names of the booster_versions which have carried the maximum payload mass. Use a subquery



```python
%sql SELECT "Booster_Version" FROM missions WHERE "Payload_Mass" = (SELECT MAX("Payload_Mass") FROM missions);

```

     * sqlite:///my_data1.db
    (sqlite3.OperationalError) no such table: missions
    [SQL: SELECT "Booster_Version" FROM missions WHERE "Payload_Mass" = (SELECT MAX("Payload_Mass") FROM missions);]
    (Background on this error at: https://sqlalche.me/e/20/e3q8)


### Task 9


##### List the records which will display the month names, failure landing_outcomes in drone ship ,booster versions, launch_site for the months in year 2015.

**Note: SQLLite does not support monthnames. So you need to use  substr(Date, 6,2) as month to get the months and substr(Date,0,5)='2015' for year.**



```python
%sql 
SELECT 
    strftime('%m', "Date") AS "Month", 
    "Landing_Outcome", 
    "Booster_Version", 
    "Launch_Site"
FROM missions
WHERE SUBSTR("Date", 0, 5) = '2015'
  AND "Landing_Outcome" = 'Failure (drone ship)';

```


      Cell In[19], line 3
        strftime('%m', "Date") AS "Month",
        ^
    IndentationError: unexpected indent



### Task 10




##### Rank the count of landing outcomes (such as Failure (drone ship) or Success (ground pad)) between the date 2010-06-04 and 2017-03-20, in descending order.



```python
%sql SELECT "Landing_Outcome", COUNT(*) AS "Count" FROM missions WHERE "Date" BETWEEN '2010-06-04' AND '2017-03-20' GROUP BY "Landing_Outcome" ORDER BY "Count" DESC;

```

### Reference Links

* <a href ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20String%20Patterns%20-%20Sorting%20-%20Grouping/instructional-labs.md.html?origin=www.coursera.org">Hands-on Lab : String Patterns, Sorting and Grouping</a>  

*  <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Built-in%20functions%20/Hands-on_Lab__Built-in_Functions.md.html?origin=www.coursera.org">Hands-on Lab: Built-in functions</a>

*  <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sub-queries%20and%20Nested%20SELECTs%20/instructional-labs.md.html?origin=www.coursera.org">Hands-on Lab : Sub-queries and Nested SELECT Statements</a>

*   <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-3-SQLmagic.ipynb">Hands-on Tutorial: Accessing Databases with SQL magic</a>

*  <a href= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-4-Analyzing.ipynb">Hands-on Lab: Analyzing a real World Data Set</a>




## Author(s)

<h4> Lakshmi Holla </h4>


## Other Contributors

<h4> Rav Ahuja </h4>


<!--
## Change log
| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2024-07-10 | 1.1 |Anita Verma | Changed Version|
| 2021-07-09 | 0.2 |Lakshmi Holla | Changes made in magic sql|
| 2021-05-20 | 0.1 |Lakshmi Holla | Created Initial Version |
-->


## <h3 align="center"> © IBM Corporation 2021. All rights reserved. <h3/>

