import ast
import operator

class CompilerDesign:

    operators_dictionary = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
                 ast.Div: operator.truediv}  #This dictionary is to map the ast operators to the python operators
    symbol = {} # This dictionary (symbol table) is to store the variables for the evaluation of the code

    def process(self,node):  #This is a recursive function to parse through the nodes of ast and evaluate it.
        if isinstance(node, ast.Name): # <number>
            return self.symbol[node.id]
        elif(isinstance(node,ast.Num)):
            return node.n
        elif isinstance(node, ast.BinOp): # <left> <operator> <right>
            return self.operators_dictionary[type(node.op)](self.process(node.left), self.process(node.right))
        elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
            return self.operators_dictionary[type(node.op)](self.process(node.operand))

    def start(self):
        f=open('ex1.py','r') #reading file
        stringg=f.read()
        file=stringg.split('\n')  #Since the interpreter excutes one statement at a time, file list consist of all the statements which will be parsed in a sequential manner
        # print file
        list=[]
        for s in file:
            if(s!=''): #If the file has a line which has no statements, then that line is ignored
        #s='print x+10'
                node=ast.parse(s,mode='exec')
                #print (node.body[0])
                # print node.body[0].targets[0].id
                if(isinstance(node.body[0],ast.Assign)):
                    self.symbol[node.body[0].targets[0].id]=self.process(node.body[0].value)
                elif (isinstance(node.body[0],ast.Print)):
                    print self.process(node.body[0].values[0])
                    list.append(self.process(node.body[0].values[0]))
        return list

CompilerDesign().start()

