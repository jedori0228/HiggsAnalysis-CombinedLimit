# Using condor

Write the full paths of data card to a txt file; e.g., Year2016Cards.txt
Then, run
```
./create-batch -n <job name> -l <txt filename with full paths of data cards>
#### above command will print job submission command
#### run those lines
#### When all jobs are finshed, extract the results with
./read_Asymptotic.py -i <job dir name>
```
