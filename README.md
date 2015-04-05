# MakeyPi
A connected Bird table to take a picture every time it lands

## Install daemon

```bash
cp makeypi /etc/init.d/makeypi
```
## Run daemon

```bash
sudo service makeypi start
```

## Add daemon at startup

```bash
sudo insserv makeypi
```

## Remove ademon at startup

```bash
sudo insserv -r makeypi
```