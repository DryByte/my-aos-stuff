# My scripts
All scripts here is made to be used with [Piqueserver](https://github.com/piqueserver/piqueserver).

## Scripts Informations
<details><summary>AutoUpdater<summary>

- Made by sByte

Auto update your scripts, its useful when you use the same
script in various servers and need to change something
in a specific server, this is compatible with local files
and web files, like in github.

Always keep this script at the top of all other scripts that
will receive an update.

Add this to your config:

```toml
[autoupdater]
  [autoupdater.yourscript]
  url = "../path/to/the/script/yourscript.py"

  [autoupdater.mycoolscript]
  url = "http://myhttpserver/mycoolscript.py"
```

(and yes, you can auto update the script, using the script)

</details>

<details><summary>customMessages</summary>
Made by sByte

A script for helping with custom messaging (screen messages)
for BetterSpades and OpenSpades.

How to use?
- Put this script on the top of the script list in config.toml,
then the functions "connection.send_cmsg(Message, Type)" and "protocol.broadcast_cmsg(Message, Type)"

Message types:
- Notice
- Status
- Warning
- Error

Test commands:
- /csay Type Message
- /cpm Player Type Message

</details>

<details><summary>utils</summary>
Made by sByte

A script where i will add useful functions i use when
coding scripts, like create_block, destroy_block, etc

How to use?
- Put this script on the top of the script list in config.toml,
to be able to use the functions.
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━> FUNCTIONS <━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┣━> create_block(coords: tuple, save: bool=False, color: tuple=None)┃
┣> Available on protocol and connection classes.                    ┃
┃                                                                   ┃
┣> Create a block, on the map. If Save is True, block               ┃
┃  will be saved in the map for future connections.                 ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┣━> destroy_block(coords: tuple, save: bool=False)                  ┃
┣> Available on protocol and connection classes.                    ┃
┃                                                                   ┃
┣> Destroy a block. If Save is True, destroyed block                ┃
┃  will be saved in the map for future connections.                 ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┣━> gravity(body: dict)                                             ┃
┣> Available only in protocol                                       ┃
┃                                                                   ┃
┣> Calculate how the gravity will work passing the                  ┃
┃  mass and velocity.                                               ┃
┃                                                                   ┃
┣━> Body structure                                                  ┃
┣> position: z_coordinate (Float)                                   ┃
┣> mass: Int                                                        ┃
┣> velocity: Int                                                    ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┣━> gradient_fog(tuple: fog, float: speed)							┃
┣> Available only in protocol										┃
┃																	┃
┣> Change fog color in a gradient effect.							┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━> FUNCTIONS <━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

</details>