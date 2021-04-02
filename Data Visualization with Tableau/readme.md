Sales Performance Analysis
Domain: Ecommerce

Objective:
Mike Goodman, the head of Product Management of a retail products company, is responsible for determining which products his company should continue to offer for sale and which products should be discontinued from the company’s product catalog. 
To build a dashboard that will present monthly sales performance by product segment and product category to help client identifying the segments and categories that have met or exceeded their sales targets, as well as those that have not met their sales targets.
Analysis to be done:
1.	Use the Saved Sample – Superstore dataset. 
2.	Create a bullet chart with Category and Segment dimensions and Sales measures. 
3.	Blend the data with the Saved Sample - Sales Target data set to bring in the Sales Target measure. 
4.	Color code the chart to identify Categories and Segments that are above or below target. 
5.	Add the year of sales to the view to identify trends and outliers. 
6.	Add a filter so that the user can select one, more than one, or all years. 
7.	Create a dashboard with this view.
Approach:
1. We can connect to a Microsoft excel file and open the Sample – Superstore dataset.
2. By referring to the template given in the question we can add category dimension, sales measure in columns and segment, order date dimensions drilled down to the month level.
3. We can add a new data source and blend the Sample - Sales Target data with the Sample – Superstore data, and bring in the Sales Target measure to the detail in the marks pane and add a reference line (distribution to represent the Target Sales (grey) over the actual Sales) to represent the template given.
4. We can simply create a Calculated field where in if the sum of actual sales is above the target sales then it can be marked as ‘Above Target’ else it can be marked as ‘Below Target’ and assign appropriate colors to both of them.
5. Order date which contains Year of sales can be added into the visualization.
6. The same Order date dimension -> #year can be added to the filter and all years can be chosen so that the user is free to choose one, more than one, or all years for which sales is displayed.
7. A simple suitably named dashboard can be created using the sheet we just created above.
