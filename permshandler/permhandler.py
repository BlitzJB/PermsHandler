from .models import Permissions
import inspect


class PermsHandler:
    def __init__(
        self, path_to_perm_store: str = "./permshandler/permstore.json"
    ) -> None:
        """
        :param path_to_perm_store: Path to the file that stores the permissions from the root dir
        """
        self.permissions = Permissions(path_to_perm_store)

    def check(self, group: str):
        """
        :param group: The name of the minimum group required to use this command
        """

        def decorator(func):
            async def wrapper(ctx, *args, **kwargs):

                if not self.permissions.is_user_authorized(ctx.author, group):
                    await self.handle_forbidden(ctx, group)
                    return

                await func(ctx, *args, **kwargs)

            wrapper.__name__ = func.__name__
            wrapper.__signature__ = inspect.signature(func)
            return wrapper

        return decorator

    async def handle_forbidden(self, ctx, required):
        await ctx.channel.send(
            f"You need `{required}` group permissions to use this command"
        )
