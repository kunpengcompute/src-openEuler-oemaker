%ifarch aarch64
%global efi_aa64 1
%endif

%ifarch x86_64
%global efi_x64 1
%endif

%ifarch loongarch64
%global efi_loongarch64 1
%endif

Name:           oemaker
Summary:        a building tool for DVD ISO making and ISO cutting
License:        Mulan PSL v2
Group:          System/Management
Version:        3.3.0
Release:        38
BuildRoot:      %{_tmppath}/%{name}

Source:         https://gitee.com/openeuler/oemaker/repository/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        normal_aarch64.xml
Source2:        normal_x86_64.xml
Source3:        rpmlist.xml
Source4:        edge_normal_aarch64.xml
Source5:        edge_normal_x86_64.xml
Source6:        desktop_normal_aarch64.xml
Source7:        desktop_normal_x86_64.xml
Source8:        rpmlist_riscv64.xml
Source9:        normal_riscv64.xml
Source10:	normal_loongarch64.xml
Source11:	rpmlist_loongarch64.xml
Source12:	desktop_normal_loongarch64.xml
Source13:       devstation_aarch64_rpmlist
Source14:       devstation_x86_64_rpmlist
Source15:       edge_normal_riscv64.xml

Requires:       createrepo dnf-plugins-core genisoimage isomd5sum grep bash libselinux-utils libxml2 anaconda libselinux-utils
Requires:       lorax >= 19.6.78-1
%ifarch loongarch64
Requires:       xorriso
%endif

# Patch here
Patch0001:      0001-bugfix-IABY7K.patch
Patch0002:      0001-fix-livecd-grub2-efi.cfg-not-found.patch
Patch0003:      0001-Fixes-boot-failure-caused-by-invalid-volume-IDs.patch
Patch0004:      0002-delete-package-xorg-x11-server-utils.patch
Patch0005:      backport-Compatible-with-single-line-no-newline-configuration.patch
Patch0006:      0001-replace-calamares-with-heolleo-tool.patch
Patch0007:      delete-package-avahi-libs.patch
Patch0008:      0001-set-root-passwd.patch
Patch0009:      0001-add-rich-dependency-closure-check-and-auto-download.patch
Patch0010:      0001-reset-the-path-of-yum.repos.d-for-oemaker.patch

%description
a building tool for DVD ISO making and ISO cutting

%package -n isocut
Summary: a building tool for ISO cutting
Requires: yum dnf-utils createrepo file util-linux genisoimage isomd5sum grep bash libselinux-utils libxml2
BuildRequires: bash

%description -n isocut
a building tool for ISO cutting

%package -n envmaker
Summary: a building tool for compile_env making
Requires: yum dnf-utils createrepo file util-linux genisoimage isomd5sum grep bash libselinux-utils libxml2 pigz
BuildRequires: bash

%description -n envmaker
a building tool for compile_env making

%prep
%setup -c
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/aarch64/normal.xml
cp %{SOURCE1} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/aarch64/normal.xml
rm -rf  %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/x86_64/normal.xml
cp %{SOURCE2} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/x86_64/normal.xml
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/loongarch64/normal.xml
cp %{SOURCE10} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/loongarch64/normal.xml
%ifarch loongarch64
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/rpmlist.xml
cp %{SOURCE11} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/rpmlist.xml
%else
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/rpmlist.xml
cp %{SOURCE3} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/rpmlist.xml
%endif
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/aarch64/edge_normal.xml
cp %{SOURCE4} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/aarch64/edge_normal.xml
rm -rf  %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/x86_64/edge_normal.xml
cp %{SOURCE5} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/x86_64/edge_normal.xml
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/aarch64/desktop_normal.xml
cp %{SOURCE6} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/aarch64/desktop_normal.xml
rm -rf  %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/x86_64/desktop_normal.xml
cp %{SOURCE7} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/x86_64/desktop_normal.xml
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/loongarch64/desktop_normal.xml
cp %{SOURCE12} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/loongarch64/desktop_normal.xml
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/aarch64/livecd/devstation_rpmlist
cp %{SOURCE13} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/aarch64/livecd/devstation_rpmlist
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/x86_64/livecd/devstation_rpmlist
cp %{SOURCE14} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/x86_64/livecd/devstation_rpmlist
cd %{_builddir}/%{name}-%{version}/%{name}
%autopatch -p1
%ifarch riscv64
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/rpmlist.xml
cp %{SOURCE8} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/rpmlist.xml
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/riscv64/normal.xml
cp %{SOURCE9} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/riscv64/normal.xml
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/riscv64/edge_normal.xml
cp %{SOURCE15} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/riscv64/edge_normal.xml
%endif


%install
sys_arch=$(uname -m)
mkdir -p %{buildroot}/opt/
mkdir -p %{buildroot}/opt/oemaker
mkdir -p %{buildroot}/opt/oemaker/config
mkdir -p %{buildroot}/opt/oemaker/config/${sys_arch}
mkdir -p %{buildroot}/opt/oemaker/config/${sys_arch}/livecd/live/config_files/${sys_arch}
mkdir -p %{buildroot}/opt/oemaker/config/${sys_arch}/livecd/devstation_live/config_files/${sys_arch}
mkdir -p %{buildroot}/opt/oemaker/config/common
mkdir -p %{buildroot}/opt/oemaker/config/common/livecd/live
mkdir -p %{buildroot}/opt/oemaker/docs
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/isocut
chmod 750 %{buildroot}/%{_sysconfdir}/isocut

install -m 700 %{name}/isomaker/oemaker.sh %{buildroot}/opt/oemaker/oemaker.sh
install -m 700 %{name}/isomaker/oemaker.sh %{buildroot}/%{_bindir}/oemaker
install -m 700 %{name}/isomaker/make_debug.sh %{buildroot}/opt/oemaker/make_debug.sh
install -m 700 %{name}/isomaker/img_repo.sh %{buildroot}/opt/oemaker/img_repo.sh
install -m 700 %{name}/isomaker/init.sh %{buildroot}/opt/oemaker/init.sh
install -m 700 %{name}/isomaker/iso.sh %{buildroot}/opt/oemaker/iso.sh
install -m 700 %{name}/isomaker/rpm.sh %{buildroot}/opt/oemaker/rpm.sh
install -m 700 %{name}/isomaker/env_record.sh %{buildroot}/opt/oemaker/env_record.sh
install -m 700 %{name}/isomaker/env_restore.sh %{buildroot}/opt/oemaker/env_restore.sh
install -m 400 %{name}/isomaker/config/rpmlist.xml %{buildroot}/opt/oemaker/config/rpmlist.xml
install -m 640 %{name}/isomaker/config/${sys_arch}/livecd/live/config_files/${sys_arch}/* %{buildroot}/opt/oemaker/config/${sys_arch}/livecd/live/config_files/${sys_arch}/
install -m 640 %{name}/isomaker/config/${sys_arch}/livecd/devstation_live/config_files/${sys_arch}/* %{buildroot}/opt/oemaker/config/${sys_arch}/livecd/devstation_live/config_files/${sys_arch}/
install -m 400 %{name}/isomaker/config/${sys_arch}/livecd/livecd_${sys_arch}.ks %{buildroot}/opt/oemaker/config/${sys_arch}/livecd/livecd_${sys_arch}.ks
install -m 400 %{name}/isomaker/config/${sys_arch}/livecd/devstation_livecd_${sys_arch}.ks %{buildroot}/opt/oemaker/config/${sys_arch}/livecd/devstation_livecd_${sys_arch}.ks
install -m 600 %{name}/isomaker/config/${sys_arch}/livecd/rpmlist %{buildroot}/opt/oemaker/config/${sys_arch}/livecd/rpmlist
install -m 600 %{name}/isomaker/config/${sys_arch}/livecd/devstation_rpmlist %{buildroot}/opt/oemaker/config/${sys_arch}/livecd/devstation_rpmlist
install -m 400 %{name}/isomaker/config/${sys_arch}/desktop_normal.xml %{buildroot}/opt/oemaker/config/${sys_arch}/desktop_normal.xml
install -m 400 %{name}/isomaker/config/${sys_arch}/edge_normal.xml %{buildroot}/opt/oemaker/config/${sys_arch}/edge_normal.xml
install -m 400 %{name}/isomaker/config/${sys_arch}/normal.xml %{buildroot}/opt/oemaker/config/${sys_arch}/normal.xml
install -m 400 %{name}/isomaker/config/${sys_arch}/standard.conf %{buildroot}/opt/oemaker/config/${sys_arch}/standard.conf
%ifarch x86_64
install -m 700 %{name}/isomaker/config/x86_64/livecd/live/x86.tmpl %{buildroot}/opt/oemaker/config/x86_64/livecd/live/x86.tmpl
install -m 700 %{name}/isomaker/config/x86_64/livecd/devstation_live/x86.tmpl %{buildroot}/opt/oemaker/config/x86_64/livecd/devstation_live/x86.tmpl
install -m 400 %{name}/isomaker/config/x86_64/ks.cfg %{buildroot}/opt/oemaker/config/x86_64/ks.cfg
%endif
%ifarch aarch64
install -m 700 %{name}/isomaker/config/aarch64/livecd/live/aarch64.tmpl %{buildroot}/opt/oemaker/config/aarch64/livecd/live/aarch64.tmpl
install -m 700 %{name}/isomaker/config/aarch64/livecd/devstation_live/aarch64.tmpl %{buildroot}/opt/oemaker/config/aarch64/livecd/devstation_live/aarch64.tmpl
%endif
%ifarch riscv64
install -m 700 %{name}/isomaker/config/riscv64/livecd/live/riscv64.tmpl %{buildroot}/opt/oemaker/config/riscv64/livecd/live/riscv64.tmpl
%endif
%ifarch loongarch64
install -m 700 %{name}/isomaker/config/loongarch64/livecd/live/loongarch64.tmpl %{buildroot}/opt/oemaker/config/loongarch64/livecd/live/loongarch64.tmpl
install -m 400 %{name}/isomaker/config/loongarch64/ks.cfg %{buildroot}/opt/oemaker/config/loongarch64/ks.cfg
%endif
%ifarch riscv64
install -m 700 %{name}/isomaker/config/riscv64/livecd/live/riscv64.tmpl %{buildroot}/opt/oemaker/config/riscv64/livecd/live/riscv64.tmpl
%endif
%ifarch loongarch64
install -m 700 %{name}/isomaker/config/loongarch64/livecd/live/loongarch64.tmpl %{buildroot}/opt/oemaker/config/loongarch64/livecd/live/loongarch64.tmpl
install -m 400 %{name}/isomaker/config/loongarch64/ks.cfg %{buildroot}/opt/oemaker/config/loongarch64/ks.cfg
%endif
install -m 700 %{name}/isomaker/config/common/livecd/live/* %{buildroot}/opt/oemaker/config/common/livecd/live/
install -m 700 %{name}/isomaker/config/common/livecd/live/* %{buildroot}/opt/oemaker/config/${sys_arch}/livecd/devstation_live/
install -m 400 %{name}/isomaker/config/common/livecd/root_pwd %{buildroot}/opt/oemaker/config/common/livecd/root_pwd
install -m 700 %{name}/isomaker/docs/* %{buildroot}/opt/oemaker/docs/
cp -ar %{name}/isomaker/80-openeuler %{buildroot}/opt/oemaker/

cp -ar %{buildroot}/opt/oemaker/config/common/* %{buildroot}/opt/oemaker/config/${sys_arch}/


install -m 550 %{name}/isocut/isocut.py %{buildroot}/%{_bindir}/isocut
install -m 600 %{name}/isocut/config/repodata.template %{buildroot}/%{_sysconfdir}/isocut/


install -m 600 %{name}/isocut/config/${sys_arch}/rpmlist %{buildroot}/%{_sysconfdir}/isocut/
install -m 600 %{name}/isocut/config/${sys_arch}/anaconda-ks.cfg %{buildroot}/%{_sysconfdir}/isocut/


mkdir -p %{buildroot}/opt/envmaker
mkdir -p %{buildroot}/opt/envmaker/config
mkdir -p %{buildroot}/opt/envmaker/config/${sys_arch}
mkdir -p %{buildroot}/opt/envmaker/utils

install -m 700 %{name}/envmaker/envmaker.sh %{buildroot}/opt/envmaker/envmaker.sh
install -m 700 %{name}/envmaker/utils/chroot.sh %{buildroot}/opt/envmaker/utils/chroot.sh
install -m 700 %{name}/envmaker/utils/common_fun.sh %{buildroot}/opt/envmaker/utils/common_fun.sh
install -m 700 %{name}/envmaker/utils/parse_rpmlist_xml.sh %{buildroot}/opt/envmaker/utils/parse_rpmlist_xml.sh
install -m 600 %{name}/envmaker/config/${sys_arch}/openEuler_repo.conf %{buildroot}/opt/envmaker/config/${sys_arch}/openEuler_repo.conf
install -m 600 %{name}/envmaker/config/compile_env_rpmlist.xml %{buildroot}/opt/envmaker/config/compile_env_rpmlist.xml

%postun -n isocut
if [ "$1" = "0" ]; then
  rm -rf %{_sysconfdir}/isocut/*
fi

%files
%defattr(-,root,root)
%dir /opt
%dir /opt/oemaker
/opt/oemaker/*
%{_bindir}/oemaker

%files -n isocut
%defattr(-,root,root)
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/isocut/repodata.template
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/isocut/rpmlist
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/isocut/anaconda-ks.cfg
%{_bindir}/isocut
%dir %{_sysconfdir}/isocut
%{_sysconfdir}/isocut/*

%files -n envmaker
%defattr(-,root,root)
%dir /opt
%dir /opt/envmaker
/opt/envmaker/*

%clean
rm -rf $RPM_BUILD_ROOT/*
rm -rf %{buildroot}
rm -rf $RPM_BUILD_DIR/%{name}

%changelog
* Fri Aug 28 2026 xujingmin <xujingmin@iscas.ac.cn> - 3.3.0-38
- add liteview to devstation

* Wed Aug 19 2026 maolintao <1158944345@qq.com> - 3.3.0-37
- add polymind to devstation

* Mon Aug 10 2026 dingxudong <dingxudong1@huawei.com> - 3.3.0-36
- reset the path of yum.repos.d for oemaker

* Sat Aug 08 2026 dingxudong <dingxudong1@huawei.com> - 3.3.0-35
- add rich dependency closure check and auto-download 

* Fri Aug 07 2026 lingsheng <ultra_planet@qq.com> - 3.3.0-34
- add cockpit sub packages in rpmlist

* Tue Aug 04 2026 Funda Wang <fundawang@yeah.net> - 3.3.0-33
- google noto sans symbols2 has been renamed

* Tue Aug 04 2026 Liu Wang <1823363429@qq.com> - 3.3.0-32
- remove kernel-extra-modules euler-copilot from devstation

* Wed Jul 29 2026 Liu Wang <1823363429@qq.com> - 3.3.0-31
- set root user passwd; remove polymind from devstation

* Sat Jul 25 2026 yangchaohao <yangchaohao@huawei.com> - 3.3.0-30
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:remove clutter-gst3 and related software packages

* Sat Jul 11 2026 Funda Wang <fundawang@yeah.net> - 3.3.0-29
- drop telepathy*, they are dead for years

* Fri Jul 10 2026 xinghe <xingheyd@163.com> - 3.3.0-28
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:remove avahi-libs packages

* Tue May 26 2026 zhaoyonghao <zhaoyonghao10@h-partners.com> - 3.3.0-27
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:add kernel-64k and related software packages to edge_aarch64

* Wed May 6 2026 zhaoyonghao <zhaoyonghao10@h-partners.com> - 3.3.0-26
- Type:requirement
- CVE:NA
- SUG:NA
- DESC:add kernel-64k and related software packages to aarch64
       remove kernel-64k-headers for aarch64

* Sun Apr 19 2026 Funda Wang <fundawang@yeah.net> - 3.3.0-25
- ID:NA
- SUG:NA
- DESC: remove orc-help, it is not buildable due to missing hotdoc
- DESC: remove cups-pk-helper, it has been moved into epol
- DESC: remove libsoup-devel, it has been moved into epol

* Wed Apr 01 2026 xinghe <xingheyd@163.com> - 3.3.0-24
- ID:NA
- SUG:NA
- DESC: remove bind-dyndb-ldap packages

* Sat Dec 13 2025 xiexiunian <xiexiunian@h-partners.com> - 3.3.0-23
- ID:NA 
- SUG:NA
- DESC: remove firefox and gjs from baseos

* Fri Dec 12 2025 wangmian <wangmian19@h-partners.com> - 3.3.0-22
- ID:NA 
- SUG:NA
- DESC: use python3-file-magic instead of python3-magic

* Tue Dec 09 2025 Liu Wang <1823363429@qq.com> - 3.3.0-21
- ID:NA
- SUG:NA
- DESC: add polymind to DevStation
        DevStation Installer: Replace calamares with heolleo tool

* Tue Oct 21 2025 Funda Wang <fundawang@yeah.net> - 3.3.0-20
- ID:NA
- SUG:NA
- DESC: deprecate libsexy, it was dead upstream

* Thu Oct 9 2025 yixiangzhike <yixiangzhike007@163.com> - 3.3.0-19
- ID:NA
- SUG:NA
- DESC: compatible with single-line no-newline configuration

* Wed Sep 24 2025 Li Ping <1477412247@qq.com> - 3.3.0-18
- ID:NA
- SUG:NA
- DESC: add tigervnc-selinux and mysql-selinux

* Wed Sep 17 2025 Liu Wang <1823363429@qq.com> - 3.3.0-17
- ID:NA
- SUG:NA
- DESC: add tigervnc-server

* Thu Sep 11 2025 Liu Wang <1823363429@qq.com> - 3.3.0-16
- ID:NA
- SUG:NA
- DESC: delete desktop-pet xdotool libxdo libxdo-tool

* Sat Aug 30 2025 Liu Wang <1823363429@qq.com> - 3.3.0-15
- ID:NA
- SUG:NA
- DESC: add grub2-efi-aa64/x64 dev-store software

* Mon Aug 04 2025 Liu Wang <1823363429@qq.com> - 3.3.0-14
- ID:NA
- SUG:NA
- DESC: add tigervnc software

* Sat Jul 19 2025 Funda Wang <fundawang@yeah.net> - 3.3.0-13
- ID:NA
- SUG:NA
- DESC: authselect-compat has been removed upstream

* Mon Jul 07 2025 wangchong <wangchong56@huawei.com> - 3.3.0-12
- ID:NA
- SUG:NA
- DESC: delete package xorg-x11-server-utils

* Wed Jun 04 2025 Shi Hongyu <shywzt@iCloud.com> - 3.3.0-11
- ID:NA
- SUG:NA
- DESC: replace euler-copilot-web with euler-copilot-desktop

* Mon May 26 2025 Liu Wang <1823363429@qq.com> - 3.3.0-10
- ID:NA
- SUG:NA
- DESC: add euler-copilot-web server

* Wed May 07 2025 Liu Wang <1823363429@qq.com> - 3.3.0-9
- ID:NA
- SUG:NA
- DESC: add nodejs-packaging dependency

* Mon Apr 28 2025 Liu Wang <1823363429@qq.com> - 3.3.0-8
- ID:NA
- SUG:NA
- DESC: delete code software

* Fri Apr 18 2025 Liu Wang <1823363429@qq.com> - 3.3.0-7
- ID:NA
- SUG:NA
- DESC: sync openEuler-24.03-LTS-SP2 branch to master

* Tue Apr 15 2025 Liu Wang <1823363429@qq.com> - 3.3.0-6
- ID:NA
- SUG:NA
- DESC: sync 25.03 modify to master branch and add roo-code, uv, python3-mcp packages

* Sat Mar 22 2025 Funda Wang <fundawang@yeah.net> - 3.3.0-5
- ID:NA
- SUG:NA
- DESC: logrotate-help was merged into logrotate

* Fri Mar 14 2025 wangchong <wangchong56@huawei.com> - 3.3.0-4
- ID:NA
- SUG:NA
- DESC: add kernel-rt, raspberrypi-kernel, raspberrypi-kernel-rt, haoc-kernel, vk-kernel and kernel-extra-modules to the exclude tag

* Mon Mar 3 2025 hugel <gengqihu2@h-partners.com> - 3.3.0-3
- ID:NA
- SUG:NA
- DESC: Fix boot failure caused by invalid volume IDs

* Thu Jan 23 2025 Funda Wang <fundawang@yeah.net> - 3.3.0-2
- ID:NA
- SUG:NA
- DESC: tpm2-tools-help was merged into tpm2-tools as of Oct 2024
- DESC: attr-help was merged into attr as of Dec 2024
- DESC: xorg-x11-utils was retired as of Dec 2024

* Thu Jan 23 2025 Li Ping <1477412247@qq.com> - 3.3.0-1
- ID:NA
- SUG:NA
- DESC: add new iso_type devstation devstation_netinst support for oemaker and update to 3.3.0

* Mon Dec 30 2024 Wenlong Zhang <zhangwenlong@loongson.cn> - 3.2.0-11
- ID:NA
- SUG:NA
- DESC: add rpmlist.xml normal.xml for loongarch64
	enable efi boot for loongarch64

* Tue Dec 24 2024 Ouuleilei <wangliu@iscas.ac.cn> - 3.2.0-10
- fix riscv64 livecd grub2-efi.cfg not found 

* Fri Dec 20 2024 wangchong <wangchong56@huawei.com> - 3.2.0-9
- ID:NA
- SUG:NA
- DESC: add kernel-rt, raspberrypi-kernel, raspberrypi-kernel-rt and haoc-kernel to the exclude tag

* Fri Dec 6 2024 yangchaohao <yangchaohao@huawei.com> - 3.2.0-8
- ID:NA
- SUG:NA
- DESC: edge_ISO change kubeedge to k3s

* Thu Dec 5 2024 zhaolichang <zhaolichang@huawei.com> - 3.2.0-7
- ID:NA
- SUG:NA
- DESC: delete libkperf in rpmlist.xml

* Wed Dec 4 2024 zhaolichang <zhaolichang@huawei.com> - 3.2.0-6
- ID:NA
- SUG:NA
- DESC: delete libkperf and oeAware-manager in minimal install

* Tue Dec 3 2024 sunsuwan <sunsuwan3@huawei.com> - 3.2.0-5
- ID:NA
- SUG:NA
- DESC: use xtables-nft instead of xtables-legacy for high performance

* Tue Dec 3 2024 zhaolichang <zhaolichang@huawei.com> - 3.2.0-4
- ID:NA
- SUG:NA
- DESC: add libkperf and oeAware-manager

* Wed Sep 18 2024 xiangyuning <xiangyuning@huawei.com> - 3.2.0-3
- ID:NA
- SUG:NA
- DESC: enable encrypt need install systemd-cryptsetup package

* Mon Sep 23 2024 Ouuleilei <wangliu@iscas.ac.cn> - 3.2.0-2
- fix riscv64.tmpl file miss problem and add riscv64 rpmlist.xml normal.xml

* Wed Sep 18 2024 xiangyuning <xiangyuning@huawei.com> - 3.2.0-1
- ID:NA
- SUG:NA
- upgrade to 3.2.0

* Wed Jul 10 2024 wangchong <wangchong56@huawei.com> - 3.1.0-8
- ID:NA
- SUG:NA
- DESC: fix issue IABY7K

* Thu Mar 28 2024 mayunlong <mayunlong6@huawei.com> - 3.1.0-7
- ID:NA
- SUG:NA
- DESC: delete libvirt package

* Wed Mar 20 2024 sunhai <sunhai10@huawei.com> - 3.1.0-6
- ID:NA
- SUG:NA
- DESC: delete initial-setup-gui

* Tue Mar 19 2024 sunhai <sunhai10@huawei.com> - 3.1.0-5
- ID:NA
- SUG:NA
- DESC: delete gnome group packages

* Sun Feb 4 2024 wangchong <wangchong56@huawei.com> - 3.1.0-4
- ID:NA
- SUG:NA
- DESC: delete tracker tracker-help tracker-miners tracker-miners-help from rpmlist

* Tue Jan 9 2024 wangchong <wangchong56@huawei.com> - 3.1.0-3
- ID:NA
- SUG:NA
- DESC: delete lld lld-devel lld-libs from rpmlist

* Fri Dec 8 2023 xiasenlin <xiasenlin1@huawei.com> - 3.1.0-2
- ID:NA
- SUG:NA
- DESC: delete telepathy-glib-help from rpmlist for PR:https://gitee.com/src-openeuler/telepathy-glib/pulls/3

* Mon Nov 20 2023 chenhuihan <chenhuihan@huawei.com> - 3.1.0-1
- ID:NA
- SUG:NA
- DESC: support for livecd and isocut optimize

* Mon Nov 20 2023 zhongjiawei <zhongjiawei1@huawei.com> - 3.0.4-6
- ID:NA
- SUG:NA
- DESC: update rpmlist.xml docker-runc package name tobe runc

* Tue Sep 19 2023 liyunfei <liyunfei33@huawei.com> - 3.0.4-5
- ID:NA
- SUG:NA
- DESC: Add clang-15, llvm-15 and lld-15 packages.

* Mon Sep 4 2023 luhuaxin <luhuaxin1@huawei.com> - 3.0.4-4
- ID:NA
- SUG:NA
- DESC: Add dim_tools and dim package.

* Thu Aug 31 2023 fangchuangchuang <fangchuangchuang@huawei.com> - 3.0.4-3
- ID:NA
- SUG:NA
- DESC: Add libgmem package.

* Sat Aug 26 2023 wangchong <wangchong56@huawei.com> - 3.0.4-2
- ID:NA
- SUG:NA
- DESC: fix edge start error

* Wed Aug 23 2023 xiangyuning <xiangyuning@huawei.com> - 3.0.4-1
- ID:NA
- SUG:NA
- DESC: upgrade to 3.0.4

* Thu Aug 07 2023 sunhai <sunhai10@huawei.com> - 3.0.2-4
- ID:NA
- SUG:NA
- DESC: add pre version patches

* Mon Jul 31 2023 liuyang <liuyang645@huawei.com> - 3.0.2-3
- ID:NA
- SUG:NA
- DESC: update kae rpm

* Sat Jun 10 2023 zhaotianyang <zhaotianyang4@huawei.com> - 3.0.2-2
- ID:NA
- SUG:NA
- DESC: fix wrong spelling of summary in spec file

* Tue May 23 2023 chenhuihan <chenhuihan@huawei.com> - 3.0.2-1
- ID:NA
- SUG:NA
- DESC: fix isocut

* Mon May 22 2023 chenhuihan <chenhuihan@huawei.com> - 3.0.1-1
- ID:NA
- SUG:NA
- DESC: fix isocut

* Fri May 19 2023 chenhuihan <chenhuihan@huawei.com> - 3.0.0-1
- ID:NA
- SUG:NA
- DESC: update for file-level replacement

* Thu May 18 2023 chenhuihan <chenhuihan@huawei.com> - 2.0.5-2
- ID:NA
- SUG:NA
- DESC: fix chroot

* Wed May 17 2023 chenhuihan <chenhuihan@huawei.com> - 2.0.5-1
- ID:NA
- SUG:NA
- DESC: support envmaker

* Tue Feb 21 2023 wangchong <wangchong56@huawei.com> - 2.0.4-9
- ID:NA
- SUG:NA
- DESC:fix bug I6G246

* Fri Feb 17 2023 wangchong <wangchong56@huawei.com> - 2.0.4-8
- ID:NA
- SUG:NA
- DESC:delete recycle package authz and iSulad-img

* Fri Feb 10 2023 wangzhiqiang <wangzhiqiang95@huawei.com> - 2.0.4-7
- ID:NA
- SUG:NA
- DESC:delete package cryptsetup-reencrypt

* Tue Dec 27 2022 penghaitao <htpengc@isoftstone.com> - 2.0.4-6
- ID:NA
- SUG:NA
- DESC: Remove invalid memtest

* Mon Dec 26 2022 sunhai <sunhai10@huawei.com> - 2.0.4-5
- ID:NA
- SUG:NA
- DESC: change rescue parameter with legacy too
        Enable eject in install.img

* Thu Dec 15 2022 wangkai <wangkai385@h-partners.com> - 2.0.4-3
- ID:NA
- SUG:NA
- DESC: Remove package openEuler-performance

* Tue Nov 29 2022 sunhai <sunhai10@huawei.com> - 2.0.4-2
- ID:NA
- SUG:NA
- DESC: change rescue parameter with new anaconda

* Tue Nov 22 2022 xiangyuning <xiangyuning@huawei.com> - 2.0.4-1
- ID:NA
- SUG:NA
- DESC: upgrade to 2.0.4

* Mon Aug 15 2022 gaoruoshu <gaoruoshu@huawei.com> - 2.0.3-18
- ID:NA
- SUG:NA
- DESC: add atune-engine rpm to rpmlist.xml

* Fri Jul 29 2022 wangchong <wangchong56@huawei.com> - 2.0.3-17
- ID:NA
- SUG:NA
- DESC: support Desktop iso

* Fri Jul 15 2022 caodongxia <caodongxia@h-partners.com> - 2.0.3-16
- ID:NA
- SUG:NA
- DESC: clean up dconf-editor and gnome-*

* Thu Jul 14 2022 wangchong <wangchong56@huawei.com> - 2.0.3-15
- ID:NA
- SUG:NA
- DESC: do not clean up libdiff and libcairo-script* 

* Wed Apr 20 2022 xiangyuning <xiangyuning@huawei.com> - 2.0.3-14
- ID:NA
- SUG:NA
- DESC: restore the automated kickstart function

* Thu Mar 31 2022 zhouwenpei <zhouwenpei1@h-partners.com> - 2.0.3-13
- ID:NA
- SUG:NA
- DESC: add linux-firmware subpackage

* Mon Mar 28 2022 Senlin <xiasenlin1@huawei.com> - 2.0.3-12
- ID:NA
- SUG:NA
- DESC: add exclude list for everything

* Mon Mar 7 2022 xiangyuning <xiangyuning@huawei.com> - 2.0.3-11
- ID:NA
- SUG:NA
- DESC: modify restore env mode

* Fri Mar 4 2022 xiangyuning <xiangyuning@huawei.com> - 2.0.3-10
- ID:NA
- SUG:NA
- DESC: lorax cmd add printed log

* Fri Mar 4 2022 xiangyuning <xiangyuning@huawei.com> - 2.0.3-9
- ID:NA
- SUG:NA
- DESC: fix build oemaker failed issue

* Wed Mar 2 2022 xiangyuning <xiangyuning@huawei.com> - 2.0.3-8
- ID:NA
- SUG:NA
- DESC: restore env after selinux status changes 

* Wed Feb 23 2022 zhuyuncheng <zhuyuncheng@huawei.com> - 2.0.3-7
- ID:NA
- SUG:NA
- DESC: add Server install mode and packages for edge computing iso

* Wed Feb 23 2022 hanhui <hanhui15@h-partners.com> - 2.0.3-6
- DESC: delete gamin and openjpeg
        add rsyslog-gnutls and edk2-ovmf packages
        rename hisi_rde to hisi_trng_v2,libkae to uadk_engine

* Tue Feb 22 2022 jiangheng <jiangheng12@huawei.com> - 2.0.3-5
- ID:NA
- SUG:NA
- DESC: delete nscd package

* Mon Feb 14 2022 wangchong <952173335@qq.com> - 2.0.3-4
- ID:NA
- SUG:NA
- DESC: upgrade to 2.0.3 and support usb flash drive mode and delete some packages

* Fri Jan 21 2022 zhang_xubo <2578876417@qq.com> - 2.0.0-13
- ID:NA
- SUG:NA
- DESC: add opengauss server pakcage

* Thu Jan 20 2022 yaokai13 <yaokai13@huawei.com> - 2.0.0-12
- ID:NA
- SUG:NA
- DESC: delete decay package

* Thu Oct 14 2021 miao_kaibo <miaokaibo@outlook.com> - 2.0.0-11
- ID:NA
- SUG:NA
- DESC: bugfix I3OGUT

* Tue Sep 28 2021 miao_kaibo <miaokaibo@outlook.com> - 2.0.0-10
- ID:NA
- SUG:NA
- DESC: change for edge computing iso

* Thu Aug 26 2021 miao_kaibo <miaokaibo@outlook.com> - 2.0.0-9
- ID:NA
- SUG:NA
- DESC: change exclude list

* Tue Aug 17 2021 miao_kaibo <miaokaibo@outlook.com> - 2.0.0-8
- ID:NA
- SUG:NA
- DESC: delete decay package

* Thu Jul 15 2021 miao_kaibo <miaokaibo@outlook.com> - 2.0.0-7
- ID:NA
- SUG:NA
- DESC: replace gvfs-fuse by gvfs-fuse3

* Wed May 12 2021 miao_kaibo <miaokaibo@outlook.com> - 2.0.0-6
- ID:NA
- SUG:NA
- DESC: bugfix I3QY98

* Wed Apr 7 2021 miao_kaibo <miaokaibo@outlook.com> - 2.0.0-5
- ID:NA
- SUG:NA
- DESC: change for issue I3DJJW

* Fri Apr 2 2021 miao_kaibo <miaokaibo@outlook.com> - 2.0.0-4
- ID:NA
- SUG:NA
- DESC: rename source iso

* Thu Mar 25 2021 xinghe <xinghe1@huawei.com> - 2.0.0-3
- ID:NA
- SUG:NA
- DESC: remove atlas

* Sun Mar 21 2021 miao_kaibo <miaokaibo@outlook.com> - 2.0.0-2
- ID:NA
- SUG:NA
- DESC: replace rsyslog-gnutls by rsyslog

* Fri Mar 19 2021 zhuchunyi <zhuchunyi@huawei.com> - 2.0.0-1
- ID:NA
- SUG:NA
- DESC: upgrade version

* Wed Mar 17 2021 miao_kaibo <miaokaibo@outlook.com> - 1.1.2-7
- ID:NA
- SUG:NA
- DESC: delete or replace rpms which are not exist

* Sat Mar 13 2021 miao_kaibo <miaokaibo@outlook.com> - 1.1.2-6
- ID:NA
- SUG:NA
- DESC: add exclude rpm to rpmlist 

* Sat Mar 13 2021 miao_kaibo <miaokaibo@outlook.com> - 1.1.2-5
- ID:NA
- SUG:NA
- DESC: fix bug I3B7CH 

* Wed Mar 10 2021 Chen Qun <kuhn.chenqun@huawei.com> - 1.1.2-4
- ID:NA
- SUG:NA
- DESC: add qemu-block-iscsi in virtualization-hypervisor group

* Mon Mar 08 2021 miao_kaibo <miaokaibo@outlook.com> - 1.1.2-3
- ID:NA
- SUG:NA
- DESC: change method of creating source iso

* Mon Mar 01 2021 Chen Qun <kuhn.chenqun@huawei.com> - 1.1.2-2
- ID:NA
- SUG:NA
- DESC: add stratovirt in virtualization-hypervisor group

* Thu Feb 25 2021 miao_kaibo <miaokaibo@outlook.com> - 1.1.2-1
- ID:NA
- SUG:NA
- DESC:upgrade version

* Mon Feb 08 2021 miao_kaibo <miaokaibo@outlook.com> - 1.1.1-1
- ID:NA
- SUG:NA
- DESC:upgrade version

* Thu Oct 15 2020 zhuchunyi <zhuchunyi@huawei.com> - 1.0.1-1
- ID:NA
- SUG:NA
- DESC:upgrade version

* Tue Sep 29 2020 zhuchunyi <zhuchunyi@huawei.com> - 1.0.0-2
- ID:NA
- SUG:NA
- DESC:change Source format to URL

* Sat Jul 25 2020 zhuchunyi <zhuchunyi@huawei.com> - 1.0.0-1
- ID:NA
- SUG:NA
- DESC:package init
