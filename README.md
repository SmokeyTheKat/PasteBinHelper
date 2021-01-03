# PasteBinHelper

A PasteBin helper program that can download, find, search, and upload Pastes.

## Install

Make Targets
| Target | Description |
|-------:|-------------|
| _(none)_ | same as install |
| install | adds pbh to /usr/bin |
| remove | removes pbh from /usr/bin/ |

## Usage

To download a Paste just type the UID as a paramater.
```
$ pbh j305UHn3
```

To download it to a file just pipe it to your output file.
```
$ pbh j305UHn3 > output.txt
```

Use --upload to upload anyfile and it will return the UID.
```
$ pbh --upload myfile.txt
UID: Gcr0UC1T
```

To Search on PasteBin with keywords use --find.
```
$ pbh --find "epic python program"
```

To download one of the listed file from the search, put the number you want to download after the keywords or use the live selector.
```
$ pbh --find "epic python program" 2
```

You can see the recent Public Pastes use --top.
```
$ pbh --top
1: my program    -    aJe3HC7J
2: my program    -    Nha7bI3A
3: my program    -    kAj6nE1b
4: my program    -    Hie4Hfk9
```
