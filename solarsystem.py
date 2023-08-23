# Ensure the right backend for Spyder
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
from matplotlib import animation

# Constants and initial setup with constants and the objects’ masses, velocities, and gravitational constants.
G = 6.67e-11                  # constant G
Ms = 2.0e30                   # sun
Me = 5.972e24                 # earth        
Mm = 6.39e23                  # mars
Mc = 6.39e20                  # comet
AU = 1.5e11                   # earth sun distance
daysec = 24.0*60*60           # seconds of a day
e_ap_v = 29290                # earth velocity at aphelion
m_ap_v = 21970                # mars velocity at aphelion
commet_v = 7000               # comet velocity

gravconst_e = G*Me*Ms
gravconst_m = G*Mm*Ms
gravconst_c = G*Mc*Ms

# Starting positions
# earth
xe, ye, ze = 1.0167*AU, 0, 0
xve, yve, zve = 0, e_ap_v, 0

# mars
xm, ym, zm = 1.666*AU, 0, 0
xvm, yvm, zvm = 0, m_ap_v, 0

#comet
xc, yc, zc = 2*AU, 0, 0
xvc, yvc, zvc = 0, commet_v, 0

# sun
xs, ys, zs = 0, 0, 0
xvs, yvs, zvs = 0, 0, 0

t = 0.0
dt = 1*daysec

# these lists store the points that the objects are at
xelist, yelist, zelist = [], [], []
xmlist, ymlist, zmlist = [], [], []
xclist, yclist, zclist = [], [], []
xslist, yslist, zslist = [], [], []


# save the initial position in their respective lists
#earth
xelist.append(xe)
yelist.append(ye)
zelist.append(ze)

#mars
xmlist.append(xm)
ymlist.append(ym)
zmlist.append(zm)

#comet
xclist.append(xc)
yclist.append(yc)
zclist.append(zc)


# Simulation
# The new radii, forces, velocities, and positions are calculated at each second for 5 years. The new position is then added to the object’s list. 

while t < 5*365*daysec:
    
    ################ earth #############
    # compute G force on earth
    rx,ry,rz = xe - xs, ye - ys, ze - zs
    modr3_e = (rx**2+ry**2+rz**2)**1.5
    
    fx_e = -gravconst_e*rx/modr3_e     
    fy_e = -gravconst_e*ry/modr3_e
    fz_e = -gravconst_e*rz/modr3_e
    
    # update quantities how is this calculated?  F = ma -> a = F/m
    xve += fx_e*dt/Me
    yve += fy_e*dt/Me
    zve += fz_e*dt/Me
    
    # update position
    xe += xve*dt
    ye += yve*dt 
    ze += zve*dt
    
    # save the position in list
    xelist.append(xe)
    yelist.append(ye)
    zelist.append(ze)
    
    ################ mars #############
    # compute G force on mars
    rx_m,ry_m,rz_m = xm - xs, ym - ys, zm - zs
    modr3_m = (rx_m**2+ry_m**2+rz_m**2)**1.5
    
    fx_m = -gravconst_m*rx_m/modr3_m
    fy_m = -gravconst_m*ry_m/modr3_m
    fz_m = -gravconst_m*rz_m/modr3_m

    xvm += fx_m*dt/Mm
    yvm += fy_m*dt/Mm
    zvm += fz_m*dt/Mm
    
    # update position
    xm += xvm*dt
    ym += yvm*dt 
    zm += zvm*dt
    
    # save the position in list
    xmlist.append(xm)
    ymlist.append(ym)
    zmlist.append(zm)
    
    ################ comet ##############
    # compute G force on comet
    rx_c,ry_c,rz_c = xc - xs, yc - ys, zc - zs
    modr3_c = (rx_c**2+ry_c**2+rz_c**2)**1.5
    fx_c = -gravconst_c*rx_c/modr3_c
    fy_c = -gravconst_c*ry_c/modr3_c
    fz_c = -gravconst_c*rz_c/modr3_c
    
    xvc += fx_c*dt/Mc
    yvc += fy_c*dt/Mc
    zvc += fz_c*dt/Mc
    
    # update position
    xc += xvc*dt
    yc += yvc*dt 
    zc += zvc*dt
    
    # add to list
    xclist.append(xc)
    yclist.append(yc)
    zclist.append(zc)
    
    ################ the sun ###########
    # update quantities how is this calculated?  F = ma -> a = F/m
    xvs += -(fx_e+fx_m)*dt/Ms
    yvs += -(fy_e+fy_m)*dt/Ms
    zvs += -(fz_e+fz_m)*dt/Ms
    
    # # update position
    xs += xvs*dt
    ys += yvs*dt 
    zs += zvs*dt
    xslist.append(xs)
    yslist.append(ys)
    zslist.append(zs)
    
    # update dt
    t +=dt

print('data ready')


# Animation setup

# grid size
fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect('equal')
ax.grid()

# earth is blue. The text “Earth” follows point_e as it moves
line_e, = ax.plot([], [], lw=1, c='blue')
point_e, = ax.plot([AU], [0], marker="o", markersize=4, markeredgecolor="blue", markerfacecolor="blue")
text_e = ax.text(AU, 0, 'Earth')

# mars is red. The text “Mars” follows point_m as it moves
line_m, = ax.plot([], [], lw=1, c='red')
point_m, = ax.plot([1.666*AU], [0], marker="o", markersize=3, markeredgecolor="red", markerfacecolor="red")
text_m = ax.text(1.666*AU, 0, 'Mars')

# comet is black. The text "Comet" follows point_c as it moves
line_c, = ax.plot([],[], lw=1, c='black')
point_c, = ax.plot([2*AU], [0], marker="o", markersize=2, markeredgecolor="black", markerfacecolor="black")
text_c = ax.text(2*AU,0,'Comet')

# the sun is yellow
point_s, = ax.plot([0], [0], marker="o", markersize=7, markeredgecolor="yellow", markerfacecolor="yellow")
text_s = ax.text(0, 0, 'Sun')

ax.axis('equal')
ax.set_xlim(-3*AU, 3*AU)
ax.set_ylim(-3*AU, 3*AU)

exdata, eydata = [], []
mxdata, mydata = [], []
cxdata, cydata = [], []

# The points for each object are put into their respective data sets to be plotted on grid
def update(i):
    
    exdata.append(xelist[i])
    eydata.append(yelist[i])
    
    mxdata.append(xmlist[i])
    mydata.append(ymlist[i])
    
    cxdata.append(xclist[i])
    cydata.append(yclist[i])
    
    line_e.set_data(exdata,eydata)
    point_e.set_data(xelist[i],yelist[i])
    text_e.set_position((xelist[i],yelist[i]))
    
    
    line_m.set_data(mxdata,mydata)
    point_m.set_data(xmlist[i],ymlist[i])
    text_m.set_position((xmlist[i],ymlist[i]))
    
    line_c.set_data(cxdata,cydata)
    point_c.set_data(xclist[i],yclist[i])
    text_c.set_position((xclist[i],yclist[i]))

    point_s.set_data(xslist[i],yslist[i])
    text_s.set_position((xslist[i],yslist[i]))
    
    ax.axis('equal')
    ax.set_xlim(-3*AU,3*AU)
    ax.set_ylim(-3*AU,3*AU)
    #print(i)
    return line_e,line_m,line_c,point_s,point_e,point_m,point_c,text_e,text_s,text_m,text_c

anim = animation.FuncAnimation(fig, func=update, frames=len(xelist), interval=1, blit=False)

plt.show(block=True)
