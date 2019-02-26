from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob

def damped_vibrations(t, A, b, w):
    return A*exp(-b*t)*cos(w*t)

def compute2(A, b, w, T, resolution=500):
    """Return filename of plot of the damped_vibration function."""
    t = linspace(0, T, resolution+1)
    u = damped_vibrations(t, A, b, w)
    plt.figure()  # needed to avoid adding curves in plot
    plt.plot(t, u)
    plt.title('A=%g, b=%g, w=%g' % (A, b, w))


    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)

    # Use time since Jan 1, 1970 in filename in order make
    # a unique filename that the browser has not chached
    #plotfile = os.path.join('/home/fairfieldlabs/mysite/static/', str(time.time()) + '.png')
    # plotfile = os.path.join('/home/fairfieldlabs/mysite/static/', 'pic' + '.png') THIS DOESN'T WORK

    # plotfile = os.path.join('static/', 'pic' + '.png')

    plotfile = os.path.join('static/', str(time.time()) + '.png')
    plt.savefig(plotfile)
    return plotfile

if __name__ == '__main__':
    print (compute2(1, 0.1, 1, 20))