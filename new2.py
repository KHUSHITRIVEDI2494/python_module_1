# # n=int(input('enter number'))
# # sum=0

# # for i in range(1,n+1):
# #     sum=sum+1

# print('sum=',sum)

n=int(input('enter a number'))
oddsum=0
evensum=0

for i in range(1,n+1):
    if i%2==0:
        evensum=evensum+i

    else:
        oddsum=oddsum+i

print('evensum:',evensum)
print('oddsum:',oddsum)