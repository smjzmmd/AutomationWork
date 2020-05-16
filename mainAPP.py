import tools.qqtools as qqsend
import tools.discordtools as dis
import tools.linetools as lin

version_name="洛汗M 0505版：\n 1、随游戏版本更新。\n"
file_path="F:\\zzz\\Desktop\\洛汗M_2020-05-05.rar"

MEGA_path="www.baidu.com"

'''star'''
if __name__=="__main__":
    qqsend.start_sending(version_name,file_path)
    dis.discord_send(version_name,MEGA_path)
    lin.line_send(version_name,file_path)




