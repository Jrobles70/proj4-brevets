# Project 4:  Brevet time calculator with Ajax

Reimplement the RUSA ACP controle time calculator with flask and ajax

## ACP Rules
* The first controle must be at the 0 miles, 0 km
* Riders have one hour to go through the first controle
* The final controle must be greater than or equal to the brevet distance and less than or equal to the brevet distance * 1.1
* The final controle will always have the following time limits
    *13:30 for 200 KM
    *20:00 for 300 KM
    *27:00 for 400 KM
    *40:00 for 600 KM
    *75:00 for 1000 KM
* Times are calculated using the kilometers rounded to the next kilometer
* Times are also rounded to the next minute

* The following speeds are used to calculate the open and closed times:

    | Controle location (km) | Minimum Speed (km/hr) | Maximum Speed (km/hr) |
    | ------------------------ | --------------------------- | ----------------------------- |
    | 0 - 200 | 15 | 34 |
    | 200 - 400 | 15 | 32 |
    | 400 - 600 | 15 | 30 |
    | 600 - 1000 | 11.428 | 28 |
    | 1000 - 1300 | 13.333 | 26 |
    
    Note: The control location is should be used relative to the controle distance
    For example, with a 600 km controle distance the time is calculated using the speeds for 0 - 200 for the first
    200 km, then the speeds for 200 - 400 for the next 200 km, then the speeds for 400 - 600 for the last 200 km.
    
    Open:
    200/34 + 200/32 + 200/30 = 18.799
    18 hours
    .799 * 60 = 47.941 = 48 Minutes
    
    
    Close:
    200/15 + 200/15 + 200/15 = 40
    40 Hours

## How to use
Create a credentials.ini file
Using command line to run
```
make run
```

## Testing

* `nosetests`
```
make test
```


A simple anagram game designed for English-language learning students in
elementary and middle school.
Students are presented with a list of vocabulary words (taken from a text file)
and an anagram.  The anagram is a jumble of some number of vocabulary words, randomly chosen.  Students attempt to type vocabularly words that can be created from the
jumble.  When a matching word is typed, it is added to a list of solved words.

The vocabulary word list is fixed for one invocation of the server, so multiple
students connected to the same server will see the same vocabulary list but may
have different anagrams.

## Known bugs
If a km or miles number is deleted then the other number will go to NaN


## Authors

Initial version by M Young;
Revised by Justin Robles jrobles@uoregon.edu

