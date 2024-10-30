class Spaces:

    def __init__(self, name, x, y, num, booln):
        self._name = name
        self._loc1_x = x
        self._loc2_x = self.loc1_x
        self._loc3_x = self.loc1_x + 20
        self._loc4_x = self.loc1_x + 20
        self._loc1_y = y
        self._loc2_y = self.loc1_y + 20
        self._loc3_y = self.loc1_y
        self._loc4_y = self.loc1_y + 20
        self._pos = num
        self._price = 5*num
        self._owner = []
        self._owner_color = (0, 0, 0)
        self._buyable = booln

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def loc1_x(self):
        return self._loc1_x

    @loc1_x.setter
    def loc1_x(self, value):
        self._loc1_x = value

    @property
    def loc2_x(self):
        return self._loc2_x

    @loc2_x.setter
    def loc2_x(self, value):
        self._loc2_x = value

    @property
    def loc3_x(self):
        return self._loc3_x

    @loc3_x.setter
    def loc3_x(self, value):
        self._loc3_x = value

    @property
    def loc4_x(self):
        return self._loc4_x

    @loc4_x.setter
    def loc4_x(self, value):
        self._loc4_x = value

    @property
    def loc1_y(self):
        return self._loc1_y

    @loc1_y.setter
    def loc1_y(self, value):
        self._loc1_y = value

    @property
    def loc2_y(self):
        return self._loc2_y

    @loc2_y.setter
    def loc2_y(self, value):
        self._loc2_y = value

    @property
    def loc3_y(self):
        return self._loc3_y

    @loc3_y.setter
    def loc3_y(self, value):
        self._loc3_y = value

    @property
    def loc4_y(self):
        return self._loc4_y

    @loc4_y.setter
    def loc4_y(self, value):
        self._loc4_y = value

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value

    @property
    def price(self):
        return self._price

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
        self._owner_color = value.color

    @property
    def buyable(self):
        return self._buyable

    @buyable.setter
    def buyable(self, value):
        self._buyable = value

    @property
    def owner_color(self):
        return self._owner_color

    @owner_color.setter
    def owner_color(self, value):
        self._owner_color = value

    def print_owner(self, pygame, scrn):
        if self.owner:
            if 0 < self.pos < 8:
                pygame.draw.rect(scrn, self.owner_color, pygame.Rect(self.loc1_x-14, self.loc1_y+46, 50, 10))
            if 8 < self.pos < 16:
                pygame.draw.rect(scrn, self.owner_color, pygame.Rect(self.loc1_x-25, self.loc1_y-14, 10, 50))
            if 16 < self.pos < 24:
                pygame.draw.rect(scrn, self.owner_color, pygame.Rect(self.loc1_x-14, self.loc1_y-24, 50, 10))
            if 24 < self.pos < 32:
                pygame.draw.rect(scrn, self.owner_color, pygame.Rect(self.loc1_x+40, self.loc1_y-14, 10, 50))

def make_board(board, random):
    p = 0
    while p < 32:
        go = Spaces('Go', 605, 605, 0, False)
        board.append(go)
        p += 1
        mexico = Spaces('Mexico', 543, 605, p, True)
        board.append(mexico)
        p += 1
        l1 = Spaces('Launchpad', 493, 605, 0, False)
        board.append(l1)
        p += 1
        gas = Spaces('Gas Station', 442, 605, p, True)
        board.append(gas)
        p += 1
        gcart = Spaces('Golf Cart', 390, 605, p, True)
        board.append(gcart)
        p += 1
        hh = Spaces('Happy Hamlet', 339, 605, p, True)
        board.append(hh)
        p += 1
        chest1 = Spaces('Chest', 288, 605, -(random.randint(1, 6)), False)
        board.append(chest1)
        p += 1
        pp = Spaces('Polar Peak', 237, 605, p, True)
        board.append(pp)
        p += 1
        jail = Spaces('Jail', 170, 605, 0, False)
        board.append(jail)
        p += 1
        ff = Spaces('Frosty Flights', 165, 541, p, True)
        board.append(ff)
        p += 1
        l2 = Spaces('Launchpad', 165, 490, p, False)
        board.append(l2)
        p += 1
        vv = Spaces('Viking Village', 165, 439, p, True)
        board.append(vv)
        p += 1
        plane = Spaces('Plane', 165, 389, p, True)
        board.append(plane)
        p += 1
        tt = Spaces('Tilted Towers', 165, 337, p, True)
        board.append(tt)
        p += 1
        chest2 = Spaces('Chest', 165, 287, -(random.randint(1, 6)), False)
        board.append(chest2)
        p += 1
        plst_pk = Spaces('Pleasant Park', 165, 235, p, True)
        board.append(plst_pk)
        p += 1
        free_pkng = Spaces('Free Parking', 165, 170, 0, False)
        board.append(free_pkng)
        p += 1
        hauntedh = Spaces('Haunted Hills', 237, 165, p, True)
        board.append(hauntedh)
        p += 1
        l3 = Spaces('Launchpad', 288, 165, 0, False)
        board.append(l3)
        p += 1
        jj = Spaces('Junk Junction', 339, 165, p, True)
        board.append(jj)
        p += 1
        shopping_cart = Spaces('Shopping Cart', 390, 165, p, True)
        board.append(shopping_cart)
        p += 1
        ll = Spaces('Lazy Lagoon', 442, 165, p, True)
        board.append(ll)
        p += 1
        chest3 = Spaces('Chest', 493, 165, -(random.randint(1, 6)), False)
        board.append(chest3)
        p += 1
        u_r = Spaces('Geysers', 543, 165, p, True)
        board.append(u_r)
        p += 1
        go_to = Spaces('Go To Jail', 605, 165, p, False)
        board.append(go_to)
        p += 1
        ss = Spaces('Sunny Steps', 610, 235, p, True)
        board.append(ss)
        p += 1
        l4 = Spaces('Launchpad', 610, 287, 0, False)
        board.append(l4)
        p += 1
        pressure_plant = Spaces('Pressure Plant', 610, 337, p, True)
        board.append(pressure_plant)
        p += 1
        cannon = Spaces('Cannon', 610, 389, p, True)
        board.append(cannon)
        p += 1
        r_t = Spaces('Race Track', 610, 439, p, True)
        board.append(r_t)
        p += 1
        chest4 = Spaces('Chest', 610, 490, -(random.randint(1, 6)), False)
        board.append(chest4)
        p += 1
        p_palms = Spaces('Paradise Palms', 610, 541, p, True)
        board.append(p_palms)
        p += 1

