%define _gitcommit 41c5f54507fd865c8c00fe1f4bb390a59b6894ef
%define _gitdate 20250511

%define sname vim-airline

Name:           vim-plugin-airline
Version:        0.11git%{_gitdate}
Release:        1%{?dist}
Summary:        Lean and mean status/tabline for vim that's light as air
License:        MIT
Source0:        https://github.com/%{sname}/%{sname}/archive/%{_gitcommit}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       vim-common

%description
Vim plugin that provides a nice status line at the bottom of each vim window.
That line consists of several sections, each one displaying some piece of
information.

%prep
%autosetup -n %{sname}-%{_gitcommit}

%build

%install
install -D -m644 plugin/airline.vim \
        %{buildroot}%{_datadir}/vim/vimfiles/plugin/airline.vim
install -D -m644 autoload/airline.vim \
        %{buildroot}%{_datadir}/vim/vimfiles/autoload/airline.vim
cp -pr autoload/airline \
        %{buildroot}%{_datadir}/vim/vimfiles/autoload/

%clean

%files
%license LICENSE CONTRIBUTING.md
%doc README.md CHANGELOG.md doc/airline.txt
%{_datadir}/vim/vimfiles/plugin/airline.vim
%{_datadir}/vim/vimfiles/autoload/airline.vim
%{_datadir}/vim/vimfiles/autoload/airline

%changelog
* Wed May 14 2025 Martin RS - 0.11git20250511
- Initial for Fedora
