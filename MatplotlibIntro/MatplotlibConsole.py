Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> x = np.random.randint(1000,10000,500)
>>> y = np.arange(500)
>>> len(x)
500
>>> len(y)
500
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000001F8240DF828>]
>>> plt.show()
>>> plt.plot(x,y,color='red')
[<matplotlib.lines.Line2D object at 0x000001F825BC15F8>]
>>> plt.show()
>>> y = np.random.randint(1000,10000,500)
>>> x = np.arange(500)
>>> plt.plot(x,y,color='red')
[<matplotlib.lines.Line2D object at 0x000001F825D96A58>]
>>> plt.show()
>>> plt.plot(x,y,'o')
[<matplotlib.lines.Line2D object at 0x000001F825F6AB70>]
>>> plt.show()
>>> plt.plot(x,y,'ro')
[<matplotlib.lines.Line2D object at 0x000001F82613CBA8>]
>>> plt.show()
>>> y = np.random.randint(1000,10000,20)
>>> x = np.arange(20)
>>> plt.plot(x,y,'ro')
[<matplotlib.lines.Line2D object at 0x000001F8272E7860>]
>>> plt.show()
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000001F8274D0DD8>]
>>> plt.show()
>>> 
