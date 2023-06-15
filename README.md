# Data Science Salary Estimator: Project Overview
•	Created a tool that estimates data science salaries (MAE - $ 11K) to help data scientists negotiate their income when they get a job.

•	Scraped over 1000 job descriptions from glassdoor using python and selenuim.

•	Engineered features from the text of each job description to quantify the value companies put on Python, SQL, R, Excel , AWS and Spark.

•	Optimized Linear, Lasso and Random Forest Regressors using GridSearchCV to reach out the best model.

•	Built a client facing API using flask

### Code and Resources Used
##
**Python Version**: 3.11
**Packages Used**:Pandas, Numpy, Sklearn, Seaborn, Selenium, Flask, Json, Pickle\
**For Web Framework Requirements**:`pip install -r requirements.txt`\
**Scrapper Github**: https://github.com/arapfaik/scraping-glassdoor-selenium \
**Scrapper Article**: https://mersakarya.medium.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

### Web Scrapping
##
Tweaked the web scrapper repo to scrape 1000 job postings from glassdoor.com. With each job, we got the following:

+ Job title
