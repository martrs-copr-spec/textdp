Name:           vim-plugin-zeavim
Version:        2.3.1
Release:        1%{?dist}
Summary:        Simple offline documentation browser Zeal plugin for vim
License:        Public Domain
Source0:        https://github.com/KabbAmine/zeavim.vim/archive/refs/tags/%{version}.tar.gz#/zeavim.vim-%{version}.tar.gz
BuildArch:      noarch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       vim-common

%description
Zeavim allows to use Zeal documentation browser directly from Vim

%prep
%setup -q -n zeavim.vim-%{version}

%build

%install
install -D -m644 plugin/zeavim.vim \
        %{buildroot}%{_datadir}/vim/vimfiles/plugin/zeavim.vim
install -D -m644 autoload/zeavim.vim \
        %{buildroot}%{_datadir}/vim/vimfiles/autoload/zeavim.vim

%clean

%files
%defattr(-,root,root,-)
%doc doc/zeavim.txt CHANGELOG.md README.md
%{_datadir}/vim/vimfiles/plugin/zeavim.vim
%{_datadir}/vim/vimfiles/autoload/zeavim.vim

%changelog
* Thu May  2 2019 Martin RS - 2.3.1
- update
* Sat Jul 08 2017 Martin RS - 2.2.0
- update
* Tue Feb 26 2016 Martin RS - 2.0.1
- update
* Tue Sep 15 2015 Martin RS - 1.4
- initial for Fedora
