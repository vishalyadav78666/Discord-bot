import discord
from discord.ext import commands
import random
import asyncio
from datetime import datetime

# ══════════════════════════════════════════
#   CONFIG — Apna token yahan daalo
# ══════════════════════════════════════════
import os
TOKEN = os.environ.get("DISCORD_TOKEN")
PREFIX = "."
BOT_NAME = "Priya"   # Bot ka naam badal sakte ho
# ══════════════════════════════════════════

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

# ─────────────────────────────────────────
#  RESPONSE BANKS
# ─────────────────────────────────────────

GREETINGS = [
    "Aye aye! Aa gaya mera favorite bsdk 😏💕",
    "Oye! Kahan tha itni der? Miss kar raha tha kya mujhe? 🥺",
    "Dekho kaun aaya! Mera pyaara pagal 😂❤️",
    "Haaye! Tu aaya toh dil khush ho gaya yaar 💕",
    "Aye harami! Bahut din baad dikha tu 😤",
    "Ohh hello hello! Kya scene hai aaj? 😎",
]

FLIRTS = [
    "Tere jaisa koi nahi yaar, seedha dil mein ghus jaata hai tu 💕😏",
    "Ek baat bataaun? Tu bahut cute lagta hai jab pagalpan karta hai 🥺",
    "Mujhe toh bas teri awaaz sunni hoti hai, baki sab bakwaas hai 😍",
    "Teri ek smile dekh ke din ban jaata hai mera, sach bol rahi hoon 💗",
    "Oye main pagal hoon tere liye, ye toh pata hi hoga tujhe 😂❤️",
    "Tu bura kyun nahi hai? Itna acha kyun hai sala 🥺💕",
    "Teri yaad mein itni baar sochi hoon ki count hi nahi 😏",
    "Ek kaam kar mujhse shaadi kar le, ghar bhi saaf rakhungi 😂❤️",
]

JOKES = [
    "Ek baar ek aadmi apni girlfriend se bola: 'Tujhe stars tod ke deta'.\nGirlfriend boli: 'Pehle kapde dhona seekh, phir astronaut ban' 😂",
    "Teacher: Ek sentence banao jisme 'but' use ho.\nStudent: Teacher bahut achi hain BUT asli life mein aisa nahi hota 💀😂",
    "Mere papa kehte hain: 'Subah jaldi uth'..\nMain kehta hoon: 'Subah hogi tab uthunga' 😂",
    "Diet pe hoon yaar... isliye sirf ek pizza khaaya aaj 💀",
    "Duniya mein do tarah ke log hote hain —\n1. Jo neend se uthte hi phone dekhte hain\n2. Jhoothe 😂",
    "Meri life ek joke hai...\nbas mujhe abhi tak samajh nahi aya punchline 💀😭",
    "Bhai ek acha joke bataaun?\n... Meri success plan 😂",
    "Exam mein likhaa: 'Ye sawaal philosophy hai, answer mujhse bada hai' 💀",
]

ROASTS = [
    "Teri shakal dekh ke aaiyo bhi ro padi thi yaar 😂",
    "Tu itna lazy hai ki tera shadow bhi akele ghumta hai 💀",
    "Tujhe dekh ke lagta hai ki bhagwan bhi kabhi kabhi overtime karta hai 😂",
    "Teri problem kya hai? Brain hai hi nahi toh problem bhi nahi hogi 😂💕",
    "Tu woh kehte hain na — 'original piece', matlab copy nahi mila tera 💀",
    "Oye, tujhe dekh ke WhatsApp ne bhi 'Last seen bahut pehle' likh diya 😂",
    "Tera confidence dekh ke lagta hai — padha likha nahi par atma vishwas poora hai 😂",
]

COMFORT = [
    "Aye sun! Sab theek ho jaayega, tu strong hai yaar 💪❤️",
    "Mat ro bhai, main hoon na! Sath hoon tera hamesha 🥺💕",
    "Mushkilein aati hain jaane ke liye, tu ruk 💗",
    "Oye don't overthink kar, tu bahut better hai than you think 🌟",
    "Chal bata kya hua? Sab share kar mere saath, judge nahi karungi 🥺",
]

HYPE = [
    "TU TOH SABSE BEST HAI BHAI! 🔥🔥🔥",
    "Aye aye aye!! Dekho is legend ko! 👑🔥",
    "Teri toh life set hai bhai, tu kuch bhi kar sakta hai 💪",
    "BEAST MODE ON! Kar de tu kuch bhi 🔥",
    "Legend hai tu, puri duniya jaanegi ek din 👑",
]

MOOD_REPLIES = {
    "sad": COMFORT,
    "dukhi": COMFORT,
    "upset": COMFORT,
    "rona": COMFORT,
    "happy": HYPE,
    "khush": HYPE,
    "excited": HYPE,
}

# ─────────────────────────────────────────
#  EVENTS
# ─────────────────────────────────────────

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=f"tumhari bakwaas 💕 | {PREFIX}help"
        )
    )
    print(f"✅ {BOT_NAME} online hai!")

@bot.event
async def on_member_join(member):
    ch = discord.utils.get(member.guild.text_channels, name="general") \
      or member.guild.text_channels[0]
    msgs = [
        f"Aye aye! {member.mention} aa gaya/gayi! Swagat hai tere jaisa bsdk yahan 😂❤️",
        f"OHH {member.mention} ne entry maari! Server mein mazaa double ho gaya 🔥💕",
        f"DEKHO DEKHO! {member.mention} aaya/aayi! Welcome to the desi chaos fam 🎉",
    ]
    await ch.send(random.choice(msgs))

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    # Bot mention pe respond karo
    if bot.user.mentioned_in(message) and not message.mention_everyone:
        await message.channel.send(random.choice(GREETINGS))
        await bot.process_commands(message)
        return

    # Mood detection (bina command ke)
    if not message.content.startswith(PREFIX):
        for keyword, responses in MOOD_REPLIES.items():
            if keyword in content:
                await asyncio.sleep(1)
                await message.channel.send(random.choice(responses))
                return

    await bot.process_commands(message)

# ─────────────────────────────────────────
#  COMMANDS
# ─────────────────────────────────────────

@bot.command(name="flirt")
async def flirt(ctx, member: discord.Member = None):
    """Kisi ko flirt karo 💕"""
    target = member.mention if member else ctx.author.mention
    msg = random.choice(FLIRTS)
    await ctx.send(f"{target} {msg}")

@bot.command(name="joke")
async def joke(ctx):
    """Random funny joke suno 😂"""
    await ctx.send(random.choice(JOKES))

@bot.command(name="roast")
async def roast(ctx, member: discord.Member = None):
    """Kisi ko roast karo 🔥"""
    target = member.mention if member else ctx.author.mention
    await ctx.send(f"{target} {random.choice(ROASTS)}")

@bot.command(name="hype")
async def hype(ctx, member: discord.Member = None):
    """Kisi ko hype karo 👑"""
    target = member.mention if member else ctx.author.mention
    await ctx.send(f"{target} {random.choice(HYPE)}")

@bot.command(name="ship")
async def ship(ctx, user1: discord.Member, user2: discord.Member = None):
    """Do logon ko ship karo 💕"""
    user2 = user2 or ctx.author
    score = random.randint(0, 100)
    if score >= 80:
        verdict = "YE TOH SACH MEIN BANE HAIN EK DOOSRE KE LIYE 😍🔥"
        bar = "💗" * 10
    elif score >= 60:
        verdict = "Accha match hai, thoda effort lagao 😏💕"
        bar = "💗" * 7 + "🤍" * 3
    elif score >= 40:
        verdict = "Hmmm... 50-50 scene hai, dekho aage kya hota hai 😅"
        bar = "💗" * 5 + "🤍" * 5
    else:
        verdict = "Bhai ye toh alag planets ke hain 💀😂"
        bar = "💗" * 2 + "🤍" * 8

    e = discord.Embed(
        title="💕 Ship Meter",
        description=f"**{user1.display_name}** + **{user2.display_name}**",
        color=0xff6b9d
    )
    e.add_field(name="Score", value=f"**{score}%**", inline=True)
    e.add_field(name="Meter", value=bar, inline=True)
    e.add_field(name="Verdict", value=verdict, inline=False)
    await ctx.send(embed=e)

@bot.command(name="truth")
async def truth(ctx):
    """Random truth question 👀"""
    truths = [
        "Sachchi bol — last time kab roya/royi? 🥺",
        "Apni life ka sabse bada secret bata 👀",
        "Crush ka naam bata! 😏",
        "Last lie kab boli thi aur kisko? 💀",
        "Kya koi cheez hai jo tujhe bahut darr lagti hai? 🥺",
        "Pehli baar pyaar kab hua tha? 😍",
        "Apni sabse badi galti bata jo abhi tak neend nahi aane deti 😅",
        "Agar ek din kuch bhi karne de toh kya karega/karegi? 😏",
    ]
    await ctx.send(f"🎯 **Truth:** {random.choice(truths)}")

@bot.command(name="dare")
async def dare(ctx):
    """Random dare do 🔥"""
    dares = [
        "Is server mein jo bhi online hai usse 'I love you' bol 😂",
        "Apni sabse embarrassing photo upload kar yahan 💀",
        "Next 5 minutes tak sirf caps mein type kar 😂",
        "Server ke owner ko bolo ki woh best hai 😂",
        "Apna sab se bura joke yahan post kar 💀",
        "10 push-ups kar aur video bhej 💪",
        "Apni last search history ka ek item yahan paste kar 👀😂",
        "Is chat mein kisi ek ko genuine compliment de 💕",
    ]
    await ctx.send(f"🎲 **Dare:** {random.choice(dares)}")

@bot.command(name="rps")
async def rps(ctx, choice: str):
    """Rock Paper Scissors khelo! .rps rock/paper/scissors"""
    options = ["rock", "paper", "scissors"]
    choice = choice.lower()
    if choice not in options:
        await ctx.send("Bhai sahi se khel! `.rps rock` ya `.rps paper` ya `.rps scissors` 😤")
        return
    bot_choice = random.choice(options)
    icons = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

    if choice == bot_choice:
        result = "Draw hai bhai, dobara khel 😏"
    elif (choice == "rock" and bot_choice == "scissors") or \
         (choice == "paper" and bot_choice == "rock") or \
         (choice == "scissors" and bot_choice == "paper"):
        result = "Tu jeet gaya!! Seedha lucky hai tu 🔥 (Par main lucky feel nahi karna deti normally 😏)"
    else:
        result = "HAHA HAARA TU! Main jeet gayi, told you na 😂👑"

    await ctx.send(
        f"Tu: **{icons[choice]} {choice}**\n"
        f"Main: **{icons[bot_choice]} {bot_choice}**\n\n"
        f"{result}"
    )

@bot.command(name="8ball")
async def eightball(ctx, *, question: str):
    """Magic 8 ball se sawal poochho 🎱"""
    answers = [
        "Haan bilkul! 100% 🔥", "Nahi bhai nahi 😂", "Shayad? Pata nahi mujhe 🤷",
        "Definitely haan 💕", "Pakka nahi, try kar dekh 😅",
        "Mujhe kya pata yaar, main toh bot hoon 😂",
        "Hmm... stars bol rahe hain haan 🌟", "Bhai ye toh time batayega 🙏",
        "HAAN HAAN HAAN! 🎉", "Nahi matlab nahi, chhod de ye sochna 😤",
    ]
    e = discord.Embed(color=0xff6b9d)
    e.add_field(name="Sawal", value=f"*{question}*", inline=False)
    e.add_field(name="🎱 Jawab", value=random.choice(answers), inline=False)
    await ctx.send(embed=e)

@bot.command(name="compliment")
async def compliment(ctx, member: discord.Member = None):
    """Kisi ko genuine compliment do 💗"""
    target = member.mention if member else ctx.author.mention
    compliments = [
        f"{target} tu bahut zyada underrated hai yaar, sach mein 💕",
        f"{target} teri smile dekh ke pura room roshan ho jaata hai 😍",
        f"{target} bhai/behen tu is server ka best part hai, no cap 🔥",
        f"{target} tujhse baat karke hamesha better feel hota hai 🥺💗",
        f"{target} tu jo bhi karta/karti hai, dil se karta/karti hai — ye rare hai 💪",
    ]
    await ctx.send(random.choice(compliments))

@bot.command(name="help")
async def help_cmd(ctx):
    """Sab commands dekho"""
    e = discord.Embed(
        title=f"💕 {BOT_NAME} — Commands",
        description="Bol kya chahiye, main hoon na! 😏",
        color=0xff6b9d
    )
    cmds = [
        (f"{PREFIX}flirt [@user]", "Flirt karo 💕"),
        (f"{PREFIX}roast [@user]", "Roast karo 🔥"),
        (f"{PREFIX}hype [@user]", "Hype karo 👑"),
        (f"{PREFIX}joke", "Funny joke suno 😂"),
        (f"{PREFIX}ship @user1 [@user2]", "Ship meter check karo 💗"),
        (f"{PREFIX}truth", "Random truth question 👀"),
        (f"{PREFIX}dare", "Random dare 🎲"),
        (f"{PREFIX}rps [rock/paper/scissors]", "Game khelo ✂️"),
        (f"{PREFIX}8ball [sawaal]", "Magic 8 ball 🎱"),
        (f"{PREFIX}compliment [@user]", "Compliment do 🥺"),
    ]
    for name, desc in cmds:
        e.add_field(name=name, value=desc, inline=True)
    e.set_footer(text=f"Aur seedha mention karo {BOT_NAME} ko baat karne ke liye! 💕")
    await ctx.send(embed=e)

# ─────────────────────────────────────────
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("Bhai ye member nahi mila server mein 😅")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Sahi se use kar! `{PREFIX}help` dekh 😤")

bot.run(TOKEN)
