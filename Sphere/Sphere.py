import turtle as kreggscode

kreggscode.bgcolor('black')
kreggscode.tracer(2)
kreggscode.pensize(2)
c=['yellow', 'cyan']
for I in range(1200):
    kreggscode.color(c[I%2])
    kreggscode.up()

    kreggscode.fd(I)
    kreggscode.down()
    kreggscode.rt(121)
    for k in range(5):
        kreggscode.fd(k*5)
        kreggscode.lt(130)
kreggscode.done()