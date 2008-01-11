%define version 1.8.1
%define release %mkrel 2

Summary:	View Your Mind is a tool to manage mind maps
Name: 		vym
Version: 	%version
Release: 	%release
Source0: 	http://prdownloads.sourceforge.net/vym/%{name}-%{version}.tar.bz2
URL: 		http://www.insilmaril.de/vym/
License: 	GPL
Group: 		Office
BuildRoot: 	%{_tmppath}/%{name}-buildroot
Requires:	zip
BuildRequires:	libqt-devel

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

qmake -o Makefile vym.pro

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
tar c scripts styles icons flags lang exports | tar x -C $RPM_BUILD_ROOT/%_datadir/%name
mkdir docs; tar c demos | tar x -C ./docs/
install vym $RPM_BUILD_ROOT/%_bindir/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat << EOF > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop
[DESKTOP ENTRY]
Name=VYM
StartupNotify=true
Terminal=False
Type=Application
Exec=%{_bindir}/vym
Categories=X-MandrivaLinux-Office-Graphs;Office;Chart;
EOF
install -m 644 icons/%name.png $RPM_BUILD_ROOT%{_iconsdir}

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc demos docs/*
%_datadir/%name
%_bindir/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_iconsdir}/%name.png
