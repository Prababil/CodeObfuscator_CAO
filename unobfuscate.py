from brainf import Brainf
f = open("out.bf","r")
code = f.read()
f.close();
result = Brainf().interpret(code)
exec(result);