
## CALIFORNIA HOUSE PRICE PREDICTION 

Application data source url:
(https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.tgz)

<<<<<<< HEAD
## Start Machine Learning project.

## PROJECT OUTLOOK :


![alt text](<project_Outlook/Screenshot 2024-02-22 001307.jpg>)

=======
>>>>>>> 12ec580e42d882c8236b8a28a3e4a95d7ee05a79
## Dataset Details
## Feature Description :

1. Longitude(float64)  :	
* A measure of how far west a house is; a more negative value is farther west	
* Longitude values range from -180 to +180
* Data set min: -124.3
* Data set max: -114.3

2. Latitude(float64)  :	
* A measure of how far north a house is; a higher value is farther north	
* Latitude values range from -90 to +90
* Data set min:  32.5
* Data set max:  42.5


3. HousingMedianAge(float64)  :	
* Median age of a house within a block; a lower number is a newer building	
* Data set min:  1.0
* Data set max:  52.0

4. TotalRooms(float64)  :	
* Total number of rooms within a block	                           
* Data set min:  2.0
* Data set max:  37937.0

5. TotalBedrooms(float64)  :	
* Total number of bedrooms within a block	                           
* Data set min:  1.0
* Data set max:  6445.0

6. Population(float64)  :	
* Total number of people residing within a block	                          
* Data set min:  3.0
* Data set max:  35682.0

7. Households(float64)  :	
* Total number of households, a group of people residing within a home unit, for a block	                         
* Data set min:  1.0
* Data set max:  6082.0

8. MedianIncome(float64)  :	
* Median income for households within a block of houses (measured in tens of thousands of USDollars)	     
* Data set min:  0.5
* Data set max:  15.0

9. Ocean_Proximity(string):  
* Location of the house w.r.t ocean/sea
* DatasetValues : ['<1H OCEAN','INLAND','NEAR BAY','NEAR OCEAN','ISLAND']


10. TargetFeature
* MedianHouseValue(float64)  :	Median house value for households within a block (measured in USDollars)                        
* Data set min:  14999.0
* Data set max:  500001.0


## Artifacts From The Project:
1. Data Ingestion Artifact :
* tgz_data.csv
* raw_data.csv 
* ingested data = ['training_dataset.csv','testing_datset.csv']


2. Data Transformation Artifact:
* preprocessed_model.pkl
* Transformed_data= ['test.npz','train.npz']
        

3. Data Vaildation :
* report.json
* report.html

4. Model_Training :
* trained_model.pkl


5. Model Evaluation :
* model_evaluation.yaml







