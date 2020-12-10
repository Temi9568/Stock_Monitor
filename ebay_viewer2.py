import requests
import randomheaders
import time
import random
from discord.ext import commands

"""Previous issue was that no discord integration. Now integrate but  need
to do one 'Create another command called views which can take multiple urls and will run using
#threading. Or could alter the above and save url to a file and then run that file
# if the amount of urls are greater than x or etc.' """


def viewer(url, views: int):
    if views > 200:
        return
    else:
        proxy = proxies = {
            "http": "http://20982c0c036b4a639067f3dc6634056b:@proxy.crawlera.com:8010/",
        }

        for i in range(views):
            time.sleep(random.randint(1, 3))
            requests.get(url, proxies=proxy, headers=randomheaders.LoadHeader())
            print("{} view has been completed".format(i + 1))


client = commands.Bot(command_prefix='.')


@client.command()
async def view(ctx, url, amount):
    amount = int(amount)
    if amount > 200:
        await ctx.send("Please send another request, can't do views over 200")
        await ctx.channel.purge(limit=2)
    # elif not url.startswith("http://") or not url.startswith("https://"):
    #     await ctx.send("Please send another request, url MUST start with 'https' or 'http'")
    else:
        await ctx.send("Request is successful")
        viewer(url, amount)



client.run("NzgyMjI0NTkxNjkwMjY4Njc0.X8JFaw.DWq3cWTljf--iskTelATvTLz2F4")




# urls = []
# counter = int(input("How many url's do you want to add: "))
#
# for i in range(counter):
#     urls.append(input("Enter your {} url: ".format(i + 1)))
#
# threads = [threading.Thread(target=viewer, args=(url, 10,)) for url in urls]
# for t in threads:
#     t.start()
