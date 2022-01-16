import random

# Lightbulb starting state is Off
lightbulb = True
number_of_prisoners = 100

# action (boolean) to switch the bulb on as to be counted by the leader


class Prisoner:
    def __init__(self, number, action):
        self.action = action
        self.number = number

# (regular) prisoners have a specific lightbulb switch behaviour, in opposition to the leader behaviour
    def prisoner_switch(self):
        global lightbulb

        if not lightbulb and not self.action:
            print(f'Lightbulb is initially {lightbulb}')
            lightbulb = True
            print(f'Lightbulb switched {lightbulb}')
            self.action = True
            return lightbulb, self.action
        else:               # if the lightbulb is switched on OR action already undertaken in the past, prisoner
                            # will do nothing as to not confuse the leader's counting
            print(f'Lightbulb is {lightbulb} and prisoner switch interaction is {self.action}')
            return lightbulb, self.action

# the leader has the extra count parameter


class Leader(Prisoner):

    def __init__(self, count, number, action):
        super().__init__(number, action)
        self.count = count

# the leader has a specific bulb switch behaviour in opposition to regular prisoners
    def leader_switch(self):
        global lightbulb

        if lightbulb:
            print(f'Lightbulb is initially {lightbulb}')
            lightbulb = False
            print(f'Lightbulb switched {lightbulb}')

            self.count += 1
            print(f'{self.count} prisoners have been in the room so far and counted by the leader')
            return lightbulb, self.count
        else:
            print(f'Lightbulb remains {lightbulb} and prisoner switch interaction remains {self.action}')
            print(f'Still {self.count} prisoners have been in the room so far and counted by the leader')
            return lightbulb, self.count


# Create the prisoners and leader objects

prisoner_list = []
for i in range(0, number_of_prisoners):
    if i == 0:
        leader = Leader(-1, i, False)
        prisoner_list.append(leader)
    else:
        prisoner = Prisoner(i, False)
        prisoner_list.append(prisoner)


days = 0
while True:

    random_number = random.randint(0, number_of_prisoners - 1)
    print(f'Prisoner {random_number} enters the room')
    if random_number == 0:
        lightbulb, prisoner_list[random_number].count = prisoner_list[random_number].leader_switch()
        days += 1
        if prisoner_list[random_number].count == number_of_prisoners - 1:
            print(f'The leader now knows that he and other {prisoner_list[0].count} prisoners have visited the room.')
            print(f'{days} days have passed since the beginning of the challenge. ')
            break
    elif random_number != 0:
        lightbulb, prisoner_list[random_number].action = prisoner_list[random_number].prisoner_switch()
        days += 1
    else:
        print("Check code!")    # note to self, just in case
