def calcAngle(h, m):
    if (h < 0 or m < 0 or h > 12 or m > 60):
        print('Wrong input')

    if (h == 12):
        h = 0
    if (m == 60):
        m = 0
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m
    # print(hour_angle, minute_angle)
    angle = abs(hour_angle - minute_angle)
    # print(angle)
    angle = min(360 - angle, angle)
    # print(angle)
    return angle

h = 5
m = 40
print('Angle ', calcAngle(h, m))
