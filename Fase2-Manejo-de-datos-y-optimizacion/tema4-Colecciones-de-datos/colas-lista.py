# FIFO primero entrar, primero en salir deque para usar colas en py

from  collections import deque
cola = deque(['alejandro','jose','maria'])
cola.app('juan')
cola.app('javier')

# sacar el valor con popleft para usar colas
p = cola.popleft()
