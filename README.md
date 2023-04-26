
Bee_Project_Tresha
TP3 Bee Project

Description:

The Bee Project is about a Player Bee which follow the mosue cursor while the player moves the bee. The speed of the wings could flap faster or slower. It will move faster towards the cursor if the bee cursor is moved fast. The bee will come near a pollen and collect the pollen which will be shown at the bee's feet. Taken pollen turn hollow.The player bee can take a maximum of 6 pollens. If a new pollen is take, the older one is removed from the inventory. It will also be shown at top-left-hand corner of screen as an inventory of pollens collected by the Player bee. The number of pollen cannot exceed 6 each time. If it does, the oldest pollen will be removed from the invetory for a new one to be added. The collected pollen can pollinate a flower if the color of pollen matches the flower color. If it does, it the flower will increase in size gradually until a certain size. The pollen, if still on screen, will also grow in size if that pollen was taken previously. There are two helper bees that move automatically. Going near a pollen and collecting it and pollinating a flower of the same color. Even they have a limit of 6 pollen that can be taken at one time. Again, if it pollinates a flower, the flower will increase in size gradually. The player can pause the game while pressing "p" or reset the game while pressing "r". In order to run the file, we need the background image, the bee gif and the cat gif. Also, some packages need to be installed such as from cmu_graphics, math, copy, decimal, PIL to import Image, random and time. Run the bee_tpdesai.py file on VSCode by pressing Ctrl B. 

Similar projects: 

This project is adapted from the Bee Game in Google Doodle for Earth Day 2020.  

Structure:

The code is structured into Classes, Sub-Classes, Helper Functions and App functions.

Algorithmic Complexity:

Apart from having Bee, Cat , Flower, Inventory and Pollen Classes, there are helper functions with Lists and Dictionary. However, the trickiest part would be to store the ID number of the pollen that was pollinated together with its color. Retrieving it when the flower of same color was pollinated by the Player Bee and then using that ID to enable the pollen to increase in size. This means that only if the flower is pollinated, the pollen that was taken will expand in size if still on screen. 

Timeline:

This project was completed in about 3 weeks.
