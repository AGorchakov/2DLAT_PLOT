import matplotlib.pyplot as plt

def plt2Dlat(x, L, R):
    H = 0.0
    for i in range(3, len(x), 3):
        H = H + x[i]
    fig, ax = plt.subplots(figsize=(L+4*R, H+4*R))
    plt.xlim(-2*R, L+2*R)
    plt.ylim(-2*R, H+2*R)
    h = 0.0
    for i in range(0, len(x), 3):
        l = x[i+1]
        while l <= L:
            circle1 = plt.Circle((l, h), R, color='blue')
            l = l + x[i+2]
            ax.add_artist(circle1)
        h = h + x[(i+3)%len(x)]
    grid1 = plt.grid(True) 
    fig.savefig('plotcircles.png')

x = [1,0,4,1,0.651465,1.82737,1,1.81706,3.72179,1,1.90563,3.88595]
L = 16
R=0.3
plt2Dlat(x, L,R)
