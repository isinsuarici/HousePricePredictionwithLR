# House Price Prediction with Linear Regression

Linear regression analysis;
It is used to estimate the value of one variable relative to the value of 
another variable. The variable you want to predict is called the 
dependent variable. The variable you use to predict the value of the 
other variable is called the independent variable. This form of 
analysis estimates the coefficients of the linear equation using one or 
more independent variables that best predict the value of the 
dependent variable. Linear regression sits on a straight line or surface 
that minimizes mismatches between predicted and actual output 
values. There are simple linear regression calculators that use the 
"least squares" method to discover the best fit row for a pair of 
paired datasets. Next, you predict the value of X (the dependent 
variable) from Y (the independent variable). </br> </br> 
Implementations steps;
First, I read the data for our app.
I assigned the part we want to predict from the data we read to the 
variable named price.
I did indexing and column naming to the elements in my price 
variable.
I assigned these newly generated values to the valueof_y variable.
I assigned the values other than the part we want to predict from the 
data we read to the variable named values_except_price.
I did indexing and column naming to the elements in my 
values_except_price variable.
I assigned these newly generated values to the valueof_x variable.
I added the library "from sklearn.model_selection import 
train_test_split" for the stage of splitting the data for training and 
testing.
I divided my data into x_train, x_test,y_train and y_test, dividing 20% 
of the data as test and 80% as train.
Then I added the sklearn.linear_model library and created my linear 
regression model. I have given x_train and y_train data to this linear 
regression model. At this stage, the model establishes a relationship 
between x_train data and y_train data. In short, it learns y_train from 
x_train. Then I gave the model x_test data for the model to apply 
what it learned. It obtains prediction results by applying what it has 
learned before to x_test data. I stored these prediction results in the 
y_pred variable. At this stage, we have already found my results. 
After that we had to apply RMSE to measure the accuracy of our 
model. In this part, I used 3 different evaluation methods as RMSE, 
MSE and r2 score. </br> </br> 
You can see their output below.
</br> </br> 
![UML](https://github.com/isinsuarici/HousePricePredictionwithLR/blob/master/img/output1.png)
</br> 
![UML](https://github.com/isinsuarici/HousePricePredictionwithLR/blob/master/img/output2.png)
