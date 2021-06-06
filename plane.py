from math import sin, cos, sqrt, atan2


GRAVITY = 9.8 # m/s^2


class Plane:
    global GRAVITY
    def __init__(self):
        self.tile_x = 0
        self.tile_y = 0
        self.angle = 0.017#1.4 #0.3 
        self.speed_angle = 0
        self.speed = 0
        self.v_speed = 0
        self.h_speed = 150
        self.thrust = 0 
        self.wheels_on = True 

        self.width = 6.13
        self.height = 1.3
        self.mass = 1500 # kg
        self.wing_surface = 29 # m^2
        self.front_surface = 3.4 # ~ m^2
        self.wheels_surface = 0.23 # ~ m^2
        self.max_thurst = 100000 # N
        self.wind_coef = 200 

    def calc(self, time):
        self.tile_x += self.h_speed 
        self.tile_y += self.v_speed 

        wind_pressure = self.speed * self.wind_coef
        multiplier = self.thrust * self.max_thurst / self.mass
        self.v_speed -= time * GRAVITY
        self.v_speed += sin(self.angle) * time * 0.01 * multiplier
        self.h_speed += cos(self.angle) * time * 0.01 * multiplier 

        delta_angle = self.angle - self.speed_angle
        force = sin(delta_angle) * self.wing_surface * wind_pressure
        #print(force, 'force')
        self.v_speed += time / self.mass * force * cos(self.angle)
        #print('1', (time  * force * cos(self.angle)) / self.mass, cos(self.angle))
        #print(' v_sp ', self.v_speed)
        #print('2', (time  * force * sin(self.angle)) / self.mass, sin(self.angle))
        self.h_speed -= time / self.mass * force * sin(self.angle)
        '''

        drag = self.front_surface * wind_pressure 
        self.v_speed -= time / self.mass * drag * cos(self.angle)
        print('drag', time / self.mass * drag * cos(self.angle))
        self.h_speed -= time / self.mass * drag * sin(self.angle)
        '''

        self.speed = sqrt(self.h_speed**2 + self.v_speed**2)
        self.speed_angle = atan2(self.v_speed, self.h_speed)

    def thrust_up(self, amount):
        self.thrust += amount
        if self.thrust < 0:
            self.thrust = 0
        if self.thrust > 100:
            self.thrust = 100

    def rotate(self, amount):
        self.angle += amount


