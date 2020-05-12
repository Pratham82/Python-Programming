'''
 Laziness and the infinite 
 Generators only do enough work to produce requested data
 This allows generators to model infinite(just very large) sequences
 Examples: Sensor readings, Mathematical sequences, Content of large files
'''
def lucas():
    yield 2
    a = 2
    b = 3
    while True:
        yield b
        a,b = b, a+b

for x in lucas():
    print(x)

