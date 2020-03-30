# Enigma

Encrypt machine.

## How to use

`virtualenv` is recommended. Use `requirements` to install required package.
```
pip3 install -r requirements.txt
```

See `demos` for examples.

Temporary solution to missing module

```
export PYTHONPATH=/your/path/to/Enigma
```

### UI

Since UI is supported now, with `pyqt5`, simply run

```
python3 ui.py
```

## TODO

### Rotor

1. Support Chinise rotor.
2. Support Japanese rotor.

### Enigma

1. ~~Support to encrypt a string.~~
2. Support random reflector generation.
3. Expose a way to exchange the order of the rotors.
4. ~~Support '\n'.~~

### UI

1. ~~Create a UI to encode/decode.~~
2. Create a button to save the input and output to a file.
3. Create a loading alert, which needs an async call.

### Unit Test

1. ~~Cover super long string case.~~
2. Cover complex mulit rotations.

## Future

1. Create IOS/Android apps.
2. Create as a web serivce.
