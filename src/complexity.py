import time, random
from Coord import Point
import matplotlib.pyplot as plt
import brute as b
import jarvis as j
import graham as g

def random_points(points, n):
    randomx = []
    randomy = []
    for i in range(0, n):
        # any random numbers from 0 to 1000
        randomx.append(random.randint(0,100))
        randomy.append(random.randint(0,100))
        x,y = randomx[i], randomy[i]
        points.append(Point(x, y))


def time_complexity(k):
    points = []
    times_brute = []
    times_jarvis = []
    times_graham = []
    n = []

    for i in range(5,k+5):
        n.append(i)
        random_points(points, i)
        print(i-4)
        # Brute
        tic = time.perf_counter()
        b.convex_hull(points, len(points))
        toc = time.perf_counter()
        times_brute.append(toc-tic)

        # Jarvis
        tic = time.perf_counter()
        j.convex_hull(points, len(points))
        toc = time.perf_counter()
        times_jarvis.append(toc-tic)

        # Graham
        tic = time.perf_counter()
        g.convex_hull(points)
        toc = time.perf_counter()
        times_graham.append(toc-tic)

    return n, times_brute, times_jarvis, times_graham



n, times_brute, times_jarvis, times_graham = time_complexity(20)


# Plot brute algo
fig, ax = plt.subplots()
ax.plot(n,times_brute)

ax.set(xlabel='Time required', ylabel='No. of elements',
       title='Brute algo time complexity')
ax.grid()

fig.savefig("brute.png")
plt.show()

# Plot Jarvis algo
fig, ax = plt.subplots()
ax.plot(n,times_jarvis)

ax.set(xlabel='Time required', ylabel='No. of elements',
       title='Jarvis algo time complexity')
ax.grid()

fig.savefig("jarvis.png")
plt.show()


# Plot Graham algo
fig, ax = plt.subplots()
ax.plot(n,times_graham)

ax.set(xlabel='Time required', ylabel='No. of elements',
       title='Graham algo time complexity')
ax.grid()

fig.savefig("graham.png")
plt.show()