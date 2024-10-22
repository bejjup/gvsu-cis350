class Spaces:

    def __init__(self, name, x, y, num):
        self._name = name
        self._loc_1_x = x
        self._loc_2_x = self._loc_1_x
        self._loc_3_x = self._loc_1_x + 20
        self._loc_4_x = self._loc_1_x + 20
        self._loc_1_y = y
        self._loc_2_y = self._loc_1_y + 20
        self._loc_3_y = self._loc_1_y
        self._loc_4_y = self._loc_1_y + 20
        self._pos = num
        self._price = 5*num

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def loc1_x(self):
        return self._loc_1_x
    @loc1_x.setter
    def loc1_x(self, value):
        self._loc_1_x = value
    @property
    def loc2_x(self):
        return self._loc_2_x
    @loc2_x.setter
    def loc2_x(self, value):
        self._loc_2_x = value
    @property
    def loc3_x(self):
        return self._loc_3_x
    @loc3_x.setter
    def loc3_x(self, value):
        self._loc_3_x = value
    @property
    def loc4_x(self):
        return self._loc_4_x
    @loc4_x.setter
    def loc4_x(self, value):
        self._loc_4_x = value
    @property
    def loc1_y(self):
        return self._loc_1_y
    @loc1_y.setter
    def loc1_y(self, value):
        self._loc_1_y = value
    @property
    def loc2_y(self):
        return self._loc_2_y
    @loc2_y.setter
    def loc2_y(self, value):
        self._loc_2_y = value
    @property
    def loc3_y(self):
        return self._loc_3_y
    @loc3_y.setter
    def loc3_y(self, value):
        self._loc_3_y = value
    @property
    def loc4_y(self):
        return self._loc_4_y
    @loc4_y.setter
    def loc4_y(self, value):
        self._loc_4_y = value
    @property
    def pos(self):
        return self._pos
    @pos.setter
    def pos(self, value):
        self._pos = value
    @property
    def price(self):
        return self._price

def make_board(board):
    p = 0
    while p < 32:
        go = Spaces('Go', 605, 605, p)
        board.append(go)
        p += 1
        mexico = Spaces('Mexico', 543, 605, p)
        board.append(mexico)
        p += 1
        l1 = Spaces('Launchpad', 493, 605, p)
        board.append(l1)
        p += 1
        gas = Spaces('Gas Station', 442, 605, p)
        board.append(gas)
        p += 1
        gcart = Spaces('Golf Cart', 390, 605, p)
        board.append(gcart)
        p += 1
        hh = Spaces('Happy Hamlet', 339, 605, p)
        board.append(hh)
        p += 1
        chest1 = Spaces('Chest', 288, 605, p)
        board.append(chest1)
        p += 1
        pp = Spaces('Polar Peak', 237, 605, p)
        board.append(pp)
        p += 1
        jail = Spaces('Jail', 170, 605, p)
        board.append(jail)
        p += 1
        ff = Spaces('Frosty Flights', 165, 541, p)
        board.append(ff)
        p += 1
        l2 = Spaces('Launchpad', 165, 490, p)
        board.append(l2)
        p += 1
        vv = Spaces('Viking Village', 165, 439, p)
        board.append(vv)
        p += 1
        plane = Spaces('Plane', 165, 389, p)
        board.append(plane)
        p += 1
        tt = Spaces('Tilted Towers', 165, 337, p)
        board.append(tt)
        p += 1
        chest2 = Spaces('Chest', 165, 287, p)
        board.append(chest2)
        p += 1
        plst_pk = Spaces('Pleasant Park', 165, 235, p)
        board.append(plst_pk)
        p += 1
        free_pkng = Spaces('Free Parking', 165, 170, p)
        board.append(free_pkng)
        p += 1
        hauntedh = Spaces('Haunted Hills', 237, 165, p)
        board.append(hauntedh)
        p += 1
        l3 = Spaces('Launchpad', 288, 165, p)
        board.append(l3)
        p += 1
        jj = Spaces('Junk Junction', 339, 165, p)
        board.append(jj)
        p += 1
        shopping_cart = Spaces('Shopping Cart', 390, 165, p)
        board.append(shopping_cart)
        p += 1
        ll = Spaces('Lazy Lagoon', 442, 165, p)
        board.append(ll)
        p += 1
        chest3 = Spaces('Chest', 493, 165, p)
        board.append(chest3)
        p += 1
        u_r = Spaces('Geysers', 543, 165, p)
        board.append(u_r)
        p += 1
        go_to = Spaces('Go To Jail', 605, 165, p)
        board.append(go_to)
        p += 1
        ss = Spaces('Sunny Steps', 610, 235, p)
        board.append(ss)
        p += 1
        l4 = Spaces('Launchpad', 610, 287, p)
        board.append(l4)
        p += 1
        pressure_plant = Spaces('Pressure Plant', 610, 337, p)
        board.append(pressure_plant)
        p += 1
        cannon = Spaces('Cannon', 610, 389, p)
        board.append(cannon)
        p += 1
        r_t = Spaces('Race Track', 610, 439, p)
        board.append(r_t)
        p += 1
        chest4 = Spaces('Chest', 610, 490, p)
        board.append(chest4)
        p += 1
        p_palms = Spaces('Paradise Palms', 610, 541, p)
        board.append(p_palms)
        p += 1
