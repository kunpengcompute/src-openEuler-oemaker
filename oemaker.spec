%ifarch aarch64
%global efi_aa64 1
%endif

%ifarch x86_64
%global efi_x64 1
%endif

Name:           oemaker
Summary:        a building tool for DVD ISO making and ISO cutting
License:        Mulan PSL v2
Group:          System/Management
Version:        3.1.0
Release:        6
BuildRoot:      %{_tmppath}/%{name}

Source:         https://gitee.com/openeuler/oemaker/repository/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        normal_aarch64.xml
Source2:        normal_x86_64.xml
Source3:        rpmlist.xml
Source4:        edge_normal_aarch64.xml
Source5:        edge_normal_x86_64.xml
Source6:        desktop_normal_aarch64.xml
Source7:        desktop_normal_x86_64.xml

Requires:       createrepo dnf-plugins-core genisoimage isomd5sum grep bash libselinux-utils libxml2 anaconda libselinux-utils
Requires:       lorax >= 19.6.78-1

# Patch here
Patch0001:      0001-bugfix-IABY7K.patch

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
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/rpmlist.xml
cp %{SOURCE3} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/rpmlist.xml
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/aarch64/edge_normal.xml
cp %{SOURCE4} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/aarch64/edge_normal.xml
rm -rf  %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/x86_64/edge_normal.xml
cp %{SOURCE5} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/x86_64/edge_normal.xml
rm -rf %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/aarch64/desktop_normal.xml
cp %{SOURCE6} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/aarch64/desktop_normal.xml
rm -rf  %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/x86_64/desktop_normal.xml
cp %{SOURCE7} %{_builddir}/%{name}-%{version}/%{name}/isomaker/config/x86_64/desktop_normal.xml
cd %{_builddir}/%{name}-%{version}/%{name}
%autopatch -p1

%install
sys_arch=$(uname -m)
mkdir -p %{buildroot}/opt/
mkdir -p %{buildroot}/opt/oemaker
mkdir -p %{buildroot}/opt/oemaker/config
mkdir -p %{buildroot}/opt/oemaker/config/${sys_arch}
mkdir -p %{buildroot}/opt/oemaker/config/${sys_arch}/livecd/live/config_files/${sys_arch}
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
install -m 400 %{name}/isomaker/config/${sys_arch}/livecd/livecd_${sys_arch}.ks %{buildroot}/opt/oemaker/config/${sys_arch}/livecd/livecd_${sys_arch}.ks
install -m 600 %{name}/isomaker/config/${sys_arch}/livecd/rpmlist %{buildroot}/opt/oemaker/config/${sys_arch}/livecd/rpmlist
install -m 400 %{name}/isomaker/config/${sys_arch}/desktop_normal.xml %{buildroot}/opt/oemaker/config/${sys_arch}/desktop_normal.xml
install -m 400 %{name}/isomaker/config/${sys_arch}/edge_normal.xml %{buildroot}/opt/oemaker/config/${sys_arch}/edge_normal.xml
install -m 400 %{name}/isomaker/config/${sys_arch}/normal.xml %{buildroot}/opt/oemaker/config/${sys_arch}/normal.xml
install -m 400 %{name}/isomaker/config/${sys_arch}/standard.conf %{buildroot}/opt/oemaker/config/${sys_arch}/standard.conf
%ifarch x86_64
install -m 700 %{name}/isomaker/config/x86_64/livecd/live/x86.tmpl %{buildroot}/opt/oemaker/config/x86_64/livecd/live/x86.tmpl
install -m 400 %{name}/isomaker/config/x86_64/ks.cfg %{buildroot}/opt/oemaker/config/x86_64/ks.cfg
%else
install -m 700 %{name}/isomaker/config/aarch64/livecd/live/aarch64.tmpl %{buildroot}/opt/oemaker/config/aarch64/livecd/live/aarch64.tmpl
%endif
install -m 700 %{name}/isomaker/config/common/livecd/live/* %{buildroot}/opt/oemaker/config/common/livecd/live/
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

%pre

%post

%preun

%postun

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
* Wed Jul 10 2024 wangchong <wangchong56@huawei.com> - 3.1.0-6
- ID:NA
- SUG:NA
- DESC: fix issue IABY7K

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
