class Weapon:
    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage

    def attack(self):
        print(f"You attacked with damage {self.damage}")


class Sword(Weapon):
    def __init__(self, damage: int):
        self.damage = damage
        self.name = "sword"
        super().__init__(self.name, self.damage)

    def attack(self):
        print(f"You attacked with sword, damage: {self.damage}")


class Gun(Weapon):
    def __init__(self, damage: int):
        self.damage = damage
        self.name = "gun"
        super().__init__(self.name, self.damage)

    def attack(self):
        print(f"You shot your gun with damage: {self.damage}")


class Player:
    def __init__(self, name: str, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def attack(self):
        self.weapon.attack()

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon


sword = Sword(damage=10)
gun = Gun(damage=300)

player = Player(name="Hero", weapon=sword)
player.attack()

player.change_weapon(gun)
player.attack()
