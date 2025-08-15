# isocut 使用指南

## 简介

openEuler 光盘镜像较大，下载、传输镜像很耗时。另外，使用 openEuler 光盘镜像安装操作系统时，会安装镜像所包含的全量 RPM 软件包，用户无法只安装部分所需的软件包。

在某些场景下，用户不需要安装镜像提供的全量软件包，或者需要一些额外的软件包。因此，openEuler 提供了镜像裁剪定制工具。通过该工具，用户可以基于 openEuler 光盘镜像裁剪定制仅包含所需 RPM 软件包的 ISO 镜像。这些软件包可以来自原有 ISO 镜像，也可以额外指定，从而满足用户定制需求。

本文档介绍 openEuler 镜像裁剪定制工具的安装和使用方法，以指导用户更好的完成镜像裁剪定制。

## 软硬件要求

使用 openEuler 裁剪定制工具制作 ISO 所使用的机器需要满足如下软硬件要求：

- CPU 架构为 AArch64 或者 x86_64
- 操作系统为 openEuler 20.03 LTS SP3
- 建议预留 30 GB 以上的磁盘空间（用于运行裁剪定制工具和存放 ISO 镜像）

## 安装工具

此处以 openEuler 20.03 LTS SP3 版本的 AArch64 架构为例，介绍 ISO 镜像裁剪定制工具的安装操作。

1. 确认机器已安装操作系统 openEuler 20.03 LTS SP3（镜像裁剪定制工具的运行环境）。

   ``` shell script
    $ cat /etc/openEuler-release 
    openEuler release 20.03 (LTS-SP3)
   ```

2. 下载对应架构的 ISO 镜像（必须是 everything 版本），并存放在任一目录（建议该目录磁盘空间大于 20 GB），此处假设存放在 /home/isocut_iso 目录。

   AArch64 架构的镜像下载链接为：

   <https://repo.openeuler.org/openEuler-20.03-LTS-SP3/ISO/aarch64/openEuler-20.03-LTS-SP3-everything-aarch64-dvd.iso>

   > [!NOTE]说明\
   > x86_64 架构的镜像下载链接为：
   > <https://repo.openeuler.org/openEuler-20.03-LTS-SP3/ISO/x86_64/openEuler-20.03-LTS-SP3-everything-x86_64-dvd.iso>

3. 创建文件 /etc/yum.repos.d/local.repo，配置对应 yum 源。配置内容参考如下，其中 baseurl 是用于挂载 ISO 镜像的目录：

   ``` shell script
   [local]
   name=local
   baseurl=file:///home/isocut_mount
   gpgcheck=0
   enabled=1
   ```

4. 使用 root 权限，挂载光盘镜像到 /home/isocut_mount 目录（请与上述 repo 文件中配置的 baseurl 保持一致）作为 yum 源，参考命令如下：

   ```shell
   sudo mount -o loop /home/isocut_iso/openEuler-20.03-LTS-SP3-everything-aarch64-dvd.iso /home/isocut_mount
   ```

5. 使 yum 源生效：

   ```shell
   yum clean all
   yum makecache
   ```

6. 使用 root 权限，安装镜像裁剪定制工具：

   ```shell
   sudo yum install -y isocut
   ```

7. 使用 root 权限，确认工具已安装成功。

   ```shell
    $ sudo isocut -h
    Checking input ...
    usage: isocut [-h] [-t temporary_path] [-r rpm_path] [-k file_path] source_iso dest_iso
    
    Cut openEuler iso to small one
    
    positional arguments:
      source_iso         source iso image
      dest_iso           destination iso image
    
    optional arguments:
      -h, --help         show this help message and exit
      -t temporary_path  temporary path
      -r rpm_path        extern rpm packages path
      -k file_path       kickstart file
   ```

## 裁剪定制镜像

此处介绍如何使用镜像裁剪定制工具基于 openEuler 光盘镜像裁剪或添加额外 RPM 软件包制作新镜像的方法。

### 命令介绍

#### 命令格式

镜像裁剪定制工具通过 isocut 命令执行功能。命令的使用格式为：

`isocut [ --help | -h ] [ -t <*temp_path*> ] [ -r <*rpm_path*> ] [ -k <*file_path*> ]  < *source_iso* > < *dest_iso* >`

#### 参数说明

| 参数             | 是否必选 | 参数含义                                                     |
| ---------------- | -------- | ------------------------------------------------------------ |
| --help \| -h     | 否       | 查询命令的帮助信息。                                         |
| -t \<*temp_path*> | 否       | 指定工具运行的临时目录 *temp_path*，其中 *temp_path* 为绝对路径。默认为 /tmp 。 |
| -r \<*rpm_path*>  | 否       | 用户需要额外添加到 ISO 镜像中的 RPM 包路径。                 |
| -k \<*file_path*> | 否       | 用户需要使用 kickstart 自动安装，指定 kickstart 模板路径。   |
| *source_iso*     | 是       | 用于裁剪的 ISO 源镜像所在路径和名称。不指定路径时，默认当前路径。 |
| *dest_iso*       | 是       | 裁剪定制生成的 ISO 新镜像存放路径和名称。不指定路径时，默认当前路径。 |

### 软件包来源

新镜像的 RPM 包来源有：

- 原有 ISO 镜像。该情况通过配置文件 /etc/isocut/rpmlist 指定需要安装的 RPM 软件包，配置格式为`软件包名.对应架构`，例如：`kernel.aarch64`。

- 额外指定。执行 **isocut** 时使用 -r 参数指定软件包所在路径，并将添加的 RPM 包按上述格式添加到配置文件 /etc/isocut/rpmlist 中。

  > [!NOTE]说明\
  > 裁剪定制镜像时，若无法找到配置文件中指定的 RPM 包，则镜像中不会添加该 RPM 包。\
  > 若 RPM 包的依赖有问题，则裁剪定制镜像时可能会报错。

### kickstart 功能介绍

用户需要实现镜像自动化安装，可以通过 kickstart 的方式。在执行 **isocut** 时使用 -k 参数指定 kickstart 文件。

isocut 为用户提供了 kickstart 模板，路径是 /etc/isocut/anaconda-ks.cfg，用户可以基于该模板修改。

#### 修改 kickstart 模板

若用户需要使用 isocut 工具提供的 kickstart 模板，需要修改以下内容：

- 必须在文件 /etc/isocut/anaconda-ks.cfg 中配置 root 和 grub2 的密码。否则镜像自动化安装会卡在设置密码的环节，等待用户手动输入密码。
- 如果要添加额外 RPM 包，并使用 kickstart 自动安装，则在 /etc/isocut/rpmlist 和 kickstart 文件的 %packages 字段都要指定该 RPM 包。

接下来介绍 kickstart 文件详细修改方法。

##### 配置初始密码

###### 配置 root 初始密码

/etc/isocut/anaconda-ks.cfg 中 root 初始密码的默认配置如下，其中 ${pwd} 需要替换成用户实际的加密密文：

```shell
rootpw --iscrypted ${pwd}
```

这里给出设置 root 初始密码的方法（需使用 root 权限）：

1. 添加用于生成密码的用户，此处假设 testUser。

   ``` shell script
   $ sudo useradd testUser
   ```

2. 设置 testUser 用户的密码。参考命令如下，根据提示设置密码：

   ``` shell script
   $ sudo passwd testUser
   Changing password for user testUser.
   New password: 
   Retype new password: 
   passwd: all authentication tokens updated successfully.
   ```

3. 查看 /etc/shadow 文件，获取加密密码（用户 testUser 后，两个 : 间的字符串，此处使用 *** 代替）。

   ``` shell script
   $ sudo cat /etc/shadow | grep testUser
   testUser:***:19052:0:90:7:35::
   ```

4. 拷贝上述加密密码替换 /etc/isocut/anaconda-ks.cfg 中的 pwd 字段，如下所示（请用实际内容替换 *** ）：

   ``` shell script
   rootpw --iscrypted ***
   ```

###### 配置 grub2 初始密码

/etc/isocut/anaconda-ks.cfg 文件中添加以下配置，配置 grub2 初始密码。其中 ${pwd} 需要替换成用户实际的加密密文：

```shell
%addon com_huawei_grub_safe --iscrypted --password='${pwd}'
%end
```

> [!NOTE]说明
>
> - 配置 grub 初始密码需要使用 root 权限。
> - grub 密码对应的默认用户为 root。
> - 系统中需有 grub2-set-password 命令，若不存在，请提前安装该命令。

1. 执行如下命令，根据提示设置 grub2 密码：

   ```shell
   $ sudo grub2-set-password -o ./
   Enter password: 
   Confirm password: 
   grep: .//grub.cfg: No such file or directory
   WARNING: The current configuration lacks password support!
   Update your configuration with grub2-mkconfig to support this feature.
   ```

2. 命令执行完成后，会在当前目录生成 user.cfg 文件，grub.pbkdf2.sha512 开头的内容即 grub2 加密密码。

   ```shell
   $ sudo cat user.cfg 
   GRUB2_PASSWORD=grub.pbkdf2.sha512.***
   ```

3. 复制上述密文，并在 /etc/isocut/anaconda-ks.cfg 文件中增加如下配置：

   ```shell
   %addon com_huawei_grub_safe --iscrypted --password='grub.pbkdf2.sha512.***'
   %end
   ```

##### 配置 %packages 字段

如果需要添加额外 RPM 包，并使用 kickstart 自动安装，需要在 /etc/isocut/rpmlist 和 kickstart 文件的 %packages 字段都指定该 RPM 包。

此处介绍在 /etc/isocut/anaconda-ks.cfg 文件中添加 RPM 包。

/etc/isocut/anaconda-ks.cfg 文件的 %packages 默认配置如下：

```shell
%packages --multilib --ignoremissing
acl.aarch64
aide.aarch64
......
NetworkManager.aarch64
%end
```

将额外指定的 RPM 软件包添加到 %packages 配置中，需要遵循如下配置格式：

`软件包名.对应架构`，例如：kernel.aarch64

```shell
%packages --multilib --ignoremissing
acl.aarch64
aide.aarch64
......
NetworkManager.aarch64
kernel.aarch64
%end
```

### 操作指导

> [!NOTE]说明    
> 请不要修改或删除 /etc/isocut/rpmlist 文件中的默认配置项。   
> isocut 的所有操作需要使用 root 权限。    
> 待裁剪的源镜像可以为基础镜像，也可以是 everything 版镜像，例子中以基础版镜像 openEuler-20.   03-LTS-SP3-aarch64-dvd.iso 为例。      
> 例子中假设新生成的镜像名称为 new.iso，且存放在 /home/result 路径；运行工具的临时目录为 /home/temp；额外的 RPM 软件包存放在 /home/rpms 目录。     

1. 修改配置文件 /etc/isocut/rpmlist，指定用户需要安装的 RPM 软件包（来自原有 ISO 镜像）。

   ``` shell script
    sudo vi /etc/isocut/rpmlist
   ```

2. 确定运行镜像裁剪定制工具的临时目录空间大于 8 GB 。默认临时目录为 /tmp，也可以使用 -t 参数指定其他目录作为临时目录，该目录必须为绝对路径。本例中使用目录 /home/temp，由如下回显可知 /home 目录可用磁盘为 38 GB，满足要求。

   ```shell
    $ df -h
    Filesystem                            Size  Used Avail Use% Mounted on
    devtmpfs                              1.2G     0  1.2G   0% /dev
    tmpfs                                 1.5G     0  1.5G   0% /dev/shm
    tmpfs                                 1.5G   23M  1.5G   2% /run
    tmpfs                                 1.5G     0  1.5G   0% /sys/fs/cgroup
    /dev/mapper/openeuler_openeuler-root   69G  2.8G   63G   5% /
    /dev/sda2                             976M  114M  796M  13% /boot
    /dev/mapper/openeuler_openeuler-home   61G   21G   38G  35% /home
   ```

3. 执行裁剪定制。

    **场景一**：新镜像的所有 RPM 包来自原有 ISO 镜像

    ``` shell script
    $ sudo isocut -t /home/temp /home/isocut_iso/openEuler-20.03-LTS-SP3-aarch64-dvd.iso /home/result/new.iso
      Checking input ...
      Checking user ...
      Checking necessary tools ...
      Initing workspace ...
      Copying basic part of iso image ...
      Downloading rpms ...
      Finish create yum conf
      finished
      Regenerating repodata ...
      Checking rpm deps ...
      Getting the description of iso image ...
      Remaking iso ...
      Adding checksum for iso ...
      Adding sha256sum for iso ...
      ISO cutout succeeded, enjoy your new image "/home/result/new.iso"
      isocut.lock unlocked ...
    ```

    回显如上，说明新镜像 new.iso 定制成功。

    **场景二**：新镜像的 RPM 包除来自原有 ISO 镜像，还包含来自 /home/rpms 的额外软件包

    ```shell
    sudo isocut -t /home/temp -r /home/rpms /home/isocut_iso/openEuler-20.03-LTS-SP3-aarch64-dvd.iso /home/result/new.iso
    ```

    **场景三**：使用 kickstart 文件实现自动化安装，需要修改 /etc/isocut/anaconda-ks.cfg 文件

    ```shell
    sudo isocut -t /home/temp -k /etc/isocut/anaconda-ks.cfg /home/isocut_iso/openEuler-20.03-LTS-SP3-aarch64-dvd.iso /home/result/new.iso
    ```
