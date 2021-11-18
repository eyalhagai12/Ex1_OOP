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






