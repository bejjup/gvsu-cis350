from render import render_text


class Players:

    def __init__(self, num, p, file):
        self._order = num
        #self._money = 0
        self._money = 200
        self._loc_x = 0
        self._loc_y = 0
        self._num = p
        self._icon_x = 0
        self._icon_y = 0
        self._name_text_x = 0
        self._name_text_y = 0
        self._name = "Placeholder"
        self._color = 0, 0, 0
        self._img = "Placeholder"
        self.set_playa(num, file)
        self._space = 0
        self._inventory = []
        self._material_image = file.materials
        #self._health = 200
        self._health = 50
        self._jail = False
        self._doubles_count = 0

    # returns the name of the player
    @property
    def order(self):
        return self._order

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value

    @property
    def loc_x(self):
        return self._loc_x

    @loc_x.setter
    def loc_x(self, value):
        self._loc_x = value

    @property
    def loc_y(self):
        return self._loc_y

    @loc_y.setter
    def loc_y(self, value):
        self._loc_y = value

    @property
    def num(self):
        return self._num

    @property
    def name_text_x(self):
        return self._name_text_x

    @name_text_x.setter
    def name_text_x(self, value):
        self._name_text_x = value

    @property
    def name_text_y(self):
        return self._name_text_y

    @name_text_y.setter
    def name_text_y(self, value):
        self._name_text_y = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        self._img = value

    @property
    def space(self):
        return self._space

    @space.setter
    def space(self, value):
        if value > 31:
            self._space = value - 32
            self.money += 100
        else:
            self._space = value
    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value

    def add_to_inventory(self, value):
        self._inventory.append(value)

    @property
    def material_image(self):
        return self._material_image

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    @property
    def jail(self):
        return self._jail

    @jail.setter
    def jail(self, value):
        self._jail = value

    @property
    def doubles_count(self):
        return self._doubles_count

    @doubles_count.setter
    def doubles_count(self, value):
        self._doubles_count = value
        if self.doubles_count == 3:
            self.jail = True
            self.space = 8

    # sets the name of the player depending on what icon they chose
    def set_playa(self, num, file):
        if num == 1:
            self.name = "Nog Ops"
            self.color = 89, 211, 227
            self.img = file.nog_ops

        if num == 2:
            self.name = "Jonesy"
            self.color = 219, 31, 62
            self.img = file.jonesy

        if num == 3:
            self.name = "Raven"
            self.color = 137, 42, 156
            self.img = file.raven

        if num == 4:
            self.name = "John Wick"
            self.color = 82, 82, 82
            self.img = file.john_wick

    def set_start_val(self):
        if self._num == 1:
            self.loc_x = 605
            self.loc_y = 605

        if self._num == 2:
            self.loc_x = 605
            self.loc_y = 625

        if self._num == 3:
            self.loc_x = 625
            self.loc_y = 605

        if self._num == 4:
            self.loc_x = 625
            self.loc_y = 625

    def get_icon_location(self, board):
        if self.num == 1:
            self.loc_x = board[self.space].loc1_x
            self.loc_y = board[self.space].loc1_y

        elif self.num == 2:
            self.loc_x = board[self.space].loc2_x
            self.loc_y = board[self.space].loc2_y

        elif self.num == 3:
            self.loc_x = board[self.space].loc3_x
            self.loc_y = board[self.space].loc3_y

        elif self.num == 4:
            self.loc_x = board[self.space].loc4_x
            self.loc_y = board[self.space].loc4_y

    def render_output(self, img_pos, mats_x, mats_y, vals, scrn, pygame):
        img = pygame.image.load(self.img)
        img = pygame.transform.scale(img, (100, 100))
        scrn.blit(img, img_pos)

        pygame.draw.rect(scrn, (255, 0, 0), pygame.Rect(img_pos[0], img_pos[1]+105, 100, 10))
        if 0 < self.health <= 100:
            pygame.draw.rect(scrn, (0, 200, 0), pygame.Rect(img_pos[0], img_pos[1] + 105, self.health, 10))
        if self.health > 100:
            pygame.draw.rect(scrn, (0, 200, 0), pygame.Rect(img_pos[0], img_pos[1] + 105, 100, 10))
            pygame.draw.rect(scrn, (0, 255, 255), pygame.Rect(img_pos[0], img_pos[1] + 105, self.health-100, 10))

        render_text(vals.font4, scrn, f'{self.money}', (245, 245, 245), (mats_x+10, mats_y+20))
        render_text(vals.font2, scrn, f'{self.doubles_count}', (245, 245, 245), (mats_x + 10, mats_y + 40))


    def p1_out(self, vals, scrn, pygame):
        self.render_output( (145, 675), 300, 690,  vals, scrn, pygame)

    def p2_out(self, vals, scrn, pygame):
        self.render_output((25, 145), 60, 260,  vals, scrn, pygame)

    def p3_out(self, vals, scrn, pygame):
        self.render_output((145, 25), 300, 40,  vals, scrn, pygame)

    def p4_out(self, vals, scrn, pygame):
        self.render_output((675, 145), 710, 260, vals, scrn, pygame)

    def render_circle(self, scrn, pygame):
        if self.space == 8 and self.jail:
            self.loc_x = 170 + 10*self.num
            self.loc_y = 585 + 10*self.num
            pygame.draw.circle(scrn, self.color, [self.loc_x, self.loc_y], 10, 0)
        else:
            pygame.draw.circle(scrn, self.color, [self.loc_x, self.loc_y], 10, 0)
