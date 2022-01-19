## Setup 
in permstore.json (permshandler > permstore.json) to be setup as shown below:
```json
{}
```
add a perm group
```json
{
    "group1": {
        "level": 0,
        "users": [],
        "roles": []
    }
}
```
add userids or roleids to whitelist
```json
{
    "group1": {
        "level": 0,
        "users": [
            182838238188231,
            399459499393939
        ],
        "roles": [
            772727573737732,
            838384858181818
        ]
    }
}
```
Add more perm groups
```json
{
    "Higher": {
        "level": 1,
        "users": [
            182838238188231,
            399459499393939
        ],
        "roles": [
            772727573737732,
            838384858181818
        ]
    },
    "group1": {
        "level": 0,
        "users": [
            182838238188231,
            399459424393939
        ],
        "roles": [
            772727573737732,
            838384858181818
        ]
    },
    "group3": {
        "level": 0,
        "users": [
            182838238188231,
            399459499393939
        ],
        "roles": [
            772727573737732,
            838384858181818
        ]
    }
}
```
In the above setup ^ anybody whitelisted in `Higher` will be able to clear commands protected with `group1` or `group2` because of being at a higher level. Naturally, the converse is not true. It is worth noting that somebody with `group1` CANNOT clear a commnd protected with `group2` as being of the same level.

you can protect commands like so:
```python
perms = PermsHandler()

@bot.command()
@perms.check("Admin")
async def adminstuff(ctx):
    await ctx.send("Just admin stuff")
```