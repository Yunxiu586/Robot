# Debug

### `Setup.py`

```
colcon build --packages-select my_robot
```

**Bug**

The file `setup.py` contains a non-breaking space U+00A0, which is unrecognizable to the Python interpreter, leading to a syntax parsing failure.

```
SyntaxError: invalid non-printable character U+00A0
```

**Debug**

Replace all non-breaking spaces U+00A0 in the file with ordinary spaces.

+ `-i` means modify the original file directly.

+ `\xc2\xa0 `is the byte sequence of the U+00A0 character in UTF‑8 encoding.

```
sed -i 's/\xc2\xa0/ /g' setup.py
```



### `apt`

```
sudo apt update
sudo apt install ros-rolling-ros-gz
```

**Bug**

The issue was an invalid ROS APT repository configuration that broke HTTPS certificate validation and prevented package index retrieval. Replacing the stale repository definition with the official `ros2-apt-source` package restored normal APT behavior and allowed `ros-rolling-ros-gz` to be installed successfully.

```
Err:2 https://packages.ros.org/ros2/ubuntu noble InRelease                     
  Certificate verification failed: The certificate is NOT trusted. The name in the certificate does not match the expected.  Could not handshake: Error in the certificate verification.
```

APT could not validate the server certificate during the HTTPS handshake.

```
Certificate verification failed
```

The certificate chain presented by the remote endpoint did not pass trust validation.

```
The certificate is NOT trusted
```

The certificate subject/SAN did not match the requested hostname, which strongly suggests an incorrect endpoint, redirection issue, or stale source entry.

```
The name in the certificate does not match the expected.
```

**Debug**

ROS repository hostnames are the official server domains (e.g., `packages.ros.org`for ROS 1 and `repo.ros2.org`for ROS 2) used to distribute software packages. These URLs are specified in your system's APT source list files, which tell the package manager where to locate and download software.

The main source list file for the APT package manager is `/etc/apt/sources.list`. Third-party software sources, such as those for ROS, are typically added as separate `.list` files in the `/etc/apt/sources.list.d/*` directory.

Recursively search the main APT source list and all source list fragments for ROS-related repository definitions. The pattern matches common ROS repository hostnames. 

 Redirecting stderr to `/dev/null` suppresses warnings for nonexistent files.

```
grep -R "packages.ros.org\|repo.ros2.org\|ros2" /etc/apt/sources.list /etc/apt/sources.list.d/* 2>/dev/null
```

Delete legacy ROS 2 source list files that may conflict with the current repository configuration.

```
sudo rm -f /etc/apt/sources.list.d/ros-latest.list
sudo rm -f /etc/apt/sources.list.d/ros2.list
```

Install utilities required for repository management, including add-apt-repository.

Enable the Ubuntu Universe repository, which is commonly required for ROS dependencies on Ubuntu.

```
sudo apt install software-properties-common -y
sudo add-apt-repository universe -y
```

Refresh local package metadata from all configured repositories after repository cleanup and repository enablement. Install curl, which is used to query the GitHub API and download the repository package.

```
sudo apt update
sudo apt install curl -y
```

Query the GitHub API for the latest release of `ros-apt-source`, extracts the tag name, and stores it in the environment variable `ROS_APT_SOURCE_VERSION`.

```
export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F'"' '{print $4}')
```

Download the ROS 2 APT source package that matches Ubuntu Noble. The `-L` option follows redirects, and `-o` writes the file to `/tmp/ros2-apt-source.deb`.

```
curl -L -o /tmp/ros2-apt-source.deb \
"https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"
```

Installs the downloaded Debian package, which adds the official ROS 2 repository configuration and associated key material.

```
sudo dpkg -i /tmp/ros2-apt-source.deb
```

Refreshes package indexes again so APT can read metadata from the newly installed ROS repository. Installs the target ROS package after the repository configuration has been corrected.

```
sudo apt update
sudo apt install ros-rolling-ros-gz
```



