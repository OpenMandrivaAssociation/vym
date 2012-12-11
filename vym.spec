%define Werror_cflags %nil

Name:		vym
Version:	2.3.5
Release:	1
Summary:	Tool to manage mind maps
License:	GPLv2
Group:		Office
Source0:	http://prdownloads.sourceforge.net/vym/%{name}-%{version}.tar.bz2
URL:		http://www.insilmaril.de/vym/
Requires:	zip
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(xext)

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
%qmake_qt4 -d PREFIX=%{_prefix}

#really disable Werror flags
%__sed -i -e 's|-Wformat -Werror=format-security||g' Makefile*

%make

%install
%__make install INSTALL_ROOT=%{buildroot}

%__install -Dpm644 icons/%{name}-16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%__install -Dpm644 icons/%{name}.xpm %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.xpm
%__install -Dpm644 icons/%{name}-128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%__install -Dpm644 icons/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%__install -Dpm644 icons/%{name}-editor.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}-editor.png

#clean files and let files section handle docs
%__rm -rf %{buildroot}%{_docdir}/packages

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=Vym
Comment=View your mind
StartupNotify=true
Terminal=false
Type=Application
Icon=%{name}
Exec=%{name} %%f
MimeType=application/x-vym;application/zip;
Categories=KDE;Qt;Office;Chart;
EOF

%__mkdir_p %{buildroot}%{_datadir}/mime/packages/
%__cat << EOF > %{buildroot}%{_datadir}/mime/packages/vym.xml
<?xml version="1.0" encoding="UTF-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
  <mime-type type="application/x-vym">
    <sub-class-of type="application/zip"/>
    <comment>View Your Mind file</comment>
    <glob pattern="*.vym"/>
  </mime-type>
</mime-info>
EOF

# Remove it as it's OpenSUSE-based
%__rm -rf %{buildroot}%{_datadir}/%{name}/scripts/bugger

%files
%doc LICENSE.txt README.txt doc/*
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_iconsdir}/hicolor/*/apps/*


