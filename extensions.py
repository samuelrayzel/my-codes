print('File name:')

x = input()

z = x.lower().strip()

#.gif,.jpg,.jpeg,.png,.pdf,.txt,.zip

if(z[-1] == 'f' and z[-2] == 'i' and z[-3] == 'g' and z[-4] == '.' ):

    print('image/gif')

elif(z[-1] == 'g' and z[-2] == 'p' and z[-3] == 'j' and z[-4] == '.' ):

    print('image/jpeg')

elif(z[-1] == 'g' and z[-2] == 'e' and z[-3] == 'p' and z[-4] == 'j' and z[-5] == '.' ):

    print('image/jpeg')

elif(z[-1] == 'g' and z[-2] == 'n' and z[-3] == 'p' and z[-4] == '.' ):

    print('image/png')

elif(z[-1] == 'f' and z[-2] == 'd' and z[-3] == 'p' and z[-4] == '.' ):

    print('application/pdf')

elif(z[-1] == 't' and z[-2] == 'x' and z[-3] == 't' and z[-4] == '.' ):

    print('text/plain')

elif(z[-1] == 'p' and z[-2] == 'i' and z[-3] == 'z' and z[-4] == '.' ):

    print('application/zip')

elif(z[-1] == 'n' and z[-2] == 'i' and z[-3] == 'b' and z[-4] == '.' ):

    print('application/octet-stream')

else:

    print('application/octet-stream')
