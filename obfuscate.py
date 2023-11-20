from brainf import Brainf
f = open("test.py","r")
code = f.read()
f.close();
result = Brainf().convert(code)
f =  open("out.bf","w")
f.write(result)
print(result)
f.close