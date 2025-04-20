Production Data Analysis

This project aims to analyze industrial production data to understand the performance of machines, identify failure patterns, and analyze energy consumption and downtime during days when production goals were not met.

Project Description

The code simulates a dataset of production from two machines in a factory, namely M2 and M4. The goal is to:

    Verify if the daily production goal (400 units) was achieved.

    Analyze downtime during the days when the goal was not met.

    Calculate the average energy consumed during those days.

Features

    Production analysis by machine: The code calculates how many days the production goal was not achieved.

    Average downtime: It calculates the average downtime on the days of production failure.

    Average energy consumption: It calculates the average energy consumed on days of production failure.

Code Objectives

    Simulate a dataset of production (produced by machines).

    Identify which days the production goal was not achieved.

    Analyze the impact of downtime and energy consumption on production failures.

How to Run the Code
Prerequisites

To run this code, you need to have Python installed and the following libraries:

    pandas

To install pandas, run the following command in your terminal:

pip install pandas

Running the Code

Simply run the Python script (e.g., production_analysis.py) in your terminal or preferred Python editor.

python production_analysis.py

The script will generate the following analyses:

    Production data table, where you will see the information for each machine, such as produced units, downtime, and energy consumption.

    Goal achievement analysis: Whether the production goal was met.

    Counting the days when the goal was not achieved by machine.

    Average downtime during the failure days.

    Average energy consumed during the failure days.

Code Structure

    Simulating data: A dataset of production is simulated for two machines (M2 and M4).

    DataFrame: pandas is used to organize the data and perform the analysis.

    Filtering and calculations:

        Identifies whether the production goal was met.

        Calculates the average downtime and energy for failure days.

Example Output

After running the script, the code will produce the following output in the terminal:

         date machine  produced_units  downtime_minutes  energy_kwh
0  2025-04-08      M2             390                45         220
1  2025-04-09      M2             350                60         230
2  2025-04-10      M2             410                15         215
3  2025-04-08      M4             420                10         200
4  2025-04-09      M4             390                30         210
5  2025-04-10      M4             370                50         225
         date machine  produced_units  downtime_minutes  energy_kwh  met_goal
0  2025-04-08      M2             390                45         220     False
1  2025-04-09      M2             350                60         230     False
2  2025-04-10      M2             410                15         215      True
3  2025-04-08      M4             420                10         200      True
4  2025-04-09      M4             390                30         210     False
5  2025-04-10      M4             370                50         225     False
machine
M2    2
M4    2
dtype: int64
Avarage of downtime during days of failure: 55.0 minutes
Average energy consumed on days of failure: 217.5 kWh

Conclusion

This project can be expanded to include more machines, different time periods, and other parameters related to production performance. It can be useful for data engineers and production analysts who want to monitor and improve the efficiency of industrial operations.

👩‍💻 Author

Karine Oliveira 
Computer Science student at Saint Leo University 
Currently living in Weert, Netherlands 🇳🇱

📬 Contact:

LinkedIn https://www.linkedin.com/in/karine-c-oliveira/
