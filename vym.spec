%define Werror_cflags %nil

Name:		vym
Version:	2.8.8
Release:	1
Summary:	Tool to manage mind maps
License:	GPLv2
Group:		Office
Source0:	http://prdownloads.sourceforge.net/vym/%{name}-%{version}.tar.bz2
Patch0:   fix-install-dir.patch
URL:		http://www.insilmaril.de/vym/
Requires:	zip
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:	qt5-qtbase-devel
BuildRequires:	pkgconfig(xext)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Svg)

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
%autopatch -p1

%build
%cmake -DCMAKE_INSTALL_DATAROOTDIR="share/vym"

%make_build

%install
%make_install -C build

%files
%doc LICENSE* README* doc/*
#{_datadir}/%{name}
%{_bindir}/%{name}
#{_datadir}/applications/mandriva-%{name}.desktop
#{_datadir}/mime/packages/%{name}.xml
#{_iconsdir}/hicolor/*/apps/*


