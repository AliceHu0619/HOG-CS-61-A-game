import code
import functools
import inspect
import re
import signal
import sys


def main(fn):

	if inspect.stack()[1][0].f_locals['__name__'] == '__main__':
		args = sys.argv[1:]
		fn(*args)

	return functools


_PREFIX = ''

def trace(fn):

	@functools.wraps(fn)

	def wrapped(*args, **kwds):
		global _PREFIX
		reprs = [repr(e) for e in args]
		reprs += [repr(k) + '=' + repr(v) for k, v in kwds.items()]

		log('{0}({1})'.format(fn.__name__, ','.join(reprs)) + ':')

		_PREFIX += '      '

		try:
			result = fn(*args, **kwds)
			_PREFIX = _PREFIX[:4]

		except Exception as e:
			log(fn.__name__ + 'exited via exeception')
			_PREFIX = _PREFIX[:4]
			raise


		log('{0}({1}) -> {2}'.format(fn.__name__, ','.join(reprs), result))
		return result

	return wrapped


def log(message):
	print(_PREFIX + re.sub('\n', '\n' + _PREFIX, str(message)))















