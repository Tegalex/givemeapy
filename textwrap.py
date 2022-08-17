import textwrap

doc="""the wrap() method is just like fill() excepet that it returns a list of strings instead of one big string with newlines to separeta the wrapped lines."""

#print(textwrap.fill(doc, width=50))
print(textwrap.shorten(doc, width=50, placeholder="...ect"))