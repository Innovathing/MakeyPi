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
insserv makeypi
```

## Remove ademon at startup

```bash
insserv -r makeypi
```