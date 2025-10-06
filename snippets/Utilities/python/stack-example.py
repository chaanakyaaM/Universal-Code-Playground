# Title: Basic stack implementation
# Topic: Utilities
# Language: python
# Example: see bottom

def main(n=10):
    a,b=0,1
    out=[]
    for _ in range(n):
        out.append(a)
        a,b=b,a+b
    return out

if __name__ == '__main__':
    print(main(10))
