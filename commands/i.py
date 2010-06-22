def _DOWN(env, document):
	env.y += env.num or 1
	if env.y > Hmaxw:
		if (document.yindex + env.y - Hmaxw) < len(document.text): #FIXME
			document.yindex += env.y - Hmaxw
		else:
			document.yindex = len(document.text) - 1
		env.y = Hmaxw
		refreshscreen()
	env.clampx(env, document)
	updatepos()
def _UP(env, document):
	env.y -= env.num or 1
	if env.y < 0:
		if document.yindex > -env.y:
			document.yindex += env.y
		else:
			document.yindex = 0
		env.y = 0
		refreshscreen()
	env.clampx(env, document)
	updatepos()
def _LEFT(env, document):
	env.x = max(env.x - 1, 0)
	env.clampx(env, document)
	updatepos()
def _RIGHT(env, document):
	#env.x = min(env.x + 1, Wmax)
	env.x = env.x + 1
	env.clampx(env, document)
	updatepos()

self['\x1b[A'] = _UP
self['\x1b[B'] = _DOWN
self['\x1b[C'] = _RIGHT
self['\x1b[D'] = _LEFT
