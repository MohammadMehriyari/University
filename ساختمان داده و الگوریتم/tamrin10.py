import time
print('Recrusive Way')
start = time.time()

def TowerOfHanoi(n , source, destination, auxiliary):
	if n==1:
		print ("Move disk 1 from source",source,"to destination",destination)
		return
	TowerOfHanoi(n-1, source, auxiliary, destination)
	print ("Move disk",n,"from source",source,"to destination",destination)
	TowerOfHanoi(n-1, auxiliary, destination, source)

n = 4
TowerOfHanoi(n,'A','B','C')
end = time.time()
print('\nTimer =',end-start)
print('////////////////////////////////////////\n')

print('Iterative Way')
start = time.time()
def hanoi_iterative(n, source, auxiliary, target):
    stack = [(n, source, auxiliary, target)]
    while stack:
        n, source, auxiliary, target = stack.pop()
        if n == 1:
            print(f"Move disk 1 from {source} to {target}")
        else:
            stack.append((n-1, source, target, auxiliary))
            stack.append((1, source, auxiliary, target))
            stack.append((n-1, auxiliary, source, target))
hanoi_iterative(3,'A','B','C')
end = time.time()
print('\nTimer =',end-start)