from mod_soma import add as somaai
import wikipedia

summary = wikipedia.summary("Python (programming language)", sentences=2)
print(summary)
vamosver = somaai(2,4)
print(vamosver)
