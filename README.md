## Repository URL 
[Repository](https://github.com/ucl-comp0035/comp0034-cw1-g-group-v-gruppe-tiger.git)

## Set-up instructions
Assume that requirements will be installed from requirements.txt.


## Problem definition
Investing in a start-up business entity is considered as high-risk investment [1]. This is because a lot of resources is 
required for the entity to carry out its operation and the uncertainty of the entity survivability period may influence 
the investors’ or entrepreneurs’ earnings or loss. As of 2021, 60% of the businesses in the UK fail within their first 
3 years, which imply that most businesses usually failed in the early stage of their course of operations. This can 
severely cripple someone financially, leading to additional social issues such as bankruptcy and unemployment. 
However, through careful planning and analysing of data, we can cultivate a thriving environment for the business to 
operate in, increasing its chances of long-term survival and profitability. Data on businesses demographics and their 
survival rate is available on the London Database[2], which we can implement in our project. 

Our target audience are entrepreneurs and businessmen looking to invest in or create a start-up and are likely 
acquainted with data driven applications such as trading platforms. We can use this familiarity to create an app that 
will utilise data science and software development to develop a dashboard. This will show how the survival rate, life 
expectancy and the trends of businesses varies between different locations in the UK. This project will provide a means 
for our target audience to gather information and make better and logical financial decisions when choosing a suitable 
location for their business.

### Target audience
[persona](coursework-1-JYTan-bot-master(1)/assets/Persona.pptx)

### Questions to be answered
a.	What is the survival rate of businesses in different areas?

b.	Which is the best and worst areas to start a business?

c.	How long is the life expectancy of businesses in the area?

d.	Is there a trend of increasing or decreasing life expectancy over the years?

## Web Apps Features and descriptions

The web apps encompass with few simple layouts/features listed as follows:

• Homepage

The homepage of the web apps describe the overview of what kind of information that users or the target audiences 
can obtain. The type of information that the target audiences or users intended to view are stored in the subpage or
subsection on the navigation bar, which categorized by the survival rate based on 'Area', 'Year', and in Choropleth 
'Map' format. In addition to this, for the ease of the users to view the required information quickly, the homepage is 
designed to consist of shortcut or direct link that route towards respective subsections or subpages. 


• Navigation bar/ Navigation menu

The menu bar allows the users to easily navigate to the page that they intend to view. It consists of quick search bar 
and three subpages that store the graphical information about the business survival rate of the UK enterprise with 
respect to 'Area', 'Year' and in the Choropleth 'Map' format/view. When the browser screen view is minimised, the 
search bar along with the three subpage/module will turn into a hamburger button or 3 lines button. In this case, 
clicking it will reveal all the modules/subsections horizontally.

• Search bar

The search bar is a subunit or feature on the Navigation bar. The function of this feature is to allow the users or 
target audience to quickly search or query information they intended to view by entering the keyword on the placeholder. 
However, the query in current stage not yet been developed. 


• Area page module

This is a sub-module page storing and show graphical information regarding the survival rate of the UK's business 
entities with respect to the area they set up for trading. 


• Year page module

Another sub-module page revealing the graphical information regarding the longevity of the business entities in the UK 
for different period of time 


• Map page module

This sub-module page is storing and displayed the UK's business survival rate in a geographical map. 


## Explanation of each visualisation

### Area module page

*• Dual Input Bar Chart:*

The bar chart shows the how's the UK business survival rate changes at different area for a specific year and the period 
of the business longevity. This chart enables the target audience or user to freely customise the period of 
survivability of a business and year to visualise what is the survival rate of the business entities in a specific 
region in UK. The chart consists of unique colours to highlight the area with the highest and lowest survival rate, 
allowing the target audience or user to determine which is the best location to start up their business.   

Answers to question: a. and b. 

*• Single Input Grouped Bar Chart:*

The grouped bar chart revealed the different longevity of business survival rate at different area in UK. The year can 
be customised to allow the user or target audience to visualise, compare, analyse and anticipate how long can the 
entities survive in the specific area relative to the other. From this chart, the investor can also understand the 
economic conditions and developments between different region. 

Answers to question: a. b. and c.

*• Reasoning for selecting Bar chart*

Bar chart enables the users to view and make comparison between business survival rate at different areas and also the 
longitivty



**Conclusion**

It can be observed from the figure that the survival rate is decreasing year by year,
also the difference between the survival rate of different regions in the same survival rate year is generally not more than 20%.
In the fifth survival rate year, the highest survival rate is always 45%-55%.
While the lowest survival rate areas are often between 25% and 35%, 
but there was an exception, in 2005, Newham's fifth-year survival rate was only 16%.

### Year module page
*• Single Input line chart:*

The line chart depicts the variation in the UK's business survival rate of different longevity in different birth year. 
The chart enable the area of business to be tailored to view how's the trend of the business survival rate in a certain 
region changes over the year, providing the investors an understanding of how's the economic condition of that specific
area, and hence enable them to forecast whether when is the right time to start up or expand their business for a 
particular area.  

Answer to question: d.


**Conclusion**

From the line chart, the survival rate of cities 
has not changed much because of the change of birth year, except for London.
In London, taking 2008 as the boundary, 
the survival rate before 2008 was higher than the survival rate after 2008 by more than 10%, 
especially in 2008, the survival rate was particularly low.

### Choropleth Map module page

*• Dual Input Choropleth Map* 

The map illustrates the business survival rate in different district area for a given birth years and business longevity  
time period. On the map, different colour scale represent different survival rate. For district area that are bound by 
lighter color scale indicate that the particular area has lower survival rate. In contrast, the district area that are 
bounded by darker colour scale indicate that the particular area has higher survival rate. This pictorial chart may seem
similar to the bar chart plotted on the area module page, however sometimes geographical mapping provides a better 
understanding compare to the chart plotted in graphical format, which help the users to make a better decision in 
choosing the most appropriate business area to start-up.    


Answers to question: a. and b.


Survival rate maps show the survival rate in the 5th year at different regions for companies in different birth years. 
These graphs are able to answer the questions a and b above. 
On these maps, different colors are used to express different survival rates, 
the lighter the color, the lower the survival rate, and vice versa. They intuitively show the living conditions of enterprises for different regions.
Helps the investors understand the location of the company as investing.

**Conclusion**

The survival rate map shows that in most cases, 
the survival rate in London is very low, and often the lowest.
And with London as the center, the survival rate of enterprises closer to the periphery is higher.

## Evaluation of web apps and visualisation 

Current webapps consists of very basic and simple features that barely satisfied the target's user need. However, there 
is still room for improvement. The first point of the improvement would be on search bar. A good search should be able 
to use keywords for query, but in current phase of development, the query function is not yet fully-developed. The 
reason for this is that the creation query database is currently beyond the study scope dated in week 5, hence the 
database were not being developed. 

The second point of improvement is related to line chart on the Year module page. It was observed that for year beyond 
2014, the survival rate in the line chart drop to zero, except for the 1-year survival rate category. The zero value do 
not imply that the survival rate is zero, but it simply means that there was no available data beyond 2014. One 
improvement can be done is by setting limit for year. 

The last point of improvement is to add a login and sign up module on the navigation bar, so that the information was 
not provided to external users for free. The reason this module was not create is due to fact that the login credential 
database will be learnt in the incoming lecture. 



## Testing 
Continuous integration pipeline had been setup on github action creating a workflow that test our pytest and code using 
flake8 linter. Several unit test had also been made to check the code of the website 


## References

[1] Kepka, A., 2021. Business Startup Statistics UK (2021 Update) | Fundsquire. [online] Fundsquire UK. Available at: <https://fundsquire.co.uk/startup-statistics/> [Accessed 2 November 2021].<br />
[2] Data.london.gov.uk. 2021. Business Demographics and Surviva  l Rates, Borough – London Datastore. [online] Available at: <https://data.london.gov.uk/dataset/business-demographics-and-survival-rates-borough> [Accessed 2 November 2021].

