# **Documentation**

## **Decorators**

### **Log in validation**
- The validation in the decorator definition doesn't work
```
if logged_in == True:
    return new_func
else:
    return  /None
```
- Tried raising UserNotLoggedInException
 - However, it seems not to check if logged_in even if it is True
 - Will try printing as I go along
 - It seems I have to set logged_in before everything runs, which means `@requires_login` is running before everything else?
 - Remember there's also:
 ```
 if __name__ == __main__:
      pass
      # Test things
 ```
for testing things locally
