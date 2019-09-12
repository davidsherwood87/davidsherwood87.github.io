# Core Programming by David Sherwood

## About The Author

When i left college in 2006, i did not, at the time, want to go to university. Instead i chose
to continue working in retail, where having spent 5 years in the role with no chance of promotion,
i decided to undertake a degree in 2010.
Having completed my Bachelors degree in Environmental Studies with the Open University
in 2013, i decided in 2014 to become a teacher. I decided to study my PGCE at the
University of Sunderland, and passed the course the following year in 2015. Having spent
a year as a full time teacher, i decided it was not really for me and looked at different
avenues to pursue. I had always had a passion for Geography throughout my life and was 
very keen on statistics and maps. So in 2017 i decided to once again become a distance-learning
student at the University of Leeds, studying GIS. I am currently in my second year of the course
and am in my final module of year 2. My previous modules this year have included:
1. Remote Sensing
2. Planning
3. Population and demographic analysis

### Why Programming?

As probably noted by the amount of emails i have sent my tutor, my experience in Python has
been so far very limited, with some experience coming from teaching Computer Science whilst
a cover teacher. 

Wanting to find a new career, i have noticed that a lot of jobs in the sector want Python 
experience, and so i chose this course to gain at least some experience in programming.

## About the code

To explain what the code itself does, it would be easier to use the same analogy the course 
materials do, and that is with the use of sheep. 
Essentially what the code will do is randomly place our sheep within a field, whilst there the
sheep will eat some grass and whilst there search for nearby sheep and share resources with them.
The code will then be used in an animation that will show the sheep moving around the environment
and parts of the environment being eaten away as each iteration is passed.

### Simple breakdown of code

1. We import all modules we need
2. Make a list for the environment that contains data on what our environment looks like
3. Create another class that contains functions:
   Our sheep being given random coordinates
   The Y and X coordinates being moved
   The sheep eating the grass (environment)
   The sheep communicating with other sheep
   A calculation determining the distance between sheep
4. Back in our original code, we determine how many sheep and iterations there will be
5. We then make a new list for our agents, putting our environment into the list.
6. We then use for-loops to run through our move,eat and share funtions for 100 iterations.
7. The data is then plotted and the animation will run through each iteration until complete.

### Where to find the code

The code is available from the GitHub website by clicking [HERE](https://davidsherwood87.github.io)





