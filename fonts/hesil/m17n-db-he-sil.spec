Name:           m17n-db-he-sil
Version:        5.0.1
Release:        1%{?dist}
Summary:        m17n Hebrew layout similar to SIL Biblical Hebrew layout

License:        GPL-2.1
URL:            https://berithroad.blogspot.com/2011/01/sbl-hebrew-keyboard-for-linux.html
Source0:        he-kbd.mim_sil%{version}

Requires:       m17n-db ibus-m17n

BuildArch:      noarch

%description
This provides the m17n Hebrew keyboard layout similar to the SIL Biblical
Hebtew keyboard layout. It replaces the original Hebrew keyboard layout
offered by AIST offered as part of the m17n database.


%global _m17nkbd      %{_datadir}/m17n/he-kbd.mim
%global _m17nkbd_orig %{_m17nkbd}_aist
%global _m17nkbd_sil  %{_m17nkbd}_sil%{version}
%global _ibusm17ncfg  %{_datadir}/ibus-m17n/default.xml


%prep
%autosetup -c -T


%build
sed -e '/^;;; /,$d' -e 's/^;; //' %{SOURCE0} > LICENSE


%install
%__mkdir -p %{buildroot}%{_datadir}/m17n
install -m644 %{SOURCE0} %{buildroot}%{_m17nkbd_sil}


%triggerin -- m17n-db
mv -f %{_m17nkbd} %{_m17nkbd_orig}
cp -pf %{_m17nkbd_sil} %{_m17nkbd}

%triggerun -- m17n-db
/bin/mv -f %{_m17nkbd_orig} %{_m17nkbd}


%triggerin -- ibus-m17n
grep -q '<name>m17n:he:' %{_ibusm17ncfg} || ed %{_ibusm17ncfg} <<EOF
/<name>m17n:hi:\*/
.,/<engine>/y
/<engine>/x
?m17n:hi:?
s/hi/he/
wq
EOF

%triggerun -- ibus-m17n
grep -q '<name>m17n:he:' %{_ibusm17ncfg} && ed %{_ibusm17ncfg} <<EOF
/<name>m17n:he:/
.,/<engine>/d
wq
EOF


%files
%license LICENSE
%{_m17nkbd_sil}
%ghost %{_m17nkbd}
%ghost %{_m17nkbd_orig}
%ghost %{_ibusm17ncfg}


%changelog
* Sun May 04 2025 Martin RS - 5.0.1
- initial for Fedora 
