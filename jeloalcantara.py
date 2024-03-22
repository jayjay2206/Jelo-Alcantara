class Player:
    def __init__(self, name, health, attack_power, monster):
        self.name, self.health, self.attack_power = name, health, attack_power
        self.monster = monster

    @property
    def fame(self):
        return self.name

    def attack(self):
        input(f'{self.name} meets Jelo! Jelo attacks first, do you want to attack back?')
        self.monster.take_damage -= self.attack_power

    @property
    def take_damage(self):
        return self.health

    @take_damage.setter
    def take_damage(self, new_health):
        self.health = new_health
        print(f'You got hit! Your new health is {new_health}')
        
    def is_alive(self):
        return self.health > 0

class Monster:
    def __init__(self, name, health, attack_power):
        self.name, self.health, self.attack_power = name, health, attack_power

    def attack(self):
        print ('Jelo is attacking!')
        player1.take_damage -= self.attack_power

    @property
    def take_damage(self):
        return self.health

    @take_damage.setter
    def take_damage(self, new_health):
        self.health= new_health
        print (f'Jelo took damage! Jelo new health is {new_health}')

    @property
    def is_alive(self):
        return self.health > 0

m1 = Monster(name='Jelo', health= 300, attack_power= 25)
player1 = Player(name='Opli', health=100, attack_power=100, monster=m1)

print(f'Welcome {player1.name}.')
player1.attack()
