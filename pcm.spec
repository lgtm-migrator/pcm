
Name:            pcm
Version:         0
Release:         0
Summary:         Processor Counter Monitor
Group:           System/Monitoring
License:         BSD-3-Clause
Url:             https://github.com/opcm/pcm/archive
Source:          master.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
AutoReqProv:    on
BuildRequires:  unzip
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description

Processor Counter Monitor (PCM) is an application programming interface (API) and a set of tools based on the API to monitor performance and energy metrics of Intel(r) Core(tm), Xeon(r), Atom(tm) and Xeon Phi(tm) processors. PCM works on Linux, Windows, Mac OS X, FreeBSD and DragonFlyBSD operating systems.

%prep
%setup -n pcm-master

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT/%{_bindir}/.. -DCMAKE_BUILD_TYPE=RelWithDebInfo ..
make -j 

%install
rm -rf $RPM_BUILD_ROOT
cd build
make install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%postun

%files
%defattr(-,root,root,0755)
%doc doc/license.txt doc/LINUX_HOWTO.txt
%{_sbindir}/pcm-core
%{_sbindir}/pcm-iio
%{_sbindir}/pcm-latency
%{_sbindir}/pcm-lspci
%{_sbindir}/pcm-memory
%{_sbindir}/pcm-msr
%{_sbindir}/pcm-mmio
%{_sbindir}/pcm-numa
%{_sbindir}/pcm-pcicfg
%{_sbindir}/pcm-pcie
%{_sbindir}/pcm-power
%{_sbindir}/pcm-sensor
%{_sbindir}/pcm-sensor-server
%{_sbindir}/pcm-tsx
%{_sbindir}/pcm-raw
%{_sbindir}/pcm
%{_bindir}/pcm-client
%{_sbindir}/pcm-daemon
%{_sbindir}/pcm-bw-histogram
%{_datadir}/pcm/

%changelog
* Tue Jun 04 2022 - maria.markova@intel.com
        Add cmake adaptation
* Fri Dec 17 2021 - maria.markova@intel.com
        Move licence.txt Linix_HOWTO.txt to doc folder
* Tue Aug 25 2020 - roman.dementiev@intel.com
        Add pcm-raw under %files
* Wed Apr 01 2020 - otto.g.bruggeman@intel.com
        Add pcm-sensor-server under %files
* Mon Nov 25 2019 - roman.dementiev@intel.com
        call make install and use %{_sbindir} or %{_bindir}
* Mon Oct 21 2019 - roman.dementiev@intel.com
	add opCode file to /usr/share/pcm
	use "install" to copy pcm-bw-histogram.sh
* Fri Oct 18 2019 - roman.dementiev@intel.com
	created spec file
