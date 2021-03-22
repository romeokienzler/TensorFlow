
# Flights - README

## Summary
This dataset reports flights in the United States, including carriers, arrival and departure delays, and reasons for delays, for 2008. This dataset was obtained from the **RITA** (Research and Technology Bureau of Transportation Statistics) found [here](https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp).

## Getting Started
### Dependencies
- Windows 10
- Python 3


### Libraries
- pandas
- numpy
- matplotlib
- seaborn
- calendar


## Steps
### 1. Assess the data
I started this project by importing essential packages and reading the **.csv** file. Then, using common data assessing code, I found that the data set is very large. I decided to use a sample of the full data set to save some time.
I decided that I wanted to focus on flight delays and cancellations.

### 2. Univariate Exploration
I began my univariate exploration by looking at how many domestic flights there were in the United States based on day of week, month, and day of year. Then, I looked at percentage of flight cancellations. Finally, I looked at duration of some type of delay.

### 3. Bivariate Exploration
I focused my bivariate exploration on the relationship between delays/cancellations and month/day of week.

### 4. Multivariate Exploration
I focused my multivariate exploration on the relationship between average lengths of some type of delay/type of cancellation and month/day of week.


## Main Findings
## Results

### Univariate Exploration
#### Total Flights by Month
Most flights occur in the months of Mar and May. the least flights are in the month Jul.

#### Total Flights by Day of Week
Most flights occur on Thursday. Saturday have the least number of flights

#### Percentage of Flights that are Cancelled
2.31% of all flights are cancelled. That is almost two flights per one hundred.

#### Causes of Flight Cancellations
The most common cause of flight cancellations is carrier.

#### Length of Carrier Delays
Carrier delays are most commonly 1-8 minutes long

### Bivariate Exploration
#### Cancellation cf. Month
Flights are most commonly cancelled in Feb. Flights are least commonly cancelled in Jul.

#### Weather Delay cf. Month
Flights experience weather delays most commonly in Mar. Flights are least commonly delayed by weather in Jul.

#### Cancellations cf. Day of Week
Flights are most commonly cancelled on Wednesday. Flights are least commonly cancelled on Saturdays.

#### NAS Delay cf. Day of Week
Flights experience NAS delays most commonly on Tuesday. Flights are least commonly delayed by carrier on Wednesday

#### Late Aircraft Delay cf. Day of Week
Flights experience late aircraft delays most commonly on Sunday. Flights are least commonly delayed by late aircraft carriers on Wednesday.

### Multivariate Exploration
#### Types of Cancellations by Month
Carrier is the most common monthly cause for flight cancellations, followed by weather. NAS cancellations are the least common cause for cancellations for all months.

#### Average Length of Delays by Month
carrier and late Aircraft delays have the longest average duration of delay of total monthly flights amd Weather has the shortest duration of delay of total monthly flights.

#### Types of Cancellations by Day of Week
carrier is the most common weekly cause for flight cancellations, followed by Weather. NAS cancellations are the least common cause for cancellations for all days of the week.

#### Average Length of Delays by Day of Week
NAS and late carrier delays had the longest average delay length. Weather delays had the shortest average delay length for all days of the week

#### Percent of Flights Delayed by Type and Day of Week
Results were similar to that of types of delays by week where weather and late Aircraft delays have the highest percentage of delays of total weekly flights and Weather has the least percentage of delays of total weekly flights.