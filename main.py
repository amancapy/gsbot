import discord
from discord.ext import tasks
import os
import random
import datetime
# from mcstatus import MinecraftServer
from keepalive import keep_alive
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import Firefox

client = discord.Client()

@client.event
async def on_ready():
  print(f"We have logged in as {client.user}.")

@tasks.loop(minutes=1)
async def bday_reminder():
    if datetime.datetime.now().hour == 18:
        channel = client.get_channel(channel id)
        bdays = open("bdays.txt", "r")
        content = bdays.read().split("\n")
        bdays.close()
        for pair in content:
            if pair:
                name = pair.split("÷")[0]
                date = pair.split("÷")[1]
                day = int(date.split("-")[2])
                mon = int(date.split("-")[1])
                year = int(date.split("-")[0])
                
                if datetime.datetime.now().minute == 25:
                    if (datetime.datetime(datetime.datetime.now().year, mon, day) - datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)).days == 1:
                        await channel.send(f"@here, {name} turns {datetime.datetime.now().year -year} in {30 - datetime.datetime.now().minute} minute(s)!")
                
                if datetime.datetime.now().minute == 30:
                    if (datetime.datetime(datetime.datetime.now().year, mon, day) - datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)).days == 1:
                        await channel.send(f"@everyone, it's {name}\'s birthday today, they're {datetime.datetime.now().year - year}!")


@bday_reminder.before_loop
async def before():
    await client.wait_until_ready()
bday_reminder.start()

@client.event
async def on_message(msg):
    
    if msg.author == client.user:
        return
  
    elif msg.content.lower().startswith("gsbot") and msg.guild.id != bot self id:
            message = msg.content.lower().split()
            command = message[1]

            if command == "help":
                description = "• gsbot pic [name] | • gsbot pic random\n• gsbot quote [name] <keyword> | • gsbot quote random\n• gsbot bday [name]\n\n• gsbot list pics\n• gsbot list quotes\n• gsbot list bdays\n\n• gsbot add_pic [name] (attach pic)\n• gsbot add_quote [name] [quote] **(no new lines in the quote)**\n• gsbot add_bday [name] dd mm yyyy\n\n• gsbot toread [name] [bookname]\n• gsbot doneread [name] [bookname]\n• gsbot books [name]"
                embed = discord.Embed(title="Commands Available:", description=description, color=discord.Colour.green())
                await msg.channel.send(embed=embed)

            elif command == "test":
                await msg.channel.send(f"Arthur penis dragon. The present is {datetime.datetime.today()}.")

            elif command == "list":
                ctype = message[2]
                if ctype == "pics":
                    fpics = open("pics.txt", "r")
                    content = fpics.read().split("\n")
                    fpics.close()
                    available_pics = ""
                    for pair in content:
                        if pair:
                            name = pair.split()[0]
                            if name not in available_pics:
                                available_pics += (name + "\n")
                    embed = discord.Embed(title="Pics Available:", description=available_pics, color=discord.Colour.green())
                    await msg.channel.send(embed=embed)
                
                elif ctype == "quotes":
                    fquotes = open("quotes.txt", "r")
                    content = fquotes.read().split("\n")
                    fquotes.close()
                    available_quotes = ""
                    for pair in content:
                        if pair:
                            name = pair.split("÷")[0]
                            if name not in available_quotes:
                                available_quotes += (name + "\n")
                    embed = discord.Embed(title="Quotes Available", description=available_quotes, color=discord.Colour.green())
                    await msg.channel.send(embed=embed)
                
                elif ctype == "bdays":
                    fbdays = open("bdays.txt", "r")
                    content = fbdays.read().split("\n")
                    fbdays.close()
                    all_bdays = ""
                    bday_list = []
                    for pair in content:
                        if pair:
                            bday_split = []

                            name = pair.split("÷")[0]
                            bday = pair.split("÷")[1]
                            year = int(bday.split("-")[0])
                            mon = int(bday.split("-")[1])
                            day = int(bday.split("-")[2])

                            bday_split.extend([name, year, mon, day])
                            
                            if (datetime.datetime(datetime.datetime.now().year+1, mon, day) - datetime.datetime.now()).days <= 365:
                                bday_split.append(((datetime.datetime(datetime.datetime.now().year+1, mon, day) - datetime.datetime.now()).days) % 365)
                            else:
                                bday_split.append(((datetime.datetime(datetime.datetime.now().year, mon, day) - datetime.datetime.now()).days) % 365)

                            bday_list.append(bday_split)
                    
                    bday_list.sort(key = lambda x: len(x[0]))
                    long_name_len = len(bday_list[-1][0])

                    bday_list.sort(key = lambda x: x[-1])

                    all_bdays = "```"
                    space = " "
                    print(bday_list)
                    for bday in bday_list:
                        bday_ = ""
                        bday_ += (f"{bday[0]}: {space * (long_name_len - len(bday[0]))} {bday[3]}-{bday[2]}-{bday[1]}")

                        
                        all_bdays += bday_ + (27 - len(bday_)) * space + str(f"({bday[4]})") + "\n"

                    

                    all_bdays += "```"

                    embed = discord.Embed(title="All Birthdays:", description=f"```name: {space * (long_name_len - 3)}dd-mm-yyyy (days remaining)\n\n```" + all_bdays, color=discord.Colour.red())
                    await msg.channel.send(embed=embed)

            elif command == "add_pic":
                name = message[2]
                if len(message) == 3 and len(msg.attachments):
                    fpics = open("pics.txt", "a")
                    for url in msg.attachments:
                        fpics.write(f"{name} {url}\n")        
                        embed = discord.Embed(title="Pic Added:", color=discord.Colour.green())
                        embed.set_image(url=url)
                        await msg.channel.send(embed=embed)
                    fpics.close()
                else:
                    embed = discord.Embed(description="Adding links is **no longer supported**. Please attach an image.\n\nCorrect command format: ```gsbot add_pic [name] (attach image)```", color=discord.Colour.red())
                    await msg.channel.send(embed=embed)

            elif command == "add_quote":
                for chunk in message:
                    if "\n" in chunk:
                        embed = discord.Embed(description="You can not have a new-line in your quote.", color=discord.Colour.red())
                        await msg.channel.send(embed=embed)
                        break
                else:
                    name = message[2]
                    quote = ""
                    for i in range(3, len(message)):
                        quote += message[i] + " "
                    fquotes = open("quotes.txt", "a")
                    fquotes.write(f"{name}÷{quote}\n")
                    fquotes.close()
                    embed = discord.Embed(description=f"{name} says {quote}", title="Quote Added:", color=discord.Colour.green())
                    await msg.channel.send(embed=embed)

            elif command == "add_bday":
                if len(message) == 6 and message[3].isdigit() and message[4].isdigit() and message[5].isdigit():
                    for chunk in message:
                        if "\n" in chunk:
                            embed = discord.Embed(description="You can not have a new-line in your quote.", color=discord.Colour.red())
                            await msg.channel.send(embed=embed)
                            break
                    else:
                        name = message[2]
                        day = int(message[3])
                        month = int(message[4])
                        year = int(message[5])
                        fbdays = open("bdays.txt", "a")
                        fbdays.write(f"{name}÷{year}-{month}-{day}\n")
                        fbdays.close()
                        embed = discord.Embed(description=f"{name}\'s birthday is {day}-{month}-{year}", title="Birthday Added:", color=discord.Colour.green())
                        await msg.channel.send(embed=embed)
                else:
                    embed = discord.Embed(description="Correct format: gsbot add_bday [name] dd mm yyyy", color=discord.Colour.red())
                    await msg.channel.send(embed=embed)


            elif command == "classes":
                if len(message) >= 3:
                    if len(message[2]) < 2:
                        await msg.channel.send("That's not a valid day mf.")

                    else:
                        day = message[2][0].upper() + message[2].lower()[1]

                else:
                    day = (datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)).strftime("%A")[:2]
                
                recd = False
                if msg.author.id == id:
                    tt = open("tts/tt_name.txt", "r")
                    name = "name"
                    recd = True
                elif msg.author.id == id:
                    tt = open("tts/tt_name.txt", "r")
                    name = "name"
                    recd = True
                elif msg.author.id == id:
                    name = "name"
                    tt = open("tts/tt_name.txt", "r")
                    recd = True
                elif msg.author.id == id:
                    tt = open("tts/tt_name.txt", "r")
                    name = "name"
                    recd = True
                
                if recd:
                    content = tt.read().split("\n")
                    tt.close()

                    description = ""
                    for class_ in content:
                        if class_:
                            if day in class_:
                                description += class_ + "\n"

                    embed = discord.Embed(title=f"{name}'s classes on {day}", description=description, color=discord.Colour.blue())

                else:
                    embed = discord.Embed(description="Who are you mf", color=discord.Colour.red())

                await msg.channel.send(embed=embed)


            elif  len(message) >= 3:
                name = message[2]
                if command == "quote":
                    if len(message) == 4:
                        matches = []
                        keyword = message[3]
                        fquotes = open("quotes.txt", "r")
                        content = fquotes.read().split("\n")
                        fquotes.close()
                        for pair in content:
                            if pair:
                                n = pair.split("÷")[0]
                                quote = pair.split("÷")[1]
                                if keyword.lower() in quote.lower() and n == name:
                                    matches.append(pair)
                        if matches:
                            pair = random.choice(matches)
                            name = pair.split("÷")[0]
                            quote = pair.split("÷")[1]
                            await msg.channel.send(f"{name} says {quote}")
                        else:
                            await msg.channel.send("what mf")
                                                    
                    elif len(message) == 3:
                        if name == "random":
                            fquotes = open("quotes.txt", "r")
                            content = fquotes.read().split("\n")
                            fquotes.close()
                            content.remove("")
                            pick = random.choice(content)
                            name = pick.split("÷")[0]
                            quote = pick.split("÷")[1]
                            await msg.channel.send(f"{name} says {quote}")

                        else:
                            fquotes = open("quotes.txt", "r")
                            content = fquotes.read().split("\n")
                            fquotes.close()
                            quotelist = []
                            for pair in content:
                                if pair:
                                    n = pair.split("÷")[0]
                                    if n == name:   
                                        quote = pair.split("÷")[1]
                                        quotelist.append(quote)
                            if quotelist:
                                await msg.channel.send(f"{name} says {random.choice(quotelist)}")
                            else:
                                await msg.channel.send("who tf is that")
                        
                elif command == "pic":
                    name = message[2]
                    if name != "random":
                        fpics = open("pics.txt", "r")
                        content = fpics.read().split("\n")
                        fpics.close()
                        linklist = []
                        for pair in content:
                            if pair:
                                n = pair.split()[0]
                                if n == name:
                                    link = pair.split()[1]
                                    linklist.append(link)
                        if linklist:
                            url = random.choice(linklist)
                            embed = discord.Embed(color=discord.Colour.blue())
                            embed.set_image(url=url)
                            await msg.channel.send(embed=embed)
                        else:
                            await msg.channel.send("who mf")
                    else:
                        fpics = open("pics.txt", "r")
                        content = fpics.read().split("\n")
                        fpics.close()
                        pick = ""
                        while not pick:
                            pick = random.choice(content)
                        name = pick.split()[0]
                        url = pick.split()[1]
                        embed = discord.Embed(title=name, color=discord.Colour.blue())
                        embed.set_image(url=url)
                        await msg.channel.send(embed=embed)

                elif command == "bday":
                    if len(message) >=3:
                        name = message[2]
                        fbdays = open("bdays.txt", "r")
                        content = fbdays.read().split("\n")
                        fbdays.close()
                        for pair in content:
                            if pair:
                                n = pair.split("÷")[0]
                                bday = pair.split("÷")[1]
                                day = int(bday.split("-")[2])
                                mon = int(bday.split("-")[1])
                                year = int(bday.split("-")[0])
                                if n == name:
                                    if (datetime.datetime(datetime.datetime.now().year+1, mon, day) - datetime.datetime.now()).days <= 365:
                                        await msg.channel.send(f"{name}\'s birthday is on {day}-{mon}, which is **{(datetime.datetime(datetime.datetime.now().year+1, mon, day) - datetime.datetime.now()).days % 365}** days away.")
                                        break
                                    else:
                                        await msg.channel.send(f"{name}\'s birthday is on {day}-{mon}, which is **{(datetime.datetime(datetime.datetime.now().year, mon, day) - datetime.datetime.now()).days}** days away.")
                                        break
                        else:
                            await msg.channel.send("who mf")

                elif command == "toread":
                    name = message[2]
                    bname = ""
                    for word in message[3:]:
                        bname += str(word) + " "
                    blist = list(open(f"books/{name}.txt", "r").read().split(", "))
                    blist += [bname]
                    bstr = ""
                    for bnames in blist:
                        if bnames != "":
                            bstr += bnames + ", "
                    print(bstr)
                    file = open(f"books/{name}.txt", "w")
                    file.write(bstr)
                    file.close()
                    await msg.channel.send(f"{bname} added to reading list.")

                elif command == "doneread":
                    name = message[2]
                    bname = ""
                    for word in message[3:]:
                        bname += str(word) + " "
                    text = open(f"books/{name}.txt").read().split(", ")
                    if bname in text or bname[:-1] in text:
                        if bname[:-1] in text:
                            torem = bname[:-1]
                        elif bname in text:
                            torem = bname

                        text.remove(torem)
                        file = open(f"books/{name}.txt", "w")
                        for bookname in text:
                            if bookname != "":
                                file.write(bookname + ", ")
                        file.close()
                        await msg.channel.send(f"{bname}removed from reading list.")
                    else:
                        await msg.channel.send(f"{bname}wasn't in your reading list.")

                elif command == "books":
                    name = message[2]
                    file = open(f"books/{name}.txt").read()
                    text = ""
                    for line in file.split(", "):
                        text += line + "\n"
                    if len(file.split(", ")) == 0:
                        await msg.channel.send("Your reading list is empty.")
                    else:
                        await msg.channel.send("You have yet to read\n" + text)
                    
                else:
                    embed = discord.Embed(description="Command not recognised.\nUse `gsbot help` to see a list of available commands.", color=discord.Colour.red())
                    await msg.channel.send(embed=embed)
            
            else:
                embed = discord.Embed(description="Command not recognised.\nUse `gsbot help` to see a list of available commands.", color=discord.Colour.red())
                await msg.channel.send(embed=embed)
    
token = os.environ['token']

keep_alive()
client.run(token)
