````                                                                                                                                                                                                                                                                               
FFFFFFFFFFFFFFFFFFFFFFIIIIIIIIIITTTTTTTTTTTTTTTTTTTTTTTMMMMMMMM               MMMMMMMM        CCCCCCCCCCCCC
F::::::::::::::::::::FI::::::::IT:::::::::::::::::::::TM:::::::M             M:::::::M     CCC::::::::::::C
F::::::::::::::::::::FI::::::::IT:::::::::::::::::::::TM::::::::M           M::::::::M   CC:::::::::::::::C
FF::::::FFFFFFFFF::::FII::::::IIT:::::TT:::::::TT:::::TM:::::::::M         M:::::::::M  C:::::CCCCCCCC::::C
  F:::::F       FFFFFF  I::::I  TTTTTT  T:::::T  TTTTTTM::::::::::M       M::::::::::M C:::::C       CCCCCC
  F:::::F               I::::I          T:::::T        M:::::::::::M     M:::::::::::MC:::::C              
  F::::::FFFFFFFFFF     I::::I          T:::::T        M:::::::M::::M   M::::M:::::::MC:::::C              
  F:::::::::::::::F     I::::I          T:::::T        M::::::M M::::M M::::M M::::::MC:::::C              
  F:::::::::::::::F     I::::I          T:::::T        M::::::M  M::::M::::M  M::::::MC:::::C              
  F::::::FFFFFFFFFF     I::::I          T:::::T        M::::::M   M:::::::M   M::::::MC:::::C              
  F:::::F               I::::I          T:::::T        M::::::M    M:::::M    M::::::MC:::::C              
  F:::::F               I::::I          T:::::T        M::::::M     MMMMM     M::::::M C:::::C       CCCCCC
FF:::::::FF           II::::::II      TT:::::::TT      M::::::M               M::::::M  C:::::CCCCCCCC::::C
F::::::::FF           I::::::::I      T:::::::::T      M::::::M               M::::::M   CC:::::::::::::::C
F::::::::FF           I::::::::I      T:::::::::T      M::::::M               M::::::M     CCC::::::::::::C
FFFFFFFFFFF           IIIIIIIIII      TTTTTTTTTTT      MMMMMMMM               MMMMMMMM        CCCCCCCCCCCCC                                     

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
