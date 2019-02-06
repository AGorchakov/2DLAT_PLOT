import matplotlib.pyplot as plt

def plt2Dlat(x, L, R, deltaH=0):
    H = 0.0
    for i in range(3, 3*len(x), 3):
        H = H + x[(i+3*deltaH)%len(x)]
    fig, ax = plt.subplots(figsize=(L+4*R, H+4*R))
    plt.xlim(-2*R, L+2*R)
    plt.ylim(-2*R, H+2*R)
    h = 0.0
    for i in range(0, 3*len(x), 3):
        l = x[(i+3*deltaH)%len(x)+1]
        while l <= L:
            circle1 = plt.Circle((l, h), R, color='blue')
            l = l + x[(i+3*deltaH)%len(x)+2]
            ax.add_artist(circle1)
        h = h + x[((i+3*deltaH)+3)%len(x)]
    grid1 = plt.grid(True) 
    fig.savefig('plotcircles.png')

x = 0.730256,0,2.52968,1.46051,0,2.52968,0.730256,1.26484,2.52968,1.46051,1.26484,2.52968
    
L = 16
R=0.3
plt2Dlat(x, L, R, 0)
