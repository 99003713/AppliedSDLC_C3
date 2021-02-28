
***Need:***

To Analysis the performance of an individual student in their assessments we generated the report card so that the Faculty can track the performance of every student, Every student can also track their performance so to make a report We need to do a detailed analysis of Pre survey, Post survey, Pre-test marks, and post-test marks.

**Introduction:**

We are doing data analysis for determine the performance of Student and analyzing the field of improvement where the student need to be Improved also determining the strength or weakness of whole class in Different Module.

**Requirements:**

**High level Requirements:**

|**Requirement Id**|**Description** |
| :- | :- |
|Student Score|Score of a student in particular learning module|
|Average student |Average score of students in a particular module|
|Class max|Highest score of class in a module|
|Class min|Lowest score of class in a module|
|Student max|Maximum score of a student|
|Student min|Minimum score of a student|

**Lower-level Requirements:**          

|**Requirement Id**|**Description** |
| :- | :- |
|Top five|Top five score in a particular learning module|
|Bottom five|Bottom five score in a particular learning module|
|Difference of average and student|Difference of student score and average score of class|



** 


**Market Feasibility**: -

1. Statistical analysis software products are specialized programs designed to allow users to perform complex statistical analysis
1. Marking of scores in necessary to determine the overall performance of the individual also it is needed to determine the areas of the improvement where the individual need the improvement 
1. It is also needed to plot the graph of the evaluation so that it can easily be understood by the evaluator to evaluate
1. The scoring method is based on quality and productivity improvements or losses compared to a mid-point.
1. Rating Scales for Employees with Similar Jobs within the organization according to which the employee is put under projects
1. Score Analysis Software are used in the Banking sector, **higher education and healthcare** industrial use to determine the productivity
1. IBM SPSS Statics, JMP, Stata, Origin, GNU Octave etc. are some of the well renounced statistical software which are used in the industries and these software’s cost very high
1. **Manage large volumes of data, gain insight into company data and Better understand potential outcomes and scenarios**
1. **Regression analysis,** **Predictive analytics,** **Survival analysis,** **Time series analysis,** **Bayesian analysis and Decision trees are some of the statistical tools available on the market**






**SWOT:** 

![](https://github.com/99003713/AppliedSDLC_C3/blob/main/swot.png)




**4W H1**
1. ## 4W1H:
   1. ## What- Data analysis refers to the technique of collecting raw data, analyzing it and transforming it into information that can be used to reach a specific conclusion.
   1. ## Why- ***Data analysis*** provide you with more insights into your customers, allowing you to tailor customer service to their needs, provide more personalization and build stronger relationships with them.
   1. ## When- The systematic application of statistical and logical techniques to describe the data scope, modularize the data structure, condense the data representation, illustrate via images, tables, and graphs, and evaluate statistical inclinations, probability data, to derive meaningful conclusions,
   1. ## Where- Data Scientists and Analysts use data analytics techniques in their research, and businesses also use it to inform their decisions.
   1. ## How- It is a way of thinking and resolving the problems. Includes setting goals, collecting, cleaning, and analyzing data, then With We Check parameters like what benchmark to select for checking the quality of requirement
**Test Plan: -**

**Low Level**

|TEST ID|DESCRIPTION|EXPECTED INPUT|EXPECTED OUTPUT|<p>ACTUAL</p><p>OUTPUT</p>|
| :- | :- | :- | :- | :- |
|L\_01|<p>Check for the empty values</p><p>(requirement based)</p>|` `Leaves empty values in input module|Prompt display missing values|Missing value as 0|
|L\_02|<p>Check if the e-mail id is entered not correctly</p><p>(boundary based)</p>|Incorrect e-mail id|Prompt to display correct email address|Mail not sent due to wrong e-mail id|
|L\_03|<p>To check if multiple ID’s with same credentials display in same order depending on the alphabetic order</p><p>(scenario based)</p>|Scores resulting to same total values for multiple id’s|Id’s displayed in alphabetical order for same values|<p>Id’s displayed with corresponding marks in alphabetical order</p><p>successfully</p>|


**High Level**

|TEST ID|DESCRIPTION|EXPECTED INPUT|EXPECTED OUTPUT|<p>ACTUAL</p><p>OUTPUT</p>|
| :- | :- | :- | :- | :- |
|H\_O1|To check if the statistical analysis has produced all the required outputs such as max, medium, histogram, etc. (Requirement-based)|Input modules with all values within boundaries|Statistical analysis for all inputs|Produced statistical analytical results for all inputs successfully|
|H\_02|To check if e-mail is triggered to every stakeholder. (Scenario-based)|Module with e-mail IDs of stakeholders other than students|e-mail triggered to every stakeholder.|Mails not triggered to stakeholders other than students|
|H\_03|To check if the results are not more than input rows (Boundary-based)|Mark values of all students|Output rows same as input rows|Repetition of student IDs after input module integration|





