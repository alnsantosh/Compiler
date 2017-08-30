import ast
import operator

operators_dictionary = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
             ast.Div: operator.truediv}  #This dictionary is to map the ast operators to the python operators
symbol = {} # This dictionary (symbol table) is to store the variables for the evaluation of the code

def process(node):  #This is a recursive function to parse through the nodes of ast and evaluate it.
    if isinstance(node, ast.Name): # <number>
        return symbol[node.id]
    elif(isinstance(node,ast.Num)):
        return node.n
    elif isinstance(node, ast.BinOp): # <left> <operator> <right>
        return operators_dictionary[type(node.op)](process(node.left), process(node.right))
    elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
        return operators_dictionary[type(node.op)](process(node.operand))


f=open(sys.argv[1],'r') #reading file
stringg=f.read()
file=stringg.split('\n')  #Since the interpreter excutes one statement at a time, file list consist of all the statements which will be parsed in a sequential manner
# print file
for s in file:
    if(s!=''): #If the file has a line which has no statements, then that line is ignored
#s='print x+10'
        node=ast.parse(s,mode='exec')
        #print (node.body[0])
        # print node.body[0].targets[0].id
        if(isinstance(node.body[0],ast.Assign)):
            symbol[node.body[0].targets[0].id]=process(node.body[0].value)
        elif (isinstance(node.body[0],ast.Print)):
            print process(node.body[0].values[0])
