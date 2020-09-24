from vpython import *
from numpy import array, append
import matplotlib.pyplot as plt

ball = sphere(pos=vector(12, 0, 0), velocity=vector(0, 0, 0), radius=0.5, mass=0.5,
              color=color.yellow)  # Creates the ball
pivot = vector(0, 0, 0)  # Center or coordinate system
speed = vector(0.5, 0, 0)  # Change this to change speed
spring = helix(pos=pivot, velocity=speed, axis=ball.pos - pivot, radius=0.4, constant=1,
               thickness=0.1, coils=20, color=color.red)  # Creates the spring
hanger = box(pos=pivot, velocity=speed, color=color.white)  # Creates the block
eq = vector(9, 0, 0)  # Equilibrium position (how far away it would need to be away from spring to be at equilibrium)

field = box(pos=vector(0, -5, 0), axis=vector(0, 0, 0), size=vector(20, 1, 10),
            color=color.green)  # Creates the field

animation_time_step = 0.001  # seconds
rate_of_animation = 1 / animation_time_step
time_step = 0.01
stop_time = 50.0  # This can be changed for a longer animation

Time_1 = array([])
Force_1 = array([])
time = 0
while time < stop_time:
    rate(rate_of_animation)

    acceleration = (eq - ball.pos) * (
            spring.constant / ball.mass)  # a = x * k / kg  (Similar to F=-k*x, although lacks mass)

    ball.velocity = ball.velocity + acceleration * time_step
    ball.pos = ball.pos + ball.velocity * time_step + spring.velocity * time_step  # Moves ball with spring

    spring.pos = spring.pos + spring.velocity * time_step  # Moves spring with given speed from earlier
    spring.axis = ball.pos - spring.pos

    hanger.pos = hanger.pos + hanger.velocity * time_step  # Moves block with given speed from earlier

    if hanger.pos.x > 2:  # Keeps it to a confined space
        spring.velocity = -spring.velocity
        hanger.velocity = -hanger.velocity

    if hanger.pos.x < -2:  # Keeps it to a confined space
        spring.velocity = -spring.velocity
        hanger.velocity = -hanger.velocity

    Time_1 = append(Time_1, time)
    Force_1 = append(Force_1, (acceleration * ball.mass).x)

    time += time_step

"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$This_is_just_a_divider_to_make_things_look_pretty$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""

ball = sphere(pos=vector(12, -2, 0), velocity=vector(0, 0, 0), radius=0.5, mass=1.0,
              color=color.cyan)  # Creates the ball
pivot = vector(0, -2, 0)  # Center or coordinate system
speed = vector(0.5, 0, 0)  # Change this to change speed
spring = helix(pos=pivot, velocity=speed, axis=ball.pos - pivot, radius=0.4, constant=1,
               thickness=0.1, coils=20, color=color.red)  # Creates the spring
hanger = box(pos=pivot, velocity=speed, color=color.white)  # Creates the block
eq = vector(9, -2, 0)  # Equilibrium position (how far away it would need to be away from spring to be at equilibrium)

Time_2 = array([])
Force_2 = array([])
time = 0
while time < stop_time:
    rate(rate_of_animation)

    acceleration = (eq - ball.pos) * (
            spring.constant / ball.mass)  # a = x * k / kg  (Similar to F=-k*x, although lacks mass)

    ball.velocity = ball.velocity + acceleration * time_step
    ball.pos = ball.pos + ball.velocity * time_step + spring.velocity * time_step  # Moves ball with spring

    spring.pos = spring.pos + spring.velocity * time_step  # Moves spring with given speed from earlier
    spring.axis = ball.pos - spring.pos

    hanger.pos = hanger.pos + hanger.velocity * time_step  # Moves block with given speed from earlier

    if hanger.pos.x > 2:  # Keeps it to a confined space
        spring.velocity = -spring.velocity
        hanger.velocity = -hanger.velocity

    if hanger.pos.x < -2:  # Keeps it to a confined space
        spring.velocity = -spring.velocity
        hanger.velocity = -hanger.velocity

    Time_2 = append(Time_2, time)
    Force_2 = append(Force_2, (acceleration * ball.mass).x)

    time += time_step

"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$This_is_just_a_divider_to_make_things_look_pretty$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""

ball = sphere(pos=vector(12, -4, 0), velocity=vector(0, 0, 0), radius=0.5, mass=2.0,
              color=color.magenta)  # Creates the ball
pivot = vector(0, -4, 0)  # Center or coordinate system
speed = vector(0.5, 0, 0)  # Change this to change speed
spring = helix(pos=pivot, velocity=speed, axis=ball.pos - pivot, radius=0.4, constant=1,
               thickness=0.1, coils=20, color=color.red)  # Creates the spring
hanger = box(pos=pivot, velocity=speed, color=color.white)  # Creates the block
eq = vector(9, -4, 0)  # Equilibrium position (how far away it would need to be away from spring to be at equilibrium)

Time_3 = array([])
Force_3 = array([])
time = 0
while time < stop_time:
    rate(rate_of_animation)

    acceleration = (eq - ball.pos) * (
            spring.constant / ball.mass)  # a = x * k / kg  (Similar to F=-k*x, although lacks mass)

    ball.velocity = ball.velocity + acceleration * time_step
    ball.pos = ball.pos + ball.velocity * time_step + spring.velocity * time_step  # Moves ball with spring

    spring.pos = spring.pos + spring.velocity * time_step  # Moves spring with given speed from earlier
    spring.axis = ball.pos - spring.pos

    hanger.pos = hanger.pos + hanger.velocity * time_step  # Moves block with given speed from earlier

    if hanger.pos.x > 2:  # Keeps it to a confined space
        spring.velocity = -spring.velocity
        hanger.velocity = -hanger.velocity

    if hanger.pos.x < -2:  # Keeps it to a confined space
        spring.velocity = -spring.velocity
        hanger.velocity = -hanger.velocity

    Time_3 = append(Time_3, time)
    Force_3 = append(Force_3, (acceleration * ball.mass).x)

    time += time_step

ax = plt.subplots()
ax = plt.gca()
ax.set_facecolor((0.0, 0.0, 0.0))  # Sets Background to black
plt.plot(Time_1, Force_1, color="yellow", label='Mass = 0.5')
plt.plot(Time_2, Force_2, color="cyan", label='Mass = 1.0')
plt.plot(Time_3, Force_3, color="magenta", label='Mass = 2.0')
plt.xlabel('Time')
plt.ylabel('Force')
plt.legend()
plt.show()
