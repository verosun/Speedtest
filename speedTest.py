import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import speedtest
import time
plt.style.use('fivethirtyeight')
plt.ylim((0,150))
st = speedtest.Speedtest()
timeList= []
speed = []
startTime = time.time()
index = count()


def animate(i):
    plt.cla()
    plt.ylim((0,150))
    dls = st.download() /1000 /1000
    curTime = time.time() - startTime
    timeList.append(curTime)
    speed.append(dls)
    print(dls )
    plt.plot(timeList,speed)

    plt.legend(loc='upper left')
    plt.xlabel("Time (sec)")
    plt.ylabel("MB/s")
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=10000)

plt.tight_layout()
plt.show()