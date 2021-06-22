  <h3 align="center">cRona-Invaders Covid Shooter Game</h3>

  <p align="center">
    June 2021 - Abhinav Ramesh
    <br />
    <a href=""><strong></strong></a>
    <br />
    <br />
    <a href=""></a>
    ·
    <a href=""></a>
    ·
    <a href=""></a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Developed Using](#developed-using)
* [The Software](#the-software)
  * [Classes and Functions](#class-objects)
  * [Main Method](#main-method)
* [Usage and Execution](#usage-and-execution)
* [Final Thoughts](#final-thoughts)
* [References](#references)




<!-- ABOUT THE PROJECT -->
## About The Project

This project is a fun space-invaders styled game made using Pygame. The project demonstrates knowledge of Python, Pygame, OOP and some data structures. 
### Developed Using
This project was developed using the Atom Text Editor. Of course, such a project can be created using any editor that suits you.
* [Atom](https://atom.io/)


<!-- GETTING STARTED -->


## The Software

### Class Objects


```python
	 
class Player(Virus):
    def __init__ (self, x, y, health=100):
        super().__init__(x, y, health)
        self.player_image = player_image
        self.mask = pygame.mask.from_surface(self.player_image)
        self.max_health = health
    def move_lasers (self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.offTheScreen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)
```
NOTE: One example of a class used to create a player object and inheriting from the Virus class

### Main Method
The main method is the heart of the program. This is where user input is taken, variables are assinged to those inputs and the class methods are called and ran

![Main Method](https://user-images.githubusercontent.com/64025335/84406797-0433a300-abd8-11ea-8fc0-d9c3562da8bc.gif)

The main method begins by defining the scanner input for user input. It then asks for specific user input for each of the class method parameters and assigns them to variables. Finally it calls on the class methods to be executed

## Usage and Execution

The program executes in the console as follows: 

![Console SS](https://user-images.githubusercontent.com/64025335/84409701-bf117000-abdb-11ea-9f0b-a821a589c0e0.png)

Observe how if the inputed parameter exceeds the limtitations set in the method (see full code for details), the user is told that the rocket is NOT go for launch. If however the inputed data is within the acceptable range, then they are told that the rocket is go for launch

For the real experience, copy the code into an IDE of your choice and run the code for yourself. You'll observe how the sleep() method adds a nice flow to the program (instead of it all being printed to the console at once)




## Final Thoughts
ICS3U0 was very fun and engaging. The course taught me the basics of java and helped improve my programming and problem solving skills. This code showcases some of the various skills and techniques learned throughout the course

Please refer to the References section for additional reading and sources

Kindly also view the infographic made in conjunction with this project (linked below)


## Contact and Infographic

Abhinav Ramesh - [](abhinavramesh03@gmail.com) abhinavramesh03@gmail.com

Project Link: [https://github.com/AbhiByte/ICS3U0-ISU-Artifact](https://github.com/AbhiByte/ICS3U0-ISU-Artifact)

Infographic: [https://create.piktochart.com/output/47262699-my-visual](https://create.piktochart.com/output/47262699-my-visual)




## References
* [NASA Launch Weather Criteria for Falcon 9](https://www.nasa.gov/pdf/649911main_051612_falcon9_weather_criteria.pdf)
* [Additional Reading on Launch Commit Criteria](https://en.wikipedia.org/wiki/Launch_commit_criteria)
* [README Format Adapted from othneildrew](https://github.com/othneildrew/Best-README-Template.git)

