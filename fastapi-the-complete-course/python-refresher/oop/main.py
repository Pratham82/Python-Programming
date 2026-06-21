from Enemy import *

enemy1 = Enemy()

enemy1.type_of_enemy = "Zombie"
print(
    f"Enemy {enemy1.type_of_enemy} has {enemy1.health_points} health points "
    f"and can do attack damage of {enemy1.attack_damage}"
)
