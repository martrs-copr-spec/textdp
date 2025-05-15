%global debug_package %nil

%global _gitcommit c7dfcef3f96b33aeb26403636ba546653dabd8fe
%global _gitdate 20110328

Name:           SolarAndLunar
Version:        0.1git20110328
Release:        1%{?dist}
Summary:        Convert the calendar between Gregorian and Chinese lunar

License:        Unknown
URL:            https://github.com/lihow731/SolarAndLunar
Source0:        https://github.com/lihow731/SolarAndLunar/archive/%{_gitcommit}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++ glibc-devel dos2unix

%description
Convert the calendar between Gregorian and Chinese lunar.

%prep
%autosetup -n %{name}-%{_gitcommit}
dos2unix main.cpp
sed -i SolarAndLunar.c -e 's:\(fopen("\)db2":\1%{_datadir}/%{name}/db2.data":'
sed -i main.cpp \
  -e "s/else if ( argc == 1 )/else if ((argc==2)\&\&(argv[1][0]=='4')\&\&(argv[1][1]==0))/" \
  -e "s/else$/else if ((argc==2)\&\&(argv[1][0]=='2')\&\&(argv[1][1]==0))/" \
  -e "/save2file()/a}else{printf(\"usage: %{name} YEAR MONTH DAY \[0\]\\\\n\");"
sed -i Makefile \
  -e 's:\(\./transfer\)\s*$:\1 2:' \
  -e 's:\(\./transfer\) 24$:\1 4:' \
  -e '/all:/s/transfer.*create/create/' \
  -e 's/create_db:\s*$/create_db: transfer/'

%build
%make_build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}
install -m 755 transfer %{buildroot}%{_bindir}/SolarAndLunar
install -m 644 db2 %{buildroot}%{_datadir}/%{name}/db2.data

%files
%doc README
%{_bindir}/SolarAndLunar
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/db2.data


%changelog
* Fri Jan 14 2022 Martin RS - 0.1git20110328
- new for Fedora 35 
