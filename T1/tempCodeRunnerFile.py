def drawline2():
    x1_v, y1_v, x2_v, y2_v = 250, 10, 250, 500
    x1_h, y1_h, x2_h, y2_h = 10, 250, 500, 250
    can1.create_line(x1_v, y1_v, x2_v, y2_v, width=2, fill='red')
    can1.create_line(x1_h, y1_h, x2_h, y2_h, width=2, fill='red')
