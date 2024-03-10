# Unittest for console.py

For testing the console, you should “intercept” STDOUT of it, we highly recommend you to use:
```
with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")
```
Otherwise, you will have to re-write the console by replacing `precmd` by `default`.
