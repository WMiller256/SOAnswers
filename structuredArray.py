import numpy as np

def add_field(a, *descr):
	shape = a.shape if len(a.shape) else (1,)
	b = np.empty(shape, dtype=a.dtype.descr + [*descr])
	for name in a.dtype.names:
	    b[name] = a[name]
	return b

a = np.array(
    [(1, False), (2, False), (3, False), (4, True)],
    dtype=[('id', 'i4'), ('used', '?')]
)

b = add_field(a, ('new', 'O'))
b['new'] = [[]*b.shape[0]]
print(b)

c = a[0]
d = add_field(c, ('newer', 'O'))
d['newer'] = [[]*d.shape[0]]
print(d)
