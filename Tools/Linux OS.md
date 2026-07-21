# Linux Operating System

An operating system (Operating System, OS) is the most fundamental **system software** in a computer system. It is a collection of programs that manage computer hardware and software resources and provide services to users and other software. 

The operating system kernel must be **compiled** for a CPU's instruction set before it can run on that CPU. A CPU defines the basic operational commands it can understand and execute through its instruction set.

| Operating System | Category | Vendor / Nature |
| ---------------- | -------- | --------------- |
| Windows          | Desktop Operating System | Microsoft |
| macOS            | Desktop Operating System | Apple |
| Linux            | Server Operating System | Open Source |
| Android          | Mobile Operating System | Google |
| iOS              | Mobile Operating System | Apple |
| HarmonyOS        | Mobile Operating System | Huawei |

The **Linux kernel** provides core Linux system capabilities such as hardware scheduling and management, and it is free and open source. 

On top of the Linux kernel, system-level applications are packaged together; these combined packages are referred to as Linux distributions, such as Ubuntu and CentOS.

The Linux directory structure is a **tree structure** with only one **root directory `/`**, and all files reside under this root directory. The slash `/` is used to represent hierarchical relationships in a path.

```bash
# The first / in a path represents the root directory
# subsequent / characters indicate hierarchy
/user/local/hello.txt
```



### Linux Commands

A Linux command is essentially a Linux program; each command is a Linux program. The command line refers to the Linux terminal (Terminal).

Press `Ctrl+Alt+T` to open the terminal.

```bash
command [-options] [parameter]
# options control command behavior details
# parameter specifies the target operated on by the command
```

`ls` 

```bash
ls [-a -l -h] [LinuxPath]
```

```bash
ls # List the contents of the current working directory
```

When the Linux command-line terminal starts, it loads the **HOME directory** of the currently logged-in user as the current working directory by default. 

Therefore, the `ls` command lists the contents of the HOME directory, which is the personal account directory of each Linux user. Its path is `/home/username`.

```bash
/home/yunxiu
```

| Option / Parameter | Description |
| ------------------ | ----------- |
| `-a` | **all** files: list all files, including hidden files or directories (those beginning with `.`) |
| `-l` | **long** listing format: display items vertically with more details |
| `-h` | **human-readable** file sizes: display file sizes in a readable format such as K, M, or G; usually used together with `-l` |
| `LinuxPath` | Specifies the target directory |

```bash
ls / # View the contents of the root directory
```

```bash
ls -l -a / # Mixed usage of -options and parameter
ls -la /
ls -al /
ls -lh /
```



##### Directory navigation commands

`cd`: Change Directory, used to switch the working directory.

```bash
cd [LinuxPath]
```

If no parameter is provided, it returns to the HOME directory by default.

`pwd`: Print Working Directory, used to display the current working directory.

```bash
pwd
```



Absolute path: starts from the root directory.

```bash
cd /home/yunxiu/Desktop
```

Relative path: starts from the current directory.

```bash
cd Desktop
```

Special path symbols:

```bash
cd ./Desktop     # Switch to the Desktop directory under the current directory; same effect as cd Desktop
cd ..            # Switch to the parent directory
cd ../..         # Switch to the grandparent directory
cd ~             # Switch to the HOME directory
cd ~/Desktop     # Switch to the Desktop directory under HOME
```



`mkdir`: Make Directory, used to create a new directory (folder). Permissions are generally limited to the HOME directory.

```bash
mkdir [-p] LinuxPath
```

The `LinuxPath` parameter is required.

`-p` automatically creates nonexistent parent directories and is suitable for creating multi-level directory structures in one command.

```bash
mkdir /home/yunxiu/test1
mkdir ./test2
mkdir ~/test3
mkdir -p ~/TEST/test4   # Equivalent to mkdir ~/TEST/test4 if TEST already exists
```



##### File operation commands

`touch`: create a file.

```bash
touch LinuxPath
```

```bash
touch test.txt
```

`cat`: concatenate; displays the entire file content directly.

```bash
cat LinuxPath
```

```bash
cat test1.txt
```

`more`: view file content page by page; press Space to advance and `Q` to quit.

```bash
more LinuxPath
```

```bash
more /etc/services
```

 `cp` : copy files or directories.

```bash
cp [-r] param1 param2
```

`-r` option: used when copying directories; indicates recursive copy.

`param1`: Linux path representing the source file or directory.

`param2`: Linux path representing the destination.

```bash
cp test1.txt text2.txt  # File copy
cp -r test1 text2       # Directory copy
```

 `mv` : move files or directories.

```bash
mv param1 param2
```

`param1`: Linux path representing the file or directory to be moved.

`param2`: Linux path representing the destination. If the destination does not exist, the item will be renamed; otherwise, ensure the target exists.

```bash
mv test1.txt Desktop     # Move a file
mv test1.txt renamed.txt # Rename a file
mv test Desktop          # Move a directory
```

 `rm` : remove files or directories.

```bash
rm [-r -f] param1 param2 ...
```

+ `-r`: same as in the `cp` command; used for deleting directories
+ `-f`: force deletion without a confirmation prompt. Ordinary users are usually not prompted, while the `root` user may receive a prompt; therefore, ordinary users generally do not need `-f`
+ `param1 param2 ... paramN`: paths of files or directories to delete, separated by spaces

```bash
rm text1.txt test2.txt
rm test1 test2
```

The symbol `*` indicates a **wildcard**, meaning it matches arbitrary content (including empty strings).

```bash
mv test*    # Indicates deleting anything that starts with test
mv *test    # Indicates deleting anything that ends with test
mv *test*   # Indicates deleting anything that contains test
```

```bash
rm -rf /    # Format the system
rm -rf /*
```



##### Search commands

 `which` : locate the executable file of a command (program).

```bash
which command
```

```bash
which pwd
/usr/bin/pwd
```

 `find`

Search by file name:

```bash
su -root
find startpath -name "filename"
```

Search by file size:

```bash
su -root
find startpath -size +/- n[kMG]
```

```bash
find / -size -100k   # Find files smaller than 100 KB
find / -size +1G     # Find files larger than 1 GB
```

 `history` : display previously entered commands.

```bash
history
```

 `grep` : **G**lobal **R**egular **E**xpression **P**rint; filters file lines by keyword.

```bash
grep [-n] keywords LinuxPath
```

+ Option `-n`: optional; displays the line number of matching lines in the result
+ `param1` keyword: required; the keyword to filter by. If it contains spaces or other special symbols, it is recommended to wrap it in quotation marks
+ `param2` file path: required; the file path whose content is to be filtered; can also be provided through a pipeline

 `wc` : word count.

```bash
wc [-c -m -l -w] 文件路径
```

+ `-c`: count bytes
+ `-m`: count characters
+ `-l`: count lines
+ `-w`: count words
+ file path: the file to be counted; can also be provided through a pipeline

**Pipeline (`|`)**: passes the output on the left as the input to the command on the right.

```bash
cat file.text | grep word
```

```bash
cat file.text | wc -l
```

 `echo` :

```bash
echo output_content
```

For complex output, it is recommended to wrap the content in quotation marks.

```bash
echo "Hello World!"
```

```bash
echo `pwd`   # Content inside backticks is executed as a command
/home/yunxiu
```

| Redirection Operator | Description |
| -------------------- | ----------- |
| `>`  | Overwrite the target file on the right with the output of the command on the left |
| `>>` | Append the output of the command on the left to the target file on the right |

```bash
echo "Hello World!" > file.text
```

```bash
echo "Hello World!" >> file.text
```

```bash
echo "Current working directory: `pwd`" > work.text
```

 `tail` : view the end of a file and track the latest changes.

```bash
tail [-f -num] LinuxPath
```

+ `LinuxPath`: the path of the file being tracked
+ `-f`: follow mode; continue tracking until you press `Ctrl+C`
+ `-num`: specifies how many lines from the end to display; defaults to 10 if omitted

```bash
tail -5 file.text
```

```bash
tail -f file.text
```

```bash
echo "content" >> work.text
tail -f work.text
```



##### Users and permissions

Ordinary users: generally unrestricted within the HOME directory. Outside the HOME directory, they usually have only read and execute permissions, but not write permissions.

 `root` user**: the account with the highest privileges (superuser).

 `su` : **S**witch **U**ser.

```bash
su [-] [username]
```

+ `-`: whether to load environment variables after switching users
+ `username`: if omitted, it defaults to the `root` user

```bash
exit        # Return to the previous user, or press Ctrl+D
```

```bash
su -root    # Switch to the root user
# Enter password
exit        # Return to the ordinary user
```

 `sudo` : authorizes an ordinary command to run temporarily with `root` privileges. It requires sudo authentication to be configured for the ordinary user.

```bash
sudo command
```



##### User and group management

Require `root` privileges.

Create a user group:

```bash
groupadd usergroupname
```

Delete a user group:

```bash
groupdel usergroupname
```

Create a user:

```bash
useradd [-g -d] username
```

+ `-g`: specify an existing user group. If a group with the same name already exists, `-g` must be used. If `-g` is omitted, a group with the same name is created automatically and the user is added to it
+ `-d`: specify the user's HOME path; if omitted, the default is `/home/username`

View / delete a user:

```bash
userdel [-r] username
```

+ `-r`: delete the user's HOME directory; often not used

View the groups to which a user belongs:

```bash
id [username]
```

Modify a user's group membership:

```bash
usermod -aG
```

View all user information in the current system:

```bash
getent passwd
```

View all group information in the current system:

```bash
getent group
```



##### Permission control

**Understanding permission metadata**

| Type | Owner |  |  | Group |  |  | Others |  |  |
| ---- | ---------------- | -- | -- | ---------------- | -- | -- | ---------------- | -- | -- |
| `-` / `d` / `l` | `r` / `-` | `w` / `-` | `x` / `-` | `r` / `-` | `w` / `-` | `x` / `-` | `r` / `-` | `w` / `-` | `x` / `-` |

+ First character: `-` indicates a file, `d` indicates a directory, and `l` indicates a symbolic link
+ `w` (write): write permission
+ `x` (execute): execute permission
+ `r` (read): read permission

 `chmod` : change mode; modifies permissions of files or directories.

Only the **owner of the file or directory, or the `root` user**, can modify permissions.

```bash
chmod [-R] <permissions> <files/dirctorise>
```

+ `-R`: apply the same operation recursively to all contents within a directory

```bash
chmod u=rwx,g=rx,o=x file.txt   # Set permissions of file.txt to rwxr-x--x
```

`u` stands for user (owner), `g` for group, and `o` for others.

| Number | Permission |
| ------ | ---------- |
| 0 | `---` |
| 1 | `--x` |
| 2 | `-w-` |
| 3 | `-wx` |
| 4 | `r--` |
| 5 | `r-x` |
| 6 | `rw-` |
| 7 | `rwx` |

```bash
chmod 751 file.txt   # Shorthand for u=rwx,g=rx,o=x
```

 `chown` : change owner; modifies the owner and group of a file or directory.

Only the **`root` user** can modify the owner and group of a file or directory.

```bash
chown [-R] [username][:][usergroupname] <files/dirctorise>
```

+ `-R`: apply the same operation recursively to all contents within a directory

```bash
chown root file.text   # Change the owner of file.text to root
```

```bash
chown :root file.text  # Change the group of file.text to root
```

```bash
chown yunxiu:root file.text   # Change the owner of file.text to yunxiu and the group to root
```



| Shortcut | Function |
| -------- | -------- |
| `Ctrl+C` | Force stop; cancel current input and re-enter |
| `Ctrl+D` | Exit a user session or some specific programs; cannot exit vi/vim |
| `!command_prefix` | Automatically execute the most recent command matching the prefix |
| `Ctrl+R` | Match historical commands in the input area; use Up/Down to browse and Left/Right to edit; press Enter to execute |
| `Ctrl+A` | Jump to the beginning of the command line |
| `Ctrl+E` | Jump to the end of the command line |
| `Ctrl+Left/Right` | Jump by word |
| `Ctrl+L` | Clear terminal content, same as the `clear` command |



 `apt` : Advanced Package Tool, used for software installation.

```bash
apt [-y] [install | remove | search] softwarename
```

+ `-y`: automatically confirm installation or removal without manual confirmation

 `systemctl` : controls service startup, shutdown, and startup-on-boot behavior.

```bash
systemctl start | stop | status | enable | disable servicename
```

+ `start`: start the service
+ `stop`: stop the service
+ `status`: view service status
+ `enable`: enable the service to start automatically at boot
+ `disable`: disable the service from starting automatically at boot

Service names may include built-in system services such as `NetworkManager` (primary network service), `network` (secondary network service), `firewalld` (firewall service), and `sshd` (SSH service).

 `ln` : create a symbolic link to point a file or directory to another location.

```bash
ln -s param1 param2
```

+ `param1`: the file or directory being linked
+ `param2`: the destination of the symbolic link

 `date` : display the system time.

```bash
date -d [+formatsrtings]
```

+ `-d`: display the date according to the given string; commonly used for date calculations
+ format string: controls date output through specific placeholders

+ `%Y`: four-digit year  
+ `%y`: last two digits of the year (`00`–`99`)  
+ `%M`: month (`01`–`12`)  
+ `%d`: day (`01`–`31`)  
+ `%H`: hour (`00`–`23`)  
+ `%M`: minute (`00`–`59`)  
+ `%S`: second (`00`–`60`)  
+ `%s`: number of seconds since `1970-01-00:00:00 UTC` until now

```bash
date
Wed Jan  7 03:14:36 PM CST 2026
```

```bash
date +%Y-%m-%d
2026-01-07
```

```bash
date "+%Y-%m-%d %H:%M:%S"   # Includes spaces
2026-01-07 15:15:00
```

```bash
data -d "-1 day"            # Yesterday
Tue Jan  6 03:19:11 PM CST 2026
```

##### IP Address 

Internet Protocol Address: the address used for network communication.

IPv4 address format: `a.b.c.d`, where `a`, `b`, `c`, and `d` are numbers from `0` to `255`, for example `192.168.232.204`.

```bash
idconfig    # View IP addresses
eno1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether e0:73:e7:ee:4d:97  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 1682  bytes 310736 (310.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1682  bytes 310736 (310.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlo1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.232.204  netmask 255.255.255.0  broadcast 192.168.232.255
        inet6 fe80::170c:deb4:6f30:ba6c  prefixlen 64  scopeid 0x20<link>
        ether 74:97:79:8a:b1:0d  txqueuelen 1000  (Ethernet)
        RX packets 91726  bytes 111372710 (111.3 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 43329  bytes 8457019 (8.4 MB)
        TX errors 0  dropped 59 overruns 0  carrier 0  collisions 0
```

| Interface Name | Network Adapter |
| -------------- | --------------- |
| `eno1` | Wired network adapter (Ethernet) |
| `lo` | Virtual loopback interface, used for internal local communication |
| `wlo1` | Wireless network adapter (Wi-Fi) |

+ `UP`: the system has enabled this network interface
+ `RUNNING`: the physical link is active
+ `0.0.0.0`: can refer to the local host, can be used to determine binding relationships in port binding, and can represent all IP addresses in some address restriction scenarios—for example, a rule set to `0.0.0.0` allows access from any IP
+ `127.0.0.1`: loopback address; accessing this address means accessing the local computer
+ `192.168.232.204`: an IPv4 address

##### Hostname

```bash
hostname
yunxiu-OMEN-by-HP-Gaming-Laptop-16-xf0xxx
```

```bash
hostnamectl set-hostname <hostname>   # Change the hostname
```

Domain name resolution:
