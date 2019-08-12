# Slice piece of "World"
s = 'Hello, World!'
Start = s.find('World')
End = s.find('!')
print("1st:", s[Start:End])

step = 5
# Reverse sequence of numbers divided by 5
arr_len = 100
a = list(range(arr_len))
print("2nd:", a[arr_len - step::-step])

# Named slice
arr_len = 200
a = list(range(arr_len))
x = slice(arr_len - step, None, -step)
print("3rd:", a[x])as