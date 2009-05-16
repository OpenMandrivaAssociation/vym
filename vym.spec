%define version 1.12.2
%define release %mkrel 1

Summary:	Tool to manage mind maps
Name: 		vym
Version: 	%version
Release: 	%release
Source0: 	http://prdownloads.sourceforge.net/vym/%{name}-%{version}.tar.bz2
URL: 		http://www.insilmaril.de/vym/
Patch0:         vym-1.10.0-dir-vars.patch
Patch1:         vym-1.10.0-docdir-searchList.patch
Patch2:         vym-1.10.0-xdg-open.patch
Patch3:         vym-0.10.0-editxlinkdialog-typeinfo.patch
Patch4:         vym-0.10.0-selection-typeinfo.patch
Patch5:         vym-0.10.0-mainwindow-typeinfo.patch
Patch6:         vym-0.10.0-xml-vym-typeinfo.patch
Patch7:         vym-1.10.0-ornamentedobj-typeinfo.patch
License: 	GPLv2
Group: 		Office
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Requires:	zip
BuildRequires:	libqt4-devel libxext-devel desktop-file-utils

%description
VYM (View Your Mind) is a tool to generate and manipulate maps which
show your thoughts. Such maps can help you to improve your creativity
and effectivity. You can use them for time management, to organize
tasks, to get an overview over complex contexts, to sort your ideas etc.

Maps can be drawn by hand on paper or a flip chart and help to structure
your thoughs. While a tree like structure can be drawn by hand or any
drawing software vym offers much more features to work with such maps.

vym is not another drawing software, but a tool to store and modify
information in an intuitive way. For example you can reorder parts of
the map by pressing a key or add various information like a complete
email by a simple mouse click.

%prep
%setup -q

%build
qmake DOCDIR="%{_docdir}/%{name}-%{version}" PREFIX=%{_prefix}
%make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install INSTALL_ROOT=%{buildroot} COPY="%{__cp} -p -f"

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
%{__cp} -p icons/%{name}-16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{__cp} -p icons/%{name}.xpm %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.xpm

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
%{__cp} -p icons/%{name}-128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
%{__cp} -p icons/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{__cp} -p icons/%{name}-editor.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}-editor.png


%{__mv} %{buildroot}%{_docdir}/%{name}-%{version}/ %{buildroot}%{_docdir}/%{name}/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat << EOF > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=VYM
StartupNotify=true
Terminal=false
Type=Application
Icon=%{name}
Exec=%{_bindir}/vym
Categories=Office;Chart;
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE.txt README.txt INSTALL.txt demos/* doc/*
%_datadir/%name/
%_bindir/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_iconsdir}/hicolor/16x16/apps/%{name}*
%{_iconsdir}/hicolor/48x48/apps/%{name}*
%{_iconsdir}/hicolor/128x128/apps/%{name}.png

