class Weapon:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage

    def attack(self):
        # changing base class for new functionality -> bad
        if "gun" in self.name:
            print(f"You shouted a gun with damage {self.damage}")
        elif "sword" in self.name:
            print(f"You stroke with damage {self.damage}")
        else:
            print(f"You attacked with damage {self.damage}")


class Player:
    def __init__(self, name: str, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def attack(self):
        self.weapon.attack()

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon


gun = Weapon(name="gun", damage=300)
sword = Weapon(name="sword", damage=20)

player = Player(name="Hero", weapon=sword)
player.attack()

player.change_weapon(gun)
player.attack()
