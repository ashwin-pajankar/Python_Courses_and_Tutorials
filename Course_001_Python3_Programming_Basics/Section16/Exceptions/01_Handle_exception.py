try:
    a = 1
    b = 0
    c = a / b
    print('DEBUG: This will not be executed!')
except Exception:
    print('Exception Encountered!')

print('DEBUG: This will be executed!')
