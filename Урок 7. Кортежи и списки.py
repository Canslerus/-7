immutable_var= 5, 3, 'z', 'b'
print (immutable_var)
# изменить не получается, так как кортеж не поддаётся изменению
# чтобы можно было изменять содержимое переменной используем список
mutable_list=[3, 6, 'Tbi', 'd']
mutable_list[2]='h'
print (mutable_list)
mutable_list.append('Tb')
print (mutable_list)

