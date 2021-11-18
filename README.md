# Ex1_OOP

github repo: https://github.com/eyalhagai12/Ex1_OOP.git

## The Algorithm:

This algorithm is actually an union of two algorithms:
One is an offline algorithm that uses the advantage of knowing all the calls and the times beforehand.
The other is more of an online algorithm which simulates the building and the elevators and assigns calls based on each elevator's criteria.

### Offline Algorithm:
This algorithm receives as input a building (that has elevators) and a list of elevator calls.

1. Given a list of calls, scan the entire list and look for the call that has the maximum  
   absolute distance between the source and destination floors (Let it be "maxLength").
2. Given a building, count the number of elevators in the building. (Let it be "elevNum").
3. Divide maxLength by elevNum and have the following result (Let it be "Division"):  
   maxNum/elevNum = Division
4. Sort the building's elevators into list by their start and stop times, open and close times and their
   speed.
5. - Scan the list of calls again. for each call calculate its absolute distance from source to destination.
   - for each calculation, divide by "Division"
   - This is the elevator index for each call. Assign the call to the elevator.

### "Online like" simulation:
this algorithm gets a building and a list of call objects as its input and simulates simulates the movement and position of the calls
first i get the total simulation time by taking the last calls initiation time and add two minutes to that time
then i run a loop over the total simulation time, each loop is a second in the simulation, this loop does 3 simple steps:

1. get all the calls in the current second in the simulation
2. find the best elevator to which to assign this call to, this is done by calculating how long will it take for each elevator to finish its route with the new call, and then choose the one that takes the least amount of time
3. move the elevators one step in the direction they were going


### the algorithm itself:
the algorithm itself simply chooses the best algorithm according to the amount of elevators, if there is a small amount of elevators we use the offline algorithm and if there are many elevators (we chose 8+ elevators) we use the online simulation algorithm, this way gave us the best results in all our tests

### UML Graph:
![uml1](https://user-images.githubusercontent.com/77681248/142482512-8cf81f74-be20-42e8-a5ae-f02c82c271f1.png)
