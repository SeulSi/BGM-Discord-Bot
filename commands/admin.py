import discord
import asyncio
import aiomysql
import PW
import time
import TOKEN

from send import Command

prefix = TOKEN.prefix

"""
서버 어드민들이 사용 가능한 봇의 명령어를 수록합니다.
(단, 100줄 이상의 명령어는 따로 분리처리)
"""


""" Function """

""" Main """ 
class admin(Command):
    
    def __init__(self, *args, **kwargs):
        Command.__init__(self, *args, **kwargs)
          


    async def on_message(self, message):


        if message.content.startswith(prefix+"뮤트"):
            if message.author.guild_permissions.administrator == True:
                try:
                    if not message.mentions == []:
                        member = message.mentions[0]

                        overwrite = discord.PermissionOverwrite()
                        overwrite.send_messages = False
                        await message.channel.set_permissions(member, overwrite=overwrite)
                        embed=discord.Embed(title="✅ 유저 뮤트", description="뮤트를 성공했습니다.",color=0x1dc73a)
                        await message.channel.send(embed=embed)
                    else:
                        embed=discord.Embed(title="⚠ 주의", description="`"+prefix+"뮤트 @유저` 형식으로 명령어를 사용해주세요. 선택된 사용자가 없습니다.",color=0xd8ef56)
                        await message.channel.send(embed=embed)
                        
                except:
                    embed=discord.Embed(title="❌ 오류 발생", description="뮤트를 실패하였습니다. 권한을 확인해 주세요. "  ,color=0xff0909)    
                    await message.channel.send(embed=embed)

            else:
                embed=discord.Embed(title="⚠ 주의", description="관리자 권한이 있어야 사용 가능한 명령어입니다.",color=0xd8ef56)
                await message.channel.send(embed=embed)


        if message.content.startswith(prefix+"언뮤트"):
            if message.author.guild_permissions.administrator == True:
                try:
                    if not message.mentions == []:
                        member = message.mentions[0]
                        overwrite = discord.PermissionOverwrite()
                        overwrite.send_messages = True
                        await message.channel.set_permissions(member, overwrite=overwrite)
                        embed=discord.Embed(title="✅ 유저 언뮤트", description="언뮤트를 성공했습니다.",color=0x1dc73a )
                        await message.channel.send(embed=embed)
                    else:
                        embed=discord.Embed(title="⚠ 주의", description="`"+prefix+"언뮤트 @유저` 형식으로 명령어를 사용해주세요. 선택된 사용자가 없습니다.",color=0xd8ef56)
                        await message.channel.send(embed=embed)
                        
                except:
                    embed=discord.Embed(title="❌ 오류 발생", description="뮤트를 실패하였습니다. 권한을 확인해 주세요." ,color=0xff0909)    
                    await message.channel.send(embed=embed)
            else:
                embed=discord.Embed(title="⚠ 주의", description="관리자 권한이 있어야 사용 가능한 명령어입니다.",color=0xd8ef56)
                await message.channel.send(embed=embed)


        if message.content.startswith(prefix+"전체뮤트"):
            if message.author.guild_permissions.administrator == True:
                try:
                    role = discord.utils.get(message.guild.roles, name="@everyone")
                    await message.channel.set_permissions(role, send_messages=False)
                    embed=discord.Embed(title="✅ 전체 뮤트", description="관리자를 제외한 모든 유저의 뮤트를 성공했습니다.",color=0x1dc73a )
                    await message.channel.send(embed=embed)
                except:
                    embed=discord.Embed(title="❌ 오류 발생", description="뮤트를 실패하였습니다. 권한을 확인해 주세요." ,color=0xff0909)    
                    await message.channel.send(embed=embed)

            else:
                embed=discord.Embed(title="⚠ 주의", description="관리자 권한이 있어야 사용 가능한 명령어입니다.",color=0xd8ef56)
                await message.channel.send(embed=embed)


        if message.content.startswith(prefix+"전체언뮤트"):
            if message.author.guild_permissions.administrator == True:
                try:
                    role = discord.utils.get(message.guild.roles, name="@everyone")
                    await message.channel.set_permissions(role, send_messages=True)
                    embed=discord.Embed(title="✅ 전체 언뮤트", description="모든 유저의 언뮤트를 성공했습니다.",color=0x1dc73a )
                    await message.channel.send(embed=embed)

                except: 
                    embed=discord.Embed(title="❌ 오류 발생", description="뮤트를 실패하였습니다. 권한을 확인해 주세요." ,color=0xff0909)    
                    await message.channel.send(embed=embed)

            else:
                embed=discord.Embed(title="⚠ 주의", description="관리자 권한이 있어야 사용 가능한 명령어입니다.",color=0xd8ef56)
                await message.channel.send(embed=embed)

        if message.content.startswith(prefix+"밴") :
            if message.author.guild_permissions.administrator == True:
                try:
                    if not message.mentions == []:
                        member = message.mentions[0]
                        await message.guild.ban(member,reason=str(message.author) + "님의 명령어 사용으로 인해 밴 당하셨습니다.", delete_message_days=7)
                        embed=discord.Embed(title="✅ 유저 밴", description="유저의 밴을 완료했습니다.",color=0x1dc73a )
                        await message.channel.send(embed=embed)
                    else:
                        embed=discord.Embed(title="⚠ 주의", description="`"+prefix+"밴 @유저` 형식으로 명령어를 사용해주세요. 선택된 사용자가 없습니다.",color=0xd8ef56)
                        await message.channel.send(embed=embed)

                except:
                    embed=discord.Embed(title="❌ 오류 발생", description="밴을 실패하였습니다. 권한을 확인해보세요." ,color=0xff0909)    
                    await message.channel.send(embed=embed)
            else:
                embed=discord.Embed(title="⚠ 주의", description="관리자 권한이 있어야 사용 가능한 명령어입니다.",color=0xd8ef56)
                await message.channel.send(embed=embed)



        if message.content.startswith(prefix+"언밴"):
            if message.author.guild_permissions.administrator == True:
                try:    
                    memberid = message.content.replace(prefix+"언밴 ", "")
                    memberid = memberid.replace("<", "")
                    memberid = memberid.replace("@", "")
                    memberid = memberid.replace("!", "")
                    memberid = memberid.replace(">", "")
                    
                    if not memberid == "":
                        embed=discord.Embed(title="✅ 유저 언밴", description="유저의 언밴을 완료했습니다.",color=0x1dc73a )
                        await message.channel.send(embed=embed)
                
                    else:
                        embed=discord.Embed(title="⚠ 주의", description="`"+prefix+"언밴 [유저ID]` 형식으로 명령어를 사용해주세요. 선택된 사용자가 없습니다.",color=0xd8ef56)
                        await message.channel.send(embed=embed)
             
                except:
                    embed=discord.Embed(title="❌ 오류 발생", description="언밴을 실패하였습니다. 권한을 확인해보세요." ,color=0xff0909)    
                    await message.channel.send(embed=embed)

            else:
                embed=discord.Embed(title="⚠ 주의", description="관리자 권한이 있어야 사용 가능한 명령어입니다.",color=0xd8ef56)
                await message.channel.send(embed=embed)




        if message.content.startswith(prefix+"킥") :
            if message.author.guild_permissions.administrator == True:
                try:
                    if not message.mentions == []:

                        member = message.mentions[0]
                        await message.guild.kick(member,reason=str(message.author) + "님의 명령어 사용으로 인해 킥 당하셨습니다.")
                        embed=discord.Embed(title="✅ 멤버 킥", description="킥을 날려버렸습니다.",color=0x1dc73a)
                        await message.channel.send(embed=embed)
                    else:
                        embed=discord.Embed(title="⚠ 주의", description="`"+prefix+"킥 @유저` 형식으로 명령어를 사용해주세요. 선택된 사용자가 없습니다.",color=0xd8ef56)
                        await message.channel.send(embed=embed)
                       
                except:
                    embed=discord.Embed(title="❌ 오류 발생", description="킥을 실패하였습니다. 권한을 확인해 주세요." ,color=0xff0909)    
                    await message.channel.send(embed=embed)
            else:
                embed=discord.Embed(title="⚠ 주의", description="관리자 권한이 있어야 사용 가능한 명령어입니다.",color=0xd8ef56)
                await message.channel.send(embed=embed)


