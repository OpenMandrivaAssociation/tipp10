%define name tipp10
%define version 2.0.3
%define fversion 2-0-3
%define release 5
%define qtver 4.2.2
Summary: German touch typing learning program
Name: %{name}
Version: %{version}
Release: %{release}
Source0: tipp10_source_v%{fversion}.zip
Source1: %name.png
Patch0: tipp10-gcc4.5.patch
License: GPLv2+
Group: Education
Url: http://www.tipp10.de/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: locales-de
%if %mdvver >= 200910
Requires: qt4-database-plugin-sqlite
%else
Requires: qt4-database-plugin-sqlite-%_lib >= %qtver
%endif
BuildRequires: qt4-devel >= %qtver

%description
Learn touch typing with a nice and easy graphical user interface. At
the moment, the program comes with German texts only.

%prep
%setup -q -n %name
%autopatch -p1
find -name Thumbs.db |xargs rm -fv

%build
%_prefix/lib/qt4/bin/qmake
%make

%install
rm -rf %{buildroot}
mkdir -p %buildroot{%_bindir,%_libdir/%name,%_datadir/applications}
cp -r help tipp10  tipp10v2.template  wrong.wav %buildroot%_libdir/%name

cat > %buildroot%_bindir/%name << EOF
#!/bin/bash
cd %_libdir/%name
./tipp10 "\$@"
EOF

install -m 644 -D %SOURCE1 %buildroot%_datadir/pixmaps/%name.png

cat > %buildroot%_datadir/applications/mandriva-%name.desktop << EOF
[Desktop Entry]
Name=Tipp10
Comment=Touch typing trainer
Comment[de]=Schreibtrainer
Exec=tipp10
Icon=tipp10
Terminal=false
Type=Application
Categories=Education;Qt;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt
%attr(755,root,root) %_bindir/%name
%_libdir/%name
%_datadir/pixmaps/%name.png
%_datadir/applications/mandriva-%name.desktop


%changelog
* Thu Sep 22 2011 Götz Waschk <waschk@mandriva.org> 2.0.3-4mdv2012.0
+ Revision: 700803
- rebuild

* Tue Sep 21 2010 Götz Waschk <waschk@mandriva.org> 2.0.3-3mdv2011.0
+ Revision: 580369
- fix build

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 2.0.3-2mdv2010.0
+ Revision: 445468
- rebuild

* Fri Feb 13 2009 Götz Waschk <waschk@mandriva.org> 2.0.3-1mdv2009.1
+ Revision: 340018
- new version
- fix qt dep on 2009.1+

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 2.0.1-5mdv2009.0
+ Revision: 261563
- rebuild
- rebuild

* Thu Mar 20 2008 Götz Waschk <waschk@mandriva.org> 2.0.1-2mdv2008.1
+ Revision: 189100
- fix qt dep on x86_64
- fix buildrequires

* Wed Mar 19 2008 Götz Waschk <waschk@mandriva.org> 2.0.1-1mdv2008.1
+ Revision: 188809
- import tipp10


