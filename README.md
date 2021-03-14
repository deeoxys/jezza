````                                                                                                                                                                                                                                                                               
MMMMMMMM               MMMMMMMM               AAA           YYYYYYY       YYYYYYY
M:::::::M             M:::::::M              A:::A          Y:::::Y       Y:::::Y
M::::::::M           M::::::::M             A:::::A         Y:::::Y       Y:::::Y
M:::::::::M         M:::::::::M            A:::::::A        Y::::::Y     Y::::::Y
M::::::::::M       M::::::::::M           A:::::::::A       YYY:::::Y   Y:::::YYY
M:::::::::::M     M:::::::::::M          A:::::A:::::A         Y:::::Y Y:::::Y   
M:::::::M::::M   M::::M:::::::M         A:::::A A:::::A         Y:::::Y:::::Y    
M::::::M M::::M M::::M M::::::M        A:::::A   A:::::A         Y:::::::::Y     
M::::::M  M::::M::::M  M::::::M       A:::::A     A:::::A         Y:::::::Y      
M::::::M   M:::::::M   M::::::M      A:::::AAAAAAAAA:::::A         Y:::::Y       
M::::::M    M:::::M    M::::::M     A:::::::::::::::::::::A        Y:::::Y       
M::::::M     MMMMM     M::::::M    A:::::AAAAAAAAAAAAA:::::A       Y:::::Y       
M::::::M               M::::::M   A:::::A             A:::::A      Y:::::Y       
M::::::M               M::::::M  A:::::A               A:::::A  YYYY:::::YYYY    
M::::::M               M::::::M A:::::A                 A:::::A Y:::::::::::Y    
MMMMMMMM               MMMMMMMMAAAAAAA                   AAAAAAAYYYYYYYYYYYYY                               

Discord bot written with discord.py.
Written and somewhat maintained by r333mo for a private server, but feel free to use if you want to.
Started writing on 2/10/2020.
Named after Jeremy Clarkson of course.

Prefix is "j" or "J".
Bot is NOT case sensitive.

COMMAND LIST:
PING -> Bot ping.
UPTIME -> Bot uptime in seconds.
QUOTE <mention user> -> Gets a random quote from a user. (Alias "Q")
MESSAGECOUNT <mention user> -> Gets total message count from a user. (Alias "MC")
GIVE ALL <role> -> Give all users a specified role (requires an admin role).

OTHER FEATURES:
Has a sort of database of messages sent by users in the ./messages/ directory.
Filters out bad words which can be specified if you make the ./assets/.gitignore badwords.txt directory (each line is a bad word).
Bot key is stored safely in ./assets/.gitignore NAME.txt (name can be changed in jezza.py).
