<center><img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/images/SN_web_lightmode.png" alt="cognitiveclass.ai logo" width="300"/></center>

<h1 align="center">

<font size = 5>Assignment: Notebook for Graded Assessment</font>

</h1>

# Introduction

Using this Python notebook you will:

1.  Understand three Chicago datasets
2.  Load the three datasets into three tables in a SQLIte database
3.  Execute SQL queries to answer assignment questions

## Understand the datasets

To complete the assignment problems in this notebook you will be using three datasets that are available on the city of Chicago's Data Portal:

1.  <a href="https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01">Socioeconomic Indicators in Chicago</a>
2.  <a href="https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01">Chicago Public Schools</a>
3.  <a href="https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01">Chicago Crime Data</a>

### 1. Socioeconomic Indicators in Chicago

This dataset contains a selection of six socioeconomic indicators of public health significance and a “hardship index,” for each Chicago community area, for the years 2008 – 2012.

A detailed description of this dataset and the original dataset can be obtained from the Chicago Data Portal at:

[https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2](https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)

### 2. Chicago Public Schools

This dataset shows all school level performance data used to create CPS School Report Cards for the 2011-2012 school year. This dataset is provided by the city of Chicago's Data Portal.

A detailed description of this dataset and the original dataset can be obtained from the Chicago Data Portal at:

[https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t](https://data.cityofchicago.org/Education/Chicago-Public-Schools-Progress-Report-Cards-2011-/9xs2-f89t?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)

### 3. Chicago Crime Data

This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2001 to present, minus the most recent seven days.

A detailed description of this dataset and the original dataset can be obtained from the Chicago Data Portal at:

[https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork-20127838&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ)

### Download the datasets

This assignment requires you to have these three tables populated with a subset of the whole datasets.

In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet.

Use the links below to read the data files using the Pandas library.

-   Chicago Census Data

<https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01>

-   Chicago Public Schools

<https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01>

-   Chicago Crime Data

<https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01>

**NOTE:** Ensure you use the datasets available on the links above instead of directly from the Chicago Data Portal. The versions linked here are subsets of the original datasets and have some of the column names modified to be more database friendly which will make it easier to complete this assignment.

Execute the below code cell to avoid prettytable default error.

``` python
!pip install ipython-sql prettytable

import prettytable

prettytable.DEFAULT = 'DEFAULT'
```

```         
Collecting ipython-sql
  Downloading ipython_sql-0.5.0-py3-none-any.whl.metadata (17 kB)
Collecting prettytable
  Downloading prettytable-3.12.0-py3-none-any.whl.metadata (30 kB)
Requirement already satisfied: ipython in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (8.22.2)
Requirement already satisfied: sqlalchemy>=2.0 in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (2.0.30)
Collecting sqlparse (from ipython-sql)
  Downloading sqlparse-0.5.3-py3-none-any.whl.metadata (3.9 kB)
Requirement already satisfied: six in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (1.16.0)
Requirement already satisfied: ipython-genutils in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (0.2.0)
Requirement already satisfied: wcwidth in /opt/conda/lib/python3.11/site-packages (from prettytable) (0.2.13)
Requirement already satisfied: typing-extensions>=4.6.0 in /opt/conda/lib/python3.11/site-packages (from sqlalchemy>=2.0->ipython-sql) (4.12.2)
Requirement already satisfied: greenlet!=0.4.17 in /opt/conda/lib/python3.11/site-packages (from sqlalchemy>=2.0->ipython-sql) (3.0.3)
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
Downloading ipython_sql-0.5.0-py3-none-any.whl (20 kB)
Downloading prettytable-3.12.0-py3-none-any.whl (31 kB)
Downloading sqlparse-0.5.3-py3-none-any.whl (44 kB)
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m44.4/44.4 kB[0m [31m5.8 MB/s[0m eta [36m0:00:00[0m
[?25hInstalling collected packages: sqlparse, prettytable, ipython-sql
Successfully installed ipython-sql-0.5.0 prettytable-3.12.0 sqlparse-0.5.3
```

### Store the datasets in database tables

To analyze the data using SQL, it first needs to be loaded into SQLite DB. We will create three tables in as under:

1.  **CENSUS_DATA**
2.  **CHICAGO_PUBLIC_SCHOOLS**
3.  **CHICAGO_CRIME_DATA**

Load the `pandas` and `sqlite3` libraries and establish a connection to `FinalDB.db`

``` python
# Load the required libraries
!pip install pandas
!pip install sqlite3
import pandas as pd
import sqlite3

# Establish a connection to the SQLite database 'FinalDB.db'
conn = sqlite3.connect('FinalDB.db')

# Optional: Print a success message to confirm the connection
print("Connected to FinalDB.db successfully!")
```

```         
Collecting pandas
  Downloading pandas-2.2.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (89 kB)
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m89.9/89.9 kB[0m [31m10.4 MB/s[0m eta [36m0:00:00[0m
[?25hCollecting numpy>=1.23.2 (from pandas)
  Downloading numpy-2.2.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (62 kB)
[2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m62.0/62.0 kB[0m [31m7.7 MB/s[0m eta [36m0:00:00[0m
[?25hRequirement already satisfied: python-dateutil>=2.8.2 in /opt/conda/lib/python3.11/site-packages (from pandas) (2.9.0)
Requirement already satisfied: pytz>=2020.1 in /opt/conda/lib/python3.11/site-packages (from pandas) (2024.1)
Collecting tzdata>=2022.7 (from pandas)
  Downloading tzdata-2024.2-py2.py3-none-any.whl.metadata (1.4 kB)
Requirement already satisfied: six>=1.5 in /opt/conda/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)
Downloading pandas-2.2.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (13.1 MB)
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m13.1/13.1 MB[0m [31m110.0 MB/s[0m eta [36m0:00:00[0m00:01[0m0:01[0m
[?25hDownloading numpy-2.2.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.4 MB)
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m16.4/16.4 MB[0m [31m105.1 MB/s[0m eta [36m0:00:00[0m00:01[0m00:01[0m
[?25hDownloading tzdata-2024.2-py2.py3-none-any.whl (346 kB)
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m346.6/346.6 kB[0m [31m41.4 MB/s[0m eta [36m0:00:00[0m
[?25hInstalling collected packages: tzdata, numpy, pandas
Successfully installed numpy-2.2.1 pandas-2.2.3 tzdata-2024.2
[31mERROR: Could not find a version that satisfies the requirement sqlite3 (from versions: none)[0m[31m
[0m[31mERROR: No matching distribution found for sqlite3[0m[31m
[0mConnected to FinalDB.db successfully!
```

Load the SQL magic module

``` python
# Step 1: Install the package (if not already installed)
!pip install ipython-sql

# Step 2: Load the SQL magic module
%load_ext sql
```

```         
Requirement already satisfied: ipython-sql in /opt/conda/lib/python3.11/site-packages (0.5.0)
Requirement already satisfied: prettytable in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (3.12.0)
Requirement already satisfied: ipython in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (8.22.2)
Requirement already satisfied: sqlalchemy>=2.0 in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (2.0.30)
Requirement already satisfied: sqlparse in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (0.5.3)
Requirement already satisfied: six in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (1.16.0)
Requirement already satisfied: ipython-genutils in /opt/conda/lib/python3.11/site-packages (from ipython-sql) (0.2.0)
Requirement already satisfied: typing-extensions>=4.6.0 in /opt/conda/lib/python3.11/site-packages (from sqlalchemy>=2.0->ipython-sql) (4.12.2)
Requirement already satisfied: greenlet!=0.4.17 in /opt/conda/lib/python3.11/site-packages (from sqlalchemy>=2.0->ipython-sql) (3.0.3)
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
The sql extension is already loaded. To reload it, use:
  %reload_ext sql
```

Use `Pandas` to load the data available in the links above to dataframes. Use these dataframes to load data on to the database `FinalDB.db` as required tables.

``` python
# Example URLs (replace with actual links)
url1 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCensusData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01"
url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoPublicSchools.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01v"
url3 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01"
# Load data into DataFrames
census = pd.read_csv(url1)
school = pd.read_csv(url2)
crime = pd.read_csv(url3)
# Display the first few rows of each DataFrame
print(crime.head())
```

```         
         ID CASE_NUMBER        DATE                     BLOCK IUCR  \
0   3512276    HK587712  2004-08-28        047XX S KEDZIE AVE  890   
1   3406613    HK456306  2004-06-26  009XX N CENTRAL PARK AVE  820   
2   8002131    HT233595  2011-04-04        043XX S WABASH AVE  820   
3   7903289    HT133522  2010-12-30      083XX S KINGSTON AVE  840   
4  10402076    HZ138551  2016-02-02           033XX W 66TH ST  820   

  PRIMARY_TYPE                    DESCRIPTION          LOCATION_DESCRIPTION  \
0        THEFT                  FROM BUILDING            SMALL RETAIL STORE   
1        THEFT                 $500 AND UNDER                         OTHER   
2        THEFT                 $500 AND UNDER  NURSING HOME/RETIREMENT HOME   
3        THEFT  FINANCIAL ID THEFT: OVER $300                     RESIDENCE   
4        THEFT                 $500 AND UNDER                         ALLEY   

   ARREST  DOMESTIC  ...  DISTRICT  WARD  COMMUNITY_AREA_NUMBER  FBICODE  \
0   False     False  ...         9  14.0                   58.0        6   
1   False     False  ...        11  27.0                   23.0        6   
2   False     False  ...         2   3.0                   38.0        6   
3   False     False  ...         4   7.0                   46.0        6   
4   False     False  ...         8  15.0                   66.0        6   

  X_COORDINATE  Y_COORDINATE  YEAR   LATITUDE  LONGITUDE  \
0    1155838.0     1873050.0  2004  41.807440 -87.703956   
1    1152206.0     1906127.0  2004  41.898280 -87.716406   
2    1177436.0     1876313.0  2011  41.815933 -87.624642   
3    1194622.0     1850125.0  2010  41.743665 -87.562463   
4    1155240.0     1860661.0  2016  41.773455 -87.706480   

                        LOCATION  
0    (41.8074405, -87.703955849)  
1  (41.898279962, -87.716405505)  
2  (41.815933131, -87.624642127)  
3  (41.743665322, -87.562462756)  
4  (41.773455295, -87.706480471)  

[5 rows x 21 columns]
```

Establish a connection between SQL magic module and the database `FinalDB.db`

``` python

# Step 3: Connect to your SQLite database
%sql sqlite:///FinalDB.db
```

You can now proceed to the the following questions. Please note that a graded assignment will follow this lab and there will be a question on each of the problems stated below. It can be from the answer you received or the code you write for this problem. Therefore, please keep a note of both your codes as well as the response you generate.

## Problems

Now write and execute SQL queries to solve assignment problems

### Problem 1

##### Find the total number of crimes recorded in the CRIME table.

``` python
# Step 3: Create SQLite database and load the data
conn = sqlite3.connect('ChicagoData.db')

# Load the DataFrames into SQLite database tables
census.to_sql('CENSUS', conn, if_exists='replace', index=False)
school.to_sql('SCHOOL', conn, if_exists='replace', index=False)
crime.to_sql('CRIME', conn, if_exists='replace', index=False)
# Step 4: Query to find the total number of crimes recorded in the CRIME table
query = "SELECT COUNT(*) AS Total_Crimes FROM CRIME;"
result = pd.read_sql(query, conn)

# Display the result
print("Total number of crimes recorded in the CRIME table:")
print(result)
conn.close()
```

```         
Total number of crimes recorded in the CRIME table:
   Total_Crimes
0           533
```

### Problem 2

##### List community area names and numbers with per capita income less than 11000.

``` python
# Step 1: Connect to the SQLite database
conn = sqlite3.connect('ChicagoData.db')

# Step 2: Write and execute the SQL query
query = """
SELECT 
    Community_Area_Number, 
    Community_Area_Name, 
    Per_Capita_Income 
FROM 
    CENSUS 
WHERE 
    Per_Capita_Income < 11000;
"""

# Fetch the result as a Pandas DataFrame
result = pd.read_sql(query, conn)

# Display the result
print("Community areas with per capita income less than $11,000:")
print(result)

# Step 3: Close the connection
conn.close()
```

```         
Community areas with per capita income less than $11,000:
   COMMUNITY_AREA_NUMBER COMMUNITY_AREA_NAME  PER_CAPITA_INCOME
0                   26.0  West Garfield Park              10934
1                   30.0      South Lawndale              10402
2                   37.0         Fuller Park              10432
3                   54.0           Riverdale               8201
```

### Problem 3

##### List all case numbers for crimes involving minors?(children are not considered minors for the purposes of crime analysis)

``` python
# Step 1: Connect to the SQLite database
conn = sqlite3.connect('ChicagoData.db')

# Step 2: Write and execute the SQL query
query = """
SELECT 
    Case_Number 
FROM 
    CRIME 
WHERE 
    Description LIKE '%minor%';
"""

# Fetch the result as a Pandas DataFrame
result = pd.read_sql(query, conn)

# Display the result
print("Case numbers for crimes involving minors:")
print(result)

# Step 3: Close the connection
conn.close()
```

```         
Case numbers for crimes involving minors:
  CASE_NUMBER
0    HL266884
1    HK238408
```

### Problem 4

##### List all kidnapping crimes involving a child?

``` python
# Step 1: Connect to the SQLite database
conn = sqlite3.connect('ChicagoData.db')

# Step 2: Write and execute the SQL query
query = """
SELECT 
     *
FROM 
    CRIME 
WHERE 
    PRIMARY_TYPE LIKE 'KIDNAPPING';
"""

# Fetch the result as a Pandas DataFrame
result = pd.read_sql(query, conn)

# Display the result
print("Case numbers for crimes involving minors:")
print(result)

# Step 3: Close the connection
conn.close()
```

```         
Case numbers for crimes involving minors:
        ID CASE_NUMBER        DATE                 BLOCK  IUCR PRIMARY_TYPE  \
0  5276766    HN144152  2007-01-26  050XX W VAN BUREN ST  1792   KIDNAPPING   

                DESCRIPTION LOCATION_DESCRIPTION  ARREST  DOMESTIC  ...  \
0  CHILD ABDUCTION/STRANGER               STREET       0         0  ...   

   DISTRICT  WARD  COMMUNITY_AREA_NUMBER  FBICODE X_COORDINATE  Y_COORDINATE  \
0        15  29.0                   25.0       20    1143050.0     1897546.0   

   YEAR   LATITUDE  LONGITUDE                       LOCATION  
0  2007  41.874908 -87.750249  (41.874908413, -87.750249307)  

[1 rows x 21 columns]
```

### Problem 5

##### List the kind of crimes that were recorded at schools. (No repetitions)

``` python
# Step 1: Connect to the SQLite database
conn = sqlite3.connect('ChicagoData.db')

# Step 2: Write and execute the SQL query
query = """
SELECT 
     PRIMARY_TYPE
FROM 
    CRIME 
WHERE 
    LOCATION_DESCRIPTION LIKE 'SCHOOL%';
"""

# Fetch the result as a Pandas DataFrame
result = pd.read_sql(query, conn)

# Display the result
print("Case numbers for crimes involving minors:")
print(result)

# Step 3: Close the connection
conn.close()
```

```         
Case numbers for crimes involving minors:
              PRIMARY_TYPE
0                  BATTERY
1                  BATTERY
2                  BATTERY
3                  BATTERY
4                  BATTERY
5          CRIMINAL DAMAGE
6                NARCOTICS
7                NARCOTICS
8                  ASSAULT
9        CRIMINAL TRESPASS
10  PUBLIC PEACE VIOLATION
11  PUBLIC PEACE VIOLATION
```

### Problem 6

##### List the type of schools along with the average safety score for each type.

``` python
import pandas as pd
import sqlite3

# Step 1: Connect to the SQLite database
conn = sqlite3.connect('ChicagoData.db')

# Step 2: Write and execute the SQL query
query = """
SELECT 
    "Elementary, Middle, or High School" AS School_Type,
    AVG(Safety_Score) AS Average_Safety_Score
FROM 
    SCHOOL
GROUP BY 
    "Elementary, Middle, or High School";
"""

# Fetch the result as a Pandas DataFrame
result = pd.read_sql(query, conn)

# Display the result
print("School types and their average safety scores:")
print(result)

# Step 3: Close the connection
conn.close()
```

```         
School types and their average safety scores:
  School_Type  Average_Safety_Score
0          ES             49.520384
1          HS             49.623529
2          MS             48.000000
```

### Problem 7

##### List 5 community areas with highest % of households below poverty line

``` python
import pandas as pd
import sqlite3

# Step 1: Connect to the SQLite database
conn = sqlite3.connect('ChicagoData.db')

# Step 2: Write and execute the SQL query
query = """
SELECT 
    Community_Area_Number, 
    Community_Area_Name, 
    Percent_Households_Below_Poverty 
FROM 
    CENSUS 
ORDER BY 
    Percent_Households_Below_Poverty DESC 
LIMIT 5;
"""

# Fetch the result as a Pandas DataFrame
result = pd.read_sql(query, conn)

# Display the result
print("Top 5 community areas with highest percentage of households below poverty line:")
print(result)

# Step 3: Close the connection
conn.close()
```

```         
Top 5 community areas with highest percentage of households below poverty line:
   COMMUNITY_AREA_NUMBER COMMUNITY_AREA_NAME  PERCENT_HOUSEHOLDS_BELOW_POVERTY
0                   54.0           Riverdale                              56.5
1                   37.0         Fuller Park                              51.2
2                   68.0           Englewood                              46.6
3                   29.0      North Lawndale                              43.1
4                   27.0  East Garfield Park                              42.4
```

### Problem 8

##### Which community area is most crime prone? Display the coumminty area number only.

``` python
# Step 1: Connect to the SQLite database
conn = sqlite3.connect('ChicagoData.db')

# Step 2: Write and execute the SQL query
query = """
SELECT 
    Community_Area AS Community_Area_Number
FROM 
    CRIME
GROUP BY 
    Community_Area
ORDER BY 
    COUNT(*) DESC
LIMIT 1;
"""

# Fetch the result as a Pandas DataFrame
result = pd.read_sql(query, conn)

# Display the result
print("Top 5 community areas with highest percentage of households below poverty line:")
print(result)

# Step 3: Close the connection
conn.close()
```

```         
---------------------------------------------------------------------------

OperationalError                          Traceback (most recent call last)

File /opt/conda/lib/python3.11/site-packages/pandas/io/sql.py:2674, in SQLiteDatabase.execute(self, sql, params)
   2673 try:
-> 2674     cur.execute(sql, *args)
   2675     return cur


OperationalError: no such column: Community_Area


The above exception was the direct cause of the following exception:


DatabaseError                             Traceback (most recent call last)

Cell In[18], line 18
      5 query = """
      6 SELECT 
      7     Community_Area AS Community_Area_Number
   (...)
     14 LIMIT 1;
     15 """
     17 # Fetch the result as a Pandas DataFrame
---> 18 result = pd.read_sql(query, conn)
     20 # Display the result
     21 print("Top 5 community areas with highest percentage of households below poverty line:")


File /opt/conda/lib/python3.11/site-packages/pandas/io/sql.py:706, in read_sql(sql, con, index_col, coerce_float, params, parse_dates, columns, chunksize, dtype_backend, dtype)
    704 with pandasSQL_builder(con) as pandas_sql:
    705     if isinstance(pandas_sql, SQLiteDatabase):
--> 706         return pandas_sql.read_query(
    707             sql,
    708             index_col=index_col,
    709             params=params,
    710             coerce_float=coerce_float,
    711             parse_dates=parse_dates,
    712             chunksize=chunksize,
    713             dtype_backend=dtype_backend,
    714             dtype=dtype,
    715         )
    717     try:
    718         _is_table_name = pandas_sql.has_table(sql)


File /opt/conda/lib/python3.11/site-packages/pandas/io/sql.py:2738, in SQLiteDatabase.read_query(self, sql, index_col, coerce_float, parse_dates, params, chunksize, dtype, dtype_backend)
   2727 def read_query(
   2728     self,
   2729     sql,
   (...)
   2736     dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",
   2737 ) -> DataFrame | Iterator[DataFrame]:
-> 2738     cursor = self.execute(sql, params)
   2739     columns = [col_desc[0] for col_desc in cursor.description]
   2741     if chunksize is not None:


File /opt/conda/lib/python3.11/site-packages/pandas/io/sql.py:2686, in SQLiteDatabase.execute(self, sql, params)
   2683     raise ex from inner_exc
   2685 ex = DatabaseError(f"Execution failed on sql '{sql}': {exc}")
-> 2686 raise ex from exc


DatabaseError: Execution failed on sql '
SELECT 
    Community_Area AS Community_Area_Number
FROM 
    CRIME
GROUP BY 
    Community_Area
ORDER BY 
    COUNT(*) DESC
LIMIT 1;
': no such column: Community_Area
```

Double-click **here** for a hint

```{=html}
<!--
Query for the 'community area number' that has most number of incidents
-->
```
### Problem 9

##### Use a sub-query to find the name of the community area with highest hardship index

``` python
# Step 1: Connect to the SQLite database
conn = sqlite3.connect('ChicagoData.db')

# Step 2: Write and execute the SQL query with a sub-query
query = """
SELECT 
    Community_Area_Name 
FROM 
    CENSUS
WHERE 
    Hardship_Index = (
        SELECT 
            MAX(Hardship_Index) 
        FROM 
            CENSUS
    );
"""

# Fetch the result as a Pandas DataFrame
result = pd.read_sql(query, conn)

# Display the result
print("Community area with the highest hardship index:")
print(result)

# Step 3: Close the connection
conn.close()
```

```         
Community area with the highest hardship index:
  COMMUNITY_AREA_NAME
0           Riverdale
```

### Problem 10

##### Use a sub-query to determine the Community Area Name with most number of crimes?

``` python
# Step 1: Connect to the SQLite database
conn = sqlite3.connect('ChicagoData.db')

# Step 2: Write and execute the SQL query with a sub-query
query = """
SELECT 
    CENSUS.Community_Area_Name 
FROM 
    CENSUS
WHERE 
    CENSUS.Community_Area_Number = (
        SELECT 
            Community_Area 
        FROM 
            CRIME
        GROUP BY 
            Community_Area
        ORDER BY 
            COUNT(*) DESC
        LIMIT 1
    );
"""

# Fetch the result as a Pandas DataFrame
result = pd.read_sql(query, conn)

# Display the result
print("Community Area Name with the most number of crimes:")
print(result)

# Step 3: Close the connection
conn.close()
```

```         
---------------------------------------------------------------------------

OperationalError                          Traceback (most recent call last)

File /opt/conda/lib/python3.11/site-packages/pandas/io/sql.py:2674, in SQLiteDatabase.execute(self, sql, params)
   2673 try:
-> 2674     cur.execute(sql, *args)
   2675     return cur


OperationalError: no such column: Community_Area


The above exception was the direct cause of the following exception:


DatabaseError                             Traceback (most recent call last)

Cell In[20], line 25
      5 query = """
      6 SELECT 
      7     CENSUS.Community_Area_Name 
   (...)
     21     );
     22 """
     24 # Fetch the result as a Pandas DataFrame
---> 25 result = pd.read_sql(query, conn)
     27 # Display the result
     28 print("Community Area Name with the most number of crimes:")


File /opt/conda/lib/python3.11/site-packages/pandas/io/sql.py:706, in read_sql(sql, con, index_col, coerce_float, params, parse_dates, columns, chunksize, dtype_backend, dtype)
    704 with pandasSQL_builder(con) as pandas_sql:
    705     if isinstance(pandas_sql, SQLiteDatabase):
--> 706         return pandas_sql.read_query(
    707             sql,
    708             index_col=index_col,
    709             params=params,
    710             coerce_float=coerce_float,
    711             parse_dates=parse_dates,
    712             chunksize=chunksize,
    713             dtype_backend=dtype_backend,
    714             dtype=dtype,
    715         )
    717     try:
    718         _is_table_name = pandas_sql.has_table(sql)


File /opt/conda/lib/python3.11/site-packages/pandas/io/sql.py:2738, in SQLiteDatabase.read_query(self, sql, index_col, coerce_float, parse_dates, params, chunksize, dtype, dtype_backend)
   2727 def read_query(
   2728     self,
   2729     sql,
   (...)
   2736     dtype_backend: DtypeBackend | Literal["numpy"] = "numpy",
   2737 ) -> DataFrame | Iterator[DataFrame]:
-> 2738     cursor = self.execute(sql, params)
   2739     columns = [col_desc[0] for col_desc in cursor.description]
   2741     if chunksize is not None:


File /opt/conda/lib/python3.11/site-packages/pandas/io/sql.py:2686, in SQLiteDatabase.execute(self, sql, params)
   2683     raise ex from inner_exc
   2685 ex = DatabaseError(f"Execution failed on sql '{sql}': {exc}")
-> 2686 raise ex from exc


DatabaseError: Execution failed on sql '
SELECT 
    CENSUS.Community_Area_Name 
FROM 
    CENSUS
WHERE 
    CENSUS.Community_Area_Number = (
        SELECT 
            Community_Area 
        FROM 
            CRIME
        GROUP BY 
            Community_Area
        ORDER BY 
            COUNT(*) DESC
        LIMIT 1
    );
': no such column: Community_Area
```

## Author(s)

<h4>Hima Vasudevan</h4>

<h4>Rav Ahuja</h4>

<h4>Ramesh Sannreddy</h4>

## Contribtuor(s)

<h4>Malika Singla</h4>

<h4>Abhishek Gagneja</h4>

```{=html}
<!--
## Change log

| Date       | Version | Changed by        | Change Description                             |
| ---------- | ------- | ----------------- | ---------------------------------------------- |
|2023-10-18  | 2.6     | Abhishek Gagneja  | Modified instruction set |
| 2022-03-04 | 2.5     | Lakshmi Holla     | Changed markdown.                   |
| 2021-05-19 | 2.4     | Lakshmi Holla     | Updated the question                           |
| 2021-04-30 | 2.3     | Malika Singla     | Updated the libraries                          |
| 2021-01-15 | 2.2     | Rav Ahuja         | Removed problem 11 and fixed changelog         |
| 2020-11-25 | 2.1     | Ramesh Sannareddy | Updated the problem statements, and datasets   |
| 2020-09-05 | 2.0     | Malika Singla     | Moved lab to course repo in GitLab             |
| 2018-07-18 | 1.0     | Rav Ahuja         | Several updates including loading instructions |
| 2018-05-04 | 0.1     | Hima Vasudevan    | Created initial version                        |
-->
```
\##

<h3 align="center">

© IBM Corporation 2023. All rights reserved.

<h3/>
