Comcast Telecom Consumer Complaints
Domain: Consumer

Objective:
Comcast is an American global telecommunication company. The firm has been providing terrible customer service. They continue to fall short despite repeated promises to improve. Only last month (October 2016) the authority fined them a $2.3 million, after receiving over 1000 consumer complaints.
The existing database will serve as a repository of public customer complaints filed against Comcast.
It will help to pin down what is wrong with Comcast's customer service.
Analysis to be done:
1.	Import data into Python environment.
2.	Provide the trend chart for the number of complaints at monthly and daily granularity levels.
3.	Provide a table with the frequency of complaint types.
4.	Which complaint types are maximum i.e., around internet, network issues, or across any other domains.
5.	Create a new categorical variable with value as Open and Closed. Open & Pending is to be categorized as Open and Closed & Solved is to be categorized as Closed.
6.	Provide state wise status of complaints in a stacked bar chart. Use the categorized variable from Q3. Provide insights on:
7.	Which state has the maximum complaints
8.	Which state has the highest percentage of unresolved complaints
9.	Provide the percentage of complaints resolved till date, which were received through the Internet and customer care calls.

Approach:

1.	Dataset can be imported to the environment using pandas data frames.
2.	Trend chart can be plotted using plot() function of matplotlib based on the Date column.
3.	Table with frequency of complaint types can be obtained by searching the column Customer Complaint sing regular expressions.
4.	Maximum can be obtained by getting the first element in a descending sorted list.
5.	Categorical variables can be created using data frames and if else loops.
6.	State wise complaint status can be plotted using plot.bar() function of matplotlib based on the categorical variable column.
7.	Maximum can be obtained by getting the first element in a descending sorted list.
8.	Unresolved complaints % can be obtained by total Open / total Count and by getting the first element in a descending sorted list.
9.	Complaints resolved variable and groupin can be created using data frames and conditional formatting and resolved complaints % can be obtained by total Closed / total Count
