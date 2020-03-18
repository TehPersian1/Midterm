import pygame as pg
from pygame.locals import *
from pygame.sprite import Sprite
import pygame.time
from vector import Vector

class Ship:
    def __init__(self, vector = Vector(), game):
        self.game = game
        self.vector = vector
        self.screen = game.screen.get_rect()
        self.screen_mid_bot = self.screen.mid_bot
        self.image = pg.image.load('shipimage.png')
        self.image_rect = self.image.get_rect()

        self.laser = pg.sprite.Group()
        self.lives = 3

    def center_ship(self):
        self.rect.mid_bot = self.screen.mid_bot

    def fire(self):
        laser = Laser(self.game)
        self.lasers.add(laser)

    def remove_lasers(self):
        for laser in self.laser:
            if laser.rect.bottom < 0:
                self.lasers.remove(laser)

    def move(self):
        if self.velocity == Vector():
            return
        self.rect.left += self.velocity.x
        self.rect.top += self.velocity.y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.move()
        self.draw()
        for alien in self.game.aliens:
            pg.sprite.groupcollide(alien, self.laser, False, True)
        if len(self.game.aliens) <= 0:
            self.center_ship()
            self.game.restart()


class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector ({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y) # or self.add(-1*other)

    def __rmul__(self, n: float):
        return Vector(n * self.x, n * self.y)

    def __mul__(self, n: float):
        return rmul(n)

    def __truediv__(self, other):
        return rmul(1.0/n)

    def __neg__(self):
        return Vector(self.x * -1, self.y * -1)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @staticmethod
    def test():
        v = Vector(x=5, y=5)
        u = Vector(x=4, y=4)
        print('v is {}'.format(v))
        print('u is {}'.format(u))
        print('u plus v is {}'.format(u + v))
        print('u minus v is {}'.format(u - v))
        print('ku is {}'.format(3*u))
        print('-u is {}'.format(-1 * u))
