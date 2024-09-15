<img src="readme/title1.svg"/>

<br><br>

<!-- project philosophy -->
<img src="readme/title2.svg"/>

> A data project based on Recidivism and Crimes records to uncover its results affected by a set of individual history and public factors.
>
>  Recidivism Radar, leverages advanced data analytics to understand and predict patterns of recidivism within the criminal justice system. By integrating comprehensive datasets encompassing socioeconomics, poverty, population demographics, and crime statistics, it aims to uncover critical insights that influence recidivism rates over time.

### User Stories
- As a researcher, I want to analyze recidivism trends over time, so I can identify patterns and key factors influencing recidivism rates.
- As a policymaker, I want to visualize socioeconomic and demographic data using interactive dashboards, so I can understand the underlying causes of recidivism and inform policy decisions.
- As a law enforcement officer, I want to explore real-time insights on recidivism rates using Power BI, so I can allocate resources effectively and reduce repeat offenses.

<br><br>
<!-- Tech stack -->
<img src="readme/title3.svg"/>

###  Recidivism Radar is built using the following technologies:

- Python: Python is the core programming language used for data analysis, machine learning, and building predictive models. It allows us to efficiently process and analyze large datasets related to recidivism, socioeconomics, and crime.
- SQL: SQL is used to manage and query the data warehouse, enabling the extraction of relevant data such as demographic information, crime statistics, and socioeconomic factors for further analysis and reporting.
- Power BI: Power BI is employed for data visualization and reporting. It provides interactive dashboards that display time series trends and insights into recidivism rates, allowing stakeholders to explore the data dynamically.


<br><br>



### Mockups
| Home screen  | Menu Screen | Order Screen |
| ---| ---| ---|
| ![Landing](./readme/demo/1440x1024.png) | ![fsdaf](./readme/demo/1440x1024.png) | ![fsdaf](./readme/demo/1440x1024.png) |

<br><br>

<!-- Data warehouse Design -->
<img src="readme/title5.svg"/>

###  Architecting Data Excellence: Innovative Data warehouse Design Strategies:

- Insert ER Diagram here


<br><br>


<!-- Implementation -->
<img src="readme/title6.svg"/>


### User Screens (Mobile)
| Login screen  | Register screen | Landing screen | Loading screen |
| ---| ---| ---| ---|
| ![Landing](https://placehold.co/900x1600) | ![fsdaf](https://placehold.co/900x1600) | ![fsdaf](https://placehold.co/900x1600) | ![fsdaf](https://placehold.co/900x1600) |
| Home screen  | Menu Screen | Order Screen | Checkout Screen |
| ![Landing](https://placehold.co/900x1600) | ![fsdaf](https://placehold.co/900x1600) | ![fsdaf](https://placehold.co/900x1600) | ![fsdaf](https://placehold.co/900x1600) |

### Admin Screens (Web)
| Login screen  | Register screen |  Landing screen |
| ---| ---| ---|
| ![Landing](./readme/demo/1440x1024.png) | ![fsdaf](./readme/demo/1440x1024.png) | ![fsdaf](./readme/demo/1440x1024.png) |
| Home screen  | Menu Screen | Order Screen |
| ![Landing](./readme/demo/1440x1024.png) | ![fsdaf](./readme/demo/1440x1024.png) | ![fsdaf](./readme/demo/1440x1024.png) |

<br><br>


<!-- Prompt Engineering -->
<img src="readme/title7.svg"/>

###  Mastering AI Interaction: Unveiling the Power of Prompt Engineering:

- This project uses advanced prompt engineering techniques to optimize the interaction with natural language processing models. By skillfully crafting input instructions, we tailor the behavior of the models to achieve precise and efficient language understanding and generation for various tasks and preferences.

<br><br>

<!-- AWS Deployment -->
<img src="readme/title8.svg"/>

###  Efficient AI Deployment: Unleashing the Potential with AWS Integration:

- This project leverages AWS deployment strategies to seamlessly integrate and deploy natural language processing models. With a focus on scalability, reliability, and performance, we ensure that AI applications powered by these models deliver robust and responsive solutions for diverse use cases.

<br><br>

<!-- Unit Testing -->
<img src="readme/title9.svg"/>

###  Precision in Development: Harnessing the Power of Unit Testing:

- This project employs rigorous unit testing methodologies to ensure the reliability and accuracy of code components. By systematically evaluating individual units of the software, we guarantee a robust foundation, identifying and addressing potential issues early in the development process.

<br><br>


<!-- How to run -->
<img src="readme/title10.svg"/>

> To set up Recidivism Radar locally, follow these steps:

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip
  ```sh
   pip install pandas
   pip install numpy
   pip install scikit-learn
   pip install mlflow
   pip install sqlalchemy
   pip install flask

  ```
    

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._


1. Clone the repo
   git clone [github](https://github.com/SalehMk0/Recidivism-Radar.git)
2. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```
3. Run the sql file dwh.sql to initialize the data warehouse.

4. Run the cleaning files.
5. Run the Load file to load the data into the data warehouse.
6. Run the timeseries analysis file to run the timeseries
7. Run the Model file to set up the model and make predictions.
8. Open the analysis (power bi) file to see further analysis.
 


Now, you should be able to setup Recidivism Radar locally and explore its features.
