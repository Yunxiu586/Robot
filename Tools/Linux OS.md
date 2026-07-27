# Linux Operating System

[toc]

An operating system (OS) is fundamental **system software** in a computer system. It is a collection of programs that manage computer hardware and software resources and provide services to users and other software.

An operating-system kernel must be built for a compatible CPU architecture before it can run natively on that CPU. A CPU architecture defines the machine instructions the processor can understand and execute.

| System | Common Use | Vendor / Nature |
| ------ | ---------- | --------------- |
| Windows | Desktop and server operating systems | Microsoft |
| macOS | Desktop operating system | Apple |
| GNU/Linux distributions | Desktop, server, embedded, and other systems | Open source |
| Android | Mobile operating system | Google-led open-source ecosystem (AOSP) |
| iOS | Mobile operating system | Apple |
| HarmonyOS | Mobile and embedded operating system family | Huawei |

The **Linux kernel** provides core capabilities such as process scheduling, memory management, device management, file-system support, and networking, and it is free and open source.

A Linux distribution combines the Linux kernel with system libraries, command-line tools, package-management software, and other applications. Examples include Ubuntu and CentOS Stream.

The Linux directory structure is a **tree structure** with only one **root directory `/`**, and all files reside under this root directory. The slash `/` separates components in a path.

```bash
# The first / in a path represents the root directory
# subsequent / characters indicate hierarchy
/usr/local/hello.txt
```

### Linux Commands

A shell command may be a shell builtin, function, alias, script, or external executable. A terminal is the interface used to interact with a shell, while the command line is the text-based interface provided by the shell.

On many Ubuntu desktop environments, press `Ctrl+Alt+T` to open a terminal. This shortcut is desktop-environment dependent.

```bash
command [options] [arguments]
# options control command behavior details
# arguments specify the targets operated on by the command
```

`ls`

```bash
ls [OPTION]... [FILE]...
```

```bash
ls # List the contents of the current working directory
```

A newly opened terminal usually starts the shell in the current user's **HOME directory**, although terminal settings or the launching application may choose another directory.

Therefore, when the current directory is HOME, `ls` lists the contents of HOME. A regular user's HOME is commonly `/home/username`; the `root` user's HOME is usually `/root`, and administrators may configure other locations.

```bash
/home/yunxiu
```

| Option / Parameter | Description |
| ------------------ | ----------- |
| `-a` | **all** files: list all files, including hidden files or directories (those beginning with `.`) |
| `-l` | **long** listing format: display items vertically with more details |
| `-h` | **human-readable** file sizes: display file sizes in a readable format such as K, M, or G; usually used together with `-l` |
| `FILE` | Specifies a file or directory to list; if omitted, the current directory is used |

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
cd [DIRECTORY]
```

If no directory is provided, `cd` changes to the HOME directory.

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

`mkdir`: Make Directory, used to create a new directory (folder). Whether creation is allowed depends on the write and search permissions of the parent directory.

```bash
mkdir [-p] DIRECTORY...
```

At least one directory path is required.

`-p` automatically creates nonexistent parent directories and is suitable for creating multi-level directory structures in one command.

```bash
mkdir /home/yunxiu/test1
mkdir ./test2
mkdir ~/test3
mkdir -p ~/TEST/test4   # Equivalent to mkdir ~/TEST/test4 if TEST exists and test4 does not exist
```

##### File operation commands

`touch`: update a file's access and modification timestamps; if the file does not exist, create an empty file by default.

```bash
touch FILE...
```

```bash
touch test.txt
```

`cat`: concatenate files and write their contents to standard output.

```bash
cat FILE...
```

```bash
cat test1.txt
```

`more`: view file content page by page; press Space to advance and `q` to quit.

```bash
more FILE
```

```bash
more /etc/services
```

`cp` : copy files or directories.

```bash
cp [OPTION]... SOURCE DEST
```

`-r` option: copy directories recursively.

`SOURCE`: source file or directory.

`DEST`: destination path.

```bash
cp test1.txt text2.txt  # File copy
cp -r test1 text2       # Directory copy
```

`mv` : move files or directories.

```bash
mv [OPTION]... SOURCE DEST
```

`SOURCE`: file or directory to be moved.

`DEST`: destination path. If it is an existing directory, the source is moved into that directory. Otherwise, the source is renamed or replaces the destination according to permissions and options.

```bash
mv test1.txt Desktop     # Move a file
mv test1.txt renamed.txt # Rename a file
mv test Desktop          # Move a directory
```

`rm` : remove files or directories.

```bash
rm [OPTION]... FILE...
```

+ `-r`: same as in the `cp` command; used for deleting directories
+ `-f`: ignore nonexistent files and never prompt
+ `FILE...`: one or more paths to remove

```bash
rm text1.txt test2.txt
rm -r test1 test2   # Delete directories recursively
```

In shell pathname expansion, `*` is a **wildcard** that matches zero or more characters within one path component. By default, it does not match a leading `.` in hidden names.

```bash
rm test*    # Delete matching files whose names start with test
rm *test    # Delete matching files whose names end with test
rm *test*   # Delete matching files whose names contain test
```

> **Warning:** Do not use commands such as `rm -rf /*`. They attempt to delete large parts of the file system; this is deletion, not disk formatting. GNU `rm` normally rejects an argument that resolves directly to `/`, but similar variants can still destroy the system.

##### Search commands

`which`: locate an executable file in `PATH`.

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
find START_PATH -name "FILE_NAME"
# Use sudo only when the search needs access to protected directories
sudo find / -name "FILE_NAME"
```

Search by file size:

```bash
find START_PATH -size [+|-]N[kMG]
```

```bash
find / -size -100k   # Find files whose rounded size is less than 100 KiB
find / -size +1G     # Find files whose rounded size is greater than 1 GiB
```

`history` : display previously entered commands.

```bash
history
```

`grep` : **G**lobal **R**egular **E**xpression **P**rint; filters file lines by keyword.

```bash
grep [-n] "PATTERN" [FILE]...
```

+ Option `-n`: optional; displays the line number of matching lines in the result
+ `PATTERN`: required; quote it when it contains spaces or shell-special characters
+ `FILE`: optional; if omitted, `grep` reads standard input

`wc` : word count.

```bash
wc [-c -m -l -w] [FILE]...
```

+ `-c`: count bytes
+ `-m`: count characters
+ `-l`: count lines
+ `-w`: count words
+ file path: the file to be counted; can also be provided through a pipeline

**Pipeline (`|`)**: passes the standard output of the command on the left to the standard input of the command on the right.

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
echo "$(pwd)"   # Recommended command-substitution syntax
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
echo "Current working directory: $(pwd)" > work.text
```

`tail` : view the end of a file and track the latest changes.

```bash
tail [-f] [-n NUM] FILE...
```

+ `FILE`: the path of the file being viewed or tracked
+ `-f`: follow mode; continue tracking until you press `Ctrl+C`
+ `-n NUM`: specifies how many lines from the end to display; defaults to 10 if omitted

```bash
tail -n 5 file.text
```

```bash
tail -f file.text
```

```bash
echo "content" >> work.text
tail -f work.text
```

##### Users and permissions

An ordinary user's access is determined by file permissions, ACLs, ownership, and other security controls. Users commonly own and can modify their HOME directory, but access elsewhere is not determined solely by whether a path is inside or outside HOME.

**`root` user**: the traditional superuser account with the highest discretionary privileges.

`su`: **s**ubstitute **u**ser identity.

```bash
su [-] [username]
```

+ `-` or `--login`: start a login shell, change to the target user's HOME directory, and initialize an environment similar to a direct login
+ `username`: if omitted, it defaults to the `root` user

```bash
exit        # Return to the previous user, or press Ctrl+D
```

```bash
su - root   # Switch to root using a login shell; `su -` is equivalent
# Enter password
exit        # Return to the ordinary user
```

`sudo`: authorizes a command to run as another user, `root` by default. It requires sudo authentication to be configured for the ordinary user.

```bash
sudo command
```

##### User and group management

These operations normally require `root` privileges, typically obtained with `sudo`.

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
useradd [-m] [-g GROUP] [-d HOME_DIR] USERNAME
```

+ `-g GROUP`: specify the initial login group; default group behavior depends on system configuration
+ `-d HOME_DIR`: specify the HOME path; the default depends on system configuration
+ `-m`: create the HOME directory if it does not already exist

Delete a user:

```bash
userdel [-r] username
```

+ `-r`: also remove the user's HOME directory and mail spool

View a user's UID, primary GID, and supplementary groups:

```bash
id [username]
```

Modify a user's group membership:

```bash
usermod -aG GROUP1,GROUP2 USERNAME
```

View entries in the system user database:

```bash
getent passwd
```

View entries in the system group database:

```bash
getent group
```

##### Permission control

**Understanding permission metadata**

| Type | Owner |  |  | Group |  |  | Others |  |  |
| ---- | ---------------- | -- | -- | ---------------- | -- | -- | ---------------- | -- | -- |
| `-` / `d` / `l` | `r` / `-` | `w` / `-` | `x` / `-` | `r` / `-` | `w` / `-` | `x` / `-` | `r` / `-` | `w` / `-` | `x` / `-` |

+ First character: `-` indicates a regular file, `d` a directory, and `l` a symbolic link
+ `r` (read): read permission
+ `w` (write): write permission
+ `x` (execute/search): execute permission for files and search/traverse permission for directories

`chmod` : change mode; modifies permissions of files or directories.

The file owner can normally change its mode; `root` can also do so.

```bash
chmod [-R] MODE FILE...
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

Changing a file's owner normally requires `root` privileges. A file owner may be allowed to change the group to one of their own groups; exact restrictions depend on the system.

```bash
chown [-R] [OWNER][:[GROUP]] FILE...
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
| `Ctrl+C` | Send an interrupt signal (`SIGINT`) to the foreground process; the process may handle or ignore it |
| `Ctrl+D` | Send end-of-file input; at an empty shell prompt this usually exits the shell |
| `!command_prefix` | Automatically execute the most recent command matching the prefix |
| `Ctrl+R` | Start reverse incremental history search; press `Ctrl+R` again for earlier matches, then edit or press Enter |
| `Ctrl+A` | Jump to the beginning of the command line |
| `Ctrl+E` | Jump to the end of the command line |
| `Ctrl+Left/Right` | Jump by word |
| `Ctrl+L` | Clear terminal content, same as the `clear` command |

`apt` : Advanced Package Tool command-line interface used on Debian-based distributions such as Ubuntu.

```bash
sudo apt install [-y] PACKAGE...
sudo apt remove [-y] PACKAGE...
apt search PATTERN
```

+ `-y`: automatically answer yes to confirmation prompts; use it cautiously

`systemctl` : inspects and controls the `systemd` system and service manager.

```bash
systemctl {start|stop|status|enable|disable} UNIT...
```

+ `start`: start the service
+ `stop`: stop the service
+ `status`: view service status
+ `enable`: enable the service to start automatically at boot
+ `disable`: disable the service from starting automatically at boot

Unit names are distribution- and installation-dependent. Examples may include `NetworkManager.service` and `ssh.service`. Use `systemctl list-unit-files --type=service` to inspect available service units. Note that `enable` configures startup links but does not necessarily start the service immediately; use `enable --now` when both actions are intended.

`ln -s`: create a symbolic link to point a file or directory to another location.

```bash
ln -s TARGET LINK_NAME
```

+ `TARGET`: the target file or directory
+ `LINK_NAME`: the name/path of the symbolic link to create

`date` : display the system time.

```bash
date [OPTION]... [+FORMAT]
date -d "DATE_STRING" [+FORMAT]
```

+ `-d`: display the date according to the given string; commonly used for date calculations
+ format string: controls date output through specific placeholders

+ `%Y`: four-digit year
+ `%y`: last two digits of the year (`00`–`99`)
+ `%m`: month (`01`–`12`)
+ `%d`: day (`01`–`31`)
+ `%H`: hour (`00`–`23`)
+ `%M`: minute (`00`–`59`)
+ `%S`: second (`00`–`60`)
+ `%s`: number of seconds since the Unix Epoch, `1970-01-01 00:00:00 UTC`

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
date -d "-1 day"            # Yesterday
Tue Jan  6 03:19:11 PM CST 2026
```

##### IP Address

Internet Protocol Address: the address used for network communication.

IPv4 address format: `a.b.c.d`, where `a`, `b`, `c`, and `d` are numbers from `0` to `255`, for example `192.168.232.204`.

```bash
ifconfig    # Legacy command; may require the net-tools package
# Modern alternative: ip address
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
+ `RUNNING`: the interface is considered operational by the kernel; it does not guarantee Internet connectivity
+ `0.0.0.0`: the IPv4 unspecified address. When a server binds to it, the socket listens on all local IPv4 interfaces. In CIDR notation, `0.0.0.0/0` represents all IPv4 addresses.
+ `127.0.0.1`: loopback address; accessing this address means accessing the local computer
+ `192.168.232.204`: an IPv4 address

##### Hostname

```bash
hostname
yunxiu-OMEN-by-HP-Gaming-Laptop-16-xf0xxx
```

```bash
sudo hostnamectl set-hostname NEW_HOSTNAME   # Change the hostname
```

