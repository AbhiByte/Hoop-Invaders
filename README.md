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

## Usage and Execution

The home page executes as follows: 

![Console SS](https://i.postimg.cc/ryBxF8DC/hiii.png)]

After the mouse is clicked, the main game runs:

![ola.png](https://i.postimg.cc/Prnvn27S/ola.png)]

The lives decrement when the viruses hit the bottom of the screen and if lives == 0, a lost message is displayed and the game is ended


## Final Thoughts
This project was quite fun and I learned a lot about OOP and how to use classes and objects in my projects. It helped solidify my Python skills and gives me a strong foundation for future projects!

Please refer to the References section for additional reading and sources

## Contact and Infographic

Abhinav Ramesh - [](abhinavramesh03@gmail.com) abhinavramesh03@gmail.com

Project Link: [https://github.com/AbhiByte/c-Rona-Invaders] (https://github.com/AbhiByte/cRona-Invaders)


## References
* [Based off of tutorial from Tech With Tim](https://www.youtube.com/watch?v=Q-__8Xw9KTM&ab_channel=TechWithTim)
* [Pygame Documentation](https://www.pygame.org/docs/)
* [README Format Adapted from othneildrew](https://github.com/othneildrew/Best-README-Template.git)

