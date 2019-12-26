import subprocess

try:
    from IPython.display import Javascript
    from IPython.display import display
except:
    print('unable to import from `IPython` package, this extension will not work')
    raise ImportError()

'''
TODOs

[ ] some git subprocess commands


'''

# JS Functionality ----------------------

def demo_js():
    ''' 
         demo_js uses `display.display()` to execute a Javascript payload
    '''
    
    print('see devtools console for output')
    display(
        Javascript(data='console.log("demo_js");')
    )
    
def demo_js_to_python():
    ''' 
         a trick to get data in js into the python kernel the notebook
         is connected to
    '''
    
    js = '''
    IPython.notebook.kernel.execute("a=1");
    IPython.notebook.kernel.execute("print(f'the value of `a` is : {a}`");
    '''

    js = '\n'.join([line.strip() for line in js.split('\n') if line.strip !=''])
    
    display(Javascript(data=js))


def promise_pattern():
    '''
         show how to run code syncronously with promise pattern

         open devtools console before running, to see ~1 second delay
         before console outputs.
    '''    
    
    js = '''
    function demo() {
        function lots(){
            var x = 1;
            for (var i=0; i<1000000000; i++) {
                x += i
            }
        }
        Promise.resolve(
            lots()
            ).then(function(){
                return console.log('printing out with ~1 sec delay?')
                }
            );
        }
    demo();
    '''
    print('see devtools console for printout')
    display(Javascript(data=js))

def promise_set_print():
    '''
         doesnt work yet
         
         designed to show sync execution with messaging to python kernel

         works when function is called twice probably because biggie 
         has already been set at that point
    '''    
    
    js = '''
    
    var biggie = 0;
    
    function demo() {
        function lots(){
            var x = 1;
            for (var i=0; i<1000000000; i++) {
                x += i
            }
            biggie = x
        }
        Promise.resolve(
            lots()
            ).then(function(){
                return secondFunction();
                }
            ).then(function(){
                return thirdFunction();
                }
            );
            
            function secondFunction() {
                IPython.notebook.kernel.execute("a="+ biggie);
            }
            function thirdFunction() {
                  console.log('printing out with ~1 sec delay and setting a to bigges value')
            }
        }
    
    demo();
    '''
    
    display(Javascript(data=js))
    print('done')
    
    #These don't work right now, `a` only becomes available once we're back in notebook
    # global a
    # print([(k,v) for k,v in globals().items() if k == 'a'])
    # print(a)
    # print(f'the value of biggie (the variable `a` is this kernel) is: {a}')

def get_a():
    # doesnt work either
    global a
    print(a)
    