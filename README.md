# Time Server Assignment

### **_Author:_**
Hunter Bernier

## **_Code Explanation:_**
#### **_Time Server_**
* This code contains four routes:
    * `/time`
        * Returns the current time (HH:MM:SS) 
    * `/date`
        * Returns the current date (MM/DD/YYYY)
    * `/age`
        * Using an inputted JSON dictionary of:
        ```
        {
            date: <date string>
        }
        ```
        * Calculates the amount of years from the inputted date to the current date
    * `/until_next_meal/<meal>`
        * Using an inputted meal string (breakfast, lunch, or dinner), it calculates the amount of hours till/since the meal occurs/occurred
        * The times are preset for each meal at 8:00 AM, 1:00 PM, and 6:00 PM
#### **_Time Client_**
* This code is used for running and testing the routes created within the server.py file