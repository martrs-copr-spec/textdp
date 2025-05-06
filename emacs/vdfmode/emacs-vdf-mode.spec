%global pkg vdf-mode
%global _gitcommit 0910d4f847e9c817eb8da5434b3879048ec4ac92
%global _gitdate 20210302

Name:		emacs-%{pkg}
Version:	1.2git%{_gitdate}
Release:	1%{?dist}
Summary:	Major mode Valve VDF files
License:	GPL-3.0
URL:		https://github.com/plapadoo/vdf-mode/
Source0:	https://github.com/plapadoo/vdf-mode/archive/%{_gitcommit}/%{pkg}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	emacs >= 24.3
BuildRequires:	pkgconfig
Requires:	emacs(bin) >= 24.3

%description
Major mode for editing Valve VDF (KeyValues) files. For a definition of
this format, see https://developer.valvesoftware.com/wiki/KeyValues
This mode features indentation, highlighting and parentheses matching.
Created while developing reaktron.


%prep
%autosetup -n %{pkg}-%{_gitcommit}

%build
%{_emacs_bytecompile} %{pkg}.el

%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{pkg}
install -p -m 0644 %{pkg}.el %{pkg}.elc \
  %{buildroot}%{_emacs_sitelispdir}/%{pkg}

%files
%license LICENSE
%doc README.org
%{_emacs_sitelispdir}/%{pkg}

%changelog
* Sun Aug 25 2024 Martin RS - 1.2git20210302
- Initial for Fedora
