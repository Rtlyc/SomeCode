# CS-UY 1114
# Final project

import math
import turtle

def create_table(file_name):
    """
    sig: str -> tuple(list(float), list(float), list(str))
    Given a file name, read the file into a tuple containing
    two lists of type float and one list of type string.
    The features of the dataset should be of type float
    and the label should be of type string. 
    """
    f = open(file_name,"r")
    lst1 = []
    lst2 = []
    lst3 = []
    for line in f:
        line = line.strip().split(",")
        lst1.append(float(line[0]))
        lst2.append(float(line[1]))
        lst3.append(line[-1])
    f.close()
    return lst1,lst2,lst3

def print_range_max_min(data):
    """
    sig: tuple(list(float), list(float)) -> NoneType
    Print the max, min and range of both features in the dataset.
    """
    max0 = max(data[0])
    max1 = max(data[1])
    min0 = min(data[0])
    min1 = min(data[1])
    range0 = max0 - min0
    range1 = max1 - min1
    print("Feature 1 - min:",min0,"max:",max0,"range:",range0)
    print("Feature 2 - min:",min1,"max:",max1,"range:",range1)    

def find_mean(feature):
    """
    sig: list(float) -> float
    Return the mean of the feature.
    """
    Sum = sum(feature)
    return Sum/len(feature)

def find_std_dev(feature, mean):
    """
    sig: list(float), float -> float
    Return the standard deviation of the feature. 
    """
    acc = 0
    for i in feature:
        acc += (i-mean)**2
    return (acc/len(feature))**0.5

def normalize_data(data):
    """
    sig: tuple(list(float), list(float), list(str)) -> NoneType
    Print the mean and standard deviation for each feature.
    Normalize the features in the dataset by
    rescaling all the values in a particular feature
    in terms of a mean of 0 and a standard deviation of 1.
    Print the mean and the standard deviation for each feature, now normalized.
    After normalization, each of your features should display a mean of 0
    or very close to 0 and a standard deviation of 1 or very close to 1. 
    """
    current_mean0 = find_mean(data[0])
    current_std0 = find_std_dev(data[0],current_mean0)
    current_mean1 = find_mean(data[1])
    current_std1 = find_std_dev(data[1],current_mean1)
    list0 = data[0]
    for i in range(len(list0)):
        list0[i] = (list0[i]-current_mean0)/current_std0
    list1 = data[1]
    for i in range(len(list1)):
        list1[i] = (list1[i]-current_mean1)/current_std1
    new_mean0 = find_mean(list0)
    new_std0 = find_std_dev(list0,new_mean0)
    new_mean1 = find_mean(list1)
    new_std1 = find_std_dev(list1,new_mean1)
    print("Feature 1 - mean:",current_mean0, "std dev:",current_std0)
    print("Feature 1 after normalization - mean:",new_mean0,"std dev:",new_std0)
    print("Feature 2 - mean:",current_mean1, "std dev:",current_std1)
    print("Feature 2 after normalization - mean:",new_mean1,"std dev:",new_std1)


def make_predictions(train_set, test_set):
    """
    sig: tuple(list(float), list(float), list(str)), tuple(list(float), list(float), list(str)) -> list(str)
    For each observation in the test set, you'll need to check all of
    the observations in the training set to see which is the `nearest neighbor.'
    The function should make a call to the function find_dist.
    Accumulate a list of predicted iris types for each of the test set
    observations. Return this prediction list.
    """
    ls = []
    for test in range(len(test_set[0])):
        distance = find_dist(test_set[0][test],test_set[1][test],train_set[0][0],train_set[0][0])
        for train in range(len(train_set[0])):
            if distance > find_dist(test_set[0][test],test_set[1][test],train_set[0][train],train_set[0][train]):
                distance = find_dist(test_set[0][test],test_set[1][test],train_set[0][train],train_set[0][train])
                name = train_set[-1][train]
        ls.append(name)
    return ls
           
def find_dist(x1, y1, x2, y2):
    """
    sig: float, float, float, float -> float
    Return the Euclidean distance between two points (x1, y1), (x2, y2).
    """
    output = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    return output
        
def find_error(test_data, pred_lst):
    """
    sig: tuple(list(float), list(float), list(str)) -> float
    Check the prediction list against the actual labels for
    the test set to determine how many errors were made.
    Return a percentage of how many observations in the
    test set were predicted incorrectly. 
    """
    count = 0
    for i in range(len(test_data[-1])):
        if test_data[-1][i] != pred_lst[i]:
            count += 1
    return count/len(test_data[-1]) * 100

def plot_data(train_data, test_data, pred_lst):
    """
    sig: tuple(list(float), list(float), list(str)), tuple(list(float), list(float), list(str)), list(str)
        -> NoneType
    Plot the results using the turtle module. Set the turtle window size to #500 x 500.
    Draw the x and y axes in the window. Label the axes "petal width" and "petal length". 
    Plot each observation from your training set on the plane, using a #circle shape
    and a #different color for each type of iris. Use the value of the first feature
    for the x-coordinate and the value of the second feature for the y-coordinate.
    Use a dot size of 10. Recall that the features have been normalized to have a mean
    of 0 and a standard deviation of 1. You will need to `stretch' your features across
    the axes to make the best use of the 500 x 500 window. Ensure that none of your
    points are plotted off screen. Also plot each correct prediction from your test
    set in the corresponding color. Use a #square to indicate that the value is a prediction.
    Plot the incorrect predictions that were made for the test set in red, also using a
    square to indicate that it was a prediction. Include a key in the upper left
    corner of the plot as shown in the sample plot. The function will make a call
    to the function draw_key in order to accomplish this task. 
    """
    draw_key()

    turtle.color("black")
    turtle.setup(500,500)
    turtle.goto(-250,0)
    turtle.pendown()
    turtle.goto(250,0)
    turtle.penup()
    turtle.goto(0,-250)
    turtle.pendown()
    turtle.goto(0,250)
    turtle.penup()
    turtle.goto(200,10)
    turtle.write("petal length")
    turtle.goto(10,-230)
    turtle.write("petal width")
    for i in range(len(train_data[0])):
        if train_data[-1][i] == "Iris-setosa":
            turtle.color("blue")
        elif train_data[-1][i] == "Iris-versicolor":
            turtle.color("green")
        elif train_data[-1][i] == "Iris-virginica":
            turtle.color("orange")
        turtle.goto(train_data[0][i]*100,train_data[1][i]*100)
        turtle.dot(10)
    for i in range(len(test_data[0])):
        if pred_lst[i] == test_data[-1][i] == "Iris-setosa":
            turtle.color("blue")
        elif pred_lst[i] == test_data[-1][i] == "Iris-versicolor":
            turtle.color("green")
        elif pred_lst[i] == test_data[-1][i] == "Iris-virginica":
            turtle.color("orange")
        else:
            turtle.color("red")
        turtle.goto(test_data[0][i]*100,test_data[1][i]*100)
        turtle.begin_fill()
        for j in range(4):
            turtle.pendown()
            turtle.fd(7)
            turtle.rt(90)
            turtle.penup()
        turtle.end_fill()
            
            

def draw_key():
    """
    sig: () -> NoneType
    Draw the legend for the plot indicating which group is shown by each color/shape combination.  
    """
    turtle.penup()
    turtle.goto(-200,200)
    turtle.write("Iris-setosa")
    turtle.goto(-200,190)
    turtle.write("Iris-versicolor")
    turtle.goto(-200,180)
    turtle.write("Iris-virginica")
    turtle.goto(-200,170)
    turtle.write("predicted Iris-setosa")
    turtle.goto(-200,160)
    turtle.write("predicted Iris-versicolor")
    turtle.goto(-200,150)
    turtle.write("predicted Iris-virginica")
    turtle.goto(-200,140)
    turtle.write("predicted Incorrectly")
    turtle.goto(-210,205)
    turtle.color("blue")
    turtle.dot(10)
    turtle.goto(-210,195)
    turtle.color("green")
    turtle.dot(10)
    turtle.goto(-210,185)
    turtle.color("orange")
    turtle.dot(10)
    color = ["blue","green","orange","red"]
    for i in range(4):
        turtle.goto(-215,180-i*10)
        turtle.begin_fill()
        turtle.color(color[i])
        for j in range(4):
            turtle.pendown()
            turtle.fd(7)
            turtle.rt(90)
            turtle.penup()
        turtle.end_fill()
    turtle.update()

def main():
    """
    sig: () -> NoneType
    The main body of the program. It will use the other
    functions to load the data, process the training set,
    analyze the test set, and display its conclusions.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    train_data = create_table("iris_train.csv")
    print_range_max_min(train_data[:2])
    print()
    normalize_data(train_data)
    test_data = create_table("iris_test.csv")
    print()
    normalize_data(test_data)
    pred_lst = make_predictions(train_data, test_data)
    error = find_error(test_data, pred_lst)
    print()
    print("The error percentage is: ", error)
    plot_data(train_data, test_data, pred_lst)

main()




