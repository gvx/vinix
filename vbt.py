import lpod
import lpod.document
#doc = lpod.document.odf_new_document_from_type('text')
doc = lpod.document.odf_get_document('simple.odt')
body = doc.get_body()
elemlist = []
metalist = body.get_children()[1:]
print(doc.get_content().serialize(True))
for e in metalist:
	#print(e)
	start = len(e.get_text())
	spans = []
	for k in e.get_span_list():
		end = start + len(k.get_text())
		style = k.get_text_style()
		mode = '\x1b[0m'
		if style:
			style = doc.get_style("text", style)
			properties = style.get_style_properties()
			if properties.get('fo:font-weight') == 'bold':
				mode = '\x1b[1m'
			elif properties.get('fo:font-style') == 'italic':
				mode = '\x1b[4m'
		spans.append((start,end, mode))
		print(e,start,end,mode)
		start = end
	text = e.get_text(True)
	for start, end, mode in reversed(spans):
		text = (text[:start] + mode + text[start:end] + '\x1b[0m' +
			text[end:])
	if e.get_tag() == 'text:h':
		text = (e.get_outline_level()-1)* ' ' + '\x1b[1;4m' + text + '\x1b[0m'
	else:
		text = '    ' + text
	elemlist.append(text)
	#print(e.get_children())
print('\n'.join(elemlist))
